"""
Kolton Chiu
This programs prints the initial letters of the users input.
"""
#Get user's full name
user_name = input("")

#Splits the user's name
user_name = user_name.split()

#Get first letter of name & make it upper case
#https://www.w3schools.com/python/ref_string_join.asp
#https://www.w3schools.com/python/ref_string_upper.asp
initial_upper = [i[0].upper() for i in user_name]
final_initial = "".join(initial_upper)
print (final_initial + "\n") 
