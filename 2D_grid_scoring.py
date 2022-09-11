# 2D Dice Grid Scoring Algorithm - http://www.101computing.net/2d-dice-grid-scoring-algorithm/

from random import randint

grid = []
length = 4

#A procedure to generate/shake a new 4 by 4 grid of 16 dice 
def resetGrid():
  global grid
  grid = []
  for row in range(length):
    grid.append([])
    for col in range(length):
      dice = randint(1,9)
      grid[row].append(dice)
  
#A procedure to display the dice grid
def displayGrid():
  global grid
  for row in range(length):
    st="| " 
    for col in range(length):
      st = st + str(grid[row][col]) + " | "
    print(st)

#A function to check if a number is an even number
def isEven(number):
  if number%2 == 0:
    return True
  else:
    return False

#A function to check if a number is an odd number
def isOdd(number):
  if number%2 == 1:
    return True
  else:
    return False

#A function to check if all elements in list are even
def isEvenList(grid):
    for i in range(len(grid)):
        if isOdd(grid[i]): return False
    return True

#A function to check if all elements in list are odd
def isOddList(grid):
    for i in range(len(grid)):
        if isEven(grid[i]): return False
    return True

####### Main Program Starts Here #######
resetGrid()
displayGrid()
score = 0

for i in range(len(grid)):
    score += sum(grid[i])
    if isEvenList(grid[i]) or isOddList(grid[i]): 
        print("Found even or odd numbers row ! +20")
        score+=20

    column = [grid[j][i] for j in range(len(grid))]
    if isEvenList(column) or isOddList(column):
        print("Found even or odd numbers column ! +20")
        score+=20

#Check if the four corners are even numbers
if isEven(grid[0][0]) and isEven(grid[0][length-1]) and isEven(grid[length-1][0]) and isEven(grid[length-1][length-1]):
  print("Four even corners! +20pts")
  score = score + 20

#Check if the four corners are odd numbers
if isOdd(grid[0][0]) and isOdd(grid[0][length-1]) and isOdd(grid[length-1][0]) and isOdd(grid[length-1][length-1]):
  print("Four odd corners! +20pts")
  score = score + 20

#Check if diagonal are even numbers
i = 0
j = 0
diag = []
while i < len(grid) and j < len(grid):
    diag.append(grid[i][j])
    i += 1
    j += 1
if isEvenList(diag) or isOddList(diag):
    print("Even or diagonal ! +20pts")
    score = score + 20

i = 0
j = len(grid)-1
diag = []
while i < len(grid) and j >= 0:
    diag.append(grid[i][j])
    i += 1
    j -= 1
if isEvenList(diag) or isOddList(diag):
    print("Even or diagonal ! +20pts")
    score = score + 20

#Complete the grid scoring algorithm here...

  
print("\nGrid score: " + str(score) + " pts.")