file = open("input.txt", 'r')
lines = file.readlines()

network = []
def calcSimilarityScores(network):
    n = int(network[0])
    similarityMatrix = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        similarityMatrix.append(temp)
    return similarityMatrix
def numinCommonBetweenLists(li1, li2):
    n = 0
    for i in li1:
        for j in li2:
            if(i == j):
                n+=1
    return n
def calcMatrixes(friendMatrix, similarityMatrix):
    for i in range(len(friendMatrix)):

        for j in range(len(friendMatrix)):
            if(j != i):
                n = numinCommonBetweenLists(friendMatrix[i], friendMatrix[j])
                similarityMatrix[i][j] = n
    return similarityMatrix
def recommend(id, network, similarityMatrix):
    rec = 0
    for i in range(int(network[0])):
        if similarityMatrix[id][i]>similarityMatrix[id][rec] and (not str(i) in friendMatrix[id]):
                rec = i
    return rec
n = 0
for line in lines:
    if(n==0):
        network.append(line[0:2])
    else:
        network.append([line[0], line[3]])
    n += 1
similarityMatrix = calcSimilarityScores(network)
friendMatrix = []
for i in range(int(network[0])):
    temp = []
    friends = []
    for j in network[1:]:
        if str(i) in j:
            temp = j.copy()
            temp.remove(str(i))
            friends.append(temp[0])
    friendMatrix.append(friends)
similarityMatrix = calcMatrixes(friendMatrix,similarityMatrix)
print("input: ")
x = int(input())
print("network: ", network)
print("friend: ", friendMatrix)
print("similarity: ", similarityMatrix)
print("user similarity: ", similarityMatrix[x])


ans = recommend(x, network, similarityMatrix)
for i in range(10):
    print(recommend(i, network, similarityMatrix))
print('The answer is: ', ans)
file.close()