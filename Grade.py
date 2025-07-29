#Marksheet grades
marks =int(input("Enter The Marks : "))
if(marks >= 90 )& (marks <=100):
    print("Grade: A")
elif(marks >= 80):
    print("Grade : B")
elif(marks >=70):
    print("Grade : C")
elif(marks >= 60):
    print("Grade : D")
else :
    print("Failed")