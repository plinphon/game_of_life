import copy

class Board:
    def __init__(self,width,height):
        self.board= [[False]*width for _ in range(height)]
    
    def as_str(self):
        rv=''
        for row in self.board:
             rv+=''.join('.0'[c] for c in row)
             rv+= '\n'
        return rv
    
    def place_cells(self, coordinates):
        for row, col in coordinates:
            self.board[row][col] = True

    def count(self,row,col):
        count=0
        dd = [-1,0,1]
       
        for r in dd:
            for c in dd:
                if r == 0 and c == 0:
                    continue
                if row+r <0 or col+c <0:
                    continue
                try:
                    if self.board[row+r][col+c] == True:
                        count += 1
                except:
                    continue
        return count
    
    def next(self):
        self.newboard = copy.deepcopy(self.board)
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.count(r,c) == 3:
                    self.newboard[r][c]= True
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.count(r,c) == 3 or self.count(r,c) == 2:
                    continue
                else:
                    self.newboard[r][c]= False
        return self.newboard
