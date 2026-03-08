from collections import deque

def bfs(capA,capB,goal):
    queue=deque([(0,0,[0,0])])
    visited=set([0,0])
    while queue:
        currA,currB,path=queue.popleft()
        if(currA==goal or currB==goal):
            return path
        moves=[
            (capA,currB),
            (currA,capB),
            (0,currB),
            (currA,0),
            (
                currA-min(currA,capB-currB),
                currB+min(currA,capB-currB)
            ),
            (
                currA+min(currB,capA-currA),
                currB-min(currB,capA-currA)
            )
        ]
        for nextA,nextB in moves:
            if(nextA,nextB) not in visited:
                visited.add((nextA,nextB))

                queue.append((nextA,nextB,path+[(nextA,nextB)]))

result=bfs(4,3,2)

if isinstance(result,list):
    for i in result:
        print(i)
else:
    print(result)
