# Issue Type Semantic Clustering Analysis

## Overview

This document describes the methodology, pipeline, and findings of the issue type identification analysis performed in `notebooks/issue_clustering_analysis.ipynb`. The goal of this analysis is to semantically cluster commits to identify recurring themes, bug patterns, and vulnerability types within the dataset without relying on manual labeling.

## Methodology

The analysis follows a pipeline approach, transforming raw commit data into meaningful semantic clusters.

### 1. Data Aggregation & Preprocessing
- **Source Data**: The largest available dataset (e.g., `job-113755.csv`, ~1.1 GB) is loaded.
- **Grouping**: Data is grouped by `commit_url` to ensure each data point represents a unique commit.
- **Text Representation**: A rich textual representation is constructed for each commit by combining:
  - **Commit Message**: The primary description of the change.
  - **Changed Files**: Paths of files modified in the commit (limited to top 5).
  - **Changed Methods**: Names of methods modified (limited to top 5).
  - **Format**: `"{Message} | Files: {A}, {B} | Methods: {X}, {Y}"`

### 2. Embedding Generation
- **Model**: `all-MiniLM-L6-v2` from Sentence Transformers.
- **Purpose**: Converts the rich text representation into dense, high-dimensional vectors (384 dimensions). This model is chosen for its balance of speed and semantic capture quality.

### 3. Dimensionality Reduction
- **Algorithm**: UMAP (Uniform Manifold Approximation and Projection).
- **Parameters**:
  - `n_neighbors=15`: Balances local vs. global structure.
  - `n_components=50`: Reduces dimensions to 50 for effective density-based clustering.
  - `metric='cosine'`: Appropriate for high-dimensional semantic vectors.
- **Objective**: Reduce noise and computational complexity while preserving the semantic manifold of the data.

### 4. Clustering
- **Algorithm**: HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise).
- **Strategy**: 
  - `min_cluster_size=20`: Sets the minimum number of commits required to form a cluster.
  - `min_samples=5`: Controls how conservative the clustering is regarding noise points.
  - `cluster_selection_method='eom'`: Excess of Mass method to persist significant clusters.
- **Output**: Assigns a `cluster` ID to each commit or labels it as noise (`-1`).

### 5. Cluster Interpretation
- **Method**: TF-IDF (Term Frequency-Inverse Document Frequency) analysis.
- **Process**:
  - All text within a cluster is concatenated into a single "document".
  - TF-IDF scores are calculated for terms within these cluster documents.
  - The top scoring terms (keywords) are extracted to represent the cluster's topic.

## Code Structure

The analysis is contained within `notebooks/issue_clustering_analysis.ipynb`.

- **Data Loading**: Automatically selects the largest CSV file in `assets/data-samples/`.
- **Pipeline Execution**: Sequential execution of embedding, UMAP, and HDBSCAN steps.
- **Outputs**:
  - **Console**: Progress logs and cluster statistics (number of clusters, noise ratio).
  - **Visualization**: A 2D UMAP projection plot showing the cluster landscape.
  - **Summary Table**: A DataFrame displaying Cluster ID, Size, and Top TF-IDF Terms.

## Example Findings

(Based on initial runs)
- **Cluster 3**: Related to calendar and event functionality (`calendar`, `android`, `event`).
- **Cluster 14**: Eclipse plugin development (`jsf`, `jst`, `eclipse`, `plugins`).
- **Cluster 41**: Networking and routing extensions (`opennaas`, `router`, `bundles`).
- **Cluster 17/23/39**: Code generation and transformation (`codegen`, `ceylon`, `transform`).

## Usage

To run the analysis:

1. Ensure the environment has the required dependencies (`sentence-transformers`, `umap-learn`, `hdbscan`, `pandas`, `matplotlib`, `seaborn`).
2. Open `notebooks/issue_clustering_analysis.ipynb`.
3. Run all cells sequentially.
4. The notebook will automatically load the data, process it, and display the resulting clusters and visualization.
