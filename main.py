from colorama import Fore, Back, Style
import random
import os
import time

current_state =[[0 for x in range(10)] for x in range(10)]

og_map =[[0 for x in range(10)] for x in range(10)]

for i in range(10):
  for j in range(10):
    t = random.randint(1, 10)
    if(t > 8):
      current_state[i][j] = '@'
      og_map[i][j] = '@'
    else:
      current_state[i][j] = '^'
      og_map[i][j] = '^'
    
  
def print_state():
  for i in range(10):
    for j in range(10):
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

def move_player(x_pi, y_pi, x_ci, y_ci):
  current_state[x_pi][y_pi] = 'P'
  current_state[x_ci][y_ci] = og_map[x_ci][y_ci]
  print_state()
  print()
c1 = 0
c2 = 0
prev_ind = 0
while(True):
  
  p1 = int(input())
  p2 = int(input())
  os.system('clear')
  move_player(p1, p2, c1, c2)
  time.sleep(5)
  c1= p1
  c2 = p2
  
  






