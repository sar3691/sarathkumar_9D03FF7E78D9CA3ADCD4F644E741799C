class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students


from termcolor import cprint
cprint("\t\t SORTING IN DESCENDING ORDER \n\n",'red')
students = [
    Student("roshan", "B100", 7.8),
    Student("vetri", "B101", 8.9),
    Student("Sarath", "B102", 9.1),
    Student("nivetah", "B103", 9.9),
]
cprint("before sorting \n\n",'blue')
for student in students:
  cprint("Name: {}, Roll Number: {}, CGPA: {}\n\n".format(student.name,student.roll_number,student.cgpa,'green'))
sorted_students = sort_students(students)
cprint("after sorting by CGPA\n\n",'blue')
# Print the sorted list of students
for student in sorted_students:
  cprint("Name: {}, Roll Number: {}, CGPA: {}\n\n".format(student.name,student.roll_number,student.cgpa,'green'))