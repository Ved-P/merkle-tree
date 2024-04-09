import math
from utils import hash_internal, hash_leaf, str2bytes

def generate_merkle_proof(nodes, pos):

    # prepare all nodes by converting them from string to bytes
    _nodes = list(map(str2bytes, nodes))

    # compute height of merkle tree
    height = math.ceil(math.log(len(_nodes),2))

    # hash all the nodes
    state = list(map(hash_leaf, _nodes))  

    # Pad the list of hashed nodes to a power of two
    padlen = (2**height)-len(_nodes)
    state += [b"\x00"] * padlen

    # initialize a list that will contain the hashes in the proof
    proof = []

    # =============================== #
    # ==== your code starts here ==== #
    # =============================== #
    #
    #
    #
    # ============================= #
    # ==== your code ends here ==== #
    # ============================= #
    
    return proof