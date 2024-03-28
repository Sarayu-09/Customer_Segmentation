import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Function to load the data
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to perform KMeans clustering
def perform_clustering(data):
    X = data.iloc[:, [3, 4]].values
    kmeans = KMeans(n_clusters=5, init='k-means++', random_state=0)
    Y = kmeans.fit_predict(X)
    return X, Y, kmeans.cluster_centers_

def main():
    st.title('Customer Segmentation Analysis')

    # Load the data
    file_path = 'C:\\Users\\deept\\OneDrive\\Desktop\\Customer_Segmentation\\Mall_Customers.csv"'
    customer_data = load_data(file_path)

    # Display first 5 rows of the dataframe
    st.subheader('Data Preview')
    st.write(customer_data.head())

    # Display basic information about the data
    st.subheader('Data Information')
    st.write(customer_data.info())

    # Display missing values count
    st.subheader('Missing Values Count')
    st.write(customer_data.isnull().sum())

    # Plotting distribution plots for 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'
    st.subheader('Distribution Plots')
    plt.figure(figsize=(15, 6))
    for i, feature in enumerate(['Age', 'Annual Income (k$)', 'Spending Score (1-100)'], start=1):
        plt.subplot(1, 3, i)
        sns.distplot(customer_data[feature], bins=20)
        plt.title(f'Distplot of {feature}')
    st.pyplot()

    # Countplot for 'Gender'
    st.subheader('Gender Count')
    plt.figure(figsize=(8, 6))
    sns.countplot(y='Gender', data=customer_data)
    st.pyplot()

    # Performing clustering and plotting
    X, Y, centroids = perform_clustering(customer_data)
    st.subheader('Clustering Results')
    plt.figure(figsize=(10, 8))
    for cluster_num in range(5):
        plt.scatter(X[Y == cluster_num, 0], X[Y == cluster_num, 1], s=50, label=f'Cluster {cluster_num+1}')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=100, c='black', label='Centroids')
    plt.xlabel('Annual Income')
    plt.ylabel('Spending Score')
    plt.title('Customer Groups')
    plt.legend()
    st.pyplot()

if __name__ == "__main__":
    main()
