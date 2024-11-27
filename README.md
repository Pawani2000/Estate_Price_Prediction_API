# 🏡 Estate Price Prediction API  

Welcome to the **Estate Price Prediction API**!  
This project demonstrates deploying a machine learning (ML) model using **FastAPI** on **Render**, a cloud platform for seamless web service deployment.  

The guide covers:  
- 🧠 Training a linear regression model to predict real estate prices.  
- 🚀 Building a FastAPI application to serve predictions.  
- 🌐 Deploying on Render with a CI/CD pipeline for automated updates.  

---

## 📌 **API Deploy Link**  
🔗 [Estate Price Prediction API](https://estate-price-prediction-api.onrender.com)  

## 📄 **Medium Article**  
📝 Learn how to deploy a FastAPI ML app on Render:  
🔗 [How to Deploy a FastAPI Machine Learning Application in Render](https://medium.com/@nimashapawani2000/how-to-deploy-a-fastapi-machine-learning-application-in-render-9b9744582cc5)  

---

## 📊 **Training the Machine Learning Model**  

The real estate dataset includes several features influencing house prices.  
The model uses **Linear Regression** for predictions based on:  

- **🏠 House Age:** The property's age in years.  
- **🚇 Distance to MRT Station:** Proximity to the nearest transit station (in meters).  
- **🛒 Convenience Stores Nearby:** Number of stores in the vicinity.  
- **🌍 Latitude:** Geographical location of the property.  

The **target variable**: House price.  

### **Model Training Steps**  

1. **🧹 Data Preprocessing:**  
   - Cleaned data by removing missing values.  
   - Extracted input features (**X**) and target variable (**y**).  

2. **📂 Data Splitting:**  
   - Reserved 30% of data for testing using `train_test_split`.  

3. **🛠️ Model Training:**  
   - Used sklearn's Linear Regression to train the model.  

4. **📈 Prediction & Evaluation:**  
   - Compared actual vs. predicted house prices using scatter plots.  

5. **💾 Saving the Model:**  
   - Saved the trained model as `reg.pkl` for deployment.  

---

## ⚙️ **Building the FastAPI Application**  

The FastAPI app serves predictions using the trained model.  

### **Key Components**  

- **📦 Libraries Used:**  
  - **FastAPI:** Web framework for building APIs.  
  - **Pydantic:** Input data validation.  
  - **Joblib:** Load the trained ML model.  
  - **Numpy:** Handle numerical computations.  

- **📑 Input Data Model:**  
  Defined using Pydantic’s `BaseModel` for real estate features like:  
  - `house_age` (float)  
  - `distance_to_mrt` (float)  
  - `number_of_convenience_stores` (int)  
  - `latitude` (float)  

- **🔄 Prediction Endpoint:**  
  Accepts JSON input and returns predicted house prices.  

---

## 🌐 **Steps for Deployment**  

### **1. GitHub Repository**  
Push the FastAPI app and trained model to a GitHub repository.  

### **2. Render Setup**  
- Sign up at [Render](https://render.com).  
- Click **New** > **Web Service**.  
- Connect the GitHub repository.  
- Configure the build command to install dependencies.  

### **3. CI/CD with GitHub Actions**  
- Automate deployment with a GitHub Actions workflow:  
  Create `.github/workflows/deploy.yml`.  
  Push changes to automatically build and deploy on Render.  

---

## 🎯 **Summary**  

This guide covers the complete workflow for deploying a FastAPI-based ML app on Render:  

1. **📈 Training a Model:** Predict house prices with linear regression.  
2. **🖥️ Building an API:** Serve predictions via REST API.  
3. **☁️ Deploying on Render:** Simplified deployment and hosting.  
4. **🔄 CI/CD Integration:** Automate deployments with GitHub Actions.  

By following this guide, you can efficiently deploy and maintain your FastAPI-based ML model. 🚀  

---

Feel free to contribute or suggest improvements! 🌟  
**💻 Happy Coding!** 😄
