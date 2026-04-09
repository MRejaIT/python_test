# numbers = [1, 2, 3, 4]

# fruits = ["apple", "banana", "cherry"]

# mixed = [1, "apple", True]

# # print(numbers[2])
# # print(fruits[0])
# # print(mixed[2])

# fruits.append("orange")
# fruits.insert(1, "grape")

# print(fruits)

# sliced_fruits = fruits[2:4]
# print(sliced_fruits)

# fruits.remove("banana")
# print(fruits)

# del fruits[0]
# print(fruits)

# fruits.pop()
# print(fruits)



# #Truple 
# # ======================================================
# colors = ("red", "green", "blue")
# single_item = ("glass",)

# print(colors[0])
# print(colors[-1])


# # Dictionaries
# # ======================================================
# student = {"name": "Alice", "age": 25, "grade": "A"}

# student["subject"] = "Math"
# student["age"] = 32

# print(student)

# del student["grade"]

# print(student)

# student.pop("subject")

# print(student)



# # Iteration 
# # ======================================================
# student = {"name": "Alice", "age": 25, "grade": "A"}

# for key, value in student.items():
#     print(key, value)


# #Sets
# # ======================================================
# numbers = {1, 2, 3, 4}

# empty_set = set()

# print(numbers)
# numbers.add(8)
# print(numbers)
# numbers.remove(2)
# print(numbers)

# # Sets(Union)
# # -------------------------------------------------------
# set1 = {1, 2, 3}  
# set2 = {3, 4, 5}

# print(set1 | set2)

# # Sets (Intersection)
# # -------------------------------------------------------
# set1 = {1, 2, 3}  
# set2 = {3, 4, 5}

# print(set1 & set2)

# Sets (Difference)
# -------------------------------------------------------
set1 = {1, 2, 3}  
set2 = {3, 4, 5}

print(set1 - set2)