# Customer Segmentation Analysis using KMeans Clustering

This repository contains code for performing customer segmentation analysis using KMeans clustering. The analysis aims to segment customers based on their annual income and spending score.

## Description

The code performs the following tasks:

- Loads the customer data from a CSV file into a pandas DataFrame.
- Explores the data by printing the first few rows, checking the data shape and information, and identifying any missing values.
- Visualizes the distribution of age, annual income, and spending score using seaborn's distplot.
- Plots the count of customers by gender using seaborn's countplot.
- Visualizes the relationship between age, annual income, and spending score using seaborn's regplot.
- Creates a scatter plot to compare the annual income and age of customers by gender.
- Generates violin plots and swarm plots to visualize the distribution of age, annual income, and spending score by gender.
- Performs KMeans clustering to segment customers into distinct groups based on their annual income and spending score.
- Plots the clustered groups and their centroids to visualize the customer segments.

## Getting Started

To run the code:

1. Clone the repository to your local machine:

2. Install the required Python packages:

pip install -r requirements.txt

3. Run the Python script:

python customer_segmentation.py


## Dataset

The dataset used in this analysis (`Mall_Customers.csv`) contains the following columns:

- `CustomerID`: Unique identifier for each customer.
- `Gender`: Gender of the customer (Male/Female).
- `Age`: Age of the customer.
- `Annual Income (k$)`: Annual income of the customer in thousands of dollars.
- `Spending Score (1-100)`: Score assigned to the customer based on their spending behavior.

## Results

The analysis results in the segmentation of customers into distinct groups based on their annual income and spending score. The clustered groups and their centroids are visualized to provide insights into customer behavior and preferences.

