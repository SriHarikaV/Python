name = input("Enter a nme: ")
print("welcome", name, "to this adventure!")

answer = input("you are in a dirt road, it has come to an end and you can go left or right. which way yoy would like to go: ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk arround it or swim accross? Type walk to walk arround and swim to swim accross: ")
    if answer == "swim":
        print("you swam aceoss and were eaten my alligator")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and last the game")
    else:
        print("nor a valid option you loose")

elif answer == "right":
    answer = input("you come to a bridge, its looks wobbly, do you want to  cross it or head back (cross/back)? ")
    if answer == "back":
        print("you go back and lose")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. Do you talk to them(yes/no): ")
        if answer == "yes":
            print("if you talked to the stranger they will give you gold. You Win!")
        elif answer == "no":
            print("you ignore the stranger and they offened to you. You lose the game")
        else:
            print("nor a valid option you loose")
    else:
        print("nor a valid option you loose")
else:
    print("nor a valid option you loose")

print("Thank you for trying", name)

