import random
print(" Welcome to the game of Rock-Paper-Scissors-Lizard-Spock\n Hope all the Big Bang theory nerds here know the rules.")
print("\n Let me explain it in short, the Sheldon's way:\n")
print(" Rock-Paper-Scissors-Lizard-Spock was created by internet pioneer Sam Kass\n as an improvement on the classic game Rock-Paper-Scissors")
print("\n All hail Sam Kass! Hail! XD\n")
print(" The rules are really simple:\n scissors cut paper\n paper covers rock\n rock crushes lizard\n lizard poisons spock\n")
print(" spock smashes scissors\n scissors decapitate lizard\n lizard eats paper\n paper disproves spock\n spock vapourises rock\n")
print(" and as it always has.... rock crushes scissor\n") 
print("Multiplayer or with computer? \n")
score_player1 = 0
score_player2 = 0
score_computer =0
choice = input("Enter m/c:")
if choice == "c" :
     user_name = input("Enter your name: ")
     while True:
         user_action = input("Enter a choice (rock, paper, scissors,lizard, spock): ")
         possible_actions = ["rock", "paper", "scissors", "lizard", "spock"]
         computer_action = random.choice(possible_actions)
         print("\nYou chose ",user_action,", computer chose ",computer_action,"\n")
         if user_action == "rock" and (computer_action== "scissors" or computer_action == "lizard"):
             print(user_name, " wins.")
             score_player1+=1 
         elif user_action == "paper" and (computer_action == "rock" or computer_action == "spock"):
             print(user_name," wins.")
             score_player1+=1 
         elif user_action == "scissors" and (computer_action == "paper" or computer_action == "lizard"):
             print(user_name, " wins.")
             score_player1+=1 
         elif user_action == "lizard" and (computer_action == "paper" or computer_action == "spock"):
             print(user_name, " wins.")
             score_player1+=1
         elif user_action == "spock" and (computer_action == "rock" or computer_action == "scissors"):
             print(user_name, " wins.")
             score_player1+=1
         elif user_action == computer_action:
             print("Tie")
         else:
             print("Computer won")
             score_computer+=1
         play_again = input("Play again? (y/n): ")
         if play_again.lower() != "y":
             print("You scored: ", score_player1, "Computer scored: ", score_computer)
             if score_player1 > score_computer :
                 print("\n You win!")
             elif score_player1 == score_computer :
                 print("\n It's a tie!")
             else :
                 print("\n You lose. Better luck next time.:/")
             print("Thank you for playing.")
             break
elif choice == "m":
     player1_name = input(" Enter 1st player's name: ")
     player2_name = input("\n Enter 2nd player name: ")
     while True:
         print("\n Enter", player1_name, "'s choice") 
         player1_choice = input("(rock,paper,scissors, lizard, spock): ")
         print("\n Enter",player2_name,"'s choice") 
         player2_choice = input("(rock paper scissors,lizard,spock): ")
         print("\n",player1_name," chose ",player1_choice,",",player2_name," chose ",player2_choice,".\n")
         if player1_choice == "rock" and (player2_choice== "scissors" or player2_choice == "lizard"):
             print(player1_name, " wins.")
             score_player1+=1 
         elif player1_choice == "paper" and (player2_choice == "rock" or player2_choice == "spock"):
             print(player1_name, " wins.")
             score_player1+=1 
         elif player1_choice == "scissors" and (player2_choice == "paper" or player2_choice == "lizard"):
             print(player1_name, " wins.")
             score_player1+=1 
         elif player1_choice == "lizard" and (player2_choice == "paper" or player2_choice == "spock"):
             print(player1_name, " wins.")
             score_player1+=1
         elif player1_choice == "spock" and (player2_choice == "rock" or player2_choice == "scissors"):
             print(player1_name, " wins.")
             score_player1+=1
         elif player1_choice == player2_choice:
             print("Tie")
         else:
             print(player2_name, " wins")
             score_player2+=1
         play_again = input("Play again? (y/n): ")
         if play_again.lower() != "y":
             print(player1_name, " scored: ", score_player1, " ",player2_name," scored: ", score_player2)
             if score_player1 > score_player2 :
                 print("\n",player1_name," wins!")
             elif score_player1==score_player2 :
                 print("\n It's a tie.") 
             else :
                 print("\n",player2_name," wins!")
             print("Thank you for playing")
             break

