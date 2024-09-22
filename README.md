
<h1>Estate Price Prediction API</h1>

<h2>Introduction</h2>
<p>This guide will demonstrate how to deploy a machine learning (ML) model using FastAPI on Render, a cloud-based platform that simplifies web service deployment. The tutorial will cover key deployment stages, from training a linear regression model for real estate price prediction to building a FastAPI application that serves the model as an API. Additionally, we will go through the steps for deploying the app on Render, testing the API to ensure correct functionality, and setting up a CI/CD pipeline to enable continuous deployment for streamlined updates and maintenance.</p>

<h3>API Deploy Link</h3>
<p><a href="https://estate-price-prediction-api.onrender.com">https://estate-price-prediction-api.onrender.com</a></p>

<h3>Medium Article</h3>
<p>The article explains how to deploy a FastAPI machine learning app on Render, covering setup, configuration, and deployment steps.</p>
<p><a href="https://medium.com/@nimashapawani2000/how-to-deploy-a-fastapi-machine-learning-application-in-render-9b9744582cc5">https://medium.com/@nimashapawani2000/how-to-deploy-a-fastapi-machine-learning-application-in-render-9b9744582cc5</a></p>

<h2>Training the Machine Learning Model</h2>
<p>The real estate dataset used for this project contains several features that impact house prices. The goal of the machine learning model is to predict real estate prices using a simple linear regression algorithm. The features that the model uses as inputs are:</p>

<ul>
    <li><strong>House Age:</strong> The age of the house in years.</li>
    <li><strong>Distance to the Nearest MRT Station:</strong> The distance, in meters, between the house and the closest MRT (Mass Rapid Transit) station. Proximity to public transportation often influences property values.</li>
    <li><strong>Number of Convenience Stores Nearby:</strong> The number of convenience stores located near the house can be an indicator of neighborhood amenities.</li>
    <li><strong>Latitude:</strong> The geographical latitude of the property, which helps identify the house’s location and its impact on price.</li>
</ul>

<p>The target variable, which the model aims to predict, is the house price. We split the dataset into training and testing sets, ensuring that the model is trained on a portion of the data and validated on a separate test set. After training, the model was evaluated on how well it predicted prices for unseen data.</p>

<h3>The steps involved in training the model</h3>

<ul>
    <li><strong>Data Preprocessing:</strong> After loading the dataset, we identified and removed any rows with missing values to ensure the data was clean. The input features (X) were extracted from the dataset, along with the target variable (y), which represented the house prices.</li>
    <li><strong>Splitting the Data:</strong> The data was split into training and test sets using the <code>train_test_split</code> function. We reserved 30% of the data for testing the model, ensuring that the model’s performance could be evaluated on unseen data.</li>
    <li><strong>Model Training:</strong> We used the linear regression model from the sklearn library to train the model on the training data. The model learned the relationships between the input features (house age, distance to MRT, number of convenience stores, latitude) and the target variable (house price).</li>
    <li><strong>Prediction and Evaluation:</strong> After training, the model made predictions on the test set. We visualized the results using a scatter plot to compare the actual house prices against the predicted prices.</li>
    <li><strong>Saving the Model:</strong> Finally, the trained model was saved as a <code>.pkl</code> file (<code>reg.pkl</code>) using the pickle library. This file was later used in the FastAPI application to serve predictions.</li>
</ul>

<h2>Building the FastAPI Application</h2>
<p>The FastAPI application is designed to serve predictions from the trained machine learning model. Below is a breakdown of the different components of the FastAPI app and their functions.</p>

<h3>Importing Necessary Libraries</h3>
<p>At the beginning, we import the required libraries for the FastAPI application to function and handle machine learning predictions:</p>

<ul>
    <li><strong>FastAPI:</strong> The web framework for building the API.</li>
    <li><strong>Pydantic:</strong> Used for data validation. It ensures the input data to the API is structured correctly.</li>
    <li><strong>Joblib:</strong> Used to load the trained model that was saved as a <code>.pkl</code> file.</li>
    <li><strong>Numpy:</strong> For handling numerical data and arrays.</li>
    <li><strong>Mangum:</strong> A utility that allows you to deploy FastAPI on AWS Lambda, although it is optional and mainly used for serverless deployment.</li>
</ul>

<h3>Defining the Input Data Model</h3>
<p>We define the structure of the input data using Pydantic’s <code>BaseModel</code>:</p>

<ul>
    <li><code>RealEstateFeatures:</code> This class specifies the required input features for the prediction. Each feature (<code>house_age</code>, <code>distance_to_mrt</code>, <code>number_of_convenience_stores</code>, and <code>latitude</code>) is assigned a type (<code>float</code> or <code>int</code>).</li>
</ul>

<h3>Loading the Trained Model</h3>
<p>To make predictions, we need to load the previously trained machine learning model:</p>
<pre><code>model = joblib.load(“reg.pkl”)</code></pre>
<p>This line loads the model from the saved <code>.pkl</code> file so that the API can use it for predictions. The model file must be in the same directory as the FastAPI app.</p>

<h3>Defining the API Endpoints</h3>
<p>There are two main endpoints in the FastAPI app: a root endpoint and a prediction endpoint.</p>

<h3>Prediction Endpoint (POST /predict/)</h3>
<p>This endpoint accepts real estate features in a JSON format and returns the predicted house price based on the provided input.</p>

<ul>
    <li><strong>Purpose:</strong> To predict the house price based on the input features.</li>
    <li><strong>Input:</strong> A JSON object with real estate features such as house age, distance to MRT station, number of convenience stores, and latitude.</li>
    <li><strong>Response:</strong> A JSON object with the predicted house price.</li>
</ul>

<h2>Steps for Deployment</h2>
<ol>
    <li><strong>Create a GitHub Repository:</strong> Push your FastAPI code to a GitHub repository.</li>
    <li><strong>Set Up Render</strong></li>
    <ol>
        <li>Go to Render and sign up for an account.</li>
        <li>Click on <strong>New</strong> and select <strong>Web Service</strong>.</li>
        <li>Connect your GitHub repository.</li>
        <li>Render will automatically detect that have a FastAPI app and create a deployment configuration.</li>
        <li><strong>Configure Render Deployment:</strong> Set the build command to install dependencies.</li>
    </ol>
</ol>

<h2>CI/CD with GitHub Actions</h2>
<p>To automate the deployment process, can set up a CI/CD pipeline using GitHub Actions. Every time you push code changes to your GitHub repository, GitHub Actions can automatically build and deploy app to Render.</p>

<h3>GitHub Actions Workflow:</h3>
<p>Create a <code>.github/workflows/deploy.yml</code> file in repository.</p>

<h2>Summary</h2>
<p>This guide covered the complete workflow for deploying a FastAPI-based machine learning application on Render, including:</p>

<ul>
    <li><strong>Training a Linear Regression Model:</strong> Predict house prices based on real estate features.</li>
    <li><strong>Building a FastAPI Application:</strong> Serve predictions via a REST API.</li>
    <li><strong>Deploying on Render:</strong> Simplified deployment using Render’s cloud platform.</li>
    <li><strong>CI/CD Setup:</strong> Continuous integration for automatic deployment on code changes.</li>
</ul>

<p>By following these steps, you can efficiently deploy and maintain FastAPI-based ML model using Render.</p>

</body>
</html>
