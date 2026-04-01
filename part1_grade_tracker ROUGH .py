## TASK 1

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# Loop Through Each Student
for student in raw_students:

# Clean the Name
    name = student["name"].strip().title()
    
    # Covert roll no. to integer
    roll = int(student["roll"])
    
    # Convert marks_str into a list of integer marks.
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

    # print profile card
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")

  # Store student with roll.no 103
    if roll == 103:
        student_103 = name
  # print stident_103 is upper and lower case
        print(student_103.upper())
        print(student_103.lower())


## TASK 2 : Marks Analysis Using Loops & Conditionals
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


## TASK 3- Class Performance Summary

# Class data containing student names and their marks
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# Print the class report header
print("Name              | Average | Status")
print("----------------------------------------")

# Counters for pass and fail students
pass_count = 0
fail_count = 0

# Variable to calculate overall class average
total_average = 0

# Variables to track the class topper
topper_name = ""
topper_avg = 0

# Loop through each student's data
for name, marks in class_data:

    # Calculate the average marks for the student
    avg = round(sum(marks) / len(marks), 2)

    # Add the student's average to total average
    total_average += avg

    # Determine pass or fail based on average marks
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    # Check if the student is the current topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    # Print formatted row for each student
    print(f"{name:<18} | {avg:^7} | {status}")

# Calculate the overall class average
class_avg = round(total_average / len(class_data), 2)

# Print summary statistics
print("\nStudents Passed:", pass_count)
print("Students Failed:", fail_count)

# Print the class topper
print("Class Topper:", topper_name, "-", topper_avg)

# Print the class average
print("Class Average:", class_avg)

## TASK 4- String Manipulation Utility 
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Remove leading and trailing whitespace
clean_essay = essay.strip()
print("Step 1 - Clean Essay:")
print(clean_essay)

# Step 2: Convert essay to Title Case
title_case = clean_essay.title()
print("\nStep 2 - Title Case:")
print(title_case)

# Step 3: Count occurrences of the word 'python'
python_count = clean_essay.count("python")
print("\nStep 3 - Count of 'python':", python_count)

# Step 4: Replace 'python' with 'Python 🐍'
replaced_text = clean_essay.replace("python", "Python 🐍")
print("\nStep 4 - Replaced Text:")
print(replaced_text)

# Step 5: Split essay into sentences
sentences = clean_essay.split(". ")
print("\nStep 5 - Sentences List:")
print(sentences)

# Print numbered sentences
print("\nNumbered Sentences:")

for i, sentence in enumerate(sentences, start=1):

    if not sentence.endswith("."):
        sentence += "."

    print(f"{i}. {sentence}")









