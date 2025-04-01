import random
import datetime
import requests
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# AI-Powered Voice Assistant
class VoiceAssistant:
    def __init__(self):
        self.greetings = ['Hello, how can I assist you today?', 'Hi there, what can I do for you?', 'Good day! What’s on your mind?']

    def greet_user(self):
        print(random.choice(self.greetings))

    def respond_to_query(self, query):
        if 'play music' in query:
            print('Playing your favorite playlist...')
        elif 'navigate to' in query:
            destination = query.split('navigate to ')[1]
            print(f'Routing to {destination}...')
        elif 'weather' in query:
            self.get_weather()
        else:
            print("Sorry, I didn't understand that.")

    def get_weather(self):
        # Using a weather API for real-time data (example: OpenWeatherMap API)
        api_key = 'YOUR_API_KEY'
        city = 'London'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}, Temp: {data['main']['temp']}K")

# Personalized Music Recommendation System using Content-based Filtering
class MusicRecommendation:
    def __init__(self):
        # Sample music database with genre, artist, and title
        self.music_db = pd.DataFrame({
            'title': ['Song A', 'Song B', 'Song C', 'Song D', 'Song E'],
            'artist': ['Artist 1', 'Artist 2', 'Artist 3', 'Artist 4', 'Artist 5'],
            'genre': ['Pop', 'Rock', 'Classical', 'Jazz', 'Pop'],
            'lyrics': ['Love in the air', 'Rock the night away', 'Classical symphony', 'Smooth jazz vibes', 'Feel good music']
        })

    def recommend_music(self, preferred_genre='Pop'):
        print(f"Recommended music based on your interest in {preferred_genre}:")
        genre_songs = self.music_db[self.music_db['genre'] == preferred_genre]
        print(genre_songs[['title', 'artist']])

# Predictive Navigation with ML-based Route Prediction
class PredictiveNavigation:
    def __init__(self):
        # Example route data (simplified for demonstration)
        self.routes_data = pd.DataFrame({
            'from': ['Home', 'Home', 'Work', 'Work'],
            'to': ['Work', 'Gym', 'Home', 'Gym'],
            'distance': [15, 7, 15, 6],
            'traffic': [10, 5, 12, 3],  # Simulated traffic in minutes
            'time_of_day': ['Morning', 'Afternoon', 'Morning', 'Evening']
        })

    def train_model(self):
        # Feature extraction for route prediction
        vectorizer = TfidfVectorizer()
        time_vector = vectorizer.fit_transform(self.routes_data['time_of_day'])
        self.routes_data['time_feature'] = np.array(time_vector.sum(axis=1)).flatten()

    def predict_route(self, current_location, destination):
        # Train the model before making a prediction
        self.train_model()

        # Simulating a simple prediction based on previous routes
        route = self.routes_data[(self.routes_data['from'] == current_location) & 
                                 (self.routes_data['to'] == destination)]
        if not route.empty:
            predicted_time = route['traffic'].values[0] + route['time_feature'].values[0]
            print(f"Predicted route from {current_location} to {destination}: {route['distance'].values[0]} km, Estimated Time: {predicted_time} minutes")
        else:
            print("No route data available for prediction.")

# Main Application for SmartDrive AI System
class SmartDriveAI:
    def __init__(self):
        self.voice_assistant = VoiceAssistant()
        self.music_recommendation = MusicRecommendation()
        self.navigation_system = PredictiveNavigation()

    def start(self):
        print("Welcome to SmartDrive AI!")
        self.voice_assistant.greet_user()
        
        # Example usage of the voice assistant
        self.voice_assistant.respond_to_query('play music')
        
        # Personalized music recommendations based on user genre preference
        self.music_recommendation.recommend_music(preferred_genre='Pop')
        
        # Predict route using machine learning model
        self.navigation_system.predict_route('Home', 'Work')

# Running the SmartDrive AI System
if __name__ == '__main__':
    smart_drive = SmartDriveAI()
    smart_drive.start()
