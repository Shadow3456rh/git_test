a=0
b=0

cap_a=4
cap_b=3
target=2

while True:
    print("Choice 1: Fill jug A")
    print("Choice 2: Fill jug B")
    print("Choice 3: Empty jug A")
    print("Choice 4: empty jug B")
    print("Choice 5: Transfer jug A to B")
    print("Choice 6: Transger jug B to A")
    print("Choice 7: Exit")
    print("Currently in jug A: ",a, "jug B: ",b)

    if(a==target or b==target):
        print("Goal reached!")
        print("Currently in jug A: ",a, "jug B: ",b)
        break

    choice=int(input("Enter your choice: "))
    if(choice==1):
        a=cap_a
    elif(choice==2):
        b=cap_b
    elif(choice==3):
        a=0
    elif(choice==4):
        b=0
    elif(choice==5):
        transfer=min(a,cap_b-b)
        a-=transfer
        b+=transfer
    elif(choice==6):
        transfer=min(b, cap_a-a)
        b-=transfer
        a+=transfer
    elif(choice==7):
        break
        