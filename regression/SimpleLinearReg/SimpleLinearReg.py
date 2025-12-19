import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# =====================================================
# SIMPLE LINEAR REGRESSION (FROM SCRATCH)
# =====================================================
# Model equation:
#     y = m*x + c
#
# where:
#     m = slope
#     c = intercept
#
# Mathematical formulas:
#
# Mean of x:
#     x̄ = (Σ x) / n
#
# Mean of y:
#     ȳ = (Σ y) / n
#
# Slope (m):
#     m = Σ[(x - x̄)(y - ȳ)] / Σ[(x - x̄)²]
#
# Intercept (c):
#     c = ȳ - m*x̄
#
# Prediction:
#     ŷ = m*x + c
#
# Residual Error:
#     e = y - ŷ
# =====================================================


# =====================================================
# 1. Create Output Folder (for GitHub plots)
# =====================================================
os.makedirs("plots", exist_ok=True)


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
# 3. Calculate Mean
# =====================================================
# x̄ = Σx / n
# ȳ = Σy / n
x_mean = df["Experience"].mean()
y_mean = df["Salary"].mean()

print("\n================ MEAN VALUES ================\n")
print(f"x̄ (Mean of Experience) = {x_mean}")
print(f"ȳ (Mean of Salary)     = {y_mean}")


# =====================================================
# 4. Calculate Slope (m)
# =====================================================
# m = Σ[(x - x̄)(y - ȳ)] / Σ[(x - x̄)²]
numerator = np.sum(
    (df["Experience"] - x_mean) * (df["Salary"] - y_mean)
)

denominator = np.sum(
    (df["Experience"] - x_mean) ** 2
)

m = numerator / denominator


# =====================================================
# 5. Calculate Intercept (c)
# =====================================================
# c = ȳ - m*x̄
c = y_mean - m * x_mean

print("\n================ MODEL PARAMETERS ================\n")
print(f"Slope (m)     = {m:.4f}")
print(f"Intercept (c) = {c:.4f}")


# =====================================================
# 6. Linear Equation
# =====================================================
# Final equation:
#     y = m*x + c
print("\n================ LINEAR EQUATION ================\n")
print(f"Salary = {m:.2f} × Experience + {c:.2f}")


# =====================================================
# 7. Predictions
# =====================================================
# ŷ = m*x + c
df["Predicted_Salary"] = m * df["Experience"] + c

# Residual error:
# e = y - ŷ
df["Residual_Error"] = df["Salary"] - df["Predicted_Salary"]

print("\n================ PREDICTIONS ================\n")
print(df)


# =====================================================
# 8. Plot 1: Actual Data
# =====================================================
plt.figure()
plt.scatter(df["Experience"], df["Salary"])
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Actual Data")
plt.grid(True)
plt.savefig("plots/01_actual_data.png")
plt.show()


# =====================================================
# 9. Plot 2: Regression Line
# =====================================================
plt.figure()
plt.scatter(df["Experience"], df["Salary"], label="Actual Data")
plt.plot(df["Experience"], df["Predicted_Salary"],
         label="Regression Line")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Linear Regression Line")
plt.legend()
plt.grid(True)
plt.savefig("plots/02_regression_line.png")
plt.show()


# =====================================================
# 10. Plot 3: Actual vs Predicted
# =====================================================
plt.figure()
plt.plot(df["Experience"], df["Salary"], marker="o", label="Actual")
plt.plot(df["Experience"], df["Predicted_Salary"],
         marker="x", label="Predicted")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Actual vs Predicted")
plt.legend()
plt.grid(True)
plt.savefig("plots/03_actual_vs_predicted.png")
plt.show()


# =====================================================
# 11. Plot 4: Residual Error Plot
# =====================================================
plt.figure()
plt.scatter(df["Experience"], df["Residual_Error"])
plt.axhline(0, linestyle="--")
plt.xlabel("Experience (Years)")
plt.ylabel("Residual Error")
plt.title("Residual Error Plot")
plt.grid(True)
plt.savefig("plots/04_residuals.png")
plt.show()


print("\n================ FILES SAVED ================\n")
print("plots/01_actual_data.png")
print("plots/02_regression_line.png")
print("plots/03_actual_vs_predicted.png")
print("plots/04_residuals.png")

print("\n✅ LINEAR REGRESSION COMPLETED SUCCESSFULLY")
