# Simple Linear Regression

## Introduction

Simple Linear Regression is a supervised machine learning and statistical technique used to model the relationship between one independent variable and one dependent variable.  
It assumes that the relationship between the variables can be approximated using a straight line.

This method is widely used for prediction, trend analysis, and understanding the influence of one variable on another.

---

## Linear Regression Model

The mathematical form of Simple Linear Regression is:

**y = m × x + c**

Where:
- **x** – Independent variable (input)
- **y** – Dependent variable (output)
- **m** – Slope of the regression line
- **c** – Intercept of the regression line

---

## Slope (m)

The slope represents the rate of change of the dependent variable with respect to the independent variable.

**Interpretation:**
- Positive slope → y increases as x increases  
- Negative slope → y decreases as x increases  
- Zero slope → y remains constant  

The magnitude of the slope indicates how strongly the independent variable influences the dependent variable.

---

## Intercept (c)

The intercept is the value of the dependent variable when the independent variable is zero.  
It represents the point where the regression line crosses the y-axis.

---

## Mean of Variables

Mean of the independent variable:

**x̄ = (x₁ + x₂ + … + xₙ) / n**

Mean of the dependent variable:

**ȳ = (y₁ + y₂ + … + yₙ) / n**

These values are used to compute the regression parameters.

---

## Estimation of Slope (m)

The slope is estimated using the **Least Squares Method**, which minimizes the sum of squared errors.

**Formula:**

**m = Σ[(x − x̄)(y − ȳ)] / Σ[(x − x̄)²]**

---

## Estimation of Intercept (c)

Once the slope is computed:

**c = ȳ − m × x̄**

This ensures that the regression line passes through the mean point **(x̄, ȳ)**.

---

## Prediction Using the Model

Predicted values are calculated as:

**ŷ = m × x + c**

Where **ŷ** is the predicted output.

---

## Residual Error

Residual error is the difference between the actual and predicted values:

**e = y − ŷ**

Residuals are used to evaluate model accuracy and goodness of fit.

---

## Assumptions of Simple Linear Regression

- **Linearity** – Relationship between x and y is linear  
- **Independence** – Observations are independent  
- **Homoscedasticity** – Constant variance of residuals  
- **Normality** – Residuals follow a normal distribution  

Violation of these assumptions can reduce model reliability.

---

## Advantages

- Easy to understand and interpret  
- Computationally efficient  
- Works well for linearly related data  
- Strong baseline for advanced models  

---

## Applications

- Salary prediction  
- Sales forecasting  
- House price estimation  
- Financial trend analysis  
- Economic modeling  

---

## Experimental Results & Visualizations

### Input Data

![Input Data](https://github.com/user-attachments/assets/da25c4ee-b339-4b26-87c7-5c6f466bf340)

---

### Regression Line

![Regression Line](https://github.com/user-attachments/assets/206b7151-ef6e-4122-a598-ca51aeaa5016)

---

### Actual vs Predicted Values

![Actual vs Predicted](https://github.com/user-attachments/assets/81900947-176d-40b7-8f06-b400f4efd548)

---

### Residual Error Analysis

![Residual Error](https://github.com/user-attachments/assets/e88027ef-c603-4a4a-a682-d482b968b3bd)

---

## Conclusion

Simple Linear Regression is a fundamental technique in machine learning and statistics.  
Despite its simplicity, it provides valuable insights into data relationships and forms the foundation for more advanced predictive models.

---

### Repository

**classical-ml-algorithms**
