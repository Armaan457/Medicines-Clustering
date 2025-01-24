# Medicine Similarity Clustering

This project aims to cluster similar medicines based on their name, salts, and prescription requirements. 

## Methodology

1. **Data Loading and Preprocessing:**
   - The dataset is loaded from `medlr_assignment_dataset.csv`.
   - Textual features ('name' and 'salts') are preprocessed using tokenization, stop word removal, and lemmatization.
   - Missing values in numerical features are imputed using KNN Imputation.
   - Missing values in categorical features are replaced with "Unknown."

2. **Feature Engineering:**
   - Embeddings for 'name' and 'salts' are generated using the 'all-MiniLM-L6-v2' SentenceTransformer model.
   - Embeddings are scaled using RobustScaler.
   - Prescription requirement is encoded as a numerical feature (0 or 1).
   - All features are combined into a single feature matrix.

3. **Dimensionality Reduction:**
   - UMAP is used to reduce the dimensionality of the feature space, preserving local structure.

4. **Clustering:**
   - HDBSCAN is employed to cluster the data points based on their embeddings and prescription requirements.
   - Hyperparameter tuning is performed using GridSearchCV to optimize cluster quality.

## Results

- The medicines are grouped into distinct clusters based on their similarity.
- The dataset is saved by adding the clusters column to the respective medicine
- A cluster summary (`cluster_summary.csv`) is generated, providing:
    - Cluster ID
    - Number of medicines in the cluster
    - Number of unique manufacturers in the cluster
    - Most frequent medicine in the cluster
- Clusters can be visualized using UMAP embeddings to understand their distribution.

## Usage

1. Clone the repository:
```sh
> https://github.com/Armaan457/Medicines-Clustering.git
```

2. Create and activate a virtual environment:

```sh
> python -m venv venv
> venv\scripts\activate
```

3. Install dependencies:

```sh
> pip install -r requirements.txt
```

4. Run the provided Jupyter Notebook to execute the clustering pipeline.
5. The clustered dataset is saved as `medlr_assignment_dataset_clustered.csv`.
6. The cluster summary is saved as `cluster_summary.csv`.