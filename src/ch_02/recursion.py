# coprime using recursion

def is_primer(n: int) -> bool:
    def is_prime(k: int, coprime: int) -> bool:
        """Is k relatively prime to the value coprime?"""
        if k < coprime * coprime:
            return True
        if k % coprime == 0:
            return False
        return is_prime(k, coprime + 2)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return is_prime(n, 3)


if __name__ == '__main__':
    print(is_primer(13))
