import pickle
import pandas as pd

# Load the model
with open('model_pipeline.pkl', 'rb') as file:
    model = pickle.load(file)

# Example data (replace with your actual data)
data = {
    'Job': [1,2],
    'Housing': ['own', 'free'],
    'Saving accounts': ['little', 'moderate'],
    'Checking account': ['rich', 'little'],
    'Credit amount': [1200, 3000],
    'Purpose': ['radio/TV', 'education'],
    'Repayment Age': [24, 36]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)
df.head()
# If the model expects preprocessing (like encoding or scaling), you can add that here
# For example, you might need to encode categorical columns like 'Job', 'Housing', 'Purpose', etc.
# Assuming you have some encoder or scaler, you'd apply it like this:
# Example (Replace with your actual preprocessing logic):
# df_encoded = your_preprocessor.transform(df)

# Make a prediction using the model
prediction = model.predict(df)

# Output the result
print(f"Predictions: {prediction}")
