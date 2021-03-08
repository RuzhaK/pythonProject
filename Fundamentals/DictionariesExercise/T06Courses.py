line = input()
courses = {}
while line != "end":
    data = line.split(" : ")
    course_name = data[0]
    student_name = data[1]
    if data[0] not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    line = input()
sorted_courses = dict(sorted(courses.items(), key=lambda c: -len(c[1])))
for key, value in sorted_courses.items():
    print(f"{key}: {len(value)}")
    for student_name in sorted(value):
        print(f"-- {student_name}")
