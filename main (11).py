num1 = int(input("First number " ))

num2 = int(input("Second number " ))

num3 = int(input("Third number " ))

num4 = int(input("Fourth number " ))

num5 = int(input("Fifth number " ))

num6 = int(input("Sixth number " ))

num7 = int(input("Seventh number " ))

num8 = int(input("Eighth number " ))

num9 = int(input("Ninth number " ))

num10 = int(input("Tenth number " ))


total = 0
count = 0

if num1 > 0:
    total += num1
    count += 1

if num2 > 0:
    total += num2
    count += 1

if num3 > 0:
    total += num3
    count += 1

if num4 > 0:
    total += num4
    count += 1

if num5 > 0:
    total += num5
    count += 1

if num6 > 0:
    total += num6
    count += 1

if num7 > 0:
    total += num7
    count += 1

if num8 > 0:
    total += num8
    count += 1

if num9 > 0:
    total += num9
    count += 1

if num10 > 0:
    total += num10
    count += 1

if count > 0:
    average = total / count
    print("Average of positive numbers is:", average)
else:
    print("There are no positive numbers.")

    
    