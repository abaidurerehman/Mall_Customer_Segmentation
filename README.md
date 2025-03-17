REPORT:
 Customer Segmentation Using Clustering
Here's a short report covering all the required points for your Customer Segmentation Using Clustering project. 
1. Approach Used
Exploratory Data Analysis (EDA):
•	We used the Mall Customer Segmentation Dataset containing customer demographics and spending behavior.
•	Key features analyzed: Age, Annual Income (k$), Spending Score (1-100).
•	Data was cleaned, and missing values were handled.
•	We used visualizations such as histograms, scatter plots, and box plots to understand customer spending patterns.
Clustering Algorithm:
•	We applied K-Means Clustering to segment customers based on their income and spending behavior.
•	The Elbow Method was used to determine the optimal number of clusters.
•	A K-Means model with 5 clusters was trained and saved as customer_segmentation_model.pkl.
Model Deployment:
•	The model was deployed using Streamlit, creating a simple web interface.
•	Users can input their Annual Income and Spending Score, and the model predicts their customer segment.
•	The app was tested locally using streamlit run app.py.
________________________________________
2. Challenges Faced
1.	Memory Leak Warning in K-Means: 
o	Fixed by setting OMP_NUM_THREADS=1 in the environment.
2.	FileNotFoundError for Model File: 
o	Resolved by ensuring customer_segmentation_model.pkl is correctly saved and loaded.
3.	'Streamlit' Not Recognized Error: 
o	Fixed by installing Streamlit with pip install streamlit and ensuring the Python environment was activated.
4.	Choosing the Right Number of Clusters: 
o	Used the Elbow Method and Silhouette Score to determine optimal clusters.
________________________________________
3. Model Performance & Improvements
Performance Evaluation:
•	The model successfully identified 5 distinct customer segments.
•	Visualizing the clusters showed clear separations based on spending habits and income levels.
•	Customers were grouped into categories like low-income high-spenders, high-income low-spenders, balanced customers, etc.
Potential Improvements:
•	Try Hierarchical Clustering for better insights into customer relationships.
•	Feature Engineering: Include additional features like purchase frequency, preferred products, etc.
•	Hyperparameter Tuning: Experiment with different cluster initialization methods (e.g., K-Means++, MiniBatch K-Means).
________________________________________
4. Deployment Instructions
Running Locally:
1.	Ensure dependencies are installed: 
2.	pip install streamlit pandas joblib scikit-learn
3.	Run the Streamlit App: 
4.	streamlit run app.py
5.	Access the web interface at http://localhost:8501/.
________________________________________
Conclusion
This project successfully demonstrates how clustering algorithms can segment customers based on demographics and spending behavior. The deployed model provides businesses with valuable insights into different customer groups, helping improve targeted marketing strategies.
