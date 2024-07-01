import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def perform_polynomial_regression(x, y, degree):
    """
    Perform polynomial regression and return the model.
    
    Parameters:
    - x: List or array-like, independent variable values.
    - y: List or array-like, dependent variable values.
    - degree: Integer, the degree of the polynomial.

    Returns:
    - model: The trained polynomial regression model.
    - poly_features: PolynomialFeatures object used to transform the data.
    """
    x = np.array(x).reshape(-1, 1)
    y = np.array(y)
    
    # Transforming the data to include polynomial features
    poly_features = PolynomialFeatures(degree=degree)
    x_poly = poly_features.fit_transform(x)
    
    # Fitting the polynomial regression model
    model = LinearRegression().fit(x_poly, y)
    return model, poly_features

def plot_polynomial_regression(x, y, model, poly_features):
    """
    Plot the polynomial regression line along with the data points.
    
    Parameters:
    - x: List or array-like, independent variable values.
    - y: List or array-like, dependent variable values.
    - model: The trained polynomial regression model.
    - poly_features: PolynomialFeatures object used to transform the data.
    """
    plt.scatter(x, y, color='blue')
    
    # Predicting values using the model for plotting
    x_poly = poly_features.transform(np.array(x).reshape(-1, 1))
    plt.plot(x, model.predict(x_poly), color='red')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Polynomial Regression (degree={poly_features.degree})')
    plt.show()

# Example usage
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # Example data with a polynomial trend

degree = 2  # Degree of the polynomial
model, poly_features = perform_polynomial_regression(x, y, degree)

# Print model coefficients
print(f"Model Coefficients: {model.coef_}")
print(f"Model Intercept: {model.intercept_}")

# Plot the polynomial regression
plot_polynomial_regression(x, y, model, poly_features)
