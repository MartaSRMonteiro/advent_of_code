## PART I
## objective: In how many assignment pairs does one range fully contain the other?
import pandas as pd

with open('AC2022_Day4_input.txt') as file:
   sections_input = file.read().splitlines()

## Separate data into 4 columns
df = pd.DataFrame(columns = ['range_pairs'], data = sections_input)
df['range_pairs'] = df['range_pairs'].apply(lambda x: x.replace('-',','))
df[['left_1', 'right_1', 'left_2', 'right_2']] = df['range_pairs'].str.split(pat = ',', expand=True)
df = df[['left_1', 'right_1', 'left_2', 'right_2']].astype('int')

## Check wether one interval is contained in the other 
is_subset = 0
for i in range(0,(df.shape[0])):
    
    if(((df['left_1'][i] <= df['left_2'][i]) & (df['right_1'][i] >= df['right_2'][i])) | ((df['left_2'][i] <= df['left_1'][i]) & (df['right_2'][i] >= df['right_1'][i]))):
        is_subset += 1
        print(df['left_1'][i], '<=', df['left_2'][i], df['right_1'][i], '>=', df['right_2'][i])
        print('mais_um:', is_subset)
       
print('The answer is:', is_subset)
## The answer is: 475
 

## PART II
import pandas as pd

with open('AC2022_Day4_input.txt') as file:
   sections_input = file.read().splitlines()

## Separate data into 4 columns
df = pd.DataFrame(columns = ['range_pairs'], data = sections_input)
df['range_pairs'] = df['range_pairs'].apply(lambda x: x.replace('-',','))
df[['left_1', 'right_1', 'left_2', 'right_2']] = df['range_pairs'].str.split(pat = ',', expand=True)
df = df[['left_1', 'right_1', 'left_2', 'right_2']].astype('int')


## Check wether one interval is contained in the other 
is_overlapping = 0
for i in range(0,(df.shape[0])):
    
    if(((df['left_1'][i] <= df['left_2'][i]) & (df['left_2'][i] <= df['right_1'][i])) |
       ((df['left_1'][i] >= df['left_2'][i]) & (df['left_1'][i] <= df['right_2'][i]))):
        is_overlapping += 1
       
print('The answer is:', is_overlapping)
## The answer is: 825