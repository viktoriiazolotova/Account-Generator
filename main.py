# version #3 - enhacements
import random
# STEP 1 - list of student names
student_names = []
for i in range (5):
  name = input("Enter first and last name of student separated by space:\n")
  student_names.append(name)

# STEP 2 - list of students ids randomly generated
student_ids = []
while len(student_ids)< len(student_names):
  id = random.randint(111111, 999999)
  if id not in student_ids:
    if int(str(id)[-3:]) > 100:
      student_ids.append(id)


# STEP 3 - list of emails using student manes and ids
student_emails = []
for i in range(len(student_names)):
  if len(student_names[i].split(" ")) == 2:
    [first, last] = student_names[i].split(" ")
    student_emails.append(first[0] + last + str(student_ids[i])[-3:] + "@example.org")
  elif len(student_names[i].split(" ")) == 3:
    [first, middle, last] = student_names[i].split(" ")
    student_emails.append(first[0] + middle[0] + last + str(student_ids[i])[-3:] + "@example.org")

# STEP 4 - print each student account information
for i in range(len(student_names)):
  print(f'name: {student_names[i]}\nid: {student_ids[i]}\nemail: {student_emails[i]}\n')
