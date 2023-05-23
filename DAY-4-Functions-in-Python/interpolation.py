name = input("Enter your first name: ")
age = int(input("Enter your age: "))
occupation = input("Enter your occupation: ")

def sentence(name, age, occupation):
    print (f"My name is {name}, pleasure to meet you. I am a {age} year old {occupation}.")

sentence(name, age, occupation)