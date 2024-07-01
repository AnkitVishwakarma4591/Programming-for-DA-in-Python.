from scipy import stats

def calculate_mode(data):
    """
    Calculate the mode of a list of numbers.
    """
    mode, count = stats.mode(data)
    return mode[0]

# Example usage
data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
mode = calculate_mode(data)
print(f"Mode: {mode}")
