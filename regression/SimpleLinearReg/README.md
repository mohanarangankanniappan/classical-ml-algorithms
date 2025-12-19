# Simple Linear Regression

SIMPLE LINEAR REGRESSION
THEORY AND MATHEMATICAL BACKGROUND

==================================================

INTRODUCTION

Simple Linear Regression is a supervised machine learning and statistical technique used to model the relationship between one independent variable and one dependent variable.
It assumes that the relationship between the variables can be approximated using a straight line.

This method is widely used for prediction, trend analysis, and understanding the influence of one variable on another.

LINEAR REGRESSION MODEL

The mathematical form of Simple Linear Regression is:

y = m × x + c

Where:
x – Independent variable (input)
y – Dependent variable (output)
m – Slope of the regression line
c – Intercept of the regression line

This equation represents a straight line that best fits the observed data.

SLOPE (m)

The slope represents the rate of change of the dependent variable with respect to the independent variable.

Interpretation:

A positive slope means y increases as x increases

A negative slope means y decreases as x increases

A zero slope means y does not change with x

The magnitude of the slope indicates how strongly the independent variable influences the dependent variable.

INTERCEPT (c)

The intercept is the value of the dependent variable when the independent variable is zero.

It defines the point where the regression line crosses the y-axis and provides a baseline value for predictions.

MEAN OF VARIABLES

The mean of the independent variable x is calculated as:

x̄ = (x₁ + x₂ + … + xₙ) / n

The mean of the dependent variable y is calculated as:

ȳ = (y₁ + y₂ + … + yₙ) / n

These mean values are used in computing the regression parameters.

ESTIMATION OF SLOPE (m)

The slope is computed using the Least Squares Method, which minimizes the sum of squared differences between actual and predicted values.

Formula:

m = Σ[(x − x̄)(y − ȳ)] / Σ[(x − x̄)²]

This formula ensures that the regression line is the best possible linear fit for the given data.

ESTIMATION OF INTERCEPT (c)

Once the slope is calculated, the intercept is obtained using:

c = ȳ − m × x̄

This guarantees that the regression line passes through the mean point (x̄, ȳ).

PREDICTION USING THE MODEL

Predicted values are computed using:

ŷ = m × x + c

Where ŷ represents the predicted value of the dependent variable.

RESIDUAL ERROR

Residual error is the difference between the actual value and the predicted value.

Formula:

e = y − ŷ

Residuals are used to evaluate the accuracy and goodness of fit of the regression model.

ASSUMPTIONS OF SIMPLE LINEAR REGRESSION

Simple Linear Regression relies on the following assumptions:

Linearity – The relationship between x and y is linear

Independence – Observations are independent of each other

Homoscedasticity – Constant variance of residuals

Normality – Residuals are normally distributed

Violation of these assumptions may reduce model reliability.

ADVANTAGES

Easy to understand and interpret

Computationally efficient

Works well for linearly related data

Serves as a baseline model for advanced algorithms

APPLICATIONS

Salary prediction based on experience

Sales and demand forecasting

House price estimation

Financial trend analysis

Economic modeling

CONCLUSION

Simple Linear Regression is a fundamental technique in machine learning and data analysis.
Despite its simplicity, it provides valuable insights into data relationships and forms the foundation for more advanced predictive models.

Results


Plots
Input Data:
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/da25c4ee-b339-4b26-87c7-5c6f466bf340" />

Regression Line:
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/206b7151-ef6e-4122-a598-ca51aeaa5016" />

Actual Vs Predicted:
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/81900947-176d-40b7-8f06-b400f4efd548" />


Residual Error:
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/e88027ef-c603-4a4a-a682-d482b968b3bd" />



# classical-ml-algorithms
# classical-ml-algorithms
