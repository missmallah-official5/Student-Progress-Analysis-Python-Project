# STUDENT PROGRESS ANALYSIS PROJECT
# Beginner / First-Year Python Project

print("Welcome Dear Students 👋")
print("May your dreams become reality ❤️\n")


def calculate_result(name, roll_number, student_class, marks):
    total_marks = 900
    percentage = (marks / total_marks) * 100

    # Grade System
    if percentage >= 86:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 64:
        grade = "B"
    elif percentage >= 49:
        grade = "C"
    elif percentage >= 33:
        grade = "D"
    else:
        grade = "Fail"

    print("Name:", name)
    print("Roll Number:", roll_number)
    print("Class:", student_class)
    print("Marks:", marks)
    print("Percentage:", round(percentage, 2))
    print("Grade:", grade)

    if percentage >= 33:
        print("Result: Passed 🎉\n")
    else:
        print("Result: Failed ❌\n")

    return percentage


# Student Data
p1 = calculate_result("Zartasha", 37, "9th", 790)
p2 = calculate_result("Anum", 26, "9th", 590)
p3 = calculate_result("Sara", 41, "9th", 288)

# Final Comparison
if p1 > p2 and p1 > p3:
    print("Zartasha performed the best among all")
elif p2 > p1 and p2 > p3:
    print("Anum performed the best among all")
elif p3 > p1 and p3 > p2:
    print("Sara performed the best among all")
else:
    print("All students performed equally well")

print("\nHard work beats talent when talent doesn’t work hard 💪")
print("Thank you for viewing my Student Progress Project 😊")