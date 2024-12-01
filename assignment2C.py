# Step 1: Create an empty list
myList = []
print("Initial empty list:", myList)

# Step 2: Append elements to the list
print("\nAppending elements to the list:")
myList.append(10)
myList.append(20)
myList.append(30)
print("List after appending 10, 20, 30:", myList)



# Step 4: Append more elements
print("\nAppending more elements (40, 50):")
myList.append(40)
myList.append(50)
print("List after appending 40, 50:", myList)

# Step 5: Remove an element using pop()
print("\nRemoving an element using pop():")
popped_element = myList.pop()  # Removes the last element
print("Popped element:", popped_element)
print("List after popping:", myList)

# Step 6: Clear the list
print("\nClearing the entire list:")
myList.clear()
print("List after clearing:", myList)
