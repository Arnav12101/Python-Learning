import random
print("Enter the range: ")
r1 = int(input());
r2 = int(input());
target = random.randint(r1,r2);

while(True):
    inp = int(input("Enter the number: "))
    if(inp < target):
        print("Enter a greater number")
    elif(inp > target):
        print("Enter a smaller number")
    else:
        print("You found the number")
        break;
