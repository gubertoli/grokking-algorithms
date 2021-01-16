def find_lower(input_list):
    lower = input_list[0]
    lower_index = 0

    for i in range(1, len(input_list)): # starting from 1 because index 0 is already set
        if input_list[i] < lower:   # if current lower is greater than actual value
            lower = input_list[i]   # replace lower by this new lower
            lower_index = i         # save the index of the actual lower

    return lower_index

def main():   # SELECTION SORT
    n = int(input("> Enter number of elements (list): "))
    input_list = []

    for i in range(0, n):
        ele = int(input(">> Element of index " + str(i) + ": "))
        input_list.append(ele)

    print("> Current list: ", input_list)

    sorted_list = []
    for i in range(len(input_list)):
        lower = find_lower(input_list)
        sorted_list.append(input_list.pop(lower))

    print("> Sorted list (using Selection Sort): ", sorted_list)

if __name__ == "__main__":
    main()

