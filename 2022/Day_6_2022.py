## Objective: How many characters need to be processed before the first start-of-packet marker is detected?
## your subroutine needs to identify the first position where the four most recently received characters 
## were all different. Specifically, it needs to report the number of characters from the beginning of the 
## buffer to the end of the first such four-character marker.

## Examples: bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
##           nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
##           nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
##           zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

## PART I & II
## The only difference is the number of characters (no_chars) that is needed to identify the marker

with open('AC2022_Day6_input.txt') as file:
    buffer = file.read()

no_chars = 14
final = 0
for i in range(0,len(buffer)):
    four_char = buffer[i:(i + no_chars)]
    if(len(set(four_char)) < no_chars):
        next
        ##print('position:', i+1)
    else:
        final = i + no_chars
        break
if((final == 0) & (i == (len(buffer)-1))):
    print("There is no marker!")
else:
    print("Final Position:", final)

## Part I final position answer = 1578
## Part II final position answer = 2178