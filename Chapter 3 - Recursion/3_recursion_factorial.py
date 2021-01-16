def fat(num):
    if (num == 1):  # base case
        return 1
    else:           # recursive case
        return num * fat(num-1)

def main():
    print("** Let's learn RECURSION through a factorial calculation **")
    num = input("> Put a number to calculate its factorial: ")
    print("> The calculated factorial is:", fat(int(num)))

if __name__ == "__main__":
    main()