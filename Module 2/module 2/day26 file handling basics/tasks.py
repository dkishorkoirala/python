#mini task 1
file = open("message.txt", "w")
file.write("Hello from Python!")
file.close()

#mini task 2
file1 = open("message.txt", "r")
print(file1.read())
file1.close()

#mini task 3
file2 = open("message.txt", "a")
file2.write("\nAppended line using python")
file2.close()

#mini task 4
file4 = open("ok/test.txt", "w")   #inorder to run this create a folder named ok in the code loaction
file4.write("This is a test in a subfolder.")
file4.close()