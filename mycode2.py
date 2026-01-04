numbers = []

sum = 0
for item in range(5):
    number = int(input("Enter a number: "))

    if 0 < number < 20:
        sum = sum + number
        numbers.append(number)

print(numbers)
print(sum / len(numbers))
