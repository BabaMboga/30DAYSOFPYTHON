new_string = input("Enter the word for which yould like to track the letters: ")

def letter_count(string):
    track_char = {}
    for char in string:
        if char in track_char:
            track_char[char] += 1
        else:
            track_char[char] = 1

    return track_char

answer = letter_count(new_string)
print(answer)