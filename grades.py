#Elijah Mitchell
#9/8/16
#period 2
name=input("What is the student's name?")
grade=input("What is the grade they got?")
int=grade
if int(grade)>100:
    print("There is no extra credit available.")
elif int(grade)==100:
    print(""+name+" got an A+ on this.")
elif int(grade)>=90:
    print(""+name+" got an A on this.")
elif int(grade)>=80:
    print(""+name+" got a B on this.")
elif int(grade)>=70:
    print(""+name+" got a C on this.")
elif int(grade)>=60:
    print(""+name+" got a D on this.")
elif int(grade)<60:
    print(""+name+" got a F on this.")
else grade<=0:
    print("There are no negatives available.")
