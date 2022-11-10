command = input()
prime_num = 0
non_prime_num = 0
while command != "stop":
    current_num = int(command)

    if current_num < 0:
        print(f"Number is negative.")
        command = input()
        continue

    count = 0
    for i in range (1, current_num + 1):
        if current_num % i == 0:
            count += 1

    if count == 2:
        prime_num += current_num
    else:
        non_prime_num += current_num

    command = input()

print(f"Sum of all prime numbers is: {prime_num}")
print(f"Sum of all non prime numbers is: {non_prime_num}")