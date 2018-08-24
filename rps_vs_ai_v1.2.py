# Rock paper scissors
# 
# input r p or s
# computer random selection
# 
# compare
# who won

from random import randint

computer_wins = 0
player_wins = 0
winning_score = input("how many games do you want to try to win?: ")
winning_score = int(winning_score)


while computer_wins < winning_score and player_wins < winning_score:
	print (f"\n Player score: {player_wins}  Marvin's score: {computer_wins}")
	print ("\n")
	print ("rock...paper...scissors...SHOOT \n")
	player = input("\n Enter r, p, or s: ").lower()
# 	if player != "r" or player != "p" or player != "s":
# 		print ("\n YOU DID NOT ENTER r, p, or s")
# #	player = input("\n Enter r, p, or s: ").lower()
# 	else:	
# 		player = None
	computer = randint(1,3)
	if computer == 1:
		computer = "r"
	elif computer == 2:
		computer = "p"
	else:
		computer = "s"

	if computer == player:
		print ("it is a draw! \n")
	elif computer == "r" and player == "s":
		print ("marvin wins! \n")
		computer_wins += 1
	elif computer == "r" and player == "p":
		print ("player wins! \n")
		player_wins += 1	
	elif computer == "p" and player == "s":
		print ("player wins! \n")
		player_wins += 1
	elif computer == "p" and player == "r":
		print ("marvin wins! \n")
		computer_wins += 1
	elif computer == "s" and player == "p":
		print ("marvin wins! \n")
		computer_wins += 1
	elif computer == "s" and player == "r":
		print ("player wins! \n")
		player_wins += 1
	else:
		print ("try again \n")	
	    
#	print (f"computer ... {computer}   player...   {player}") 
print (f"FINAL SCORES  Player score: {player_wins}  Marvin's score: {computer_wins} \n")
    