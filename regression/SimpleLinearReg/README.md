<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple Linear Regression – Theory and Results</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.7;
            margin: 40px;
            color: #222;
        }

        h1, h2, h3 {
            color: #003366;
        }

        h1 {
            text-align: center;
            border-bottom: 3px solid #003366;
            padding-bottom: 10px;
        }

        h2 {
            border-left: 6px solid #003366;
            padding-left: 10px;
            margin-top: 40px;
        }

        h3 {
            margin-top: 25px;
        }

        p {
            text-align: justify;
        }

        ul {
            margin-left: 30px;
        }

        code, .math {
            background-color: #f4f4f4;
            padding: 6px 10px;
            display: inline-block;
            margin: 6px 0;
            border-radius: 4px;
        }

        .equation {
            background-color: #f8f8f8;
            border-left: 4px solid #003366;
            padding: 10px;
            margin: 15px 0;
            font-family: "Courier New", monospace;
        }

        .figure {
            text-align: center;
            margin: 30px 0;
        }

        .figure img {
            max-width: 90%;
            border: 1px solid #ccc;
        }

        .caption {
            font-size: 14px;
            color: #555;
            margin-top: 8px;
        }

        footer {
            text-align: center;
            margin-top: 60px;
            font-size: 14px;
            color: #666;
        }
    </style>
</head>

<body>

<h1>Simple Linear Regression</h1>

<h2>1. Introduction</h2>
<p>
Simple Linear Regression is a supervised machine learning and statistical technique used to model the
relationship between one independent variable and one dependent variable. It assumes that the
relationship between the variables can be approximated using a straight line.
</p>
<p>
This method is widely used for prediction, trend analysis, and understanding the influence of one
variable on another.
</p>

<h2>2. Linear Regression Model</h2>
<p>
The mathematical form of Simple Linear Regression is:
</p>

<div class="equation">
y = m × x + c
</div>

<p>
Where:
</p>
<ul>
    <li><b>x</b> – Independent variable (input)</li>
    <li><b>y</b> – Dependent variable (output)</li>
    <li><b>m</b> – Slope of the regression line</li>
    <li><b>c</b> – Intercept of the regression line</li>
</ul>

<h2>3. Slope (m)</h2>
<p>
The slope represents the rate of change of the dependent variable with respect to the independent
variable.
</p>

<ul>
    <li>Positive slope → y increases as x increases</li>
    <li>Negative slope → y decreases as x increases</li>
    <li>Zero slope → y remains constant</li>
</ul>

<p>
The magnitude of the slope indicates how strongly the independent variable influences the dependent
variable.
</p>

<h2>4. Intercept (c)</h2>
<p>
The intercept is the value of the dependent variable when the independent variable is zero.
It represents the point where the regression line crosses the y-axis.
</p>

<h2>5. Mean of Variables</h2>

<div class="equation">
x̄ = (x₁ + x₂ + … + xₙ) / n
</div>

<div class="equation">
ȳ = (y₁ + y₂ + … + yₙ) / n
</div>

<p>
These mean values are used to compute the regression coefficients.
</p>

<h2>6. Estimation of Slope (m)</h2>
<p>
The slope is estimated using the Least Squares Method, which minimizes the sum of squared errors.
</p>

<div class="equation">
m = Σ[(x − x̄)(y − ȳ)] / Σ[(x − x̄)²]
</div>

<h2>7. Estimation of Intercept (c)</h2>

<div class="equation">
c = ȳ − m × x̄
</div>

<p>
This ensures that the regression line passes through the mean point (x̄, ȳ).
</p>

<h2>8. Prediction Using the Model</h2>

<div class="equation">
ŷ = m × x + c
</div>

<p>
Where ŷ is the predicted value of the dependent variable.
</p>

<h2>9. Residual Error</h2>

<div class="equation">
e = y − ŷ
</div>

<p>
Residuals represent prediction errors and are used to evaluate the goodness of fit of the model.
</p>

<h2>10. Assumptions of Simple Linear Regression</h2>

<ul>
    <li><b>Linearity</b> – Linear relationship between x and y</li>
    <li><b>Independence</b> – Observations are independent</li>
    <li><b>Homoscedasticity</b> – Constant variance of residuals</li>
    <li><b>Normality</b> – Residuals follow a normal distribution</li>
</ul>

<h2>11. Advantages</h2>

<ul>
    <li>Simple and interpretable</li>
    <li>Computationally efficient</li>
    <li>Works well for linear relationships</li>
    <li>Baseline model for advanced algorithms</li>
</ul>

<h2>12. Applications</h2>

<ul>
    <li>Salary prediction</li>
    <li>Sales forecasting</li>
    <li>House price estimation</li>
    <li>Financial trend analysis</li>
    <li>Economic modeling</li>
</ul>

<h2>13. Experimental Results & Visualizations</h2>

<h3>13.1 Input Data</h3>
<div class="figure">
    <img src="https://github.com/user-attachments/assets/da25c4ee-b339-4b26-87c7-5c6f466bf340" alt="Input Data Plot">
    <div class="caption">Figure 1: Distribution of Input Data</div>
</div>

<h3>13.2 Regression Line</h3>
<div class="figure">
    <img src="https://github.com/user-attachments/assets/206b7151-ef6e-4122-a598-ca51aeaa5016" alt="Regression Line">
    <div class="caption">Figure 2: Best Fit Regression Line</div>
</div>

<h3>13.3 Actual vs Predicted Values</h3>
<div class="figure">
    <img src="https://github.com/user-attachments/assets/81900947-176d-40b7-8f06-b400f4efd548" alt="Actual vs Predicted">
    <div class="caption">Figure 3: Actual vs Predicted Outputs</div>
</div>

<h3>13.4 Residual Error Analysis</h3>
<div class="figure">
    <img src="https://github.com/user-attachments/assets/e88027ef-c603-4a4a-a682-d482b968b3bd" alt="Residual Error">
    <div class="caption">Figure 4: Residual Error Distribution</div>
</div>

<h2>14. Conclusion</h2>
<p>
Simple Linear Regression is a fundamental technique in machine learning and statistics.
Despite its simplicity, it provides valuable insights into data relationships and serves as
the foundation for more advanced predictive models.
</p>

<footer>
    <p><b>Project:</b> classical-ml-algorithms</p>
</footer>

</body>
</html>
