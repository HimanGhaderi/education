

# full_name = "wwwwwwwwwwReza Ahmadi lkdjfldj lkdjfldfj lkjdfldjf kdjfljldfj   ebrahim kdjfhiodjfd ldijfiod"


# d = {}
# for ch in full_name:
#     if ch in d:
#         d[ch] += 1
    
#     else:
#         d[ch] = 1

# print(d)


# for ch in full_name:
#     d[ch] = d.get(ch, 0) + 1

# print(d)



name = input("Please enter your name: ")
password = input("Please enter your password: ")

file = open("users.txt", "a")
file.write(name + ":" + password + "\n")
file.close()