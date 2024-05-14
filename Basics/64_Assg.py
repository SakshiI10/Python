# Write a Python Program to accept the strings which contain all consonants.

def contains_all_consonants(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    string_set = set(string)
    return string_set.isdisjoint(vowels)

def main():
    string = input("Enter a string: ")
    if contains_all_consonants(string):
        print("The string contains all consonants.")
    else:
        print("The string does not contain all consonants.")

if __name__ == "__main__":
    main()
