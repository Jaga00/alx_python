# a function that replaces or adds key/value in a dictionary.

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

my_dict = {'name': 'John', 'age': 30}
update_dictionary(my_dict, 'city', 'New York')  # Add 'city': 'New York'
update_dictionary(my_dict, 'age', 31)           # Update 'age' to 31

print(my_dict)