test_results = int(input("Enter in your percentage of test results"))
if test_results >= 60:
    if test_results > 65 and test_results < 75:
        print("Your grade for this test is A")
    else:
        print("Your grade is B")
else:
    print("You have not passed this test")