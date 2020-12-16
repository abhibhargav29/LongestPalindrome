# MNIST Dimensionality Reduction

<p align="justify">
This ipython notebook does a dimensionality reduction for the mnist dataset using PCA and t-SNE. The data is of various images of handwritten 
digits(stored in form of pixels) and the class label is the actual digit that it represents(0-9). We need to do redution for visulizaion of these digits.
The original data has 784 features or pixels and we convert them into just two dimensions for easy visualization.
</p>

PCA has been implemented from sklearn.decomposition module and also by ourselves after calculating covariance matrix and eigen vectors.<br>
t-SNE has been implemented from sklearn.manifold.

The data is taken from kaggle. It could not be uploaded due to its large size.
Link - https://www.kaggle.com/c/digit-recognizer
