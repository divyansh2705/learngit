age = int(input("Enter your age:"))

if(age<3):
  print("you are in your babyhood")
elif(age>=3) and (age<5):
    print("you are in your early childhood")
elif(age>=5) and (age<12):
    print("This is your School age")
elif(age>=12) and (age<18):
    print("Now you are a Teenager")
elif(age==18):
    print("Congratulations!!! Now you are an Adult.")
elif(age>18) and (age<40):
    print("You are in your adulthood")
elif(age>=40) and (age<60):
    print("Now you are aging")
else:
    print("Now you are a Senior citizen ")
