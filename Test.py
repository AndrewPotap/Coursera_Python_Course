score = input("Enter Score: ")
try:
    score = float(score)
except:
    score = 0
if 0 < score < 1:
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print('F')
else:
    print("The score is out of the range or doesn't contain the decimals only")
    quit()
