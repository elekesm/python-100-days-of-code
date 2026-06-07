programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}
programming_dictionary_v2 = programming_dictionary

# Retrieving items from the dictionary :(
print(programming_dictionary["Bug"]) 

# Adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Printing the dictionary
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary_v2["Bug"] = "A moth in your computer."
print(programming_dictionary_v2)

# Loop through a dictionary
for key in programming_dictionary_v2:
    #print(key)
    #print(programming_dictionary_v2[key])
    print(f"{key} »» {programming_dictionary_v2[key]}")