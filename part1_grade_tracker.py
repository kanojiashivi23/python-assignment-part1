## TASK 1

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

for student in raw_students:

    name = student["name"].strip().title()
    roll = int(student["roll"])
    
    marks = list(map(int, student["marks_str"].split(",")))

    # Check if name is valid
    is_valid= True
    for word in name.split():
        if not word.isalpha():
           is_valid= False
    if is_valid:
        print("Valid Name")

    else:
        print("invalid Name")


    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")

    if roll == 103:
        student_103 = name

        print(student_103.upper())
        print(student_103.lower())


## TASK 2
student_name = "Ayesha Sharma"

subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("Marks Report for", student_name)
print()

# PART 1 – Print subjects with grades
for i in range(len(subjects)):

    mark = marks[i]

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(subjects[i], ":", mark, "(", grade, ")")

# PART 2 – Total and average
total = sum(marks)
average = total / len(marks)

print("\nTotal Marks:", total)
print("Average:", round(average, 2))

# Highest and lowest subject
highest_mark = max(marks)
lowest_mark = min(marks)

highest_subject = subjects[marks.index(highest_mark)]
lowest_subject = subjects[marks.index(lowest_mark)]

print("Highest:", highest_subject, "-", highest_mark)
print("Lowest:", lowest_subject, "-", lowest_mark)

# PART 3 – While loop for new subjects
count = 0

while True:

    subject = input("\nEnter subject name (or type done to finish): ")

    if subject.lower() == "done":
        break

    mark_input = input("Enter marks (0-100): ")

    if not mark_input.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    mark = int(mark_input)

    if mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.")
        continue

    subjects.append(subject)
    marks.append(mark)

    count += 1

print("\nNew subjects added:", count)

new_average = sum(marks) / len(marks)

print("Updated average:", round(new_average, 2))















