from colorama import Fore, Back, Style
import random
import os
import time

n = 20

current_state =[[0 for x in range(n)] for x in range(n)]

og_map =[[0 for x in range(n)] for x in range(n)]

for i in range(n):
  for j in range(n):
    t = random.randint(1, 10)
    if(t > 8):
      current_state[i][j] = '@'
      og_map[i][j] = '@'
    else:
      current_state[i][j] = '^'
      og_map[i][j] = '^'
    
current_state[10][10] = 'P' 
def print_state():
  for i in range(n):
    for j in range(n):
      if(current_state[i][j] == '@'):
        print(Fore.RED + current_state[i][j], end="")
      elif(current_state[i][j] == '^'):
        print(Fore.GREEN + current_state[i][j], end="")
      elif(current_state[i][j] == 'P'):
        print(Fore.BLUE + 'P', end="")
    print(end="\n")

x_pi = 10
y_pi = 10

x_ci =10
y_ci = 10

def move_player(x_pi, y_pi, x_ci, y_ci):
  current_state[x_pi][y_pi] = 'P'
  current_state[x_ci][y_ci] = og_map[x_ci][y_ci]
  print_state()
  print()

def rolldie():
  d1 = random.randint(1, 6)
  d2 = random.randint(1, 6)
  return [d1, d2]
  
global shitcount 
print_state()

def explore():
  c1 = 10
  c2 = 10
  p1 = 10
  p2 = 10
  c = 0
  shitcount = 0
  while(c < 10):
    move = rolldie()
    p1 = move[0]
    p2 =  move[1] 
    os.system('clear')
    move_player(p1, p2, c1, c2)
    if(og_map[p1][p2] == '@'):
      shitcount+=1
      og_map[p1][p2] = '^'
      current_state[p1][p2] = '^'
    print(shitcount)   
    time.sleep(3)
    c1= p1
    c2 = p2
    c+=1
  
explore()





