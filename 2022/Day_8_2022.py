# The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

# 30373
# 25512
# 65332
# 33549
# 35390
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

# All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

# The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
# The top-middle 5 is visible from the top and right.
# The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
# The left-middle 5 is visible, but only from the right.
# The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
# The right-middle 3 is visible from the right.
# In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
# With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.



## =============================================================
## PART I
## Objective: how many trees are visible from outside the grid?
## =============================================================

## This task could be solved in different ways. 
## My code is not optimized because the data was small. I just wanted to end the task.
## I would have to rethink some parts if the data was larger due to memory issues. 

with open('AC2022_Day8_input.txt') as file:
    grid = file.read().splitlines()

## create a matrix with the grid values
import numpy as np
grid_matrix = np.array([list(row) for row in grid])

## create a matrix with 1's if the tree is visible and 0's if not
is_visible = np.zeros(shape=grid_matrix.shape).astype('int')

## set all border trees as visible (at least from one side)
is_visible[0] = 1
is_visible[grid_matrix.shape[0]-1] = 1 ## last row
is_visible[:,0] = 1
is_visible[:,grid_matrix.shape[1]-1] = 1 ## last column

n_rows = grid_matrix.shape[0]
n_cols = grid_matrix.shape[1]

for r in range(1,(n_rows-1)):
    for c in range(1,(n_cols)-1):
        
        v = grid_matrix[r,c]
        max_left = max(grid_matrix[r,0:c])
        max_right = max(grid_matrix[r,c+1:n_cols])
        max_up = max(grid_matrix[0:r,c])
        max_down = max(grid_matrix[r+1:n_rows,c])
              
        
        if ((v > max_left) | (v > max_right) | (v > max_up) | (v > max_down)):
            is_visible[r,c] = 1
            
print('The number of visible trees is ', np.sum(is_visible))

## Answer: The number of visible trees is  1792


## ==================================================================
## PART II
## Objective: What is the highest scenic score possible for any tree?
## ==================================================================
with open('AC2022_Day8_input.txt') as file:
    grid = file.read().splitlines()
    
## create a matrix with the grid values
import numpy as np
grid_matrix = np.array([list(row) for row in grid])

## create a matrix with 1's if the tree is visible and 0's if not
scenic_score = np.zeros(shape=grid_matrix.shape).astype('int')

n_rows = grid_matrix.shape[0]
n_cols = grid_matrix.shape[1]


## mind that all border trees have a scenic score of 0 because 
## at least one of its viewing distances will be zero

for r in range(1, n_rows-1):
    for c in range(1, n_cols-1):

        
        t_h = grid_matrix[r,c] ## tree height
       
    
        try:
            dist_left = c-[x for x,v in enumerate(grid_matrix[r,0:c]) if v >= t_h][-1]
        except:
            dist_left = c ## example: 1032, for 3 (index 2) there are 2 trees with lower height to the left

            
        try:   
            dist_right = [x for x,v in enumerate(grid_matrix[r,c+1:n_cols]) if v >= t_h][0]+1
        except:
            dist_right = n_cols - c - 1 # n_cols is the length and c is an index that is why we have to substract an extra 1
        
        
        try:   
            dist_up = r-[x for x,v in enumerate(grid_matrix[0:r,c]) if v >= t_h][-1] 
        except:
            dist_up = r
        
        
        try:   
            dist_down = [x for x,v in enumerate(grid_matrix[r+1:n_rows,c]) if v >= t_h][0]+1
        except:
            dist_down = n_rows - r - 1 # n_rows is the length and r is an index that is why we have to substract an extra 1
        
       
        
        scenic_score[r,c] = dist_left*dist_right*dist_up*dist_down

print('Answer: The highest scenic score possible is ', np.max(scenic_score))
## Answer: The highest scenic score possible is 334880