def min_max(lst):
    min_prime = None
    max_non_prime = None

    for num in lst:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break

            else:
                if min_prime is None or num < min_prime:
                    min_prime = num

        if max_non_prime is None or num > max_non_prime:
            max_non_prime = num

    return min_prime, max_non_prime


print(min_max([6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]))  # (3, 13)
