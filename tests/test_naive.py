import pytest
from implementations.naive import NaiveRSA

@pytest.fixture
def rsa():
    return NaiveRSA(key_size=256)  # smaller for fast test

def test_key_generation(rsa):
    pub, priv = rsa.generate_keys()
    e, n = pub
    d, n2 = priv
    assert n == n2
    assert e != d

def test_encrypt_decrypt(rsa):
    pub, priv = rsa.generate_keys()
    message = 12345
    cipher = rsa.encrypt(message, pub)
    plain = rsa.decrypt(cipher, priv)
    assert plain == message

def test_edge_zero(rsa):
    pub, priv = rsa.generate_keys()
    cipher = rsa.encrypt(0, pub)
    plain = rsa.decrypt(cipher, priv)
    assert plain == 0
