'''
# Student Marksheet for 2nd Year - Karachi Board (Pakistan) "Prompts"
'''


# Student Info
student_name = "Tony Mark"
roll_number = "123456"
board = "Intermediate Board Karachi"
class_name = "HSC Part-II (Pre-Engineering)"  # You can change this as needed

# Subjects and their marks (you can modify these subjects and marks)
subjects = {
    "English": {"marks_obtained": 78, "total_marks": 100},
    "Urdu": {"marks_obtained": 74, "total_marks": 100},
    "Islamiat / Pakistan Studies": {"marks_obtained": 45, "total_marks": 50},
    "Mathematics": {"marks_obtained": 90, "total_marks": 100},
    "Physics": {"marks_obtained": 85, "total_marks": 100},
    "Chemistry": {"marks_obtained": 82, "total_marks": 100}
}

# Calculate totals
total_obtained = sum(subject["marks_obtained"] for subject in subjects.values())
total_marks = sum(subject["total_marks"] for subject in subjects.values())
percentage = (total_obtained / total_marks) * 100

# Grade calculation
def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"

grade = calculate_grade(percentage)

# Display Marksheet
print("="*50)
print(f"{board:^50}")
print(f"{class_name:^50}")
print("-"*50)
print(f"Name       : {student_name}")
print(f"Roll No    : {roll_number}")
print("-"*50)
print(f"{'Subject':<25}{'Marks Obtained':<15}{'Total Marks'}")
print("-"*50)
for subject, marks in subjects.items():
    print(f"{subject:<25}{marks['marks_obtained']:<15}{marks['total_marks']}")
print("-"*50)
print(f"{'Total':<25}{total_obtained:<15}{total_marks}")
print(f"{'Percentage':<25}{percentage:.2f}%")
print(f"{'Grade':<25}{grade}")
print("="*50)






'''
Prompts : Student Marksheet for 2nd Year - Karachi Board (Pakistan) 
'''

import matplotlib.pyplot as plt

# Student Info
student_name = "Tony Mark"
roll_number = "123456"
board = "Intermediate Board Karachi"
class_name = "HSC Part-II (Pre-Engineering)"

# Subjects and Marks
subjects = {
    "English": {"marks_obtained": 78, "total_marks": 100},
    "Urdu": {"marks_obtained": 74, "total_marks": 100},
    "Islamiat / Pakistan Studies": {"marks_obtained": 45, "total_marks": 50},
    "Mathematics": {"marks_obtained": 90, "total_marks": 100},
    "Physics": {"marks_obtained": 85, "total_marks": 100},
    "Chemistry": {"marks_obtained": 82, "total_marks": 100}
}

# Totals and Percentage
total_obtained = sum(s["marks_obtained"] for s in subjects.values())
total_marks = sum(s["total_marks"] for s in subjects.values())
percentage = (total_obtained / total_marks) * 100

# Grade Function
def calculate_grade(p):
    if p >= 80:
        return "A+"
    elif p >= 70:
        return "A"
    elif p >= 60:
        return "B"
    elif p >= 50:
        return "C"
    elif p >= 40:
        return "D"
    else:
        return "Fail"

grade = calculate_grade(percentage)

# Marksheet content as a list of lines
lines = [
    "=" * 50,
    f"{board:^50}",
    f"{class_name:^50}",
    "-" * 50,
    f"Name       : {student_name}",
    f"Roll No    : {roll_number}",
    "-" * 50,
    f"{'Subject':<25}{'Marks Obtained':<15}{'Total Marks'}",
    "-" * 50,
]

# Add each subject's marks
for subject, data in subjects.items():
    lines.append(f"{subject:<25}{data['marks_obtained']:<15}{data['total_marks']}")

# Totals and summary
lines += [
    "-" * 50,
    f"{'Total':<25}{total_obtained:<15}{total_marks}",
    f"{'Percentage':<25}{percentage:.2f}%",
    f"{'Grade':<25}{grade}",
    "=" * 50,
]

# Create a centered figure
fig, ax = plt.subplots(figsize=(8, 10))
ax.axis("off")

# Draw each line of text in center alignment
y = 1.0
for line in lines:
    ax.text(0.5, y, line, fontsize=12, fontfamily='monospace', ha='center', va='top')
    y -= 0.05

# Save the image as a JPG
plt.savefig("tony_mark_marksheet.jpg", dpi=300, bbox_inches='tight')
plt.show()
