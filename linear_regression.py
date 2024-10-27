import numpy as np

# Define the hypothesis function (linear model)
def hypothesis(w, x):
    return w[0] + w[1] * x

# Gradient descent algorithm
def gradient_descent(X, y, alpha, epochs):
    # Initialize weights
    w = np.zeros(2)  # w[0] for bias, w[1] for the weight
    n = len(y)  # Number of training examples

    # Gradient descent loop
    for epoch in range(epochs):
        # Compute predictions
        predictions = hypothesis(w, X)
        
        # Calculate the error
        error = y - predictions
        
        # Update weights
        w[0] += alpha * np.sum(error) / n  # Update for w0
        w[1] += alpha * np.sum(error * X) / n  # Update for w1

        # Optionally, you can print the cost or weights at every epoch
        cost = np.mean(error**2)  # Mean Squared Error
        print(f'Epoch {epoch + 1}/{epochs}, Cost: {cost}, Weights: {w}')
    
    return w

# Example usage
if __name__ == "__main__":
    # Sample data
    X = np.array([1, 2, 3, 4, 5])  # Input features
    y = np.array([2, 4, 6, 8, 10])  # Target values (y = 2x)
    
    # Hyperparameters
    alpha = 0.01  # Learning rate
    epochs = 1000  # Number of iterations

    # Run gradient descent
    final_weights = gradient_descent(X, y, alpha, epochs)
    print(f'Final Weights: {final_weights}')
