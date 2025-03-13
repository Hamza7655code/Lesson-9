medical_cause = input("Do you have a medical condition Yes or No?")
attendence = int(input("What is your attendence of this year?"))
if medical_cause == "Yes":
    print("You are eligible for the exam since you have had a medical condition")
else:
    if attendence >= 75:
        print("You are eligible for the exam with the medical cause exception")
    else:
        print("You are not eligible since you do not meet the minimum requirments")
    
                 