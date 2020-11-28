class myBinary:
    MAXBIT = 32
    __bits = list()

    def __init__(self, number):
        if type(number) == type(""):
            self.__bits = self.__strToBin(number)
        elif type(number) == type(1):
            self.__bits = self.__intToBin(number)

    # Returns the binary equivalent of the given string binary as bool list
    def __strToBin(self, number):
        tmp = list()
        for ele in range(self.MAXBIT-len(number)):
            tmp.append(False)
        for ele in number:
            tmp.append(ele=="1")
        return tmp

    # Returns the binary equivalent of the given integer number as bool list
    def __intToBin(self,number):
        return self.__strToBin(f'{number:b}')

    #string representation of the binary numbers
    def __str__(self):
        # print(self.__bits)
        res = ""
        for ele in self.__bits:
            res += str(int(ele))
        return res

    # returns the bit in the given index
    def carryBit(self, index):
        # print("carry:", index)
        if self.__bits[index]:
            return 1
        return 0


def findAbsentNumberCaller(binList, index):
    # print("index: ", index)
    if index<0:
        return 0
    
    oddIndices = list()
    evenIndices = list()

    for ele in binList:
        if ele.carryBit(index) == 0:
            evenIndices.append(ele)
        else:
            oddIndices.append(ele)
    if len(oddIndices) >= len(evenIndices):
        return findAbsentNumberCaller(evenIndices, index-1) << 1 | 0
    else:
        return findAbsentNumberCaller(oddIndices, index-1) << 1 | 1

def findAbsentNumber(binList, lenght):
    return findAbsentNumberCaller(binList, lenght-1)


binList = [myBinary(1), myBinary(4), myBinary(3),myBinary(5), 
            myBinary(0),myBinary(2),myBinary(7)]


# binList = [myBinary("0000"), myBinary("0001"),myBinary("0010"), 
#             myBinary("0100"),myBinary("0101")]

# for ele in binList:
#     print(ele)

print(findAbsentNumber(binList,myBinary.MAXBIT))