# Example 1: Checking a condition
# ============================================

# num = 10

# if num > 0:
#     print("Positive Number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative Number")
    
    
    
# Example 2: Nested conditions
# ======================================================
# age = 22

# if age > 18:
#     if age < 30:
#         print("Young Adult")
#     else:
#         print("Adult")



# Loop through a list
# ======================================================
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# Loop with range
# for i in range(10): #[0,1,2,3,4]
#     print(i)


# Count down from 5
# ======================================================
# count = 5

# while count > 0:
#     print(count)
#     count -= 1

# print("Outside While Loop")



# for i in range(10):
#     if i == 5:
#         # break
#         continue
#     print(i)

# print("Outside For Loop")


for i in range(10):
    if i % 2 == 0:
        continue
    print(i)