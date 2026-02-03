

def login(username, password):
    file = open("users.txt", "r")

    for line in file:
        line = line.replace("\n", "")
        line_split = line.split(":")
        user_read = line_split[0]
        password_read = line_split[1]

        if username == user_read and password == password_read:
            print(f"welcome {username}")
            file.close()
            return True
        
    file.close()
    return False

def register(username, password):
    file = open("users.txt", "a")
    file.write(f"{username}:{password}\n")
    file.close()

    return f"username:{username} and password: {password} inserted "




while True:
    username_input = input("Please enter your username: ")
    password_input = input("Please enter your password: ")

    result = login(username_input, password_input)

    if result==True:
        print("You are login in website")
        break

    else:
        print("Your username and password not found in my site")

        request = input(f"Do your want register with username: {username_input}, password: {password_input} yes/no: ")
        
        if request == "yes":
            register(username_input, password_input)