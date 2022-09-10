import random

place = [1 , 2 , 3]
game = [["-", "-", "-"], ["-","-","-"], ["-","-","-"]]

def print_game(game):
    for e in game:
        for place in e:
            print("   "+ place, end=" ")
        print("")   
        
def check(x, y, ch):
    if (x and y not in place) or (game[x - 1][y - 1] != "-") or (game[x - 1][y - 1] == ch):
        return 0
    else:
        return 1
    
    
def result(game):
    #check rows amd culmns
    for x in range(0, 3):
        if (game[x][0] == game[x][1] == game[x][2] == "*") or (game[0][x] == game[1][x] == game[2][x] == "*"):
            return 1
        elif (game[x][0] == game[x][1] == game[x][2] == "O") or (game[0][x] == game[1][x] == game[2][x] == "O"):
            return 2
        
   #check Diameter
    if (game[0][0] == game[1][1] == game[2][2] == "*") or (game[1][2] == game[1][1] == game[2][1] == "*"):
           return 1
    elif (game[0][0] == game[1][1] == game[2][2] == "O") or (game[1][2] == game[1][1] == game[2][1] == "O"):
           return 2
       
       


def play_game(question):
    if question == "yes":
        print("this is game : ")
        print_game(game)
        i = 0
        while True:
            if i % 2 == 0:
                row_u , cul_u = input("please enter row and coulmns :").split(" ")
                row_u , cul_u = int(row_u), int(cul_u)
                while check(row_u, cul_u, "O") == 0:
                    print("please try again :(")
                    row_u , cul_u = input("please enter row and coulmns :").split(" ")
                    row_u , cul_u = int(row_u), int(cul_u)
                game[row_u- 1][cul_u - 1] = "*"
                print("you:")
                print_game(game)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                if result(game) == 1:
                    print("you win :)")
                    break
                
            if i % 2 != 0:
                row_c , cul_c = random.choice(place) , random.choice(place)
                while check(row_c, cul_c, "*") == 0:
                    row_c , cul_c = random.choice(place) , random.choice(place)
                game[row_c - 1][cul_c - 1] = "O"  
                print("computer:")
                print_game(game)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

                if result(game) == 2:
                    print("you lose")
                    break
                
            i += 1
        
        

question = input("are you ready for start game ? ").lower()

while question != "exit":
    play_game(question)
    question = input("are you ready for start game ? ").lower()

    
print("good bye !") 
    


    




