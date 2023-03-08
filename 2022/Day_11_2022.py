## ==========================================================================================
## PART I
## ==========================================================================================
## objective: Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. 
## What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
## 
## monkey business can be found by multiplying these two values together
## ==========================================================================================

## Starting
## Operation
## worry level to be divided by three and rounded down to the nearest integer.
## Test

import pandas as pd
import math

with open("AC2022_Day11_input.txt", "r") as file:
    data = file.read().splitlines()
    
no_rounds = 500
no_monkeys = int((len(data)+1)/7)

monkeys = pd.DataFrame(index=range(no_monkeys), columns=['objects_wl','operation','divisible_by','option_1','option_2','no_items_inspected'])
for i in range(0,no_monkeys):
    
    line = i*7
    ## populating data frame named monkey
    monkeys['objects_wl'][i] = data[line+1].replace('  Starting items: ','').split(sep=', ')
    monkeys['operation'][i] = data[line+2].replace('  Operation: new = old ','')
    monkeys['divisible_by'][i] = int(data[line+3].replace('  Test: divisible by ',''))
    monkeys['option_1'][i] = int(data[line+4].replace('    If true: throw to monkey ',''))
    monkeys['option_2'][i] = int(data[line+5].replace('    If false: throw to monkey ',''))   
    monkeys['no_items_inspected'][i] = 0   
    
    
monkeys[['operation', 'op_times']] = monkeys['operation'].str.split(' ', expand = True)
for r in range(no_rounds):
    for m in range(no_monkeys):
        for o in range(len(monkeys['objects_wl'][m])):

        
            ## increasing worry level
            if monkeys['op_times'][m] == 'old':
                monkeys['objects_wl'][m][0] = int(monkeys['objects_wl'][m][0])**2
            elif monkeys['operation'][m] == '*':
                monkeys['objects_wl'][m][0] = int(monkeys['objects_wl'][m][0])*int(monkeys['op_times'][m])
            else:
                monkeys['objects_wl'][m][0] = int(monkeys['objects_wl'][m][0]) + int(monkeys['op_times'][m])
    
    
            ## monkey bored => wl/3
            monkeys['objects_wl'][m][0] = math.floor(monkeys['objects_wl'][m][0]/3)
                        
            ## divisable by x?
            if (int(monkeys['objects_wl'][m][0]) % int(monkeys['divisible_by'][m])) == 0:
                ## send item to other monkey and delete item from self list
                monkeys['objects_wl'][monkeys['option_1'][m]].append(monkeys['objects_wl'][m].pop(0))

            else:
                ## send item to other monkey and delete item from self list
                monkeys['objects_wl'][monkeys['option_2'][m]].append(monkeys['objects_wl'][m].pop(0))
                
            ## increase number of inspected items
            monkeys['no_items_inspected'][m] += 1
        

no_items_inspected_sorted = monkeys['no_items_inspected'].sort_values(ignore_index=True, ascending = False)
print(monkeys)
print("The answer is: ", no_items_inspected_sorted[0]*no_items_inspected_sorted[1])
## The answer is: 102399


## ==========================================================================================
## PART II
## ==========================================================================================
## Objective: What is the level of monkey business after 10000 rounds and where
## worry level is not divided by 3 
## ==========================================================================================

import pandas as pd
import math

with open("AC2022_Day11_input.txt", "r") as file:
    data = file.read().splitlines()
    
no_rounds = 10000
no_monkeys = int((len(data)+1)/7)

monkeys = pd.DataFrame(index=range(no_monkeys), columns=['objects_wl','operation','divisible_by','option_1','option_2','no_items_inspected'])
for i in range(0,no_monkeys):
    
    line = i*7
    ## populating data frame named monkey
    monkeys['objects_wl'][i] = data[line+1].replace('  Starting items: ','').split(sep=', ') 
    monkeys['objects_wl'][i] = list(map(int,monkeys['objects_wl'][i]))
    monkeys['operation'][i] = data[line+2].replace('  Operation: new = old ','')
    monkeys['divisible_by'][i] = int(data[line+3].replace('  Test: divisible by ',''))
    monkeys['option_1'][i] = int(data[line+4].replace('    If true: throw to monkey ',''))
    monkeys['option_2'][i] = int(data[line+5].replace('    If false: throw to monkey ',''))   
    monkeys['no_items_inspected'][i] = 0   

    
monkeys[['operation', 'op_times']] = monkeys['operation'].str.split(' ', expand = True)
# Calculate the product of all divisors, following the Chinese remainder theorem
MEGA_DIVISOR = math.prod(monkeys['divisible_by'])


for r in range(no_rounds):
    for m in range(no_monkeys):

        ## increasing worry level
        if monkeys['op_times'][m] == 'old':
            monkeys['objects_wl'][m] = list(map(lambda x, y: x * y, monkeys['objects_wl'][m], monkeys['objects_wl'][m]))
        elif monkeys['operation'][m] == '*':
            monkeys['objects_wl'][m] = list(map(lambda x: x * int(monkeys['op_times'][m]), monkeys['objects_wl'][m]))
        else:
            monkeys['objects_wl'][m] = list(map(lambda x: x + int(monkeys['op_times'][m]), monkeys['objects_wl'][m])) 

        

        
        for o in range(len(monkeys['objects_wl'][m])):

                      
            monkeys['objects_wl'][m][0] %= MEGA_DIVISOR
                            
            ## divisable by x?
            if (int(monkeys['objects_wl'][m][0]) % int(monkeys['divisible_by'][m])) == 0:
                ## send item to other monkey and delete item from self list
                monkeys['objects_wl'][monkeys['option_1'][m]].append(monkeys['objects_wl'][m].pop(0))

            else:
                ## send item to other monkey and delete item from self list
                monkeys['objects_wl'][monkeys['option_2'][m]].append(monkeys['objects_wl'][m].pop(0))
                    
            ## increase number of inspected items
            monkeys['no_items_inspected'][m] += 1
        

no_items_inspected_sorted = monkeys['no_items_inspected'].sort_values(ignore_index=True, ascending = False)
print("The answer is: ", no_items_inspected_sorted[0]*no_items_inspected_sorted[1])
## The answer is: 23641658401