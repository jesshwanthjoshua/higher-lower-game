import art
from game_data import data
import random
from replit import clear

success =  True
win = ""

def count(user_option, count_1, count_2):
  print(f"\n\nuser_option: {user_option}, \ncount_1: {count_1}, \ncount_2: {count_2}")
  
  if user_option == "A" and count_1 > count_2:
    return True
  elif user_option == "B" and count_2 > count_1:
    return True    
  else:
    return False

def game(choice_1):
  
  print(art.logo)
  global score
  global win
  if score >0:
    print(f"Thats correct. Current score: {score}")
  

  # print(data[choice_1])
  print(f"\n\nCompare A: {data[choice_1]['name']}, a {data[choice_1]['description']}, from {data[choice_1]['country']}")
  count_1 = data[choice_1]['follower_count']
  
  print(art.vs)

  choice_2 = random.randint(0, len(data)-1)
  if choice_1 == choice_2:
    choice_2 = random.randint(0, len(data)-1)
  # print(data[choice_2])
  print(f"\n\nAgainst B: {data[choice_2]['name']}, a {data[choice_2]['description']}, from {data[choice_2]['country']}")
  count_2 = data[choice_2]['follower_count']
  
  user_option = input("Who has more followers? A or B: ").upper()
  
  win = count(user_option, count_1, count_2)

  if win == True:
    score += 1
    choice_1 = choice_2
    clear()
    game(choice_1)
  
  else:
    clear()
    
while success is True:
  score = 0
  choice_1 = random.randint(0, len(data)-1)
  game(choice_1)
  
  if win == False:
    success = False
    print(art.logo)
    print(f"Sorry that's Wrong. Your Final Score = {score}.")

  if input("Type 'y' if you want to a new game or 'n' for no: ").lower() == "y":
    clear()
    success = True
