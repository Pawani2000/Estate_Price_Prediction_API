Introduction
This guide will demonstrate how to deploy a machine learning (ML) model using FastAPI on Render, a cloud-based platform that simplifies web service deployment. The tutorial will cover key deployment stages, from training a linear regression model for real estate price prediction to building a FastAPI application that serves the model as an API. Additionally, we will go through the steps for deploying the app on Render, testing the API to ensure correct functionality, and setting up a CI/CD pipeline to enable continuous deployment for streamlined updates and maintenance.

API Deploy Link

https://estate-price-prediction-api.onrender.com

Medium Article.
The article explains how to deploy a FastAPI machine learning app on Render, covering setup, configuration, and deployment steps.
https://medium.com/@nimashapawani2000/how-to-deploy-a-fastapi-machine-learning-application-in-render-9b9744582cc5

Training the Machine Learning Model
The real estate dataset used for this project contains several features that impact house prices. The goal of the machine learning model is to predict real estate prices using a simple linear regression algorithm. The features that the model uses as inputs are:

House Age: The age of the house in years.

Distance to the Nearest MRT Station: The distance, in meters, between the house and the closest MRT (Mass Rapid Transit) station. Proximity to public transportation often influences property values.

Number of Convenience Stores Nearby: The number of convenience stores located near the house, can be an indicator of neighborhood amenities.

Latitude: The geographical latitude of the property, which helps identify the house’s location and its impact on price.

The target variable, which the model aims to predict, is the house price. We split the dataset into training and testing sets, ensuring that the model is trained on a portion of the data and validated on a separate test set. After training, the model was evaluated on how well it predicted prices for unseen data.

The steps involved in training the model
Data Preprocessing: After loading the dataset, we identified and removed any rows with missing values to ensure the data was clean. The input features (X) were extracted from the dataset, along with the target variable (y), which represented the house prices.




Splitting the Data: The data was split into traiing and test sets using the train_test_split function. We reserved 30% of the data for testing the model, ensuring that the model’s performance could be evaluated on unseen data.

Model Training: We used the linear regression model from the sklearn library to train the model on the training data. The model learned the relationships between the input features (house age, distance to MRT, number of convenience stores, latitude) and the target variable (house price).


Prediction and Evaluation: After training, the model made predictions on the test set. We visualized the results using a scatter plot to compare the actual house prices against the predicted prices.


Saving the Model: Finally, the trained model was saved as a .pkl file (reg.pkl) using the pickle library. This file was later used in the FastAPI application to serve predictions.


Building the FastAPI Application
The FastAPI application is designed to serve predictions from the trained machine learning model. Below is a breakdown of the different components of the FastAPI app and their functions.

Importing Necessary Libraries
At the beginning, we import the required libraries for the FastAPI application to function and handle machine learning predictions


FastAPI: The web framework for building the API.

Pydantic: Used for data validation. It ensures the input data to the API is structured correctly.

Joblib: Used to load the trained model that was saved as a .pkl file.

Numpy: For handling numerical data and arrays.

Mangum: A utility that allows you to deploy FastAPI on AWS Lambda, although it is optional and mainly used for serverless deployment.

app = FastAPI(): This initializes a FastAPI application instance.
handler = Mangum(app): This line is used to make the app compatible with AWS Lambda for serverless deployment. You may skip this if deploying elsewhere, such as Render.

Defining the Input Data Model
We define the structure of the input data using Pydantic’s BaseModel


RealEstateFeatures: This class specifies the required input features for the prediction. Each feature (house_age, distance_to_mrt, number_of_convenience_stores, and latitude) is assigned a type (float or int).
Pydantic validates that any request to the API provides the necessary data in the correct format.

Loading the Trained Model
To make predictions, we need to load the previously trained machine learning model


model = joblib.load(“reg.pkl”): This line loads the model from the saved .pkl file so that the API can use it for predictions. The model file must be in the same directory as the FastAPI app.

Defining the API Endpoints
There are two main endpoints in the FastAPI app: a root endpoint and a prediction endpoint.


Prediction Endpoint (POST /predict/)
This endpoint accepts real estate features in a JSON format and returns the predicted house price based on the provided input.


Purpose: To predict the house price based on the input features.
Input: A JSON object with real estate features such as house age, distance to MRT station, number of convenience stores, and latitude.
Response: A JSON object with the predicted house price.

Steps for Deployment
Create a GitHub Repository:- Push your FastAPI code to a GitHub repository.

Set Up Render

Go to Render and sign up for an account.
Click on New and select Web Service.
Connect your GitHub repository.
Render will automatically detect that you have a FastAPI app and create a deployment configuration.
Configure Render Deployment:- Set the build command to install your dependencies


The start command for FastAPI will be


CI/CD with GitHub Actions
To automate the deployment process, you can set up a CI/CD pipeline using GitHub Actions. Every time you push code changes to your GitHub repository, GitHub Actions can automatically build and deploy your app to Render.

GitHub Actions Workflow:
Create a .github/workflows/deploy.yml file in  repository


This guide covered the complete workflow for deploying a FastAPI-based machine learning application on Render, including

Training a Linear Regression Model: Predict house prices based on real estate features.
Building a FastAPI Application: Serve predictions via a REST API.
Deploying on Render: Simplified deployment using Render’s cloud platform.
CI/CD Setup: Continuous integration for automatic deployment on code changes.
By following these steps, you can efficiently deploy and maintain your FastAPI-based ML model using Render.
