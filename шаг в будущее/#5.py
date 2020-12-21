sphere,paralipipids=map(int,input().split())
spheres_data=[]
paralipipids_data=[]
for i in range(sphere):
    values=list(map(int,input().split()))
    spheres_data.append(values)
for i in range(paralipipids):
    values=list(map(int,input().split()))
    paralipipids_data.append(values)
maxx=-3000
maxy=-3000
maxz=-3000
minx = 3000
miny = 3000
minz = 3000
not_in_paralipipid=[]
for i in range(paralipipids):
    countx = 0
    county = 1
    countz = 2
    for k in range(0,24,1):
        if countx==0:
            if paralipipids_data[i][k]>maxx:
                maxx=paralipipids_data[i][k]
            elif paralipipids_data[i][k]<minx:
                minx=paralipipids_data[i][k]
            countz-=1
            county-=1
            countx=2
        elif county==0:
            if paralipipids_data[i][k]>maxy:
                maxy=paralipipids_data[i][k]
            elif paralipipids_data[i][k]<miny:
                miny=paralipipids_data[i][k]
            countz-=1
            countx-=1
            county=2
        elif countz==0:
            #print('inside z ')
            if paralipipids_data[i][k]>maxz:
                maxz=paralipipids_data[i][k]
            elif paralipipids_data[i][k]<minz:
                minz=paralipipids_data[i][k]
            county-=1
            countx-=1
            countz=2

for i in range(sphere):
    countx = 0
    county = 1
    countz = 2
    radius=spheres_data[i][-1]
    for k in range(len(spheres_data[i])-1):
        position = spheres_data[i][k]
        if countx==0:
            if position+radius>maxx or position-radius>maxx or position+radius<minx or position-radius<minx:
                not_in_paralipipid.append(i)
                break
            countx=2
            county-=1
            countz-=1
        elif county ==0:
            if position+radius>maxy  or position-radius>maxy or position+radius<miny  or position-radius<miny :
                not_in_paralipipid.append(i)
                break
            county =2
            countx-=1
            countz-=1
        elif countz ==0:
            if position+radius>maxz  or position-radius>maxz or position+radius<minz  or position-radius<minz :
                not_in_paralipipid.append(i)
                break
            countz =2
            countx-=1
            county-=1
for i in range(len(not_in_paralipipid)):
    print(not_in_paralipipid[i]+1)