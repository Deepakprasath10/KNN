#  KNN-Based Music Recommendation System

A web-based **Music Recommendation System** built using the **K-Nearest Neighbors (KNN)** algorithm and deployed with **Flask**. This project suggests similar songs based on selected audio features like tempo, energy, and more.

---

##  Features

-  Recommend similar songs using KNN
-  Choose a song and get the top 5 recommendations
-  Simple and clean user interface
-  Fast, pre-trained ML model
-  Easy to customize and extend

---

## Machine Learning Model

- **Algorithm**: K-Nearest Neighbors (KNN)
- **Library**: `scikit-learn`
- **Distance Metric**: Euclidean
- **Features Used**:
  - `tempo`
  - `energy`
  - `danceability`
  - `acousticness`
  - `popularity`

---

## 📁 Project Structure
```
music-recommender-knn/
│
├── app.py # Flask web server
├── model_knn.py # ML model training script
├── knn_model.pkl # Serialized model file
├── requirements.txt # Required Python libraries
│
├── dataset/
│ └── songs.csv # Dataset with song features
│
├── templates/
│ ├── index.html # Song selection page
│ └── result.html # Recommended songs page
│
├── static/
│ └── style.css # CSS styles
│
└── README.md # Project documentation
```


## 📦 Installation & Setup

### 🔹 1. Clone the Repository

```
git clone https://github.com/yourusername/music-recommender-knn.git
cd music-recommender-knn
```
🔹 2. Install Dependencies
Make sure Python 3.8+ is installed.
```
pip install -r requirements.txt
```
🔹 3. Train the Model
```
python model_knn.py
```
This will train and save knn_model.pkl.

🔹 4. Run the Flask App
```
python app.py
```
Now open your browser and visit:
http://127.0.0.1:5000/
---
 ## How It Works
User selects a song from the dropdown.

The app retrieves its audio features.

KNN finds the 5 most similar songs based on these features.

The recommendations are displayed on the result page.

 Sample Dataset (songs.csv)
```
track_name,artist,genre,tempo,energy,danceability,acousticness,popularity
Blinding Lights,The Weeknd,Pop,171,0.73,0.51,0.001,90
Shape of You,Ed Sheeran,Pop,95,0.65,0.82,0.08,92
Rockstar,Post Malone,Hip-Hop,160,0.85,0.68,0.02,89
Perfect,Ed Sheeran,Pop,95,0.5,0.6,0.35,91
God's Plan,Drake,Hip-Hop,154,0.88,0.58,0.01,88
```
 Screenshots
  Home Page	Recommendation Result
<img width="1049" height="657" alt="Screenshot 2025-08-01 122135" src="https://github.com/user-attachments/assets/9db12ba1-7264-4076-9acc-5418dc6141f6" />
<img width="709" height="493" alt="Screenshot 2025-08-01 122203" src="https://github.com/user-attachments/assets/63641d28-9734-4dec-a777-eed4e48d2f9d" />
<img width="860" height="599" alt="Screenshot 2025-08-01 122147" src="https://github.com/user-attachments/assets/aedcb2b5-7ba3-409a-bfc7-75a9cb19afbd" />


## Future Enhancements
  Integrate Spotify API

  Add user authentication and playlist memory

  Add audio preview and album artwork

  Make it mobile responsive with animations
