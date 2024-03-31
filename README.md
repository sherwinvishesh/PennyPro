# PennyPro: Empowering Financial Insights with Blockchain and AI


PennyPro is an innovative financial analysis platform, leveraging the cutting-edge technologies of blockchain and artificial intelligence (AI) to offer users unparalleled insights into their spending habits and financial health. Powered by Sui, a leading blockchain company, PennyPro stands at the intersection of decentralized finance (DeFi) and predictive analytics, providing secure, transparent, and predictive financial planning tools for its users.


## Features


- **Blockchain-Backed Data Security**: Utilizes the Sui blockchain to ensure the utmost security and integrity of financial data uploaded by users.
- **AI-Powered Predictive Analysis**: Leverages advanced ARIMA models for predictive spending analysis, offering users foresight into their financial future.
- **Comprehensive Financial Visualization**: Generates detailed charts and graphs, including pie charts for spending breakdowns, line graphs for predictive analysis, and radar charts for spending efficiency, all powered by AI-driven insights.
- **Decentralized Financial Insights**: Integrates with Sui's blockchain ecosystem to provide a decentralized approach to managing and analyzing personal finances.




## User Interface




## Getting Started


Follow these instructions to set up PennyPro locally for development, testing, and exploration of its blockchain and AI features.


### Prerequisites


- Python 3.7 or later
- Node.js and npm
- Access to Sui blockchain (for blockchain-specific functionalities)


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


- **Access PennyPro**: Navigate to `http://localhost:3000` to explore PennyPro's functionalities.
- **Upload and Analyze**: Securely upload your financial data in CSV format or upload manually for AI and blockchain-powered analysis.
- **Explore Insights**: Dive into the visualizations and predictions to understand and improve your financial habits.




## Graphs Used


### Monthly Expense Breakdown
**Graph Type:** Pie Chart


**Description:** This graph offers a visual breakdown of expenses by category for a given month, using a pie chart for easy understanding. It highlights where the bulk of a user's budget is going, such as rent, groceries, or entertainment, helping identify potential areas for cost-saving. The pie chart's simplicity and immediate visual impact make it a powerful tool for quick financial assessments and planning adjustments.


### Spending Efficiency Index
**Graph Type:** Radar Chart


**Description:** Utilizing a radar chart, this visualization compares spending efficiency across various categories based on value gained versus cost. It helps users pinpoint areas where spending aligns with personal value or benchmarks and where it doesn't, facilitating smarter budget allocations. This graph encourages reflection on spending habits, guiding users towards more value-conscious expenditure decisions and overall financial well-being.


### Predictive Spending by Category
**Graph Type:** Line Graph with Prediction


**Description:** Employing ARIMA or similar forecasting models, this line graph predicts future spending by category based on past data. It enables users to anticipate expenses and adjust budgets early, helping avoid overspending. By visualizing future spending trends, this tool aids in crafting a proactive financial strategy, ensuring users remain on track with their financial goals.


### Savings Opportunity Graph
**Graph Type:** Bar Chart or Dual-Axis Line Chart


**Description:** This graph compares actual spending against benchmarks in various categories, identifying areas of potential savings. Highlighting discrepancies, it quantifies how adjusting spending closer to these benchmarks can lead to savings. Through machine learning analysis, it offers personalized insights into spending patterns, empowering users with actionable advice for optimizing their budget and improving financial health.


## Technologies Used


### Frontend


- **React**: Utilized for building the user interface, providing a responsive and interactive web application experience. React's component-based architecture facilitates efficient development of complex user interfaces.


- **TypeScript**: Employed to add static type definitions to the JavaScript code, enhancing code quality and maintainability. TypeScript's type-checking capabilities help prevent runtime errors and improve developer productivity.


### Backend


- **Python**: The core programming language used for backend development. Python's extensive library ecosystem, including Flask, Pandas, and Matplotlib, supports a wide range of functionalities from web server handling to data analysis and visualization.


- **Flask**: A lightweight WSGI web application framework for Python, used to create the REST API that serves the frontend application. Flask offers simplicity and flexibility, making it suitable for projects of any scale.


- **Pandas & Matplotlib**: These libraries are utilized for data manipulation and visualization, respectively. Pandas provides powerful data analysis tools, while Matplotlib offers a wide range of plotting functions to generate graphs and charts.


- **Statsmodels**: This Python module is used for estimating and interpreting models for statistical analysis. It's particularly useful for the ARIMA model implementation for predictive spending analysis.


### Blockchain


- **Sui Blockchain**: As a sponsor and integral technology partner, the Sui blockchain's capabilities are leveraged to ensure data integrity and security. Sui, a decentralized blockchain platform, offers fast, secure, and scalable transactions, making it an ideal choice for handling sensitive financial data and fostering trust in the PennyPro platform.


### AI & Machine Learning


- **ARIMA Model**: Applied for predictive analysis of spending trends. The ARIMA (AutoRegressive Integrated Moving Average) model, a standard in time series forecasting, helps users anticipate future expenses based on historical data.


### Development & Deployment


- **npm (Node Package Manager)**: Manages dependencies for the React frontend, ensuring that all necessary JavaScript packages are installed and up-to-date.


- **Virtual Environments**: Used in Python development to manage package dependencies independently of the system-wide Python installation. This ensures that the project's libraries do not conflict with those of other projects or the system itself.








## Contributing to PennyPro


We welcome contributions from the community, especially those that enhance its blockchain and AI capabilities. Feel free to fork the repository, make your improvements, and submit a pull request.


## License


This project is licensed under the Apache-2.0 license - see the [LICENSE](LICENSE) file for details.


## Acknowledgments


- A special note of gratitude to `Mysten Labs` for their invaluable `@mysten/dapp-kit`, a foundational template that empowers the creation of decentralized applications. Their tools and frameworks have been pivotal in bringing PennyPro to life.


- Immense gratitude to `Blockchain@ASU` for hosting the hackathon that served as a launching pad for PennyPro. Their commitment to nurturing innovation in the blockchain space has not only provided us with a platform to present our work but has also been a cornerstone of our development journey.


- Heartfelt thanks to all who visit and engage with PennyPro. Your interest, usage, and feedback are the driving forces behind our continuous improvement and innovation. We're committed to delivering value and enhancing your financial management experience, inspired by your support and insights.


## Connect with Me


Feel free to reach out and connect with me on [LinkedIn](https://www.linkedin.com/in/sherwinvishesh) or [Instagram](https://www.instagram.com/sherwinvishesh/).






---


Made by Sherwin and Avi



