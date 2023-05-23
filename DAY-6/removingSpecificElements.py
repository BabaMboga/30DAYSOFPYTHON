old_list = ['Red','Green','White','Black', 'Pink', 'Yellow']
positions_to_remove = [0, 4, 5]

def remove_data(lst,indices):
    new_list = [lst[i] for i in range(len(lst)) if i not in indices]
    return new_list

ans = remove_data(old_list,positions_to_remove)
print(ans)