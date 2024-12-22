# Delay Prediction Web Application

This project is a web application that predicts whether a shipment will be delayed based on various input features. It uses a Flask backend to handle predictions using a machine learning model.

## Features

- User-friendly web interface to input shipment details.
- Predicts if a shipment is delayed based on user input.
- Built with Flask, HTML, CSS, and JavaScript.

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: scikit-learn
- **Data Handling**: pandas
- **Data Visualization**: matplotlib, seaborn
- **Excel File Handling**: openpyxl

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python src/4_api.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. **Use the web interface** to input the shipment details and click the "Predict" button to see if the shipment is delayed.

## API Endpoints

- **POST /predict**: Accepts JSON data with the following fields:
  - `Origin`: The origin of the shipment.
  - `Destination`: The destination of the shipment.
  - `Vehicle Type`: The type of vehicle used for the shipment.
  - `Weather Conditions`: The weather conditions during the shipment.
  - `Traffic Conditions`: The traffic conditions during the shipment.
  - `Shipment_Duration`: The planned shipment duration in days.
  - `Actual_Duration`: The actual duration of the shipment in days.

## Example Request
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{
"Origin": "A",
"Destination": "B",
"Vehicle Type": "Truck",
"Weather Conditions": "Clear",
"Traffic Conditions": "Normal",
"Shipment_Duration": 5,
"Actual_Duration": 4
}'


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the contributors and libraries that made this project possible.
