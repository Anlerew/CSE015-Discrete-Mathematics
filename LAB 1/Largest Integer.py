NumList = []
Number = int(input("Enter the number of integers: "))
for i in range(1, Number + 1):
    value = int(input("Enter the integer: "))
    NumList.append(value)

largest = NumList[0]    
for j in range(1, Number):
    if(largest < NumList[j]):
        largest = NumList[j]

print("The largest integer is: ", largest)
