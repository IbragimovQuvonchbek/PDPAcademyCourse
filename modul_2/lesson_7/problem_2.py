import bisect

marking_grades = [20, 40, 65, 85, 100]

grade = int(input("(0-100): "))

bisect.insort(marking_grades, grade)

mark = marking_grades.index(grade) + 1

print(f"baho: {mark}")
