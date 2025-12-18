Simple Linear Regression
Theory and Mathematical Background
Introduction
Simple Linear Regression is a supervised machine learning and statistical technique used to model the relationship between one independent variable and one dependent variable.

It assumes that the relationship between the variables can be approximated using a straight line. This method is widely used for prediction, trend analysis, and understanding variable influence.
Linear Regression Model
The mathematical form of Simple Linear Regression is:
y = m x + c
Where:
x – Independent variable (input)
y – Dependent variable (output)
m – Slope of the regression line
c – Intercept of the regression line

This equation represents a straight line that best fits the observed data.
Slope (m)
The slope represents the rate of change of the dependent variable with respect to the independent variable.

Interpretation:
• Positive slope – y increases as x increases
• Negative slope – y decreases as x increases
• Zero slope – y does not change with x

The magnitude of the slope indicates how strongly the independent variable influences the dependent variable.
Intercept (c)
The intercept is the value of the dependent variable when the independent variable is zero.

It defines the point where the regression line crosses the y-axis and provides a baseline value for predictions.
Mean of Variables
The mean of the independent variable x is:
x̄ = (x₁ + x₂ + … + xₙ) / n
The mean of the dependent variable y is:
ȳ = (y₁ + y₂ + … + yₙ) / n
These mean values are used in computing the regression parameters.
Estimation of Slope (m)
The slope is computed using the Least Squares Method, which minimizes the sum of squared differences between actual and predicted values.

m = Σ[(x − x̄)(y − ȳ)] / Σ[(x − x̄)²]

This formula ensures that the regression line is the best possible linear fit for the given data.
Estimation of Intercept (c)
Once the slope is calculated, the intercept is obtained using:

c = ȳ − m x̄

This guarantees that the regression line passes through the mean point (x̄, ȳ).
Prediction Using the Model
Predicted values are computed using:

ŷ = m x + c

Where ŷ represents the predicted value of the dependent variable.
Residual Error
Residual error is the difference between the actual value and the predicted value.

e = y − ŷ

Residuals are used to evaluate the accuracy and goodness of fit of the regression model.
Assumptions of Simple Linear Regression
• Linearity – The relationship between x and y is linear
• Independence – Observations are independent
• Homoscedasticity – Constant variance of residuals
• Normality – Residuals are normally distributed

Violation of these assumptions may reduce model reliability.
Advantages
• Easy to understand and interpret
• Computationally efficient
• Works well for linearly related data
• Serves as a baseline model for advanced algorithms
Applications
• Salary prediction based on experience
• Sales and demand forecasting
• House price estimation
• Financial trend analysis
• Economic modeling
Results
Input data plots, regression line, actual vs predicted plots, and residual error plots are included.
Conclusion
Simple Linear Regression is a fundamental technique in machine learning and data analysis. Despite its simplicity, it provides valuable insights into data relationships and forms the foundation for more advanced predictive models.
