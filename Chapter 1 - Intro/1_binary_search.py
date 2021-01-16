def main():
    n = int(input("> Enter number of elements (list): "))
    lst = []

    for i in range(0, n):
        ele = int(input(">> Element " + str(i) +": "))
        lst.append(ele)
	
    number_to_find = input("> Enter the integer to find: ")
    number_to_find = int(number_to_find)

    print("** First requirement for Binary Search -> To be a Sorted List **")

    input_list = sortlist(lst)

    print("Sorted list: ", input_list)

    position = binary_search(input_list, number_to_find)

    if position is None:
        print ("** Integer not find **")
    else:
        print ("** Integer "+str(input_list[position])+" found at position " + str(position) + " **")

def sortlist(input_list):
    return sorted(input_list)

def binary_search(input_list, item):
    lower_index = 0
    higher_index = len(input_list) - 1

    while (lower_index <= higher_index):
        middle = (lower_index + higher_index) // 2
        guess = input_list[middle]

        if guess == item:
            return middle
        if guess > item:
            higher_index = middle - 1
        else:
            lower_index = middle + 1

    return None

if __name__ == "__main__":
    main()