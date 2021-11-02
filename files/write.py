#w write on a file
#w in this mode an existing info is replaced
#file.write() function write text to file
with open('write.txt','w') as file_to_write:
    file_to_write.write("Am writing on you idiot ")

#Appending to a file
#we use 'a'
#\n introducing line breaks
name = input("What is your name idiot ? ")
with open('write.txt','a') as file_to_write:
    file_to_write.write('\n'+ name)
