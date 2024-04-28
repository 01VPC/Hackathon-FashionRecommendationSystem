from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FashionRecommender:
    def __init__(self, item_features):
        self.item_features = item_features

    def recommend_items(self, input_categories, fashion_data, n=10):
        vectorizer = TfidfVectorizer()
        # Feature Engineering
        fashion_data['features'] = fashion_data['subCategory'] + ' ' + fashion_data['baseColour'] + ' ' + fashion_data['articleType'] + ' ' + fashion_data['masterCategory'] + ' ' + fashion_data['usage'] + ' ' + fashion_data['gender'] + ' ' + fashion_data['productDisplayName']
        # Preprocess features
        item_features = vectorizer.fit_transform(fashion_data['features'])
        
        # Combine input categories into a single query
        query = ' '.join(input_categories)
        # Transform the query using the same vectorizer
        query_features = vectorizer.transform([query])
        # Calculate cosine similarity between the query and item features
        similarity_scores = cosine_similarity(query_features, item_features)
        # Find indices of the most similar items
        similar_items_indices = similarity_scores.argsort()[0][-n-1:-1][::-1]
        return fashion_data.iloc[similar_items_indices]
