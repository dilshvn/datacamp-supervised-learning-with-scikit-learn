import numpy as np

# Create X from the radio column's values
X = pd.DataFrame(sales_df['radio']).values

# Create y from the sales column's values
y = pd.DataFrame(sales_df['sales']).values

# Reshape X
X = X.reshape(-1, 1)

# Check the shape of the features and targets
print(X.shape, y.shape)