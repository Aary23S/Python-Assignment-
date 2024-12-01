# Initialize a set
mySet = {1, 2, 3, 4, 5}

print("Original Set:", mySet)

# 1. add()
mySet.add(6)
print("After using add(6):", mySet)

# 2. remove()
mySet.remove(3)
print("After using remove(3):", mySet)


# 3. discard()
mySet.discard(2)
print("After using discard(2):", mySet)

# Discarding a non-existent element (no error)
mySet.discard(10)
print("After using discard(10) on a non-existent element:", mySet)

# 4. pop()

popped_element = mySet.pop()
print(f"Popped element: {popped_element}")
print("After using pop():", mySet)


# 5. clear()
mySet.clear()
print("After using clear():", mySet)
