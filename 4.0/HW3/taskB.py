# Task condition: https://contest.yandex.ru/contest/53031/problems/B/

import math

def createAdjacensyMatrix(n):
    res = list()
    for i in range(n):
        res.append([int(i) for i in input().split()])
    return res

def findMinNotVisitedNode(visitedList, shortedDistList):
    min = math.inf
    minIndex = None
    for i in range(len(shortedDistList)):
        if visitedList[i] != True and not math.isinf(shortedDistList[i]) and shortedDistList[i] < min:
            min = shortedDistList[i]
            minIndex = i
    if minIndex is None:
        return -1
    else:
        return minIndex
    
def findShortestPath(s, f, adjMatrix):
    n = len(adjMatrix)
    visitedList = [False] * n
    shortedDistList = [math.inf] * n
    prevList = [None] * n
    prevList[s] = -1
    currentNode = s
    shortedDistList[currentNode] = 0
    res = list()
    while True: 
        visitedList[currentNode] = True
        for i in range(n):
            if adjMatrix[currentNode][i] != -1:
                currentPath = (shortedDistList[currentNode] + adjMatrix[currentNode][i])
                if visitedList[i] != True and currentPath < shortedDistList[i]:
                    shortedDistList[i] = currentPath
                    prevList[i] = currentNode
        currentNode = findMinNotVisitedNode(visitedList, shortedDistList)
        if currentNode == -1:
            break
    if math.isinf(shortedDistList[f]):
        res.append(-1)
    else:
        i = f
        res.append(f+1)
        while i != -1:
            res.append(prevList[i]+1)
            i = prevList[i]
        res.pop()
    res.reverse()
    return res

def main():
    n, s, f = map(int, input().split())
    adjMatrix = createAdjacensyMatrix(n)
    print(*findShortestPath(s-1, f-1, adjMatrix))

if __name__ == "__main__":
    main()