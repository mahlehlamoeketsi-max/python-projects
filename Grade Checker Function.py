def calculate_grade(score, passing_score=50):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"
    
name = input("Enter your name: ")
score = int(input("Enter your score: "))

result = calculate_grade(score)
print("Hello," + name + "! You scored " + str(score) + " and your result is: " + result + ".")
