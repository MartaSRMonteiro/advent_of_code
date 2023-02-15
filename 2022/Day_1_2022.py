import pandas as pd

calories_input = pd.read_csv('AC2022_Day1_input.txt', skip_blank_lines=False, header=None)
calories_input.columns = ["calories"]

## Part I

cal_per_elf = []
cal_sum = 0

for i in range(0,len(calories_input)):
    cal = calories_input['calories'][i]
    if(str(cal) == 'nan'):
        cal_per_elf.append(cal_sum)
        cal_sum = 0
    else:
        cal_sum += cal


print("Answer. The elf that is taking more food is carrying", max(cal_per_elf), "calories.")

## Part II

# Sort calories
cal_per_elf.sort()

# Sum the 3 highest values
three_highest = sum(cal_per_elf[-3:])
print("Answer: The 3 elfs that are taking more food are carrying", three_highest, "calories.")