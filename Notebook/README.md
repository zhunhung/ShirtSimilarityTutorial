# ShirtSimilarityTutorial - Notebook
Exploring and understanding the approach

## Summary of Approach

1. Load a pre-trained MobileNet model and remove the last fully-connected layer.
2. The new model will now output a feature embedding of 1024-d instead.
3. Images of shirts in the `shirt` folder are presumed to be the clothes you currently own.
4. Generate embeddings for each of the shirt and save it into `shirt_encodings.txt`.
5. For a new shirt, generate its embedding and compute the cosine similarity between the embedding and the collection of embeddings.
6. The shirt with the highest similarity score that is above the threshold will be the most 'similar' shirt.



