

def add():
    name = input("Account: ")
    password = input("Password: ")
    with open("Passwords.txt", "a") as f:
        f.write(name + " | " + password +"\n")

def view():
    with open("Passwords.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())

def remove():
    data=[]
    with open("Passwords.txt", "r+") as f:
        lin_nbr= input("Which line would you like to delete? (First line starts with 0): " + "\n")
        data = f.readlines()
        f.seek(0)
        f.truncate()
        for number, line in enumerate(data):
            if number != int(lin_nbr):
                f.write(line)

def delete():
    with open("Passwords.txt", "r+") as f:
        f.seek(0)
        f.truncate()
        
while True:
    mode = input("Would you like to add new password or view existing ones? (add/view) or type command for more commands. (Q to exit): " + "\n")
    if mode.lower()=='q':
        break

    if mode.lower() == "add":
        add()
    elif mode.lower() == "view":
        view()
    elif mode.lower() == "command":
        print("-delete: to delete a whole password page")
        print("-remove: To remove a line of passwords.")
    elif mode.lower() == "remove":
        remove()
    elif mode.lower() == "delete":
        delete()
    else:
        print("Invalid Option")
