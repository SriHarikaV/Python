print("Welcome to my computer Quiz! 😊")

Playing = input("Do you want to play? ")

if Playing.lower() != "yes":
    quit()

print("okay let's play :)")
score = 0

answer = input("What is the AWS Stands for? ")
if answer.lower() == "amazon web service":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("What is the IAM stands for? ")
if answer.lower() == "identity  access management ":
    print("correct!")
    score += 1
else:
    print("incorret")

answer = input("What is the S3 Stands for? ")
if answer.lower() == "simple storage service":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("What is the RDS Stands for? ")
if answer.lower() == "relational database service":
    print("correct!")
    score += 1
else:
    print("incorrect")

print("you got" + str(score) + "questions correct!")
print("you got" + str((score/4) * 100) + "%.")