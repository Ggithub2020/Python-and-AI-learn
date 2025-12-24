# print number from 1 to 5
# while => run until something happens
# count =0
# while count<5:
#     print(count)
#     count+=1 #count =count +1

# #exmple count evens only below 100
# count =0
# while count < 50:
#     if count % 2 == 0:  # Check if the number is even
#         print(count)
#     count += 1  # Increment the count by 1

# for num in range (1, 10,2):
#     if num % 2 == 0:  # Check if the number is even
#         print(num)  # Print the even number

# for num in range(10): # rand(0,10,1)
#     if num==5:
#         break
#     print(num)

for num in range(10): # rand(0,10,1)
    if num==5:
        continue
    print(num)