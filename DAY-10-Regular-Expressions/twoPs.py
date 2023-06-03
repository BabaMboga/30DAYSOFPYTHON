import re

#dont have to be consecutive
def start_with_p(word_list):
    pattern = r'^P\w+'
    counter = 0
    
    for word in word_list:
        if re.match(pattern, word):
            counter += 1
        
        if counter == 2:
            return True

    return False

#Example usage
words = ["Pendejo", "Mandas","Python","Miguel","Permasean" ]
result = start_with_p(words)
print(result)

#must be consecutive
import re

def check_words_start_with_p(word_list):
    pattern = r'^P\w+'
    count = 0

    for word in word_list:
        if re.match(pattern, word):
            count += 1

    return count == 2

# Example usage
words = ["Palindrome", "Program", "Solo", "Penguin"]
result = check_words_start_with_p(words)
print(result)  # Output: True