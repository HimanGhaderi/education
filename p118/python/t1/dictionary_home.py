

# names = {
#     1: {"name": "Reza", "age": 15},
#     2: {"name": "Ebrahim", "age": 14},
#     3: {"name": "Zaniyar", "age": 20}
# }


# for item in names:
#     print("name: ", names[item]["name"], " age: ", names[item]["age"])


# students = {
#     1 : {"name": "Reza", "score": 9},
#     12 : {"name": "Ebrahim", "score": 20},
#     2548 : {"name": "Zanyar", "score": 10.75}
# }

# for item in students:
#     if students[item]["score"] >= 10:
#         print(students[item]["name"])
#         print("Pass")
#     else:
#         print(students[item]["name"])
#         print("Fail")





# products = {
#     "panir" : 120,
#     "mast": 65,
#     "roghan": 300,
#     "berenje": 30000
# }

# for item in products:
#     if products[item] > 100:
#         print(item)



# students = {}
# while True:
#     name = input("Please enter your name: ")
#     score = input("Please enter your score: ")

#     students[name] = float(score)

#     e = input("Do you want to continue: yes/exit ")
#     if e=="exit":
#         break


# sum = 0
# counter = 0
# for item in students:
#     sum = sum + students[item]
#     counter += 1

# print(students)
# print("Avg: ", sum/counter)



# li = []
# while True:
#     name = input("Please enter your name: ")
#     li.append(name)
    
#     e = input("Do you want to continue: yes/exit ")
#     if e=="exit":
#         break

# print(li)


# tamrin 9
# students = {
#     1 : {"name": "Reza", "score": 9},
#     12 : {"name": "Ebrahim", "score": 20},
#     2548 : {"name": "Zanyar", "score": 10.75},
#     125 : {"name": "Ahmad", "score": 18},
#     362 : {"name": "Aram", "score": 5.75}
# }


# max = 0
# min = 21
# for item in students:
#     score = students[item]["score"]
#     name = students[item]["name"]

#     if max < score:
#         max = score
#         name_max = name

#     if min > score:
#         min = score
#         name_min = name

# print("name max: ", name_max)
# print("name min: ", name_min)


# Tamrin 10

# students={
#     "reza": [12, 15, 17],
#     "aram": [20.,19,20],
#     "sara": [10, 12, 14]
# }

# for item in students:
#     sum = 0
#     counter = 0
#     for number in students[item]:
#         sum = sum + number
#         counter += 1
    
#     print(item, "  avg: ", sum/counter)
