# Forest-Fire-Prediction-Using-Machine-Learning-
A machine learning project that predicts the likelihood and spread of forest fires based on environmental and meteorological data. This model analyzes factors like temperature, humidity, wind speed, rainfall, and vegetation indices to assess fire risk in forested regions.




RESARCH PAPER :  https://docs.google.com/document/d/1xvojKsUmLpQSMEqTS95_xsFfqG8_nIv8/edit


Brief description :


Data collection and preprocessing from multiple sources (images, weather, sensors)
Machine learning model development and training for accurate fire detection
Real-time detection system with alert notifications and visualization dashboard

Installation

1.Clone the repository:
git clone https://github.com/ARCHanavedulla/forest-fire-detection.git
2.Install required packages:
pip install -r requirements.txt

Forest Fire Detection System Workflow

1.Data Collection

Collect satellite images, weather data (temperature, humidity, wind speed), and sensor data (smoke, gas sensors).
Store raw data in a structured format.
Data Preprocessing

2.Clean the data: remove noise, handle missing values.
Normalize or standardize features.
Label the data: fire vs. non-fire instances.
For image data (satellite), resize and augment images.
Split data into training, validation, and test sets.
3.Feature Extraction and Selection

For time-series or sensor data, extract relevant features.
For image data, use convolutional layers (ConvLSTM) for spatial-temporal features.
Select important features to improve model efficiency.
Model Training

4.Train multiple models:
MLP (Multi-Layer Perceptron): For structured numerical data.
KNN (K-Nearest Neighbors): Simple baseline for classification.
Decision Tree: For interpretable rule-based classification.
RNN (Recurrent Neural Network): For sequential time-series data.
ConvLSTM: For spatiotemporal sequence data like satellite images.
Tune hyperparameters using cross-validation.
Evaluate models using accuracy, precision, recall, and F1-score.
5.Model Evaluation & Selection

Compare model performance.
Select the best performing model or ensemble models.
6.Real-Time Detection System

Deploy the selected model.
Input real-time data streams (satellite images and sensor data).
Process and predict forest fire occurrence.
Generate alerts and notifications if fire risk is detected.
7.Visualization & Monitoring

Display detected fire locations on maps.
Provide dashboards for monitoring sensor data and alerts.

[Data Collection] --> [Data Preprocessing] --> [Feature Extraction & Selection]
       |                      |                             |
       v                      v                             v
                  [Model Training with MLP, KNN, Decision Tree, RNN, ConvLSTM]
                                             |
                                             v
                              [Model Evaluation & Selection]
                                             |
                                             v
                                  [Real-Time Fire Detection]
                                             |
                                             v
