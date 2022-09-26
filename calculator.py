def add(x, y):
    result = int(x) + int(y)
    print(f"x : {x} and y : {y} and x + y : {result}")

def minus(x, y):
    result = int(x) - int(y)
    print(f"x : {x} and y : {y} and x + y :{result}")

def multiplication(x, y):
    result = int(x) * int(y)

    print(f"x : {x} and y : {y} and x + y :{result}")

def divide(x, y):
    result = int(x) / int(y)

    print(f"x : {x} and y : {y} and x + y :{result}")


def guide():
    print("------------------------------------")

    print("for add enter <<a>>")
    print("for minus enter <<m>>")
    print("for multiplication enter <<mu>>")
    print("for divide enter <<d>>")
    print("for Exit enter <<e>>")

    print("------------------------------------")

options =['a', 'm', 'mu', 'd', 'e']


def calculate():
    guide()

 
    
    while True:
        user = input("what do you do ?").lower()
        while user not in options:
            user = input("what do you do ?")
        x = input("please enter X : ")
        print()
        y = input("please enter Y : ")

        if user == "a":
            add(x, y)
        elif user == "m":
            minus(x ,y)
        elif user == "mu":
            multiplication(x ,y)
        elif user == "d":
            divide(x ,y)
        elif user == "e":
            break

    
    
    print("good bye")



        


calculate()



