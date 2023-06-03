import re

def remove_vowels(txt):
    vowels = 'aeiouAEIOU'
    pattern = "[" + vowels + "]"
    result = re.sub(pattern, "", txt)
    return result

txt = "Hello World!"
result = remove_vowels(txt)
print(result)