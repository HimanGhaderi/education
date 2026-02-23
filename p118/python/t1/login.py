



name = input("Please enter your name: ")
password = input("Please enter your password: ")


file = open("users.txt", "r")

for row in file:
    row = row.strip("\n")
    row_split = row.split(":")

    if row_split[0] == name and row_split[1]==password:
        print("you can login to website")

file.close()