## PART I

with open('AC2022_Day2_input.txt') as file:

   strategy_input = file.read().splitlines()


'''A/X = rock - 1
    B/Y = paper - 2
    C/Z = scissors - 3
    win = 6
    draw = 3
    loss = 0
    '''

def get_score(round):
    
    scores = {'A X':(3+1),'A Y':(6+2),'A Z':(0+3),
            'B X':(0+1),'B Y':(3+2),'B Z':(6+3),
            'C X':(6+1),'C Y':(0+2),'C Z':(3+3)}
    
    return scores[round]



total_score = 0

for i in range(len(strategy_input)):
    total_score += get_score(strategy_input[i])
    
print('\nAnswer: The total score is ',total_score)
##Answer: The total score is 14163



## PART II
with open('AC2022_Day2_input.txt') as file:

   strategy_input = file.read().splitlines()


'''A/X = rock - 1
    B/Y = paper - 2
    C/Z = scissors - 3
    win = Z = 6
    draw = Y = 3
    loss = X = 0
    '''

def get_score(round):
    
    scores = {'A X':(0+3),'A Y':(3+1),'A Z':(6+2),
            'B X':(0+1),'B Y':(3+2),'B Z':(6+3),
            'C X':(0+2),'C Y':(3+3),'C Z':(6+1)}
    
    return scores[round]



total_score = 0

for i in range(len(strategy_input)):
    total_score += get_score(strategy_input[i])
    
print('\nAnswer: The total score is ',total_score)
##Answer: The total score is 12091

