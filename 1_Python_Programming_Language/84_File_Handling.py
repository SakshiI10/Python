# Create and write to the file first
f = open('newfile.txt', 'w')  
f.write("This file was created with 'w' mode.\n")
f.close()

# Now open the file again in read mode and print its content
f = open('newfile.txt', 'r')
print(f.read())
f.close()

# Open the file for writing again
with open('newfile.txt', 'w') as f:
    f.write("Created and written using with-block.\n")

# Re-open for reading (you need to open in 'r' mode to read)
f = open('newfile.txt', 'r')
print(f.read()) 
f.close()

