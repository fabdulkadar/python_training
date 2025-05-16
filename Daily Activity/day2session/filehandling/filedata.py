#Write a file
# w mode will overwrite the file if it exists

f = open("test.txt","w")
f.write("Hello World")
print("File Written Successfully")
f.close()

#Read a file
f=open("test.txt", "r")
print(f.read())
print("File Read Successfully")
f.close