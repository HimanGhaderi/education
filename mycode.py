for item in range(5):
    number = input("Please enter the number : ")

    if len(number)>5:
        print("The number len grater than 5")
        continue

    sum = 0
    for num in number:
        sum += int(num)

    if sum % 2 == 0:
        print(number)
