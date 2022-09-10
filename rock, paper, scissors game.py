import random 


choices = ["rock","paper" ,"scissors"]

computer = random.choice(choices)

Rating_computer = 0

Rating_player = 0

player = input("rock,paper ,scissors ? ").lower()


while player not in choices:
    player = input("rock,paper ,scissors ? ").lower()


while True:
  


  if player == computer:

    print("computer : " + computer + "\n" + "player : " + player)   
    print("Tie ! ")
    
    print("Rating computer  : " + str(Rating_computer))
    print("Rating player  : " + str(Rating_player))   


  elif player == "rock":
    if computer == "paper":
      print("computer : " + computer + "\n" + "player : " + player)   
      print("you  lose")
      
      print("Rating computer  : " + str(Rating_computer))
      print("Rating player  : " + str(Rating_player))   
          
      Rating_computer += 1

    elif computer == "scissors":
      print("computer : " + computer + "\n" + "player : " + player)  
      print("you  win") 
      
      print("Rating computer  : " + str(Rating_computer))
      print("Rating player  : " + str(Rating_player))   
      
      Rating_player += 1




  elif player == "paper":
    if computer == "scissors":
      print("computer : " + computer + "\n" + "player : " + player)   
      print("you  lose")
      
      print("Rating computer  : " + str(Rating_computer))
      print("Rating player  : " + str(Rating_player))
         
      Rating_computer += 1

    elif computer == "rock":
      print("computer : " + computer + "\n" + "player : " + player)  
      print("you win") 
      
      print("Rating computer  : " + str(Rating_computer))
      print("Rating player  : " + str(Rating_player))
         
      Rating_player += 1



  elif player == "scissors":
    if computer == "rock":
      print("computer : " + computer + "\n" + "player : " + player)   
      print("you  lose")
      
      print("Rating computer  : " + str(Rating_computer))
      print("Rating player  : " + str(Rating_player)) 
            
      Rating_computer += 1
    elif computer == "paper":
      print("computer : " + computer + "\n" + "player : " + player)  
      print("you win")
      
      print("Rating computer  : " + str(Rating_computer))
      print("Rating player  : " + str(Rating_player))   
      
      Rating_player += 1
      
      
  if (Rating_player >= 3 or Rating_computer >= 3) and abs(Rating_computer - Rating_player >= 2):
      if Rating_computer - Rating_player >= 2:
          print("FINISH")
          print("********you lose*********")
          print("Rating computer  : " + str(Rating_computer))
          print("Rating player  : " + str(Rating_player))
      elif Rating_player - Rating_computer >= 2:
          print("FINISH")
          print("********you win********")
          print("Rating computer  : " + str(Rating_computer))
          print("Rating player  : " + str(Rating_player))   
      break
  else: 
     computer = random.choice(choices)

     player = input("rock,paper ,scissors ? ").lower()


     while player not in choices:
       player = input("rock,paper ,scissors ? ").lower()      