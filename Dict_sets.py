
####Question: store following mening in a python dictiornary


# iteams = {
#     "table" : ["a piece of furniture", "list of facts and figures"],

#     "cat" : "a small animal"
    

# }

# print(type(iteams))


#####Question: each subject will required to have seprate classroom, then how many classroom required?



# classroom = {
#     "subjects" : ["c++", "python", "java", "go"] 
# }
# total_classroom = len(classroom["subjects"])
# print(total_classroom)



#####Question: WAP to enter marks of 3 subject from user and store in them in the dictionary, start with empty dictionary & add one by one. use sub name as key and marks as value

subject_1 = input("enter chem marks: ")
subject_2 = input("enter phy marks: ")
subject_3 = input("enter math marks: ")


subject = {

    "chem" : subject_1,
    "phy" : subject_2,
    "math" : subject_3
 
}

print(subject)
