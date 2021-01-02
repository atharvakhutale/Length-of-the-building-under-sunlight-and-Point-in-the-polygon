import numpy as np
import math

def findCorner(side,building):
    
    if (side=="top-left"):
        corner1=[1000,0]
        for i in building:
            if(i[0]<=corner1[0] and i[1]>=corner1[1]):
                corner1=i
    elif (side=="top-right"):
        corner1=[0,0]
        for i in building:
            if(i[0]>=corner1[0] and i[1]>=corner1[1]):
                corner1=i
    elif (side=="bottom-right"):
        corner1=[0,1000]
        for i in building:
            if(i[0]>=corner1[0] and i[1]<=corner1[1]):
                corner1=i
    elif (side=="bottom-left"):
        corner1=[1000,1000]
        for i in building:
            if(i[0]<=corner1[0] and i[1]<=corner1[1]):
                corner1=i
    # print(corner1)
    return(corner1)

print("Please enter co-ordinates valuing less than 1000, greater than zero")
# a=input("Enter co-ordinates of light source")
# b=input("Enter co-ordinates for n buildings as an array")
a=[0,10]
b=[[[1,0],[1,2],[2,0],[2,2]],[[3,0],[3,5],[4,0],[4,5]]]

print("Source of light at "+str(a))
print(str(len(b))+" buildings near source of light")
k=0
angle1 = 100

for j in b:
    topLeft = np.array(findCorner("top-left",j))
    topRight = np.array(findCorner("top-right",j))
    bottomLeft = np.array(findCorner("bottom-left",j))
    bottomRight = np.array(findCorner("bottom-right",j))

    print("illumination of building "+str(k)+" = ")
    if(k==0):
        print(np.linalg.norm(topLeft - topRight) + np.linalg.norm(topLeft - bottomLeft))
        angle1=math.asin(abs(a[1]-topRight[1])/np.linalg.norm(np.array(a)-topRight))
    elif(math.asin(abs(a[1]-topRight[1])/np.linalg.norm(np.array(a)-topRight))<angle1):
        print(np.linalg.norm(topLeft - topRight) + (abs(math.tan(angle1)*(a[0]-topLeft[0]))-abs(a[1]-topLeft[1])))
        # print(angle1)
        angle1=math.asin(abs(a[1]-topRight[1])/np.linalg.norm(np.array(a)-topRight))
    else:
        print("0")
    # print("angle:"+str(angle1))
    k=k+1