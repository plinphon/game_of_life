from board import Board
from check import Check 

a = Board(8,8)

coordinates = [(5,5),(5,6),(6,5),(6,6),(6,0),(5,1),(7,1),(6,2),(7,2)]

a.place_cells(coordinates)
print(a.as_str())


a.board = a.next()[:]
print(a.as_str())
find =Check(a.board)
print(find.count())
              