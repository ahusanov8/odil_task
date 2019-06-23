def alphan_sort(val):  
    """  sort"""  
    numbers =[]
    lowercase =[]
    uppercase =[]
    sorted_list = []

    for char in val:
        # lowercase characters
        if (char.islower):
            lowercase.append(char)
        
        # numbers
        if (char.isnumeric):
            numbers.append(char)

        # upper cases
        if (char.isupper):
            uppercase.append(char) 

    # create sorted list 
    sorted_list.extend(sorted(numbers))
    print(sorted_list)
    sorted_list.extend(sorted(lowercase))
    print(sorted_list)
    sorted_list.extend(sorted(uppercase))

    return sorted_list

    # val = "".join(sorted(val))
    # return val


print (alphan_sort('A11a4'))

# unit tests
