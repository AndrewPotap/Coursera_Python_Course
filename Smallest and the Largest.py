largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done": break
    try:
        num = float(num)
    except:
        print('Invalid input')
        continue
    if largest is None or smallest is None:
        largest = num
        smallest = num
    elif smallest > num:
        smallest = num
    elif num > largest:
        largest = num
print("Maximum is", int(largest))
print("Minimum is", int(smallest))
