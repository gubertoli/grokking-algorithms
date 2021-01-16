import random

def quicksort(array):
    if len(array) < 2:
        # base case
        return array
    else:
        # recursive case
        pivot = array.pop(random.choice(range(0,len(array)))) # choose a random pivot
        print(">> Chosen pivot: ", pivot)

        lower = [i  for i in array if i <= pivot] # get all elements lower than pivot
        higher = [i for i in array if i  > pivot] # get all elements greater than pivot
        return quicksort(lower) + [pivot] + quicksort(higher) # divide and conquer! recursive!

def main():
    n = int(input("> Enter number of elements (list): "))
    input_list = []

    for i in range(0, n):
        ele = int(input(">> Element of index " + str(i) + ": "))
        input_list.append(ele)

    print("> Current list: ", input_list)

    print("> Sorted list (using Quicksort): ", quicksort(input_list))

if __name__ == "__main__":
    main()