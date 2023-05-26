# question for faith
# can we have a user input a list directly ?
input_list = ['g','o','o','g','l','e','c','o','m']

def remove_duplicates(input_list):
    new_list = []
    for n in input_list:
        if n not in new_list:
            new_list.append(n)
    return new_list

result = remove_duplicates(input_list)
print(result)
