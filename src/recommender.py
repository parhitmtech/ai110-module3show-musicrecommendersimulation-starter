from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(filepath):
    """
    Load songs from a CSV file and return them as a list of dictionaries.

    Args: 
        filepath (str): Path to the CSV file containing song data

    Returns:
        list: List of dictionaries, where each dictionary represents a song
    """
    songs = []

    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': int(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness']),
            }
            songs.append(song)

    return songs

def score_song(user_prefs, song):
    """
    Calculate a score for how well a song matches user preferences

    Args:
        user_prefs (dict): User profile with preferred attributes
        song (dict): Song data with attributes to match

    Returns:
        tuple: (total_score, reasons) where reasons is a list of scoring explanations
    """
    score = 0.0
    reasons = []

    # Weights from algorithm formula (total = 100)
    GENRE_WEIGHT = 25
    MOOD_WEIGHT = 20
    ENERGY_WEIGHT = 20
    VALENCE_WEIGHT = 15
    TEMPO_WEIGHT = 10
    DANCEABILITY_WEIGHT = 5
    ACOUSTICNESS_WEIGHT = 5

    # Categorical matching: Genre
    if song['genre'] == user_prefs['favorite_genre']:
        score += GENRE_WEIGHT
        reasons.append(f"Genre match: {song['genre']} (+{GENRE_WEIGHT})")

    # Categorical matching: Mood
    if song['mood'] == user_prefs['favorite_mood']:
        score += MOOD_WEIGHT
        reasons.append(f"Mood match: {song['mood']} (+{MOOD_WEIGHT})")

    # Numerical matching: Energy
    energy_dist = abs(user_prefs['target_energy'] - song['energy'])
    energy_score = ENERGY_WEIGHT * (1 - energy_dist)
    score += energy_score
    reasons.append(f"Energy similarity: {energy_score:.1f} pts (song: {song['energy']:.2f}, target: {user_prefs['target_energy']:.2f})")

    # Numerical matching: Valence
    valence_distance = abs(user_prefs['target_valence'] - song['valence'])
    valence_score = VALENCE_WEIGHT * (1 - valence_distance)
    score += valence_score
    reasons.append(f"Valence similarity: {valence_score:.1f} pts (song: {song['valence']:.2f}, target: {user_prefs['target_valence']:.2f})")

    # Numerical matching: Tempo (normalized by dividing by 100)
    tempo_distance = abs(user_prefs['target_tempo'] - song['tempo_bpm']) / 100
    tempo_score = TEMPO_WEIGHT * (1 - min(tempo_distance, 1.0))
    score += tempo_score
    reasons.append(f"Tempo similarity: {tempo_score:.1f} pts (song: {song['tempo_bpm']} BPM, target: {user_prefs['target_tempo']} BPM)")

    # Numerical matching: Danceability
    danceability_distance = abs(user_prefs['target_danceability'] - song['danceability'])
    danceability_score = DANCEABILITY_WEIGHT * (1 - danceability_distance)
    score += danceability_score
    reasons.append(f"Danceability similarity: {danceability_score:.1f} pts")

    # Numerical matching: Acousticness
    acousticness_distance = abs(user_prefs['target_acousticness'] - song['acousticness'])
    acousticness_score = ACOUSTICNESS_WEIGHT * (1 - acousticness_distance)
    score += acousticness_score
    reasons.append(f"Acousticness similarity: {acousticness_score:.1f} pts")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Recommend top k songs based on user preferences.
    
    Args:
        user_prefs (dict): User profile with preferred attributes
        songs (list): List of song dictionaries
        k (int): Number of recommendations to return (default: 5)
        
    Returns:
        list: List of tuples (song, score, reasons) sorted by score descending
    """
    # Score all songs
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, reasons))

    # Sort by score descending (highest first)
    sorted_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)

    # Return top k results
    return sorted_songs[:k]