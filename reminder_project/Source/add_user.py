import sys

username = sys.argv[1]
address = sys.argv[2]

userfile = open("users.txt", "a")

userfile.write(username + " " + address)

userfile.close()
