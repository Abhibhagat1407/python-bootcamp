# a = 7
# b = 8

# sum = a + b
# print(sum)



# def calc_sum(a, b):  #parameters 
#     return a + b

# sum = calc_sum(7, 8)  # function call; arguments
# print(sum)


#### calculate total numbers of average

# def calc_average(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# calc_average(85, 84, 86)



############# simple function for listing number of elemnts in the list 


cities = ["mumbai","delhi","pune", "noida","nashik","nagpur" ]
heroes = ["thor", "ironman", "captain amarica", "shaktiman"]

def num_of_elemnts(list):
    print(len(list))


num_of_elemnts(cities)
num_of_elemnts(heroes)