class Check:
    def __init__(self,lis):
        self.lis = lis
    

    def check_block(self):
        count = 0
        for r in range(len(self.lis)):
            for c in range(len(self.lis[r])):
                try:
                    if all((self.lis[r][c], self.lis[r][c+1], self.lis[r+1][c], self.lis[r+1][c+1])):
                        count += 1
                except:
                    continue
    
        return count
    
    def check_tub(self):
        count = 0
        for r in range(len(self.lis)):
            for c in range(len(self.lis[r])):
                try:
                    if all((self.lis[r][c], self.lis[r+1][c-1], self.lis[r+1][c+1], self.lis[r+2][c])):
                        count += 1
                except:
                    continue

        return count
    
    def check_boat(self):
        count = 0
        for r in range(len(self.lis)):
            for c in range(len(self.lis[r])):
                try:
                    if all((self.lis[r][c], self.lis[r+1][c-1], self.lis[r+1][c+1], self.lis[r+2][c], self.lis[r+2][c+1])):
                        count += 1
                except:
                    continue

        return count
                         
    def count(self):
        dic ={"block":self.check_block(),"tub":self.check_tub(),"boat":self.check_boat()}
        return list(dic.items())
        

    
     