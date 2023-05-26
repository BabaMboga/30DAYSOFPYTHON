d1 = {'a':100,'b': 200, 'c':300}
d2 = {'a':300, 'b':200, 'd':400}

combined_dict = {}

#Add values from d1 to combined_dict first

for key, value in d1.items():
    combined_dict[key] = value

#Add values from d2 to combined_dict and update existing values

for key, value in d2.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

print(combined_dict)