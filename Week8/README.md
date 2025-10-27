# Weekly Assignment Submission
 **Assignment Title:** Unsupervised Learning – K-Means Clustering

**Steps Taken**
- Loaded the cleaned Fake News Detection dataset into Jupyter Notebook.

- Removed irrelevant columns such as title, subject, and date to focus only on numerical and text-derived features.

- Selected numeric columns such as text_length, title_length, and word_count for clustering analysis.

- Filled missing values using median imputation to ensure consistent data quality.

- Standardized all numeric features using StandardScaler() for better clustering performance.

- Applied K-Means Clustering (k = 3) to identify different groups of news articles based on textual characteristics.

- Added the cluster labels back to the dataset to compare clustering patterns with real and fake news labels.

- Used PCA (2 components) for dimensionality reduction to visualize clusters in 2D space.

- Created a scatter plot showing the distribution of news clusters across two principal components.

  **Output**
  
  Cluster Distribution
  | Cluster | Count |
  | ------- | ----- |
  | 0       | 1920  |
  | 1       | 1575  |
  | 2       | 2088  |

  **PCA Visualization:**
  A colorful 2D scatter plot displaying three distinct clusters (red, blue, and green) representing different news groups. The clusters show clear separation, indicating that articles have been grouped based on similar textual characteristics.

  **Challenges Faced**
  - Faced dimension mismatch errors during label assignment — solved by aligning DataFrame indices properly.
  - Needed to tune the number of clusters (k) using the Elbow Method to find the most suitable value.
  - Adjusted scaling and PCA parameters to achieve cle**arer visualization and meaningful separation between clusters.
    
**Project Milestone**
Successfully applied Unsupervised Learning (K-Means + PCA) on the Fake News Detection dataset to group news articles into clusters based on content similarity.
This step provided deeper insights into how fake and real news articles differ in their text structure, forming the foundation for future classification improvements.
