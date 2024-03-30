# PennyPro

PennyPro is a financial analysis tool designed to help users gain insights into their spending habits through uploaded financial data. Utilizing a Python backend with Flask and a React frontend, PennyPro analyzes CSV files containing expense data and visualizes spending patterns, predictive spending, savings opportunities, and spending efficiency.

## Features

- **Upload Expense Data**: Users can upload their financial data in CSV format.
- **Visualize Spending**: Generates pie charts, line graphs, and radar charts to visualize spending habits, predictive spending, and more.
- **Predictive Spending Analysis**: Utilizes ARIMA models to forecast future spending in various categories.
- **Efficiency and Opportunity Insights**: Identifies potential savings opportunities and evaluates spending efficiency.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or later
- Node.js and npm

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/PennyPro.git
cd PennyPro
```

2. **Set up the Python virtual environment**

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install Python dependencies
pip install Flask pandas matplotlib seaborn statsmodels flask-cors
```

3. **Start the Flask backend**

```bash
# Set the FLASK_APP environment variable
export FLASK_APP=app.py  # On Windows, use 'set' instead of 'export'

# Run the Flask app
flask run
```

4. **Install and start the React frontend**

Open a new terminal or command prompt, navigate to the PennyPro directory, then:

```bash
# Navigate to the frontend directory if separate
# cd frontend  # Skip if your project is structured differently

# Install npm dependencies
npm install

# Start the React app
npm start
```

### Usage

1. **Access the Web Interface**: Open a browser and navigate to `http://localhost:3000` to access the PennyPro interface.
2. **Upload Expense Data**: Use the web interface to upload a CSV file containing your expense data.
3. **View Analysis**: After uploading, the analysis will be displayed, visualizing your spending data and insights.


## License

This project is licensed under the Apache-2.0 license - see the [LICENSE](LICENSE) file for details.

