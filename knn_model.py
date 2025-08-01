import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import NearestNeighbors
import pickle


data = pd.read_csv('dataset.csv')
data = data[['track_name', 'artists', 'danceability', 'energy', 'speechiness', 
             'acousticness', 'instrumentalness', 'track_genre']].dropna()
data['track_name_lower'] = data['track_name'].str.lower()


feature_cols = ['artists', 'danceability', 'energy', 'speechiness',
                'acousticness', 'instrumentalness', 'track_genre']

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), ['danceability', 'energy', 'speechiness', 'acousticness', 'instrumentalness']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['artists', 'track_genre'])
])

X = preprocessor.fit_transform(data[feature_cols])


knn_model = NearestNeighbors(n_neighbors=6, metric='cosine')
knn_model.fit(X)

with open("knn_model.pkl", "wb") as f:
    pickle.dump(knn_model, f)

with open("preprocessor.pkl", "wb") as f:
    pickle.dump(preprocessor, f)


data.to_csv("song_metadata.csv", index=False)


with open("knn_model.pkl", "rb") as f:
    knn_model = pickle.load(f)

with open("preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)

data = pd.read_csv("song_metadata.csv")
data['track_name_lower'] = data['track_name'].str.lower()
data.reset_index(drop=True, inplace=True)


song_to_index = pd.Series(data.index, index=data['track_name_lower'])


def recommend_songs(song_name, n=5):
    song_name = song_name.strip().lower()
    if song_name not in song_to_index:
        return ["Song not found."]
    
    idx = song_to_index[song_name]
    input_row = data.loc[[idx], ['artists', 'danceability', 'energy', 'speechiness', 
                                 'acousticness', 'instrumentalness', 'track_genre']]
    
    input_features = preprocessor.transform(input_row)
    distances, indices = knn_model.kneighbors(input_features, n_neighbors=n+1)
    
    recommendations = []
    for i in range(1, len(indices[0])): 
        track = data.iloc[indices[0][i]]
        recommendations.append(f"{track['track_name']} - {track['artists']}")
    
    return recommendations
