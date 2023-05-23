string = 'google.com'

def count_char(string):
    frequency_dict = {}
    for char in string:
        keys = frequency_dict.keys()
        if char in keys:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

freq = count_char(string)
print(freq)