# SmartDrive AI – Intelligent In-Car Experience with Generative AI

**SmartDrive AI** is an advanced **AI-powered infotainment and personalization system** designed to enhance **user-vehicle interaction**. By leveraging **Generative AI**, it creates an **adaptive, intuitive, and intelligent in-car environment**. The system features a **voice assistant**, **personalized recommendations** for music, podcasts, and more, and **predictive navigation** to make every drive smarter.

## Key Features

- 🚗 **AI-Powered Voice Assistant**  
  Provides seamless hands-free control for voice queries like playing music, navigating to destinations, and checking the weather.

- 🎵 **Personalized Infotainment Recommendations**  
  Recommends personalized media content (music, podcasts, and news) based on user preferences.

- 📍 **Predictive Navigation**  
  Uses machine learning models to predict routes and estimate travel time based on traffic conditions, time of day, and distance.

- 🧠 **Adaptive User Interface**  
  Customizes controls based on driver behavior and preferences, enhancing the overall user experience.

## Technology Stack

- **Python**: Programming language used for core application development.
- **scikit-learn**: Machine learning library used for route prediction and content recommendation.
- **Requests**: For fetching live data (e.g., weather information).
- **Pandas** & **NumPy**: For data manipulation and calculations.
- **OpenWeatherMap API**: Used for fetching real-time weather data.

## How It Works

### 1. **Voice Assistant**  
The voice assistant can respond to queries such as "Play music," "Navigate to [destination]," and even fetch the weather in real-time using the OpenWeatherMap API.

### 2. **Personalized Music Recommendation**  
The music recommendation system uses a simple **content-based filtering** approach. It suggests music based on user-defined preferences like genre. 

### 3. **Predictive Navigation**  
The predictive navigation system uses historical route data to estimate travel time and suggests the best route based on traffic and time of day. The system is trained using a machine learning model (TF-IDF) that processes time-of-day data to provide accurate predictions.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/SmartDrive-AI.git
