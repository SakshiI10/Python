# Create and write to the file first
f = open('newfile.txt', 'w')  
f.write("This file was created with 'w' mode.\n")
f.close()

# Now open the file again in read mode and print its content
f = open('newfile.txt', 'r')
print(f.read())
f.close()

# Open the file again in append mode so it doesn't overwrite
with open('newfile.txt', 'a') as f:
    f.write("Created and written using with-block.\n")

# Re-open for reading
f = open('newfile.txt', 'r')
print(f.read()) 
f.close()


