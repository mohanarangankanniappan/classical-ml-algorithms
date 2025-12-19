import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.linear_model import LinearRegression

# =====================================================
# SIMPLE LINEAR REGRESSION (USING SCIKIT-LEARN)
# =====================================================
# Model equation:
#     y = m*x + c
#
# scikit-learn internally computes:
#     m (coef_)
#     c (intercept_)
#
# Prediction:
#     ŷ = model.predict(X)
# =====================================================


# =====================================================
# 1. Create Output Folder (for GitHub plots)
# =====================================================
os.makedirs("plots_sklearn", exist_ok=True)


# =====================================================
# 2. Create Dataset using DataFrame
# =====================================================
data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [30, 35, 45, 50, 60]
}

df = pd.DataFrame(data)

print("\n================ DATASET ================\n")
print(df)


# =====================================================
# 3. Prepare Features and Target
# =====================================================
# X must be 2D in scikit-learn
X = df[["Experience"]]   # shape: (n_samples, 1)
y = df["Salary"]         # shape: (n_samples,)

print("\n================ DATA SHAPES ================\n")
print(f"X shape = {X.shape}")
print(f"y shape = {y.shape}")


# =====================================================
# 4. Create Linear Regression Model
# =====================================================
model = LinearRegression()


# =====================================================
# 5. Train (Fit) the Model
# =====================================================
model.fit(X, y)


# =====================================================
# 6. Extract Model Parameters
# =====================================================
m = model.coef_[0]
c = model.intercept_

print("\n================ MODEL PARAMETERS ================\n")
print(f"Slope (m)     = {m:.4f}")
print(f"Intercept (c) = {c:.4f}")


# =====================================================
# 7. Linear Equation
# =====================================================
print("\n================ LINEAR EQUATION ================\n")
print(f"Salary = {m:.2f} × Experience + {c:.2f}")


# =====================================================
# 8. Predictions
# =====================================================
df["Predicted_Salary"] = model.predict(X)

# Residual error
df["Residual_Error"] = df["Salary"] - df["Predicted_Salary"]

print("\n================ PREDICTIONS ================\n")
print(df)


# =====================================================
# 9. Plot 1: Actual Data
# =====================================================
plt.figure()
plt.scatter(df["Experience"], df["Salary"])
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Actual Data (scikit-learn)")
plt.grid(True)
plt.savefig("plots_sklearn/01_actual_data.png")
plt.show()


# =====================================================
# 10. Plot 2: Regression Line
# =====================================================
plt.figure()
plt.scatter(df["Experience"], df["Salary"], label="Actual Data")
plt.plot(df["Experience"], df["Predicted_Salary"],
         label="Regression Line")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Linear Regression Line (scikit-learn)")
plt.legend()
plt.grid(True)
plt.savefig("plots_sklearn/02_regression_line.png")
plt.show()


# =====================================================
# 11. Plot 3: Actual vs Predicted
# =====================================================
plt.figure()
plt.plot(df["Experience"], df["Salary"], marker="o", label="Actual")
plt.plot(df["Experience"], df["Predicted_Salary"],
         marker="x", label="Predicted")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Actual vs Predicted (scikit-learn)")
plt.legend()
plt.grid(True)
plt.savefig("plots_sklearn/03_actual_vs_predicted.png")
plt.show()


# =====================================================
# 12. Plot 4: Residual Error Plot
# =====================================================
plt.figure()
plt.scatter(df["Experience"], df["Residual_Error"])
plt.axhline(0, linestyle="--")
plt.xlabel("Experience (Years)")
plt.ylabel("Residual Error")
plt.title("Residual Error Plot (scikit-learn)")
plt.grid(True)
plt.savefig("plots_sklearn/04_residuals.png")
plt.show()


print("\n================ FILES SAVED ================\n")
print("plots_sklearn/01_actual_data.png")
print("plots_sklearn/02_regression_line.png")
print("plots_sklearn/03_actual_vs_predicted.png")
print("plots_sklearn/04_residuals.png")

print("\n✅ LINEAR REGRESSION (SCIKIT-LEARN) COMPLETED SUCCESSFULLY")

