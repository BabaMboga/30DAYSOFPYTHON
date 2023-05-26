num = [2,9,7,6,3,4,5,1,0,8]
target = 10

def unique_combinations(numbers,target):
    results = []
    numbers_set = set(numbers)

    for i in range(len(numbers)):
        for n in range(i + 1, len(numbers)):
            third_no = target - (numbers[i] + numbers[n])
            if third_no in numbers_set and third_no != numbers[i] and third_no !=numbers[n]:
                results.append([numbers[i], numbers[n], third_no])
    return results

combination = unique_combinations(num,target)

for combo in combination:
    print(combo)