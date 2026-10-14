import random
import math
from typing import Tuple

class NaiveRSA:
    """Straightforward RSA implementation using textbook algorithms.

    Attributes:
        key_size: Desired modulus size in bits.
    """

    def __init__(self, key_size: int = 512):
        self.key_size = key_size

    def _is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def _generate_prime(self) -> int:
        while True:
            # generate an odd candidate of appropriate bit length
            candidate = random.getrandbits(self.key_size // 2) | 1
            if self._is_prime(candidate):
                return candidate

    def _gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def _modinv(self, e: int, phi: int) -> int:
        # extended Euclidean algorithm (naive version)
        def egcd(a: int, b: int) -> Tuple[int, int, int]:
            if a == 0:
                return (b, 0, 1)
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)
        g, x, _ = egcd(e, phi)
        if g != 1:
            raise ValueError('e and phi are not coprime')
        return x % phi

    def _modexp(self, base: int, exp: int, mod: int) -> int:
        result = 1
        for _ in range(exp):
            result = (result * base) % mod
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
