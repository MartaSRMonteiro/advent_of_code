## ==========================================================================================
## PART I
## ==========================================================================================
## The CPU has a single register, X, which starts with the value 1. It supports only two instructions:
## » addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
## » noop takes one cycle to complete. It has no other effect.
##

## OBJECTIVE: Find the signal strength DURING the 20th, 60th, 100th, 140th, 180th, and 220th cycles. 
## What is the sum of these six signal strengths?

## signal strength = #cycle*x
## ==========================================================================================
import pandas as pd
    
# Read data input info into a data frame
data = pd.DataFrame(
            pd.read_csv("AC2022_Day10_input.txt", sep = " ", header = None, names = ['instruction', 'value']))

x = 1
cycle = 0
interesting_cycles = [20,60,100,140,180,220]
sum_of_signal_strengths = 0

for i in range(0,data.shape[0]):
    
    if(data['instruction'][i] == 'noop'):
        cycle += 1
        ## start of cycle
        if(cycle in interesting_cycles):
            sum_of_signal_strengths += cycle*x
            
    else:

        cycle +=1
        ## start of 1st cycle
        if(cycle in interesting_cycles):
            sum_of_signal_strengths += cycle*x
        
        ## start of 2nd cycle
        cycle +=1
        if(cycle in interesting_cycles):
            sum_of_signal_strengths += cycle*x
        
        x += data['value'][i]
        
print('The answer is: ', sum_of_signal_strengths)
## The answer is: 16020




## ==========================================================================================
## PART II
## ==========================================================================================
import pandas as pd
## Read data into a data frame
data = pd.DataFrame(
            pd.read_csv("AC2022_Day10_input.txt", sep = " ", header = None, names = ['instruction', 'value']))

nrows = 6
ncols = 40

## Create an empty image
image = pd.DataFrame(".", index=range(nrows), columns=range(ncols))


x = 1 # sprite position
cycle = 1
row_position = 0
col_position = 0



for i in range(0,data.shape[0]):
                   
    if(data['instruction'][i] == 'noop'):
        
        col_position = (cycle-1) % 40 
        row_position = (cycle-1) // 40

        ## start of cycle
        if (col_position-1) <= x <= (col_position+1) :
            image.at[row_position,col_position] = "#"
            
        cycle += 1
        
        
    else:
                    
        col_position = (cycle-1) % 40 
        row_position = (cycle-1) // 40
            
        ## start of 1st cycle
        if (col_position-1) <= x <= (col_position+1) :
            image.at[row_position,col_position] = "#"
        
        cycle +=1
        
        
        ## start of 2nd cycle
        col_position = (cycle-1) % 40 
        row_position = (cycle-1) // 40 
            
        if (col_position-1) <= x <= (col_position+1) :
            image.at[row_position,col_position] = "#"
     
        x += data['value'][i]
          
        cycle += 1
        
print(image)
## Answer: ECZUZALR