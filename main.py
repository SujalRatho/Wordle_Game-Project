import random
import sys
from termcolor import colored
def print_menu():
  print("Let's play Wordle:")
  print("Type a 5 letter word and hit enter!\n")

def read_randomword():
  with open("words.txt") as f:
    words = f.read().splitlines()
    return random.choice(words)

print_menu()
play_again =""
while play_again!="q":
  word = read_randomword()
  for attempt in range(1,7): 
    guess = input().lower()
    sys.stdout.write('\x1b[1A')
    for i in range(min(len(guess),5)):
      if guess[i] == word[i]:
        print(colored(guess[i], "green"), end="")
      elif guess[i] in word:
        print(colored(guess[i], "yellow"), end="")
      else:
        print(colored(guess[i], "red"), end="")
    print()  
      
    if guess == word:
      print(colored("\nYou win! The word was " + word,'green'),end = "")        
      break
    elif attempt ==6:
      print(colored("\nYou lose! The word was " + word,'red'),end = "")
  play_again = input("\nWant to play again? Type 'q' to exit or hit enter to play again:")




