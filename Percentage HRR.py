students_public = list()

student = list()
student_str = list()

num = int(input(""))

i = 0

while i < num:
    student_str = str(input(""))
    i = i + 1
    student = student_str.split(" ")
    students_public.append(student)

#print(students_public)

percentage_stud = str(input(""))

total = 0
j = 1

for i in range(len(students_public)):
    test = percentage_stud == students_public[i][0]
    if test:
        for j in range(1,len(students_public[i])):
            total  = total + float(students_public[i][j])
            percentage =total/3

#for i in students_public:
 #   for j in i:
  #      print(j, end = "\t")
   # print("\r")

print("%.2f" %percentage,end = "")

