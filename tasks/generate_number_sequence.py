def print_sequence(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i)
    print(result)

if __name__ == '__main__':
    n = int(input().strip())
    print_sequence(n)
