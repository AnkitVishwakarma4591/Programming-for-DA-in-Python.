import numpy as np

def calculate_standard_deviation(data):
    """
    Calculate the standard deviation of a list of numbers.
    """
    return np.std(data)

# Example usage
data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
std_dev = calculate_standard_deviation(data)
print(f"Standard Deviation: {std_dev}")
