import numpy as np

def calculate_mean(data):
    """
    Calculate the mean of a list of numbers.
    """
    return np.mean(data)

# Example usage
data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
mean = calculate_mean(data)
print(f"Mean: {mean}")
