from collections import deque
def water_jug_bfs(capA,capB,target):
    queue=deque([(0,0,[(0,0)])])
    visited=set([0,0])
    while queue:
        currA, currB, path = queue.popleft()
        if(currA==target or currB==target):
            return path
        moves = [
            (capA,currB),
            (currA,capB),
            (0,currB),
            (currA, 0),
            (
                currA - min(currA, capB-currB),
                currB + min(currA, capB-currB)
            ),
            (
                currB - min(currB, capA-currA),
                currA + min(currB, capA-currA)
            )
        ]

        for nextA, nextB in moves:
            if(nextA,nextB) not in visited:
                visited.add((nextA,nextB))
                queue.append((nextA,nextB, path+[(nextA,nextB)]))
# Example
result = water_jug_bfs(4, 3, 2)

if isinstance(result, list):
    print("Steps:")
    for step in result:
        print(step)
    print("Minimum steps required =", len(result) - 1)
else:
    print(result)