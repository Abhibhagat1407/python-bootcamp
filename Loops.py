



# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1

# print(count)


#######printing numbers reverse ######
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1



#######printing numbers 1-100 ######
# j = 1
# while j <= 100:
#     print(j)
#     j += 1


######print the multiplication table of number n ########

# n = 1
# while n <= 10:
#     print(3*n)
#     n +=1

# heroes = ["supernam", "batman", "ironman", "thor"]
# idx = 0
# while idx < len(heroes):
#     print(heroes[idx])
#     idx += 1



# nums = (1, 4, 9, 16, 24, 36 ,70 ,85, 88)

# x = 70

# i = 0


# while i < len(nums):
#     if (nums[i] == x ):
#         print("Found at index", i)
#     else: print("finding")
#     print("finding")
#     i += 1
        

####################################





# i = 1

# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     else:
#         print("finding...")
#     i += 1

# print("end of the loop...")



####################################



# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

# x = 36

# i = 0

# while i < len(nums):
#     if (nums[i] == x ):
#         print("found at index", i)
#         break
#     else:
#         print("finding..")
#         i += 1
# print("print end the loop")




#################################### for loop ##########


# vagies = ["tomato", "brinjal", "ladyfinger", "potato"]

# for val in vagies:
#     if(val == "ladyfinger"):
#         print("ladyfinger found...")
#         break
#     print(val)
# else:
#     print("END")



###### find number using loop #########

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# x = 49
# idx = 0

# for el in nums:
#     if(el == x):
#         print("number found at index", idx)
#         break
#     idx += 1


#######range(stop)

# for i in range(5):  
#     print(i) 


######range(start, stop)


# for i in range(4,10):
#     print(i)



########range(start, stop, step)

# for i in range(2, 10, 2):
#     print(i)




###### print table of number n

# n = int(input("enter number:"))

# for i in range(1, 11):
#     print(n * i)



###### using pass statement 


# for i in range(5):
#     pass
# print("passing this loop for future work, this when one of the resone pass is used")



####### assignment: print the total addition of the numbers in range

n = 5

sum = 0 

for i in range(1 , n+1):
    sum  += i
print("Total sum of the range =",sum)
