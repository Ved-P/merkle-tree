import hashlib
from base64 import b64encode

def hash_leaf(leaf):
    """hash a leaf value."""
    sha256 = hashlib.sha256()
    sha256.update(b"leaf:") # hash prefix for a leaf
    sha256.update(leaf)
    return sha256.digest()

def hash_internal(left, right):
    """hash an internal node."""
    sha256 = hashlib.sha256()
    sha256.update(b"node:") # hash prefix for an internal node
    sha256.update(left)
    sha256.update(right)
    return sha256.digest()

def bytes2b64(data):
    """convert hash to printable base64 string"""
    return b64encode(data).decode("utf-8")

def bytes2str(data):
    """convert node data (in bytes) to string before printing"""
    return data.decode("utf-8")

def str2bytes(data):
    """convert node data (in string) to bytes before hashing"""
    return data.encode()