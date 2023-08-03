attempts = 1
new = 2
a = 1
while attempts < new: 
    attempts += 1
    new += 1
    password = input("Enter a password: ")
    space = password.count(" ")
    special1 = password.count("#")
    special2 = password.count("@")
    if(len(password) >= 8 and space == 0):
        if(special1 >= 1 or special2 >= 1):
            for i in range(len(password) - 1):
                    if password[i] != password[i + 1]:
                        a+= 1
                        if a == len(password):
                            print("This is acceptable, program terminating")
                            new = 0
    else:
        print("This is unacceptable, try again")
                            