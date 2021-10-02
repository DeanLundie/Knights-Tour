from numpy import* 
import networkx as nx
import pylab as pyl
print('~~~~~~~~~~~~~~~~~')

#Question 1(i)
print('Question 1:')                              
def MoveTo(i,j,n):
    knight_move=[]
    if 0<=(i+1)<=n-1 and 0<=(j+2)<=n-1:
        knight_move.append((i+1,j+2))
    if 0<=(i-1)<=n-1 and 0<=(j+2)<=n-1:
        knight_move.append((i-1,j+2))
    if 0<=(i+2)<=n-1 and 0<=(j+1)<=n-1:
        knight_move.append((i+2,j+1))   
    if 0<=(i-2)<=n-1 and 0<=(j+1)<=n-1:
        knight_move.append((i-2,j+1))   
    if 0<=(i+2)<=n-1 and 0<=(j-1)<=n-1:
        knight_move.append((i+2,j-1))
    if 0<=(i-2)<=n-1 and 0<=(j-1)<=n-1:
        knight_move.append((i-2,j-1))
    if 0<=(i+1)<=n-1 and 0<=(j-2)<=n-1:
        knight_move.append((i+1,j-2))
    if 0<=(i-1)<=n-1 and 0<=(j-2)<=n-1:
        knight_move.append((i-1,j-2))
    return knight_move
#Question 1(ii)
print('(a) On a 5x5 board at square (0,0), the possible squares are', MoveTo(0,0,5))
print('(b) On a 6x6 board at square (0,4), the possible squares are', MoveTo(0,4,6))
print('(c) On a 6x6 board at square (2,5), the possible squares are', MoveTo(2,5,6))
print('~~~~~~~~~~~~~~~~~')

#Question 2(i)
print('Question 2:')
def MyBoard(n):
    m=nx.Graph()
    for i in range(0,n):
        for j in range(0,n):
            m.add_node((i,j))
            for k in range(0,len(MoveTo(i,j,n))):
                knight_move=MoveTo(i,j,n)
                m.add_edge((i,j),knight_move[k])
    return m
#Question 2(ii)
print('B5 has',MyBoard(5).number_of_nodes(),'nodes and has the graph:')
nx.draw_circular(MyBoard(5), with_labels=True)
pyl.show()
print('B7 has',MyBoard(7).number_of_nodes(),'nodes and has the graph:')
nx.draw_circular(MyBoard(7), with_labels=True)
pyl.show()
print('B8 has',MyBoard(8).number_of_nodes(),'nodes and has the graph:')
nx.draw_circular(MyBoard(8), with_labels=True)
pyl.show()
print('~~~~~~~~~~~~~~~~~')

#Question 3(a)
print('Question 3:')
def CountMoves(m):
    n=int(sqrt(m.number_of_nodes()))
    arr=zeros((n,n),int)
    for i in range(0,n):
        for j in range(0,n):
            arr[i,j]=(m.degree((i,j)))
    return arr
#Question 3(b)
print(CountMoves(MyBoard(5)),'for B5')
print(CountMoves(MyBoard(7)),'for B7')
print(CountMoves(MyBoard(8)),'for B8')
#Question 3(c)
print('For n>= 6, you can move to exactly 3 squares from the squares which are adjacent to the corner squares')
print('For n>= 6, you can move to the fewest number of squares from the corner squares')
print('The total number of possible moves on an nxn board can be found using the function: sum(CountMoves(MyBoard(n)))')
print('~~~~~~~~~~~~~~~~~')

#Question 4(a)
print('Question 4:')
def FindTour(i,j,n):
    Bn= MyBoard(n)
    curr_node=(i,j)
    tour=[]
    tour.append(curr_node)
    while curr_node in Bn:
        y=[]
        Nlist=list(Bn.neighbors(curr_node))
        for i in Nlist:
            y.append(Bn.degree(i))
        Bn.remove_node(curr_node)
        if len(y)==0:
            if Bn.number_of_nodes()==0:
                return tour
            else:
                print('Could not finish the tour')
        small=y.index(min(y))
        curr_node=Nlist[small]
        tour.append(curr_node)
#Question 4(b)
print('The knights tour starting at (0,0) on an 8x8 board has the path:',FindTour(0,0,8))
#Question 4(c)
new_arr=zeros((8,8),dtype=int)
for b in MyBoard(8):
    new_arr[b]=FindTour(0,0,8).index(b)
print(new_arr)
print('~~~~~~~~~~~~~~~~~')

#Question 5
print('Question 5:')
# The following code can be used to show a knight's tour starting at every square
def all_squares(n):
    for i in range(0,n):
        for j in range(0,n):
            print(FindTour(i,j,n))
# The function all_squares(n) shows the knight's tour, as a list, from every square on an nxn board
print("To show that there exists a complete knight's tour starting from any square on an 8x8 board simply run this: print(all_squares(8))")
# WARNING! This output is very long but it does prove that there is a complete knight's tour starting from any square on an 8x8 board
print('~~~~~~~~~~~~~~~~~')  
print(FindTour(13,9,15))



        