<<<<<<< HEAD
# Computer-Vision
=======
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple Linear Regression</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.65;
            margin: 40px auto;
            max-width: 900px;
            color: #222;
        }
        h1, h2 {
            color: #2c3e50;
        }
        hr {
            margin: 35px 0;
        }
        ul {
            margin-left: 25px;
        }
        .equation {
            background: #f5f5f5;
            padding: 10px;
            font-family: "Courier New", monospace;
            text-align: center;
            margin: 15px 0;
            border-left: 4px solid #2c3e50;
        }
        figure {
            margin: 30px 0;
            text-align: center;
        }
        figcaption {
            font-size: 0.9em;
            color: #555;
            margin-top: 8px;
        }
        img {
            border: 1px solid #ccc;
        }
    </style>
</head>
<body>

<h1>📈 Simple Linear Regression</h1>
<h3>Theory and Mathematical Background</h3>

<hr>

<h2>1. Introduction</h2>
<p>
Simple Linear Regression is a supervised machine learning and statistical technique used to model
the relationship between one independent variable and one dependent variable.
</p>
<p>
It assumes that the relationship between the variables can be approximated using a straight line.
This method is widely used for prediction, trend analysis, and understanding variable influence.
</p>

<figure>
    <img src="https://github.com/user-attachments/assets/da25c4ee-b339-4b26-87c7-5c6f466bf340"
         width="640" height="480" alt="Input Data">
    <figcaption>
        <strong>Figure 1:</strong> Input data showing the relationship between the independent
        variable (x) and dependent variable (y) before applying linear regression.
    </figcaption>
</figure>

<hr>

<h2>2. Linear Regression Model</h2>
<p>The mathematical form of Simple Linear Regression is:</p>

<div class="equation">
y = m x + c
</div>

<ul>
    <li><strong>x</strong> – Independent variable (input)</li>
    <li><strong>y</strong> – Dependent variable (output)</li>
    <li><strong>m</strong> – Slope of the regression line</li>
    <li><strong>c</strong> – Intercept of the regression line</li>
</ul>

<p>
This equation represents a straight line that best fits the observed data.
</p>

<figure>
    <img src="https://github.com/user-attachments/assets/206b7151-ef6e-4122-a598-ca51aeaa5016"
         width="640" height="480" alt="Regression Line">
    <figcaption>
        <strong>Figure 2:</strong> Fitted regression line overlaid on the input data,
        illustrating the best linear approximation obtained using the least squares method.
    </figcaption>
</figure>

<hr>

<h2>3. Slope (m)</h2>
<p>
The slope represents the rate of change of the dependent variable with respect to the independent variable.
</p>

<ul>
    <li>Positive slope → y increases as x increases</li>
    <li>Negative slope → y decreases as x increases</li>
    <li>Zero slope → y does not change with x</li>
</ul>

<p>
The magnitude of the slope indicates how strongly the independent variable influences the dependent variable.
</p>

<hr>

<h2>4. Intercept (c)</h2>
<p>
The intercept is the value of the dependent variable when the independent variable is zero.
</p>
<p>
It defines the point where the regression line crosses the y-axis and provides a baseline value for predictions.
</p>

<hr>

<h2>5. Mean of Variables</h2>

<p>Mean of the independent variable:</p>
<div class="equation">
x̄ = (x₁ + x₂ + … + xₙ) / n
</div>

<p>Mean of the dependent variable:</p>
<div class="equation">
ȳ = (y₁ + y₂ + … + yₙ) / n
</div>

<p>
These mean values are essential for estimating the regression parameters.
</p>

<hr>

<h2>6. Estimation of Slope (m)</h2>
<div class="equation">
m = Σ[(x − x̄)(y − ȳ)] / Σ[(x − x̄)²]
</div>

<p>
This formulation minimizes the sum of squared prediction errors and produces the optimal linear fit.
</p>

<hr>

<h2>7. Estimation of Intercept (c)</h2>
<div class="equation">
c = ȳ − m x̄
</div>

<p>
This ensures that the regression line passes through the mean point (x̄, ȳ).
</p>

<hr>

<h2>8. Prediction Using the Model</h2>
<div class="equation">
ŷ = m x + c
</div>

<p>
Using the estimated parameters, the model predicts output values for unseen inputs.
</p>

<figure>
    <img src="https://github.com/user-attachments/assets/81900947-176d-40b7-8f06-b400f4efd548"
         width="640" height="480" alt="Actual vs Predicted">
    <figcaption>
        <strong>Figure 3:</strong> Comparison between actual values and predicted values.
        A close alignment indicates good predictive performance.
    </figcaption>
</figure>

<hr>

<h2>9. Residual Error</h2>
<div class="equation">
e = y − ŷ
</div>

<p>
Residuals represent the unexplained portion of the data and are used to assess model adequacy.
</p>

<figure>
    <img src="https://github.com/user-attachments/assets/e88027ef-c603-4a4a-a682-d482b968b3bd"
         width="640" height="480" alt="Residual Error">
    <figcaption>
        <strong>Figure 4:</strong> Residual error plot showing the distribution of errors.
        Random dispersion around zero suggests a well-fitted model.
    </figcaption>
</figure>

<hr>

<h2>10. Assumptions of Simple Linear Regression</h2>
<ul>
    <li><strong>Linearity</strong> – Linear relationship between x and y</li>
    <li><strong>Independence</strong> – Observations are independent</li>
    <li><strong>Homoscedasticity</strong> – Constant variance of residuals</li>
    <li><strong>Normality</strong> – Residuals follow a normal distribution</li>
</ul>

<hr>

<h2>11. Advantages</h2>
<ul>
    <li>Easy to understand and interpret</li>
    <li>Computationally efficient</li>
    <li>Effective for linearly related data</li>
    <li>Baseline for advanced machine learning models</li>
</ul>

<hr>

<h2>12. Applications</h2>
<ul>
    <li>Salary prediction based on experience</li>
    <li>Sales and demand forecasting</li>
    <li>House price estimation</li>
    <li>Financial trend analysis</li>
    <li>Economic modeling</li>
</ul>

<hr>

<h2>13. Conclusion</h2>
<p>
Simple Linear Regression is a foundational technique in machine learning and data analysis.
Despite its simplicity, it provides powerful insights into data relationships and serves as
a stepping stone toward more complex predictive models.
</p>

</body>
</html>
>>>>>>> 53fa8d294907a2478bc98015891851b403674ff2
