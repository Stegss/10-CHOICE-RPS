import os

ELEMENTS = [
  "rock", "paper", "scissors", "water", "air", "fire", "earth", "grass", "arbenium", "evil"
]

ELEMENT_ICONS = {
    "rock": "🪨", "paper": "📜", "scissors": "✂️", "water": "💧",
    "air": "🌬️", "fire": "🔥", "earth": "🌍", "grass": "🌿",
    "arbenium": "⚛️", "evil": "😈"
}

WIN_CONDITIONS = {
    "rock": ["scissors", "fire", "evil", "grass"],
    "paper": ["rock", "earth", "water", "grass"],
    "scissors": ["paper", "grass", "air", "earth"],
    "water": ["fire", "rock", "scissors", "evil"],
    "air": ["fire", "water", "rock", "grass"],
    "fire": ["paper", "grass", "air", "earth"],
    "earth": ["rock", "water", "air", "evil"],
    "grass": ["earth", "water", "paper", "evil"],
    "arbenium": ["rock", "paper", "scissors", "water", "air", "fire", "earth", "grass"],
    "evil": ["rock", "paper", "scissors", "water", "air", "fire", "earth", "grass"]
}

# Prints the list of elements to remind players which elements they can chose
def printElementList():
  print("Choose your elements from the list above (without emojis!)")
  for current, element in enumerate(ELEMENTS, start=1):
    print(f"{current}. {ELEMENT_ICONS[element]}{element.capitalize()}")

# Finds if one player's choice is in the wind conditions 
def find_winner(p1choice, p2choice):
  if p1choice == p2choice:
    return "tie"
  elif p2choice in WIN_CONDITIONS[p1choice]:
    return "player1"
  elif p1choice in WIN_CONDITIONS[p2choice]:
    return "player2"
  else:
    return "tie"

# Clears all text in console so other player can't cheat
def clear_text():
  os.system('cls' if os.name == 'nt' else 'clear')

p1_score = 0
p2_score = 0

print(" Welcome to the 10 ELEMENT ROCK PAPER SCISSORS ")
print("Elements:", ", ".join(ELEMENTS))

# Player 1 choses element here
while True:
  print("Chose your elements, Player 1:")
  printElementList()
  p1_choice = input("Your choice (or type quit): ").lower()
  if p1_choice == "quit":
    break
  if p1_choice not in ELEMENTS:
    print("Answer is not a valid element. Try again.")
    continue
  clear_text()

  #Player 2's turn now
  print("Chose your elements, Player 2:")
  printElementList()
  p2_choice = input("Your choice (or type quit): ").lower()
  if p2_choice == "quit":
    break
  if p2_choice not in ELEMENTS:
    print("Answer is not a valid element. Try again.")
    continue
  clear_text()

# Print the results of the round
  print("Player 1 chose:", p1_choice.capitalize())
  print("Player 2 chose:", p2_choice.capitalize())
  result = find_winner(p1_choice, p2_choice)

  # Change scores based on who wins
  if result == "player1":
    print("Player 1 wins!", p1_choice.capitalize(), "beats", p2_choice.capitalize())
    p1_score = p1_score + 1
  elif result -- "player2":
    print("Player 2 wins!", p2_choice.capitalize(), "beats", p1_choice.capitalize())
    p2_score = p2_score + 1
  else:
    print("It is a tie.")

  print("Score -> Player 1:", p1_score, "| Player 2:", p2_score, "\n")
# Finally, determine and print the final player scores / who won
print("\nFinal Scores:")
print("Player 1:", p1_score, "\nPlayer 2:", p2_score)
if p1_score > p2_score:
  print("Player 1 has won 10 element rock paper scissors!")
elif p2_score > p1_score:
  print("Player 2 has won 10 element rock paper scissors!")
else:
  print("Both players have tied. Nature's balance has been restored!")

  

