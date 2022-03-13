counter = 1 
largest_odd = 0
even_count = 0
while counter <= 10:
    x = int(input("Enter an integer: "))
    if (x % 2 != 0 and x > largest_odd) or (x % 2 != 0 and x <= 0 and largest_odd == 0):
        largest_odd = x

    elif x % 2 == 0:
        even_count = even_count + 1

    counter = counter + 1
if even_count == 10:
    print("No odd numbers")
else:
    print("The largest odd integer is: ", largest_odd)
