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
    
    # The length of state is the length of the bottom row of the tree.
    len_row = len(state)

    # Continue until we reach the top row of the tree...
    while (len_row > 1):

        # If the node is a left node, the proof needs the
        # corresponding right node.
        if (pos % 2 == 0):
            proof.append(state[pos + 1])

        # If the node is a right node, the proof needs the
        # corresponding left node.
        else:
            proof.append(state[pos - 1])

        # Calculate the next row of the tree and fit it into the
        # start of the state list to save memory.
        # Note: len_row >> 1 is the same as len_row / 2 because
        # len_row must be even
        for i in range(0, len_row >> 1): 
            left_hash = state[2 * i]
            right_hash = state[2 * i + 1]
            state[i] = hash_internal(left_hash, right_hash)

        # Update the length of the new row and the new position.
        len_row >>= 1                # Divide by 2 and truncate.
        pos >>= 1
    
    # ============================= #
    # ==== your code ends here ==== #
    # ============================= #
    
    return proof