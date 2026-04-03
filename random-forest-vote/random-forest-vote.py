import numpy as np
from collections import Counter
def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    return np.apply_along_axis(
    lambda x: min([k for k, v in Counter(x).items() if v == max(Counter(x).values())]),
    axis=0,
    arr=predictions
    ).tolist()