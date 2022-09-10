from xml.dom.minidom import Notation
import random

def PassWord():
    word_low = "qwertyuiopasdfghjklzxcvbnm"
    word_up = word_low.upper()
    num = "0123456789"
    notation = "!@#$%^&*()[]<>/?,./|"
    temp = word_low + word_up + num + notation
    pass_word_file = open("C:\\Users\Administrator\\Desktop\\pass_word\\pass_word.txt", "r")


    list_pass = []


    for i in range(6, 26):
        pass_word = "".join((random.sample(temp, i)))
        while pass_word in pass_word_file:
            pass_word = "".join((random.sample(temp, i)))

        list_pass.append(pass_word)

    pass_word_file.close()
    print("suggestion pass word : ")
    for i in range(0, len(list_pass)):
        num = i + 1
        print(f"    {num} ---> {list_pass[i]}")

    print("for select pass word enter a number")
    n = int(input("your choice  : "))
    print(f"your pass word  :  {list_pass[n - 1]}")



    pass_word_file = open("C:\\Users\\Administrator\\Desktop\\pass_word\\pass_word.txt", "w")
    pass_word_file.write(str(list_pass[n - 1]))
    pass_word_file.close()
