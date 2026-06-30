def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num%2==0 or num < 2:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num%i==0:
            return False
    return True

print(f"Is 11 prime? {is_prime(11)}")
print(f"Is 12 prime? {is_prime(12)}")