def numbers_searching(*args):
    first_el = args[0]
    last_el = args[-1]
    missing_number = 0
    temp_list = set(args)
    duplicated_numbers = []
    final_list = []

    if first_el < last_el:
        for index in range(len(args)):
            if args[index] + 1 == args[index+1]:
                continue
            elif args[index] + 1 != args[index+1]:
                missing_number = args[index] + 1
                final_list.append(missing_number)
                break
    else:
        args_b = list(set(args))
        for index in range(len(args_b)):
            if args_b[index] + 1 == args_b[index+1]:
                continue
            elif args_b[index] + 1 != args_b[index+1]:
                missing_number = args_b[index] + 1
                final_list.append(missing_number)
                break

    for el in temp_list:
        counter = 0
        for i in args:
            if el == i:
                counter += 1
                if counter >= 2:
                    duplicated_numbers.append(el)

    final_list.append(sorted(set(duplicated_numbers)))
    return final_list


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
