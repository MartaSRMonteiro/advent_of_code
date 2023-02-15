## Objective: After the rearrangement procedure completes, what crate ends up on top of each stack?
##
## Initial position
##
##[Q] [J]                         [H]
##[G] [S] [Q]     [Z]             [P]
##[P] [F] [M]     [F]     [F]     [S]
##[R] [R] [P] [F] [V]     [D]     [L]
##[L] [W] [W] [D] [W] [S] [V]     [G]
##[C] [H] [H] [T] [D] [L] [M] [B] [B]
##[T] [Q] [B] [S] [L] [C] [B] [J] [N]
##[F] [N] [F] [V] [Q] [Z] [Z] [T] [Q]
## 1   2   3   4   5   6   7   8   9 


crates = [['Q','G','P','R','L','C','T','F'],
          ['J','S','F','R','W','H','Q','N'],
          ['Q','M','P','W','H','B','F'],
          ['F','D','T','S','V'],
          ['Z','F','V','W','D','L','Q'],
          ['S','L','C','Z'],
          ['F','D','V','M','B','Z'],
          ['B','J','T'],
          ['H','P','S','L','G','B','N','Q']]



import pandas as pd

## read data and split it by columns
moves = pd.read_csv('AC2022_Day5_input.txt', header = None, delimiter = "\t", names = ['moves_i'])
moves[['txt','n', 'txt1', 'from', 'txt2', 'to']] = moves['moves_i'].str.split(pat = ' ', expand = True)  
moves = moves[['n','from','to']]
moves = moves.astype('int')
## to turn it into Python indexing style
moves['from'] = moves['from']-1
moves['to'] = moves['to']-1


for i in range(moves.shape[0]):
    
    ## read moves
    from_i = moves['from'][i]
    to_i = moves['to'][i]
    n_i = moves['n'][i]
    
    for j in range(0,n_i):
        print('j:',j)
        crates[to_i].insert(0,crates[from_i][0])
        crates[from_i].pop(0)
        
answer = ''
for k in range(0,9):
    answer = answer + crates[k][0]
    
print('The answer is:', answer)
## The answer is: VGBBJCRMN