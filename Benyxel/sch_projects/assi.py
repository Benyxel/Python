
number_of_input = int(input("Enter a number of input: "))
listOfstudents = []



def user_input():
    name = input(f"Enter student {data_input} name: ")
    num_courses = int(input(f"Enter the number of courses student {data_input} offer: \n"))
    print(f"\n{name} offers {num_courses} courses.\n")
    list_courses = []
    for course in range(1, num_courses + 1):
        course = input(f"Enter course {course}: ")
        list_courses.append(course)
    print(f"{name} offers {num_courses} courses, and all courses are {list_courses}.\n")

    singleSdata = {}
    singleSdata["name"] = name
    singleSdata["Total courses"] = num_courses
    singleSdata["Courses"] = list_courses
    listOfstudents.append(singleSdata)



for data_input in range (1, number_of_input +1):
        user_input()
        print(listOfstudents)
        
