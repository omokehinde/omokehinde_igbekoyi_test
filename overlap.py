# Question A

def overlap(p1,p2):
    points1=[]
    points2=[]
    for i in range(p1[0],p1[1]+1):
        points1.append(i)
    for i in range(p2[0],p2[1]+1):
        points2.append(i)
    for j in points1:
        if j in points2:
            return True
    else:
        return False
# print(overlap((1,5),(2,6)))
# print(overlap((1,5),(6,8)))