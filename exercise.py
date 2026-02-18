# day 7
# n = 15
# m = 7
# ans1 = n+m
# print("Addition of",n,"and",m,"is", ans1)
# ans2 = n-m
# print("Subtraction of",n,"and",m,"is", ans2)
# ans3 = n*m
# print("Multiplication of",n,"and",m,"is", ans3)
# ans4 = n/m
# print("Division of",n,"and",m,"is", ans4)
# ans5 = n%m
# print("Modulus of",n,"and",m,"is", ans5)
# ans6 = n//m
# print("Floor Division of",n,"and",m,"is", ans6)
# ans7 = n**m
# print("square of", n ,"power to " ,m ," is", ans7) 
# import random

# # 1. Define the game elements
# # s = Snake, w = Water, g = Gun
# choices = ["s", "w", "g"]

# # 2. Computer makes a random choice
# computer = random.choice(choices)

# # 3. User input
# print("--- Snake, Water, Gun Game ---")
# user_input = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# # 4. Dictionary to make the output readable
# names_dict = {"s": "Snake", "w": "Water", "g": "Gun"}

# if user_input not in choices:
#     print("Invalid input! Please choose s, w, or g.")
# else:
#     print(f"You chose: {names_dict[user_input]}")
#     print(f"Computer chose: {names_dict[computer]}")

#     # 5. Determine the winner
#     if user_input == computer:
#         print("It's a Tie!")
#     else:
#         # Winning logic for the User
#         if (user_input == "s" and computer == "w") or \
#            (user_input == "w" and computer == "g") or \
#            (user_input == "g" and computer == "s"):
#             print("Congratulations! You Win!")
#         else:
#             print("You Lose! Better luck next time.")

# f = open("demofile.txt")
# print(f.readlines())



with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())