from collections import Counter

def calculate_earnings():
    n = int(input())
    shoe_sizes = list(map(int, input().split()))

    available_shoes = Counter(shoe_sizes)

    m = int(input())
    total_earnings = 0

    for _ in range(m):
        size, price = map(int, input().split())
        if available_shoes[size] > 0:
            total_earnings += price
            available_shoes[size] -= 1

    print(total_earnings)


if __name__ == "__main__":
    calculate_earnings()
