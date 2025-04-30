<h1>AI-Based Fraud Detection System for Financial Transactions</h1>
<p>This project is an AI-driven fraud detection system that analyzes financial transactions to identify and flag potentially fraudulent activity. It processes transaction data from a CSV file, provides results in the terminal, and generates both dynamic web dashboards and analytical visualizations using Python.</p>

<h2>Features</h2>

<h3>Terminal-Based Output</h3>
<ul>
  <li>Analyzes a CSV dataset containing various types of financial transactions.</li>
  <li>Predicts and flags transactions based on the fields <code>isFraud</code> and <code>isFlaggedFraud</code>.</li>
  <li>Displays:
    <ul>
      <li>The top 10 transactions in the file.</li>
      <li>The bottom 10 transactions in the file.</li>
      <li>Each transaction includes:
        <ul>
          <li><code>transactionType</code></li>
          <li><code>amount</code></li>
          <li><code>newbalanceDest</code></li>
          <li><code>isFraud</code></li>
          <li><code>isFlaggedFraud</code></li>
        </ul>
      </li>
      <li>Total count of transactions by type:
        <ul>
          <li><code>CASH_OUT</code>, <code>PAYMENT</code>, <code>CASH_IN</code>, <code>DEBIT</code>, <code>TRANSFER</code></li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h3>Web Dashboards</h3>
<ol>
  <li><strong>Transaction Count by Type:</strong> Bar chart showing total count for each transaction type.</li>
  <li><strong>Fraudulent vs Non-Fraudulent:</strong> Interactive pie chart that allows users to toggle categories by clicking.</li>
</ol>

<h3>Python Graphical Visualizations</h3>
<p>The application opens four graphical windows sequentially, each displaying a specific analysis:</p>
<ol>
  <li>Transaction count by type</li>
  <li>Fraudulent transactions by type</li>
  <li>Distribution of fraudulent transaction amounts</li>
  <li>Transactions distributed by hour</li>
</ol>

<h2>Technology Stack</h2>
<ul>
  <li><strong>Language:</strong> Python</li>
  <li><strong>Libraries:</strong> pandas, numpy, matplotlib, seaborn, plotly, scikit-learn</li>
</ul>

<h2>Project Structure</h2>
<pre>
fraud-detection-system/
│
├── main.py                # Main Python script
├── requirements.txt       # Required libraries
├── payment.csv            # Input CSV files
└── README.md              # Project documentation
</pre>

<h2>How to Run</h2>
<pre>
1. Clone the repository:
   git clone https://github.com/Leo-exe-24/Fraud-Detection-System-For-Financial-Transactions-Using-AI.git

2. Navigate to the project directory:
   cd Fraud-Detection-System-For-Financial-Transactions-Using-AI

3. Install required libraries:
   pip install -r requirements.txt

4. Run the application:
   python main.py
</pre>

<p><strong>Note:</strong> Ensure that your input CSV file is correctly placed in the main project folder named <code>payment.csv</code> or its path is properly referenced in <code>main.py</code>.</p>

<h2>Screenshots</h2>
<ul>
  <li>Terminal output showing top and bottom 10 transactions</li>

  ![Screenshot 2025-05-01 035517](https://github.com/user-attachments/assets/965b9592-8401-4de6-9702-8ed3f7ebd3c8)
  ![Screenshot 2025-05-01 035538](https://github.com/user-attachments/assets/874bbb51-ddda-4bf0-baf6-d0e427487392)
  <li>Interactive pie chart</li>
  
  ![Screenshot 2025-04-21 173118](https://github.com/user-attachments/assets/a6f4a32b-4fe2-480b-b709-f78402bd6e0b)
  ![Screenshot 2025-04-21 173227](https://github.com/user-attachments/assets/541660f4-fc4a-48ae-9755-9aed1af10e77)
  <li>Graphs displaying transaction patterns and fraud insights</li>
  
  ![Screenshot 2025-04-21 173302](https://github.com/user-attachments/assets/66ce03aa-9a1d-4529-9595-609aa19b19cb)
  ![Screenshot 2025-04-21 173328](https://github.com/user-attachments/assets/870b6eef-3df8-41c7-a823-60972f3b9904)
  ![Screenshot 2025-04-21 173351](https://github.com/user-attachments/assets/6494114c-d30a-443d-b6a4-fcb2170cfba1)
  ![Screenshot 2025-04-21 173424](https://github.com/user-attachments/assets/e351b8eb-065e-4e3e-84c2-4f6f66ff6759)
</ul>

<h2>Future Enhancements</h2>
<ul>
  <li>Real-time transaction monitoring with streaming tools (e.g., Apache Kafka)</li>
  <li>Web-based UI for fraud investigation and reporting</li>
  <li>Exportable fraud detection reports in CSV or PDF formats</li>
</ul>

<h2>Author</h2>
<p>
  <strong>Mohammad Liyakat Ali</strong><br>
  SRM Institute of Science and Technology<br>
  Email: <a href="mailto:ma8107@srmist.edu.in">ma8107@srmist.edu.in</a>
</p>

<p><em>This project was developed as part of an academic project focused on AI-based fraud detection in finance systems.</em></p>
