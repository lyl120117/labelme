import numpy as np


#已知平行四边形三个点，求第四个点
#计算两点之间的距离
def CalcEuclideanDistance(point1,point2):
    vec1 = np.array(point1)
    vec2 = np.array(point2)
    distance = np.linalg.norm(vec1 - vec2)
    return distance
#计算第四个点
def CalcFourthPoint(point1,point2,point3): #pint3为A点
    D = (point1[0]+point2[0]-point3[0],point1[1]+point2[1]-point3[1])
    return D
#三点构成一个三角形，利用两点之间的距离，判断邻边AB和AC,利用向量法以及平行四边形法则，可以求得第四个点D
def JudgeBeveling(point1,point2,point3):
    dist1 = CalcEuclideanDistance(point1,point2)
    dist2 = CalcEuclideanDistance(point1,point3)
    dist3 = CalcEuclideanDistance(point2,point3)
    dist = [dist1, dist2, dist3]
    max_dist = dist.index(max(dist))
    if max_dist == 0:
        D = CalcFourthPoint(point1,point2,point3)
    elif max_dist == 1:
        D = CalcFourthPoint(point1,point3,point2)
    else:
        D = CalcFourthPoint(point2,point3,point1)
    return D
