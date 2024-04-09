import sys

from collections import deque

from utils import hash_internal, hash_leaf, bytes2b64, bytes2str, str2bytes

from prover import generate_merkle_proof

def compute_merkle_root(proof, pos, data):

    _proof = deque(proof)
    _pos = pos
    
    _h = hash_leaf(str2bytes(data))
    while _proof:
        if _pos % 2 == 0:
            left, right = _h, _proof.popleft()
        else:
            left, right = _proof.popleft(), _h
        _h = hash_internal(left, right)
        _pos >>= 1
    
    # reach root and return
    return _h

def verify(fpt, pos):

    # read public data
    nodes = [] # List[str]
    with open(fpt, "r") as f:
        raw = f.readlines()

    # first line is the hash of root
    expected_hash_root_b64 = raw[0].strip()
    # then read all remaining data and hashes
    for i in range(1, len(raw)):
        n, _ = raw[i].split(" | ")
        nodes.append(n)

    assert pos < len(nodes), \
        f"Invalid pos, expected: < {len(nodes)}, got: {pos}"
    
    actual_proof = generate_merkle_proof(nodes, pos)
    actual_hash_root = compute_merkle_root(actual_proof, pos, nodes[pos])
    actual_hash_root_b64 = bytes2b64(actual_hash_root)
    print(f"expected root (b64): {expected_hash_root_b64}")
    print(f"actual root (b64): {actual_hash_root_b64}")
    assert expected_hash_root_b64 == actual_hash_root_b64, \
        f"Verification failed"
    
if __name__ == "__main__":
    
    assert len(sys.argv)-1 == 2, \
        f"Invalid number of arguments, expected: 2, got: {len(sys.argv)-1}"

    fpt = sys.argv[1]
    pos = int(sys.argv[2])
    
    verify(fpt, pos)