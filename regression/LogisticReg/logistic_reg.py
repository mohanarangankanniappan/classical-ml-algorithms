import numpy as np

# =========================================================
# STEP 1: RAW DATA (Human Readable)
# =========================================================
# Features:
# Gender: Male / Female
# Dept  : CS / EE
# Hours : numeric
# Label : Pass(1) / Fail(0)

data = [
    ("Male",   "CS", 5, 1),
    ("Female", "CS", 6, 1),
    ("Male",   "EE", 4, 1),
    ("Female", "EE", 1, 0),
    ("Male",   "CS", 2, 0),
    ("Female", "EE", 1, 0),
]

# =========================================================
# STEP 2: ONE-HOT ENCODING (MANUAL)
# =========================================================
# Gender: Male=[1,0], Female=[0,1]
# Dept  : CS=[1,0], EE=[0,1]

X = []
y = []

for gender, dept, hours, label in data:
    gender_vec = [1, 0] if gender == "Male" else [0, 1]
    dept_vec   = [1, 0] if dept == "CS" else [0, 1]

    features = gender_vec + dept_vec + [hours]
    X.append(features)
    y.append(label)

X = np.array(X, dtype=float)
y = np.array(y, dtype=float)

print("\nEncoded Input Matrix X:")
print(X)

print("\nLabels y:")
print(y)

# =========================================================
# STEP 3: INITIALIZE PARAMETERS
# =========================================================
np.random.seed(0)

weights = np.random.randn(X.shape[1]) * 0.1
bias = 0.0
learning_rate = 0.1
epochs = 10

print("\nInitial Weights:", weights)
print("Initial Bias:", bias)

# =========================================================
# STEP 4: DEFINE FUNCTIONS
# =========================================================
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_loss(y_true, y_pred):
    eps = 1e-9
    return -np.mean(
        y_true * np.log(y_pred + eps) +
        (1 - y_true) * np.log(1 - y_pred + eps)
    )

# =========================================================
# STEP 5: TRAINING LOOP (GRADIENT DESCENT)
# =========================================================
for epoch in range(epochs):
    print(f"\n======== Epoch {epoch+1} ========")

    # ---- Linear Equation ----
    z = np.dot(X, weights) + bias
    print("Linear score z:", z)

    # ---- Sigmoid ----
    y_pred = sigmoid(z)
    print("Predicted probabilities:", y_pred)

    # ---- Loss ----
    loss = compute_loss(y, y_pred)
    print("Loss:", loss)

    # ---- Gradients ----
    error = y_pred - y
    dw = np.dot(X.T, error) / len(y)
    db = np.mean(error)

    print("Gradient dw:", dw)
    print("Gradient db:", db)

    # ---- Update ----
    weights -= learning_rate * dw
    bias -= learning_rate * db

    print("Updated weights:", weights)
    print("Updated bias:", bias)

# =========================================================
# STEP 6: FINAL MODEL
# =========================================================
print("\n====== TRAINING COMPLETE ======")
print("Final Weights:", weights)
print("Final Bias:", bias)

# =========================================================
# STEP 7: PREDICTION FUNCTION
# =========================================================
def predict(features):
    z = np.dot(features, weights) + bias
    prob = sigmoid(z)
    label = 1 if prob >= 0.5 else 0
    return prob, label

# =========================================================
# STEP 8: TEST ON NEW DATA
# =========================================================
# Example: Male, CS, 4 hours
test_input = np.array([1, 0, 1, 0, 4])

prob, label = predict(test_input)

print("\n====== NEW PREDICTION ======")
print("Input: Male, CS, 4 hours")
print("Probability of PASS:", prob)
print("Predicted Class:", "PASS" if label == 1 else "FAIL")
