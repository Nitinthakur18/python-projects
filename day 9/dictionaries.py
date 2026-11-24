empty_dict={}
# print(empty_dict)
programming_dictionary={
    "Bug":"An error in a program that prevents the program from running as excepted.",
    "Function":"A piece of code that you can easily call over and over again.",
    "Loop":"the action of doing something over and over again."
}
# print(programming_dictionary)


print(programming_dictionary.keys())
print(programming_dictionary.values())
# iterating through a dictionary
for item in programming_dictionary:
    print(item)
    print(programming_dictionary[item])
  