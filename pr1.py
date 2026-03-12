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
#######missionaries
from collections import deque

# check if state is valid
def is_valid(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False
    return True

def bfs():
    start = (3, 3, 1)  # missionaries, cannibals, boat (1 = left, 0 = right)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (m, c, boat), path = queue.popleft()

        if (m, c, boat) == goal:
            return path + [(m, c, boat)]

        if (m, c, boat) in visited:
            continue

        visited.add((m, c, boat))

        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

        for m_move, c_move in moves:
            if boat == 1:  # boat on left
                new_state = (m-m_move, c-c_move, 0)
                m_right = 3-(m-m_move)
                c_right = 3-(c-c_move)
            else:  # boat on right
                new_state = (m+m_move, c+c_move, 1)
                m_right = 3-(m+m_move)
                c_right = 3-(c+c_move)

            if is_valid(new_state[0], new_state[1], m_right, c_right):
                queue.append((new_state, path + [(m, c, boat)]))

solution = bfs()

print("Solution Steps:")
for step in solution:
    print(step)
        
