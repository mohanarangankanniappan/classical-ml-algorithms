📈 Simple Linear Regression
Theory and Mathematical Background
🔹 Introduction

Simple Linear Regression is a supervised machine learning and statistical technique used to model the relationship between one independent variable and one dependent variable.

It assumes that the relationship between the variables can be approximated using a straight line.
This method is widely used for prediction, trend analysis, and understanding variable influence.

🔹 Linear Regression Model

The mathematical form of Simple Linear Regression is:

𝑦
=
𝑚
𝑥
+
𝑐
y=mx+c
Where:

x – Independent variable (input)

y – Dependent variable (output)

m – Slope of the regression line

c – Intercept of the regression line

This equation represents a straight line that best fits the observed data.

🔹 Slope (m)

The slope represents the rate of change of the dependent variable with respect to the independent variable.

Interpretation:

Positive slope → y increases as x increases

Negative slope → y decreases as x increases

Zero slope → y does not change with x

The magnitude of the slope indicates how strongly the independent variable influences the dependent variable.

🔹 Intercept (c)

The intercept is the value of the dependent variable when the independent variable is zero.

It defines the point where the regression line crosses the y-axis and provides a baseline value for predictions.

🔹 Mean of Variables

The mean of the independent variable x is:

𝑥
ˉ
=
𝑥
1
+
𝑥
2
+
⋯
+
𝑥
𝑛
𝑛
x
ˉ
=
n
x
1
	​

+x
2
	​

+⋯+x
n
	​

	​


The mean of the dependent variable y is:

𝑦
ˉ
=
𝑦
1
+
𝑦
2
+
⋯
+
𝑦
𝑛
𝑛
y
ˉ
	​

=
n
y
1
	​

+y
2
	​

+⋯+y
n
	​

	​


These mean values are used in computing the regression parameters.

🔹 Estimation of Slope (m)

The slope is computed using the Least Squares Method, which minimizes the sum of squared differences between actual and predicted values.

𝑚
=
∑
(
𝑥
−
𝑥
ˉ
)
(
𝑦
−
𝑦
ˉ
)
∑
(
𝑥
−
𝑥
ˉ
)
2
m=
∑(x−
x
ˉ
)
2
∑(x−
x
ˉ
)(y−
y
ˉ
	​

)
	​


This formula ensures that the regression line is the best possible linear fit for the given data.

🔹 Estimation of Intercept (c)

Once the slope is calculated, the intercept is obtained using:

𝑐
=
𝑦
ˉ
−
𝑚
𝑥
ˉ
c=
y
ˉ
	​

−m
x
ˉ

This guarantees that the regression line passes through the mean point 
(
𝑥
ˉ
,
𝑦
ˉ
)
(
x
ˉ
,
y
ˉ
	​

).

🔹 Prediction Using the Model

Predicted values are computed using:

𝑦
^
=
𝑚
𝑥
+
𝑐
y
^
	​

=mx+c

Where ŷ represents the predicted value of the dependent variable.

🔹 Residual Error

Residual error is the difference between the actual value and the predicted value.

𝑒
=
𝑦
−
𝑦
^
e=y−
y
^
	​


Residuals are used to evaluate the accuracy and goodness of fit of the regression model.

🔹 Assumptions of Simple Linear Regression

Simple Linear Regression relies on the following assumptions:

Linearity – The relationship between x and y is linear

Independence – Observations are independent

Homoscedasticity – Constant variance of residuals

Normality – Residuals are normally distributed

Violation of these assumptions may reduce model reliability.

🔹 Advantages

Easy to understand and interpret

Computationally efficient

Works well for linearly related data

Serves as a baseline model for advanced algorithms

🔹 Applications

Salary prediction based on experience

Sales and demand forecasting

House price estimation

Financial trend analysis

Economic modeling

🔹 Results
📊 Input Data
<img width="640" height="480" src="https://github.com/user-attachments/assets/da25c4ee-b339-4b26-87c7-5c6f466bf340" />
📈 Regression Line
<img width="640" height="480" src="https://github.com/user-attachments/assets/206b7151-ef6e-4122-a598-ca51aeaa5016" />
📉 Actual vs Predicted
<img width="640" height="480" src="https://github.com/user-attachments/assets/81900947-176d-40b7-8f06-b400f4efd548" />
📐 Residual Error
<img width="640" height="480" src="https://github.com/user-attachments/assets/e88027ef-c603-4a4a-a682-d482b968b3bd" />
🔹 Conclusion

