import pytest
from implementations.optimized import OptimizedRSA

@pytest.fixture
def rsa():
    return OptimizedRSA(key_size=256)

def test_key_generation(rsa):
    pub, priv = rsa.generate_keys()
    e, n = pub
    d, n2 = priv
    assert n == n2
    assert e != d

def test_encrypt_decrypt(rsa):
    pub, priv = rsa.generate_keys()
    message = 98765
    cipher = rsa.encrypt(message, pub)
    plain = rsa.decrypt(cipher, priv)
    assert plain == message

def test_edge_large_message(rsa):
    pub, _ = rsa.generate_keys()
    n = pub[1]
    message = n - 1  # max valid plaintext
    cipher = rsa.encrypt(message, pub)
    plain = rsa.decrypt(cipher, rsa.generate_keys()[1])
    # Decrypt with mismatched key should not equal original
    assert plain != message
