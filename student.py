import json

# 步骤 2: 读取 JSON 文件
with open('student.json', 'r') as file:
    data = json.load(file)

# 步骤 3: 处理 JSON 数据
students = data['students']

for student in students:
    student_id = student['id']
    student_name = student['name']
    student_age = student['age']
    student_grades = student['grades']
    
    print(f"ID: {student_id}, Name: {student_name}, Age: {student_age}")
    for subject, grade in student_grades.items():
        print(f"  {subject}: {grade}")