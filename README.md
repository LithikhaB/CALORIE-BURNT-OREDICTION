# Calorie Burn Prediction App

This is a web application built using Streamlit that predicts the number of calories burned based on user input. The application uses a trained Random Forest Regressor model to make predictions.

## Features

* User-friendly interface for inputting data
* Predicts calories burned based on:
	+ Gender (Male/Female)
	+ Age
	+ Height (in cm)
	+ Weight (in kg)
	+ Duration of exercise (in minutes)
	+ Heart rate (in bpm)
	+ Body temperature (in °C)
* Displays predicted calories burned with two decimal places

## Model

* Trained using a Random Forest Regressor model
* Model is saved as a pickle file and loaded into the application
* Model takes in user input data and makes predictions

## Usage

1. Clone the repository
2. Run the application using `streamlit run app.py`
3. Input data into the application and click "Predict" to see the predicted calories burned

## Note

* This application is for demonstration purposes only and should not be used for actual calorie burn tracking.
* The model is trained on a limited dataset and may not be accurate for all users.
* Please consult a healthcare professional for accurate calorie burn tracking and advice.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
