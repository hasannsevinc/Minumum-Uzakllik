
point = [(1,1),(4,5),(3,4),(5,6)]
distance = []


def euclidean_Distance(point1,point2):
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5


for i in range(len(point)- 1): #3  - 0 1 2 3
    for j in range(i + 1,len(point)):
        distance.append(euclidean_Distance(point[i],point[j]))

print(f"Minumum Mesafe : {min(distance)}")






