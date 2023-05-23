original_string = input("Enter the word you would like to create a new word: ")

def new_word(original_string):
    if len(original_string) < 2:
        return ''
    else:
        return original_string[:2] + original_string[-2:]
    
result = new_word(original_string)
print(result)