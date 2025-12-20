<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Logistic Regression From Scratch</title>

<style>
    body {
        font-family: Arial, Helvetica, sans-serif;
        line-height: 1.65;
        margin: 40px auto;
        max-width: 900px;
        color: #222;
        background: #ffffff;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    code, pre {
        background: #f4f4f4;
        padding: 10px;
        border-radius: 5px;
        display: block;
        overflow-x: auto;
        font-size: 0.95em;
    }
    table {
        border-collapse: collapse;
        margin: 15px 0;
        width: 100%;
    }
    th, td {
        border: 1px solid #bbb;
        padding: 8px 10px;
        text-align: center;
    }
    th {
        background: #ecf0f1;
    }
    hr {
        margin: 35px 0;
    }
</style>
</head>

<body>

<h1>📈 Logistic Regression (From Scratch – Python)</h1>

<p>
This project demonstrates <b>Logistic Regression implemented from scratch using NumPy</b>,
without relying on any machine-learning libraries.
The objective is to clearly explain the mathematics, optimization, and learning behavior.
</p>

<hr>

<h2>1. Problem Statement</h2>

<p>
We solve a <b>binary classification</b> problem:
</p>

<p><b>Predict whether a student PASSES (1) or FAILS (0)</b> based on:</p>
<ul>
    <li>Gender (Male / Female)</li>
    <li>Stream (CS / Non-CS)</li>
    <li>Study Mode (Online / Offline)</li>
    <li>Study Hours</li>
</ul>

<hr>

<h2>2. Feature Encoding</h2>

<p>
Categorical variables are converted using <b>one-hot encoding</b> and combined with a numeric feature.
</p>

<h3>Encoded Input Matrix <i>X</i></h3>

<pre>
X =
[[1. 0. 1. 0. 5.]
 [0. 1. 1. 0. 6.]
 [1. 0. 0. 1. 4.]
 [0. 1. 0. 1. 1.]
 [1. 0. 1. 0. 2.]
 [0. 1. 0. 1. 1.]]
</pre>

<h3>Labels <i>y</i></h3>

<pre>
y = [1. 1. 1. 0. 0. 0.]
</pre>

<hr>

<h2>3. Logistic Regression Model</h2>

<h3>Linear Score</h3>

<pre>
z = Xw + b
</pre>

<h3>Sigmoid Function</h3>

<pre>
σ(z) = 1 / (1 + e⁻ᶻ)
</pre>

<p>
The sigmoid converts the linear score into a probability between 0 and 1.
</p>

<hr>

<h2>4. Loss Function (Binary Cross-Entropy)</h2>

<pre>
L(y, ŷ) = -1/N ∑ [ y log(ŷ) + (1 − y) log(1 − ŷ) ]
</pre>

<p>
The goal is to <b>minimize this loss</b> during training.
</p>

<hr>

<h2>5. Gradient Descent Optimization</h2>

<h3>Gradients</h3>

<pre>
∂L/∂w = (1/N) · Xᵀ(ŷ − y)
∂L/∂b = (1/N) · Σ(ŷ − y)
</pre>

<h3>Parameter Updates</h3>

<pre>
w := w − α · ∂L/∂w
b := b − α · ∂L/∂b
</pre>

<hr>

<h2>6. Training Observations</h2>

<h3>Initial Parameters</h3>

<pre>
Initial Weights: [0.1764 0.0400 0.0979 0.2241 0.1868]
Initial Bias   : 0.0
</pre>

<h3>Loss Reduction</h3>

<table>
<tr><th>Epoch</th><th>Loss</th></tr>
<tr><td>1</td><td>0.6239</td></tr>
<tr><td>5</td><td>0.5797</td></tr>
<tr><td>10</td><td>0.5324</td></tr>
</table>

<p>
The steady decrease in loss confirms correct gradient descent behavior.
</p>

<hr>

<h2>7. Final Learned Parameters</h2>

<pre>
Final Weights: [ 0.1400 -0.1167  0.0555  0.0734  0.2998 ]
Final Bias   : -0.1931
</pre>

<p>
<b>Interpretation:</b>
</p>
<ul>
    <li>Positive weights increase probability of PASS</li>
    <li>Negative weights reduce probability</li>
    <li>Study hours has the strongest positive influence</li>
</ul>

<hr>

<h2>8. New Prediction Example</h2>

<pre>
Input: Male, CS, 4 hours
Probability of PASS: 0.7688
Predicted Class: PASS
</pre>

<p>
This demonstrates successful generalization to unseen data.
</p>

<hr>

<h2>9. Project Structure</h2>

<pre>
LogisticReg/
├── logistic_reg.py
└── README.html
</pre>

<hr>

<h2>10. How to Run</h2>

<pre>
python3 logistic_reg.py
</pre>

<hr>

<h2>11. Author</h2>

<p>
<b>Mohanarangan Kanniappan</b><br>
Classical Machine Learning – From Scratch Series
</p>

</body>
</html>
