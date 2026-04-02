import numpy as np

def entropy_node(y):
    _, counts = np.unique(y, return_counts=True)
    probs = counts / counts.sum()
    return -np.sum(probs * np.log2(probs))
    # Write code here
    pass