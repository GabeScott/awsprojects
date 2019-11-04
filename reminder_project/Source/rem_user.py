import sys

user = sys.argv[1].lower()

userfile = open("users.txt", "r")

userfilelines = userfile.readlines()

index_to_remove = 0

for line in userfilelines:
    lineparts = line.split(" ")
    if lineparts[0] == user:
        break;
    index_to_remove += 1

userfile.close()

newusers = open("users.txt", "w")

index = 0

for line in userfilelines:
    lineparts = line.split(" ")
    if index != index_to_remove:
        newusers.write(lineparts[0] + " " + lineparts[1])
    index += 1

newusers.close()


