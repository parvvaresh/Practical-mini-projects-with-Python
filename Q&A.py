from click import option


def new_game():
    number_game = 1
    score = 0
    Guesses = []
    for key in questions:
        print(key)
        for option in options[number_game - 1]:
            print(option)
        gusse = input("Enter A B C D ??  ").upper()    
        Guesses.append(gusse)
        print("---------------")
        score += check_answer(questions.get(key),gusse)
        number_game += 1
    
    
    display_score(score)    
        
        
    
            
    
    

def check_answer(answer, gusse):
    if answer == gusse:
        print("***You answered correctly***")
        return 1
    else:
        print("***You didn't answer correctly***")
        return 0

def display_score(score):
    
    print("youre score : " + str(int(score/len(questions) * 100)) + "%")
    print("----------------------------")
    print("Correct answers : ")
    
    for key in questions:
        print(key, end = " : ")
        print(questions.get(key))
        print()


def play_again():
    play = input("You want to play again ? ").upper()
    if play == "YES":
        return True

  
  
  
 
questions = {
       "Who is Mehrad hidden ? " : "A",
       "The best song of Z BAZI ? " : "B",
       "Who is the best composer ?" : "D",
       "The biggest Persian rap concert ? " : "C"
            }


options = [ ["A.Singer," , "B.Actor", "C.soccer player" , "D.Comdin"],
            ["A.Nakoni bavar," , "B.Tabestoon kotahe", "C.Yakh" , "D.Bache mahal"],
            ["A.Mahiyar," , "B.Sami low", "C.Catchy" , "D.Alireza JJ"],
            ["A.Moltafet," , "B.Paydar", "C.Z bazi" , "D.Wantonz"]
            
    
]

new_game()





while play_again() == True:
    new_game()
    play_again()

#this is a final a file of game 

print("Goodbye")