from colorama import Fore, Back, Style
import random
import os
import time

current_state =[]
og_map = []
for i in range(1000):
  t = random.randint(1, 10)
  if(t > 8):
    current_state.append('@')
    og_map.append('@')
  else:
    current_state.append('^')
    og_map.append('@')
    
  
def print_state():
  for i in range(1000):
    if(current_state[i] == '@'):
      print(Fore.RED + current_state[i], end="")
    elif(current_state[i] == '^'):
      print(Fore.GREEN + current_state[i], end="")
    elif(current_state[i] == 'P'):
      print(Fore.BLUE + 'P', end="")

player_index = 0

def move_player(player_index, current_index):
  current_state[player_index] = 'P'
  current_state[current_index] = og_map[current_index]
  print_state()
  print()

prev_ind = 0
while(True):
  
  com = int(input())
  os.system('clear')
  move_player(com, prev_ind)
  prev_ind = com
  time.sleep(5)






