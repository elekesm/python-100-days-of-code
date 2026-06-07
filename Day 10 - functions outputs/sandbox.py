def my_function():
    result = 3 * 4
    return result

# print(my_function())


#DOCSTRING
def format_name(first_name, last_name):
    """Formats the first and last name by capitalizing the first letter of each."""
    form_f_name = first_name.capitalize()
    form_l_name = last_name.capitalize()
    return f"{form_f_name} {form_l_name}"

def welcome_message(name):
    return f"Welcome, {name}!"

formatted_name = format_name("joHn", "doE")
print(welcome_message(formatted_name))