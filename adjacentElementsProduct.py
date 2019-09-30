def adjacentElementsProduct(inputArray):
    a=inputArray[0]
    b=a*inputArray[1]
    for i in inputArray[1::]:
        if a*i>b:
            b=a*i
        a=i
    else:
            return b
