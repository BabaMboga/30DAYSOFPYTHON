first_num_list = [0,3,4,7,9]
second_num_list = [3,5,7,13]
third_num_list = [1,5,3]

def prime_number(num_list):
    for num in num_list:
        if num < 2:
            return False
        for i in range(2,int(num**0.5) + 1):
            if num % i == 0:
                return False
        
    return True

result1 = prime_number(first_num_list)
result2 = prime_number(second_num_list)
result3 = prime_number(third_num_list)

print(result1)
print(result2)
print(result3)