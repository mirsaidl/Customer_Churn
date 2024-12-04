Machine Learning Model Deployment with Streamlit
— Introduction
This project demonstrates how to build, preprocess, and deploy a machine learning model for predicting customer churn using Python. The user-friendly interface is created with Streamlit, allowing seamless interaction and predictions.

— Installation
To set up and run this project, follow these steps:

Clone the Repository:
```
bash
git clone https://github.com/mirsaidl/Customer_Churn.git
cd Customer_Churn
```

Create a Virtual Environment (optional but recommended):

```
bash
python -m venv myenv
source myenv/bin/activate  # For Windows, use `myenv\Scripts\activate`
```

Install Dependencies:
```
bash
Copy code
pip install -r requirements.txt
```
Run the Streamlit App:

```
bash
streamlit run app.py
```
This command will launch the Streamlit app, which will open in your default web browser.

### Data Familiarization
Dataset Overview: The dataset contains the following columns:
CustomerID, Age, Gender, Tenure, Usage Frequency, Support Calls, Payment Delay, Subscription Type, Contract Length, Total Spend, Last Interaction, Churn.
Data Types:
Categorical columns: Gender, Subscription Type, Contract Length.
Numerical columns: Age, Tenure, Usage Frequency, etc.
Initial Insights: Identified data columns and prepared them for preprocessing and model training.
— Data Analysis (EDA)
Exploratory Data Analysis (EDA):
Examined the distribution of features like Age, Tenure, and Total Spend.
Analyzed relationships between Churn and input features.
Detected missing values and outliers that required attention.
Visualization: Used data visualization tools (e.g., Seaborn, Matplotlib) for histograms, bar charts, and correlation plots to understand feature distributions and interactions.


### Preprocessing the Data
Handling Missing Data: Applied data cleaning techniques to remove or fill missing values.
Encoding Categorical Variables: Used label encoding and one-hot encoding to transform categorical features for model compatibility.
Feature Scaling: Normalized numerical features for better model performance.
Pipeline Creation: Created and saved a preprocessing pipeline using joblib, which was later loaded for consistent data transformation during deployment.

### Model Development / ML
Model Selection: Chose an appropriate machine learning model, such as logistic regression or other classification models.
Training the Model: Trained the model on the preprocessed training data.
Evaluation Metrics:
Calculated metrics like accuracy, precision, recall, and F1 score.
Visualized the confusion matrix to assess true/false positives and negatives.
Model Saving: Saved the trained model using joblib to facilitate loading during deployment.

### Deployment & MLOPS
Streamlit Web Interface:
Created an interactive web app where users input customer data.
Incorporated data input fields for all necessary features.
Added a submit button to process user data and predict churn status.
Displayed warnings if required fields were missing.
Model Loading: Loaded the pre-trained model and preprocessing pipeline in the Streamlit app.
Prediction: The app processed user inputs and displayed churn predictions (e.g., 1 for likely to churn, 0 for not likely).
User Experience: The application includes a user-friendly interface with clear instructions and feedback messages.
Confusion Matrix Visualization: Provided a visual representation of model performance in the application using Seaborn.

### Future Trends and Conclusion
Vertex AI Deployment:
Plan to deploy the model on Google's Vertex AI for scalable and managed machine learning services.
More Data:
Integrate larger and more diverse datasets to improve the model's predictive capabilities and generalization.
Application in Big Tech:
Extend the model's application to big tech companies for real-time, large-scale decision-making.


### Conclusion
This project provides a comprehensive approach to developing, deploying, and maintaining a machine learning model. By combining preprocessing, model training, and an interactive web interface, the solution can effectively predict customer churn and be extended to meet future trends in machine learning and big data applications.
