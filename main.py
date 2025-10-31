#welcome
print("Welcome to my guessing game about cars")
#list
print ("this is the list of cars you can use") 
cars=["hellcat","trackhawk","skylineGTR","Honda civic","G Wagon","Corvette C6", "BMW I8"]

print(cars)

#q1
        
car1="hellcat"        
guess = input("this car has a 8 cylinder supercharged engine? ")

if car1 =="hellcat" :
    print("Congrats")
else:
    print ("thats not it. The car was{hellcat}")

#Q2
guess2 = input("this car has the same engine as the hellcat but its made by jeep? ")
print(guess2)

car2="trackhawk"
if car2 == "trackhawk":
        print("congrats you got it right")
else:
        print("you got it wrong it was{trackhawk}")
    
#q3

guess3 = input("this car is famous for being paul walkers car in fast and furious? ")
print(guess3)
car3="skylineGTR"
if car3== "skylineGTR":
    print("correct")
else:
    print("you got it wrong it was {skyline_GTR}")

#q4
               
guess4 = input("this car has a inline 4 engine and is known for being a good reliable first car? ")
print (guess4)
car4="Honda civic"
if car4=="Honda civic":
     print("correct")
else:
     print("you got it wrong it was {Honda_civic}")

#q5 
guess5=input("this SUV is known for being a luxary car and is mentioned alot in music? ")
print(guess5)
car5="G Wagon"
if car5== "G Wagon":
     print("correct")
else:
     print("you got it wrong it was{G_Wagon}")

#q6
guess6=input("This car is known for being the same car as Lightning Mcqueen from cars?" )
car6= "Corvette C6"
if car6=="Corvette C6":
     print("you got it right")
else:
    print("you got it wrong it was {corvette_C6}")
#q7
guess7=input(" This BMW is known for its butterfly doors and its supercharged 3 cylinder engine.")
car7="BMW I8"
if car7== "BMW I8":
    print("you got it right")
else:
     print("you got it wrong it was{BMW_I8}")