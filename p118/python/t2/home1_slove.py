


# text = "Adlkfj fddfdf dfdfdf dfdffd dfdfa';opipoei  ereojflkdfmFP"

# d = {}
# for ch in text:
#     if ch in d:
#         d[ch] += 1
#     else:
#         d[ch] = 1

# print(d)



# file = open("users.txt", "a")

# while True:
#     name = input("Please enter your name or end: ")
#     if name == "end":
#         break
#     file.write(name + "\n")

# file.close()



# file = open("users.txt", "r")

# users = []
# for radif in file:
#     users.append(radif.replace("\n", ""))

# file.close()



# file = open("users.txt", "a")

# while True:
#     name = input("Please enter your name or end: ")
#     if name == "end":
#         break
#     if name in users:
#         print("This name exist, please try another name.")
#         continue
#     file.write(name + "\n")
#     users.append(name)
# file.close()




# counter = 0
# sum = 0
# li = []
# while True:
#     number = input("Please enter number or end: ")
#     if number != "end":
#         number = float(number)
#         li.append(number)
#         sum = sum + number
#         counter += 1
#     else:
#         break

# print(li)
# print(sum)
# print(sum/counter)



# def average(li):
#     sum = 0
#     counter = 0
#     for item in li:
#         sum = sum + item
#         counter += 1

#     return sum/counter


# result = average([1,2,3,45,6])
# print(result)



# ===============================================





# f= [1,2,3,45,6]
# sum = 0
# counter = 0
# for item in li:
#     sum = sum + item
#     counter += 1

# print(sum/counter)


# l = [1,5,23,6,5,9, 10]
# sum = 0
# counter = 0
# for item in l:
#     sum = sum + item
#     counter += 1

# print(sum/counter)
# ===============================================



# def average(li):
#     sum = 0
#     counter = 0
#     for item in li:
#         sum = sum + item
#         counter += 1

#     return sum/counter



# result = average(l)
# print(result)
# result = average(f)
# print(result)

# ===============================================

# number = input("Please enter the number: ")
# number = int(number)
# flag = True

# for item in range(2, number):
#     if number % item == 0:
#         flag = False
#         print("Then number is not aval")
#         break
# if flag:
#     print("The number is aval")

# ==============================================
# def aval(number):

#     for item in range(2, number):
#         if number%item==0:
#             return "aval nist"
    
#     return "aval ast"

# number = input("Please enter the number: ")
# number = int(number)

# result = aval(number)
# print(result)

# ===============================================


# number1 = input("Please enter number 1:")
# number2 = input("Please enter number 2: ")


# li = [1,2,3]
# d = {1:1, 2:2}
# try:
#     number1 = int(number1)
#     number2 = int(number2)
#     print(number1/number2)
#     print(li[1])
#     print(d[5])
# except ZeroDivisionError as e:
#     print("The number 2 is zero")
# except IndexError as e:
#     print("KeyError ")
# except KeyError as e:
#     print("KeyError")
# except Exception as e:
#     print("The input data is not integer")

# ========================================


def min_max(li: list) ->tuple:
    "give the list and return th min and max"
    min = li[0]
    max = li[0]
    
    for item in  li:
        if min > item:
            min = item
        if max < item:
            max = item
    
    return min, max

min_max()

my_min, my_max = min_max([10,5,12,18,3,2])

print(my_min)
print(my_max)
