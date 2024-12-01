# Input a string
inputstring = input("Enter a string: ")

# 1. Length of the string
print("\n1. Length of the string:")
print(len(inputstring))

# 2. Convert to uppercase
print("\n2. Convert to uppercase:")
print(inputstring.upper())

# 3. Convert to lowercase
print("\n3. Convert to lowercase:")
print(inputstring.lower())

# 4. Count occurrences of a substring
substring = input("\nEnter a substring to count its occurrences: ")
print(f"Occurrences of '{substring}':", inputstring.count(substring))

# 5. Check if the string starts with a specific substring
start_substring = input("\nEnter a substring to check if the string starts with it: ")
print(f"Does the string start with '{start_substring}'?:", inputstring.startswith(start_substring))

# 6. Check if the string ends with a specific substring
end_substring = input("\nEnter a substring to check if the string ends with it: ")
print(f"Does the string end with '{end_substring}'?:", inputstring.endswith(end_substring))

# 7. Find the index of a substring
search_substring = input("\nEnter a substring to find its index: ")
index = inputstring.find(search_substring)
if index != -1:
    print(f"First occurrence of '{search_substring}' is at index:", index)
else:
    print(f"'{search_substring}' not found in the string.")

# 8. Replace a substring with another
to_replace = input("\nEnter the substring to replace: ")
replacement = input("Enter the replacement string: ")
print("After replacement:", inputstring.replace(to_replace, replacement))

# 9. Split the string into a list of words
print("\n9. Split the string into words:")
words = inputstring.split()
print("List of words:", words)

# 10. Join a list of strings into a single string
separator = input("\nEnter a separator to join words: ")
print("Joined string:", separator.join(words))

# 11. Reverse the string
print("\n11. Reverse the string:")
print("Reversed string:", inputstring[::-1])
