# student name
list_of_students = [] 
single_student_data = {}

name = input("Enter your name: ")
num_courses = int(input(f"{name}, how many courses do you offer? \n"))
print(f"\nList of {num_courses} course {name} offers")

# taking courses
list_of_courses = []
for item in range(0, num_courses):
    course = input(f"Course {item + 1}: ")
    list_of_courses.append(course)

single_student_data["name"] = name
single_student_data["courses"] = list_of_courses
list_of_students.append(single_student_data)

print(list_of_students)

# complete the above for multiple students 