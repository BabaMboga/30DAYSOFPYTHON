import re

def remove_parenthesis(string_list):
    pattern = r'\s*\([^)]*\)'
    filtered_list = []

    for string in string_list:
        filtered_string = re.sub(pattern, '', string)
        filtered_list.append(filtered_string.strip())

    return filtered_list

data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
result = remove_parenthesis(data)
print(result)