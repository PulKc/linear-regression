# Linear Regression using Gradient Descent

This repository contains a simple implementation of linear regression using gradient descent in Python. The provided algorithm is designed to learn the relationship between the input feature \(x\) and the target variable \(y\) for the linear equation \(y = 2x\). 

## Description

The code demonstrates how the weights of the linear model converge to the actual values through iterative updates. As the number of iterations increases, the weights approach the true values, illustrating the effectiveness of the gradient descent algorithm for optimizing linear regression models.

## Gradient Descent Algorithm

The gradient descent algorithm used in this implementation follows the update rules described in **Artificial Intelligence: A Modern Approach (4th Edition)**, Chapter 19.

The update equations for the weights are as follows:
- \( w_0 \leftarrow w_0 + \alpha \sum_j (y_j - h_w(x_j)) \)
- \( w_1 \leftarrow w_1 + \alpha \sum_j (y_j - h_w(x_j)) \times x_j \)

Where:
- \(w_0\) is the bias term.
- \(w_1\) is the weight associated with the input feature \(x_j\).
- \(\alpha\) is the learning rate.
- \(h_w(x_j)\) is the predicted output.

## Sample Problem

The sample problem implemented in this code is to predict \(y\) using the linear relationship:
\[ y = 2x \]

### Example Data
- Input (X): [1, 2, 3, 4, 5]
- Output (y): [2, 4, 6, 8, 10]

### Running the Code

To run the code, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your_username/linear-regression.git
   cd linear-regression
   ```

2. **Install Required Libraries**
   Make sure you have Python installed. Install NumPy if you haven't done so:
   ```bash
   pip install numpy
   ```

3. **Run the Python Code**
   You can run the code by executing the following command in your terminal:
   ```bash
   python linear_regression.py
   ```

4. **Observe the Output**
   The program will print the cost and weights for each epoch, showing how the weights converge to the true values as the iterations increase.

### Example Output

After running the code, you should see output similar to:
```
Epoch 1/1000, Cost: 6.0, Weights: [0.4 1.6]
Epoch 2/1000, Cost: 3.2, Weights: [0.72 1.84]
...
Epoch 1000/1000, Cost: 0.01, Weights: [1.98 2.02]
Final Weights: [2.0 2.0]
```
## Terms of Use
The code provided is for educational purposes only. Use this to learn about machine learning and understand the concepts involved. Please follow the terms and guidelines of GitHub while using and sharing this code.

## References
- Code generated using ChatGPT.
- **Artificial Intelligence: A Modern Approach (4th Edition)**, Chapter 19.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Instructions for Use
1. **Replace `your_username`** with your actual GitHub username in the clone URL.
2. **Add a License**: If you want to include a license for your project, create a `LICENSE` file in the repository or choose a license on GitHub when creating your repository.
3. **Markdown Formatting**: Ensure that the formatting is correct when you paste it into your GitHub repository.








