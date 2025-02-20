studentsMlist= []

def studentData():
    num_of_input = input("How many Students Do you wanna add? ")
    if not num_of_input.isdigit():
        print("You must enter a valid number to start the operation")
        return
    num_of_input = int(num_of_input)
    if num_of_input < 1:
        print("Number can't be less than '1'")
        return

    for number in range(1, num_of_input + 1):
        total_course = []
        name = input(f"Enter Student {number} Name: ")
        program = input(f"Enter Student {number} Program: ")
        num_Course = int(input(f"Enter Number of courses for student {number}: "))
        for course_num in range(1, num_Course + 1):
            course = input(f"Course {course_num}: ")
            total_course.append(course)
        students = {
            'Name': name,
            'Program': program,
            'Course': num_Course,
            'AllCourses': total_course
        }
        studentsMlist.append(students)
    print(studentsMlist)

studentData()