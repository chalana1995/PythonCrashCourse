def get_choice():
  player_choice = input("Enter a choice (rock,paper,scissors: )")
  computer_choice = "paper"
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

choices = get_choice()
print(choices)