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
    
current_state[0][0] = 'P' 
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

x_pi = 0
y_pi = 0

x_ci =0
y_ci = 0

c1 = 0
c2 = 0
p1 = 0
p2 = 0

def move_player(x_pi, y_pi, x_ci, y_ci):
  current_state[x_pi][y_pi] = 'P'
  current_state[x_ci][y_ci] = og_map[x_ci][y_ci]
  print_state()
  print()

def rolldie():
  d1 = random.randint(1, 6)
  d2 = random.randint(1, 6)
  p1 += d1
  p2 += d2
  

print_state()
while(True):
  
  p1 = int(input())
  p2 = int(input())
  os.system('clear')
  move_player(p1, p2, c1, c2)
  time.sleep(5)
  c1= p1
  c2 = p2
  
  






