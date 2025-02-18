def largest_power_of_two(n):
    power = 1
    while power <= n:
        power *= 2
    return power // 2

print(largest_power_of_two(100))
