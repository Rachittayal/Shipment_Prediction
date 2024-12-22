import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_excel('data/AI ML Internship Training Data.xlsx')

# Fill missing values
data.ffill(inplace=True)

# Feature engineering
data['Shipment_Duration'] = (
    pd.to_datetime(data['Planned Delivery Date']) - pd.to_datetime(data['Shipment Date'])
).dt.days
data['Actual_Duration'] = (
    pd.to_datetime(data['Actual Delivery Date']) - pd.to_datetime(data['Shipment Date'])
).dt.days

# Encode categorical variables
encoder = LabelEncoder()
for col in ['Origin', 'Destination', 'Vehicle Type', 'Weather Conditions', 'Traffic Conditions']:
    data[col] = encoder.fit_transform(data[col])

# Split dataset into training and testing sets
X = data.drop(columns=['Delayed', 'Shipment ID', 'Shipment Date', 'Planned Delivery Date', 'Actual Delivery Date'])
y = data['Delayed'].apply(lambda x: 1 if x == 'Yes' else 0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save processed data
X_train.to_csv('data/X_train.csv', index=False)
X_test.to_csv('data/X_test.csv', index=False)
y_train.to_csv('data/y_train.csv', index=False)
y_test.to_csv('data/y_test.csv', index=False)

print("Data preparation completed.")
