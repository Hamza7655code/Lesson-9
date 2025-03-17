print("Select your ride :")
print("1: Bike")
print("2: Car")

choice = int(input("Enter in your choice of ride"))

if choice == 1:
    print("What type of bike?")
    print("1: Scooty\n")
    print("2: Scooter\n")

choice2 = int(input("Enter in your choice 2: "))
if choice2 == 1:
    print("You have selected a scooty")
else:
    print("You have selected a scooter")

if (choice == 2):
    print("What type of car?")
    print("1: Sedan")
    print("2: SUV")
choice3 = int(input("Enter in your choice 3: "))
if choice3 == 1:
    print("You have selected a Sedan")
else:
    print("You have selected a SUV")

else:
    print("Wrong Choice!")


              