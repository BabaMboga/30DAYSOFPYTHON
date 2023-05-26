def sort_dict ():
    sample_data = {'Math':81, 'Physics':83, 'Chemistry':87}

    expected_data = sorted(sample_data.items(), key=lambda x: x[1], reverse=True)
    return expected_data

print(sort_dict())