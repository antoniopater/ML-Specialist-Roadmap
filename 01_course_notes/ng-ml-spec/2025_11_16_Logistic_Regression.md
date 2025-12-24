---
course: ng-ml-spec
lesson: "03 - Logistic Regression"
time_spent_h: 0
tags: [course, ng, ml, spec, supervised, classification, logistic-regression]
---

## Logistic Regression

### Definition and Purpose

Logistic regression is a classification algorithm used to predict binary outcomes (0 or 1, yes or no, true or false). Unlike linear regression which predicts continuous values, logistic regression predicts the probability that an input belongs to a particular class.

The key difference from linear regression is that logistic regression uses a sigmoid (logistic) function to map predictions to probabilities between 0 and 1, making it suitable for classification problems.

### The Sigmoid Function

The sigmoid function, also known as the logistic function, is defined as:

```
g(z) = 1 / (1 + e^(-z))
```

Where:

- z is the input (often z = w·x + b)
- The output is always between 0 and 1
- When z is large and positive, g(z) approaches 1
- When z is large and negative, g(z) approaches 0
- When z = 0, g(z) = 0.5

The sigmoid function creates an S-shaped curve that smoothly transitions between 0 and 1, making it ideal for representing probabilities.

### Model Representation

In logistic regression, the model is:

```
f_wb(x) = g(w·x + b) = 1 / (1 + e^(-(w·x + b)))
```

Where:

- f_wb(x) is the predicted probability that y = 1 given input x
- w is the weight vector (parameters)
- b is the bias (parameter)
- x is the input feature vector

The output f_wb(x) represents P(y = 1 | x; w, b), the probability that y = 1 given x, parameterized by w and b.

### Decision Boundary

The decision boundary is the line (or hyperplane in higher dimensions) that separates the two classes. In logistic regression:

- If f_wb(x) ≥ 0.5, we predict y = 1
- If f_wb(x) < 0.5, we predict y = 0

Since g(z) = 0.5 when z = 0, the decision boundary occurs when:

```
w·x + b = 0
```

This creates a linear decision boundary, which works well for linearly separable data.

### Cost Function

The cost function for logistic regression is different from linear regression because the sigmoid function makes the squared error cost function non-convex (has many local minima).

The logistic regression cost function is:

```
J(w,b) = (1/m) * Σ[-y^(i) * log(f_wb(x^(i))) - (1 - y^(i)) * log(1 - f_wb(x^(i)))]
```

This is also known as the log loss or binary cross-entropy loss.

Key properties:

- When y = 1: cost = -log(f_wb(x)), which is large if f_wb(x) is close to 0, and small if f_wb(x) is close to 1
- When y = 0: cost = -log(1 - f_wb(x)), which is large if f_wb(x) is close to 1, and small if f_wb(x) is close to 0
- This ensures the model is penalized more when it makes confident wrong predictions

### Gradient Descent for Logistic Regression

The gradient descent algorithm for logistic regression has the same form as linear regression:

```
Repeat until convergence:
  w = w - α * (∂J/∂w)
  b = b - α * (∂J/∂b)
```

The derivatives (gradients) are:

```
∂J/∂w_j = (1/m) * Σ[(f_wb(x^(i)) - y^(i)) * x_j^(i)]
∂J/∂b = (1/m) * Σ[(f_wb(x^(i)) - y^(i))]
```

Interestingly, these gradient formulas look identical to linear regression, but they're different because f_wb(x) is now the sigmoid function instead of a linear function.

### Implementation Considerations

1. **Feature Scaling**: Like linear regression, feature scaling can help gradient descent converge faster
2. **Regularization**: Can be added to prevent overfitting (L1 or L2 regularization)
3. **Multiple Classes**: For multi-class classification, we can use:
   - One-vs-all (one-vs-rest): Train multiple binary classifiers
   - Softmax regression: Direct extension to multiple classes

### Advantages of Logistic Regression

- Simple and interpretable
- Fast to train and make predictions
- Doesn't require feature scaling (though it helps)
- Provides probability estimates, not just predictions
- Less prone to overfitting with regularization

### Limitations

- Assumes a linear decision boundary
- May not perform well on non-linearly separable data
- Sensitive to outliers
- Requires large sample sizes for stable results

### Applications

Logistic regression is widely used in:

- Medical diagnosis (disease prediction)
- Email spam detection
- Credit approval
- Marketing (click prediction)
- Image classification (as a baseline)
- Any binary classification problem

### Key Takeaways

1. Logistic regression is a classification algorithm, not regression despite its name
2. It uses the sigmoid function to map outputs to probabilities
3. The cost function is different from linear regression (log loss vs. squared error)
4. Gradient descent works similarly but with different f_wb(x) function
5. It creates linear decision boundaries
6. It's a fundamental building block for understanding neural networks

---
