stu1=input("enter the first students name")
stu2=input("enter the second students name")
stu3=input("enter the third students name")
marks1=input("ente the first students marks")
marks2=input("enter the second students marks")
marks3=input("enter the third students marks")
students={
    stu1:marks1,
    stu2:marks2,
    stu3:marks3
}
print(students)
highest=max(students,key=students.get)
print(highest)