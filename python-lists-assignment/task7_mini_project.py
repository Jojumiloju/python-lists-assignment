student = ["John Doe", 22, "Computer Science", 4.5, "Nigeria"]

print(f"Name: {student[0]}\nAge: {student[1]}\nDepartment: {student[2]}\nCGPA : {student[3]}\nCountry: {student[4]}")

student[2] = "Robotics Engineering"
student[3] = 5.0

print(student)
print(student[::-1])
print(student[0:2])