rearrange_by_frequency=[4, 5, 6, 5, 4, 3, 4]
numbers={}
for index,number in enumerate(rearrange_by_frequency):
    if number==rearrange_by_frequency[index+1]:
        c+=1
        numbers={number: c}
print(numbers)