def mxPrint(mx):
    print("-----------------------")
    for ele in mx:
        print(ele)
    print("-----------------------")

#row reduction
def rowReduc(data):
    temp = list()
    for ele in data:
        mi =min(ele)
        col = list()
        for x in ele:
            x-=mi
            col.append(x)
        temp.append(col)
    return temp
# column redution
def colReduc(data):
    for i in range(len(data)):
        col = list()
        for j in range(len(data[0])):
            col.append(data[j][i])
        mi = min(col)
        for j in range(len(data[0])):
            data[j][i] -=mi
# applies both reduction
def reduc(data):
    data = rowReduc(data)
    colReduc(data)
    return data

# creating a map which holds values and their state of being striked
def crtMap(data):
    zeroMap = [[None for _ in range(len(data[0]))] for _ in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                zeroMap[i][j] = (0,False)
            else: 
                zeroMap[i][j] = (data[i][j],False)
    return zeroMap

# checks the rows for striking over elements
def rowCheck(zeroMap):
    for i in range(len(zeroMap)): 
        ele = None
        index = None
        for j in range(len(zeroMap[0])):
            if ele != None:
                continue
            if zeroMap[i][j] == (0,False):
                ele = zeroMap[i][j]
                index = (i,j)
                # print("#0 ||","i: ",i," j: ",j, " ele: ",ele)
            
            if ele !=None:
                check = 0
                for k in range(j+1,len(zeroMap[0])):
                    # print("#1 ||","i: ",i," k: ",k," ele: ",zeroMap[i][k])
                    if zeroMap[i][k] == ele:
                        check+=1
                if check == 0:
                    # print("#2")
                    for l in range(len(zeroMap)):
                        if (l,j) == index:
                            zeroMap[l][j] = (zeroMap[l][j][0],"square")
                        elif zeroMap[l][j] == (zeroMap[l][j][0],True):
                            zeroMap[l][j] = (zeroMap[l][j][0],"intersect")
                        else:
                            zeroMap[l][j] = (zeroMap[l][j][0],True)
# checks the columns for striking over elements
def colCheck(zeroMap):
    for i in  range(len(zeroMap[0])):
        ele = None
        index = None
        for j in range(len(zeroMap)):
            if ele != None:
                continue
            if zeroMap[j][i] == (0,False):
                index = (j,i)
                ele = (0,False)
                # print("#0 ||","i: ",i," j: ",j, " ele: ",ele)
            
            check =0
            if ele != None:
                for k in range(j+1,len(zeroMap)):
                    # print("#1 ||","i: ",i," k: ",k," ele: ",zeroMap[k][i])
                    if zeroMap[k][i] == ele:
                        check+=1
                
                if check == 0:
                    # print("#2")
                    for l in range(len(zeroMap[0])):
                        if (j,l) == index:
                            zeroMap[j][l] = (zeroMap[j][l][0], "square")
                        elif zeroMap[j][l] == (zeroMap[j][l][0], True):
                            zeroMap[j][l] = (zeroMap[j][l][0], "intersect")    
                        else:
                            zeroMap[j][l] = (zeroMap[j][l][0], True)
#checks the row and column
def check(zeroMap):
    rowCheck(zeroMap)
    colCheck(zeroMap)

#Checks that number of the squares equal to number of n. If its not updates the zeroMap and returns false, if it is returns true
def sqrCheck(zeroMap):
    count = 0
    for ele in zeroMap:
        for e in ele:
            if e[1] == "square":
                count+=1

    if(count<len(zeroMap)):
        minList = list()
        if count < len(data):
            for i in range(len(zeroMap)):
                for j in range(len(zeroMap[0])):
                    if zeroMap[i][j][1] == "intersect":
                        zeroMap[i][j] = (zeroMap[i][j][0]+1,zeroMap[i][j][1]) 
                    elif zeroMap[i][j][1] == False:
                        minList.append(zeroMap[i][j][0])

            mi = min(minList)
            # print("mi: ",mi )
            for i in range(len(zeroMap)):
                for j in range(len(zeroMap[0])):
                    if zeroMap[i][j][1] == False:
                        zeroMap[i][j] = (zeroMap[i][j][0]-mi, zeroMap[i][j][1])
        return False
    else:
        return True
# Convert map to matrix
def mapToMx(zeroMap):
    tmp = [[None for _ in range(len(zeroMap[0]))] for _ in range(len(zeroMap))]
    for i in range(len(zeroMap)):
        for j in range(len(zeroMap[0])):
            tmp[i][j]= zeroMap[i][j][0]
    return tmp

#Prints the assignments according to result matrix
def printResMap(zeroMap):
    for i in range(len(zeroMap)):
        for j in range(len(zeroMap[0])):
            if zeroMap[i][j][1] == "square":
                print("{}. job assigned to {}. person.".format(i+1,j+1))

#Combines all of the functions defined above
def assignJobs(data):
    data = reduc(data)
    zeroMap = crtMap(data)
    check(zeroMap)
    while not sqrCheck(zeroMap):
        check(zeroMap)
    printResMap(zeroMap)

data = [
        [9, 11, 14, 11, 7 ],
        [6, 15, 13, 13, 10],
        [12, 13, 6, 8, 8, ],
        [11, 9, 10, 12, 9 ],
        [7, 12, 14, 10, 14]
       ]



assignJobs(data)