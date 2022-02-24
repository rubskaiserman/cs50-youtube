def main():
    n = get_height()
    print_triangle(n)


def get_height():
    while True:
        try:
            n = int(input("Height: "))
        except ValueError:
            print("Invalid Value")
        if n > 0:
            break
    return n

def print_triangle(n):
    for i in range(n):
        print('#' * (i + 1))

if __name__ == "__main__":
    main()
