#we use "open()" function to open files
#'r' (read) mode
#file.read() function to read file content

with open('hello.txt','r') as file_to_read:
    print(file_to_read.read())