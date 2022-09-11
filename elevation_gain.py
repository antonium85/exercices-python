#Cumulative Elevation Gain Calculator - www.101computing.net/cumulative-elevation-gain-calculator/

def isDestination(dest):
    return (dest=="y")

#Input...
starting_point = int(input("Enter the starting point :"))
new_pit = starting_point
gain = 0
dest = "n"

while not isDestination(dest):
    next_point = int(input("Enter the next point : "))
    dest = input("Did you arrive (y/n) : ")
    
    gain += (next_point - new_pit) if next_point > new_pit else 0
    new_pit = next_point

print(gain)

