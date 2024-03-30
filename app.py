# Import necessary libraries
from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from datetime import timedelta
import os
import numpy as np
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['STATIC_FOLDER'] = STATIC_FOLDER

# Ensure the upload and static folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# Function to preprocess data
def preprocess_data(df):
    if 'Date' in df.columns:
        # Specify the date format if you know it, for example, '%Y-%m-%d' for '2023-01-25'
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')  # Adjust format as necessary
    return df


# Function to generate pie chart for monthly expense breakdown
def generate_monthly_expense_pie_chart(df, month=None):
    if month:
        df = df[df['Date'].dt.month == month]
    expenses = df.groupby('Category')['Amount'].sum()
    plt.figure(figsize=(8, 8))
    plt.pie(expenses, labels=expenses.index, autopct='%1.1f%%', startangle=140)
    plt.title('Monthly Expense Breakdown')
    image_path = os.path.join('static', 'images', 'monthly_expense_breakdown.png')
    plt.savefig(image_path)
    return image_path

# Function to generate line graph with ARIMA predictions
def generate_predictive_spending(df, category):
    # Replace forward slash with underscore
    category = category.replace('/', '_')
    
    df_cat = df[df['Category'] == category].set_index('Date')
    df_cat_monthly = df_cat.resample('ME').sum()
    if len(df_cat_monthly) < 3:  # ARIMA models generally need more data; adjust this threshold as needed
        print(f"Not enough data for ARIMA model in category {category}.")
        return None
    model = ARIMA(df_cat_monthly['Amount'], order=(1,1,1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=12)
    forecast_dates = [df_cat_monthly.index[-1] + timedelta(days=31*i) for i in range(1, 13)]
    plt.figure(figsize=(10, 6))
    plt.plot(df_cat_monthly.index, df_cat_monthly['Amount'], label='Actual Spending')
    plt.plot(forecast_dates, forecast, label='Predicted Spending', linestyle='--')
    plt.title('Predictive Spending for ' + category)
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.legend()
    image_path = os.path.join('static', 'images', f'predictive_spending_{category.lower()}.png')
    plt.savefig(image_path)
    return image_path

# Function to generate bar chart for savings opportunity
def generate_savings_opportunity(df, benchmarks):
    savings = {}
    for category, benchmark in benchmarks.items():
        actual_spending = df[df['Category'] == category]['Amount'].sum()
        savings[category] = actual_spending - benchmark
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(savings.keys()), y=list(savings.values()))
    plt.title('Savings Opportunity Graph')
    plt.xlabel('Category')
    plt.ylabel('Potential Savings')
    image_path = os.path.join('static', 'images', 'savings_opportunity.png')
    plt.savefig(image_path)
    return image_path

# Function to calculate the Spending Efficiency Index
def calculate_spending_efficiency_index(df, benchmarks):
    efficiency_index = {}
    for category, benchmark in benchmarks.items():
        actual_spending = df[df['Category'] == category]['Amount'].sum()
        efficiency_index[category] = actual_spending / benchmark
    return efficiency_index

# Function to generate radar chart for spending efficiency index
def generate_spending_efficiency_radar_chart(efficiency_index):
    categories = list(efficiency_index.keys())
    values = list(efficiency_index.values())
    num_categories = len(categories)
    
    angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='blue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title('Spending Efficiency Index')
    image_path = os.path.join('static', 'images', 'spending_efficiency_radar_chart.png')
    plt.savefig(image_path)
    return image_path

# Function to process uploaded CSV file
def process_uploaded_file(filename):
    df = pd.read_csv(filename)
    df = preprocess_data(df)
    # Generate analysis images and get their paths
    monthly_expense_image_path = generate_monthly_expense_pie_chart(df)
    predictive_spending_image_paths = [generate_predictive_spending(df, category) for category in df['Category'].unique()]
    savings_opportunity_image_path = generate_savings_opportunity(df, {'Food': 200, 'Utilities': 500, 'Health': 100})
    efficiency_index = calculate_spending_efficiency_index(df, {'Food': 200, 'Utilities': 500, 'Health': 100})
    efficiency_index_image_path = generate_spending_efficiency_radar_chart(efficiency_index)
    
    # Filter out None paths
    predictive_spending_image_paths = [path for path in predictive_spending_image_paths if path]

    return jsonify({
        'monthly_expense_image_path': monthly_expense_image_path,
        'predictive_spending_image_paths': predictive_spending_image_paths,
        'savings_opportunity_image_path': savings_opportunity_image_path,
        'efficiency_index_image_path': efficiency_index_image_path
    })

# Endpoint for uploading files and receiving analysis results
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return process_uploaded_file(filepath)

# Endpoint to serve images
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)