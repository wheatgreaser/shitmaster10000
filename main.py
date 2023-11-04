from colorama import Fore, Back, Style
import random
import os
import time

current_state =[]
for i in range(1000):
  t = random.randint(1, 10)
  if(t > 8):
    current_state.append('@')
  else:
    current_state.append('^')
  
def print_state():
  for i in range(1000):
    if(current_state[i] == '@'):
      print(Fore.RED + current_state[i], end="")
    elif(current_state[i] == '^'):
      print(Fore.GREEN + current_state[i], end="")
    elif(current_state[i] == 'P'):
      print(Fore.BLUE + 'P', end="")

player_index = 0
def move_player(player_index):
  current_state[player_index] = 'P'
  print_state()
  print()

while(True):
  os.system('clear')
  com = int(input())
  move_player(com)
  time.sleep(5)

  




print_state()



