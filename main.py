#welcome
print("Welcome to my guessing game about cars")
welcome = input("Do you want to play (yes/no): ")
#q1
car1="hellcat"
guess = input("this car has a 8 cylinder supercharged engine").lower()
if car1 =="hellcat" :
            print("Congrats")
else:
        print ("thats not it. The car was{hellcat}")
#q2
        trackhawk = "car2"
        guess2 = input("this car has the same engine as the hellcat but its made by jeep")
        if trackhawk == "trackhawk":
            print("congrats you got it right")
        else:
            print("you got it wrong it was{trackhawk}")