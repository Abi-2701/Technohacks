print("------------Welcome to stone paper and Scissors Game-------------")
import random
Player_1=input("Enter a choice (Rock,Paper,Scissors):")
Possible_actions=["Rock","Paper","Scissors"]
Computer_action=random.choice(Possible_actions)
print(f" You Choose:{Player_1}")
print(f"Computer Choose: {Computer_action}")

if Player_1 == Computer_action:
    print(f"Both Player selected{Player_1} It is a tie!...")
elif Player_1 == "Rock":
    if Computer_action == "Scissors":
        print("Rock smashes Scissors! You Win")
    
elif Player_1 == "Paper":
    if Computer_action == "Rock":
        print("Paper covers rock! You win!")
    
elif Player_1 == "Scissors":
    if Computer_action =="Paper":
        print("Scissors cuts paper! You win!")
else:
    print(Computer_action,"smashes",Player_1,"! You lose!")


    print("_______________________THANK YOU______________________________")
      

    