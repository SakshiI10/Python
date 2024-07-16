# Print words in a sentence in reverse order

st=input("Enter string: ")
words=st.split()
words=words[-1::-1]
output=' '.join(words)
print(output)