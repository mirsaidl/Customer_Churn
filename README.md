# Machine Learning Model Deployment with Streamlit

## Overview
This project demonstrates how to build, preprocess, and deploy a machine learning model using Python, with a Streamlit web interface for user interaction. The primary objective is to predict customer churn based on input data, leveraging a trained model and preprocessed pipeline.

## Project Structure
- **Streamlit Web Interface**: User-friendly input form for customer data.
- **Data Preprocessing**: Preprocessing pipeline loaded from a `.pkl` file.
- **Model Prediction**: Predicts churn status based on user input.
- **Evaluation**: Metrics to assess model performance.
- **Confusion Matrix**: Visualizes the model's prediction results.

## How to Run the App
1. Install these dependencies with:
```bash
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```
2. Navigate to the project directory.
3. Run the following command to launch the Streamlit app:

   ```bash
   streamlit run app.py
   ```
4. The web application will open in your default browser.

## Usage Instructions
1. **Input Fields**:
   - **CustomerID**: Unique identifier for each customer.
   - **Age**: Age of the customer.
   - **Gender**: Select from options (e.g., Male, Female).
   - **Tenure**: Duration of the customer’s subscription.
   - **Usage Frequency**: Frequency of usage (e.g., Weekly, Monthly).
   - **Support Calls**: Number of support calls made.
   - **Payment Delay**: Delay in payment (e.g., in days).
   - **Subscription Type**: Type of subscription (e.g., Basic, Premium).
   - **Contract Length**: Duration of the contract.
   - **Total Spend**: Total amount spent by the customer.
   - **Last Interaction**: Days since the last interaction.

2. **Submit Button**:
   - Ensure all fields are filled before submission.
   - If any field is missing, a warning message will be displayed.

3. **Prediction**:
   - After submission, the model predicts churn status.
   - The output will indicate whether the customer is likely to churn (1) or not (0).

## Future Trends
- **Vertex AI Deployment**:
  - Leveraging Google's Vertex AI for scalable, managed ML deployment and monitoring.
- **More Data**:
  - Incorporating larger datasets to enhance model accuracy and generalization.
- **Application in Big Tech**:
  - Custom AI solutions for real-time decision-making at scale.
- **Other Ideas**:
  - **Federated Learning**: Training models on decentralized data sources to maintain privacy.
  - **MLOps**: Implementing CI/CD pipelines for seamless model development and deployment.
  - **Explainable AI (XAI)**: Building transparent models for improved trust and interpretability.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per your needs.

---

Feel free to customize or add any additional details specific to your project or deployment instructions.
