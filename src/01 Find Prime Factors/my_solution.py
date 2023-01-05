def get_prime_factors(factor):
    answer = []
    done = False
    num = 2
    while not done:
        if factor % num == 0:
            answer.append(num)
            factor = factor / num
        else:
            num += 1
        if num > factor:
            done = True

    return answer

h = input("Please give a number to find its prime factors: ")
print(get_prime_factors(int(h)))
