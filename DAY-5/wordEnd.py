original_string = input("Enter word you like to manipulate: ")

def string_end_manipulation(original_string):
    if len(original_string) < 3:
           return original_string
    elif original_string[-3:] == 'ing':
          return original_string + 'ly'
    else:
          return original_string + 'ing'
    
new_word = string_end_manipulation(original_string)
print(new_word)