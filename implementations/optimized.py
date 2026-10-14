import random
import math
from typing import Tuple

class OptimizedRSA:
    """RSA implementation using binary exponentiation and Euclidean GCD."""

    def __init__(self, key_size: int = 512):
        self.key_size = key_size

    def _is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        r = int(math.isqrt(n))
        for i in range(3, r + 1, 2):
            if n % i == 0:
                return False
        return True

    def _generate_prime(self) -> int:
        while True:
            candidate = random.getrandbits(self.key_size // 2) | 1
            if self._is_prime(candidate):
                return candidate

    def _gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def _modinv(self, e: int, phi: int) -> int:
        # extended Euclidean algorithm (iterative)
        old_r, r = e, phi
        old_s, s = 1, 0
        while r != 0:
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
        if old_r != 1:
            raise ValueError('e and phi are not coprime')
        return old_s % phi

    def _modexp(self, base: int, exp: int, mod: int) -> int:
        result = 1
        base = base % mod
        while exp > 0:
            if exp & 1:
                result = (result * base) % mod
            exp >>= 1
            base = (base * base) % mod
        return result

    def generate_keys(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        p = self._generate_prime()
        q = self._generate_prime()
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537
        while self._gcd(e, phi) != 1:
            e += 2
        d = self._modinv(e, phi)
        return (e, n), (d, n)

    def encrypt(self, message: int, pub_key: Tuple[int, int]) -> int:
        e, n = pub_key
        return self._modexp(message, e, n)

    def decrypt(self, cipher: int, priv_key: Tuple[int, int]) -> int:
        d, n = priv_key
        return self._modexp(cipher, d, n)
