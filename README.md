# merkle-tree
This project contains an implementation of a merkle tree used to prove whether a piece of data exists at a certain location in a certain file. It does this by using the verifier file (starter code) to process the data and send it to the prover (part of which is written by me) which generates the Merkle Tree and determines the hashes that need to be sent to the verifier to get the result that is equivalent to the given Merkle hash.

# How to Run the Project
To run the program, use the following command:
```
python verifier.py <path-to-dataset> <pos>
```

The path to dataset is the path to the file that should contain a list of data as well as the final Merkle hash as the first line of the file.

The position is the index of the data within the file that the user wishes to verify the location and integrity of the data.

After running, the program will show the expected hash (given in the data file) and the calculated hash (calculated by the prover program). They should match in all instances.

# Code Organization
All code is located in the root directory.

`verifier.py` reads in the data, processes it in a way that can be sent to the prover, and confirms that the proof sent back by the prover matches the expected hash.

`prover.py` is partially implemented by me. It takes in the processed data, builds a Merkle tree row-by-row, selecting the correct hashes needed for the verifier to confirm data integrity.

`utils.py` contains utility format conversion and hash functions.

The data files that can be used as inputs are also located in the root directory.