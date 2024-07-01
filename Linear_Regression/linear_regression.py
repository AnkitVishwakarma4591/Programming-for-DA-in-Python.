import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def perform_linear_regression(x, y):
    """
    Perform linear regression and return the slope and intercept.
    """
    x = np.array(x).reshape(-1, 1)
    y = np.array(y)
    model = LinearRegression().fit(x, y)
    slope = model.coef_[0]
    intercept = model.intercept_
    return slope, intercept, model

def plot_regression_line(x, y, model):
    """
    Plot the regression line along with the data points.
    """
    plt.scatter(x, y, color='blue')
    plt.plot(x, model.predict(np.array(x).reshape(-1, 1)), color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression')
    plt.show()

# Example usage
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
slope, intercept, model = perform_linear_regression(x, y)
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
plot_regression_line(x, y, model)
