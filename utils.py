import numpy as np
import random

from sklearn.datasets import make_blobs


def generate_data(n_samples, n_features):
    """ 
    Wrapper function for make blobs, because 
    in the future I may want to do something
    more complex in the data generation stage.
    
    Returns numpy.array of size (n_samples, n_features)
    """
    features, labels = make_blobs(n_samples=n_samples, n_features=n_features)
    return features


def transform(data):
    """ 
    Transform the data to the range [0,1]
    return a new array.
    """
    xprime = data - data.min(axis=0)
    return xprime / xprime.max(axis=0)


def save_data(data, path):
    print(f"Saving data to: {path}")


def fails_occasionally(func):
    if random.random() < 0.2:
        # Replace with something more
        # appropriate 
        raise Exception("Function failed!")
    else:
        return func
