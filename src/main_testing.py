from src.recommender import load_songs, recommend_songs
 
def print_recommendations(profile_name, user_prefs, recommendations):
    """Print formatted recommendations for a given profile"""
    print("\n" + "=" * 80)
    print(f"RECOMMENDATIONS FOR: {profile_name}")
    print("=" * 80)
    
    print("\nUser Profile:")
    print(f"   Genre: {user_prefs['favorite_genre']}")
    print(f"   Mood: {user_prefs['favorite_mood']}")
    print(f"   Energy: {user_prefs['target_energy']}")
    print(f"   Valence: {user_prefs['target_valence']}")
    print(f"   Tempo: {user_prefs['target_tempo']} BPM")
    print(f"   Danceability: {user_prefs['target_danceability']}")
    print(f"   Acousticness: {user_prefs['target_acousticness']}")
    print()
    
    for i, (song, score, reasons) in enumerate(recommendations, 1):
        print(f"\n#{i} - {song['title']} by {song['artist']}")
        print(f"   Genre: {song['genre']} | Mood: {song['mood']} | Energy: {song['energy']}")
        print(f"   Total Score: {score:.1f}/100")
        print(f"   Reasons:")
        for reason in reasons:
            print(f"      • {reason}")
    
    print("\n" + "=" * 80)

def main():
    # Load songs from CSV
    songs = load_songs('data/songs.csv')
    print(f"Loaded {len(songs)} songs from catalog\n")
    
    # Profile 1: High-Energy Pop (Workout vibes)
    high_energy_pop = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.90,
        "target_valence": 0.80,
        "target_tempo": 130,
        "target_danceability": 0.85,
        "target_acousticness": 0.10
    }
    
    # Profile 2: Chill Lofi (Study/Focus mode)
    chill_lofi = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
        "target_valence": 0.60,
        "target_tempo": 75,
        "target_danceability": 0.60,
        "target_acousticness": 0.80
    }
    
    # Profile 3: Deep Intense Rock (Headbanging energy)
    intense_rock = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.92,
        "target_valence": 0.45,
        "target_tempo": 150,
        "target_danceability": 0.65,
        "target_acousticness": 0.15
    }
    
    # Profile 4: EDGE CASE - Conflicting Preferences (High energy but sad mood)
    conflicting_profile = {
        "favorite_genre": "electronic",
        "favorite_mood": "moody",
        "target_energy": 0.90,  # Very high energy
        "target_valence": 0.35,  # But very low positivity (sad/dark)
        "target_tempo": 125,
        "target_danceability": 0.85,
        "target_acousticness": 0.10
    }
    
    # Profile 5: EDGE CASE - "I want everything" (No clear preferences)
    indecisive_profile = {
        "favorite_genre": "ambient",
        "favorite_mood": "relaxed",
        "target_energy": 0.50,  # Middle of the road
        "target_valence": 0.50,  # Neutral
        "target_tempo": 90,     # Medium tempo
        "target_danceability": 0.50,
        "target_acousticness": 0.50
    }
    
    # Profile 6: EDGE CASE - Acoustic Purist (Extreme acousticness preference)
    acoustic_purist = {
        "favorite_genre": "folk",
        "favorite_mood": "relaxed",
        "target_energy": 0.40,
        "target_valence": 0.70,
        "target_tempo": 95,
        "target_danceability": 0.45,
        "target_acousticness": 0.95  # Wants almost purely acoustic
    }
    
    # Test all profiles
    profiles = [
        ("High-Energy Pop (Workout)", high_energy_pop),
        ("Chill Lofi (Study)", chill_lofi),
        ("Deep Intense Rock", intense_rock),
        ("EDGE CASE: Conflicting (High Energy + Sad)", conflicting_profile),
        ("EDGE CASE: Indecisive (All Medium)", indecisive_profile),
        ("EDGE CASE: Acoustic Purist", acoustic_purist)
    ]
    
    for profile_name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(profile_name, user_prefs, recommendations)
        print("\n" + "🔹" * 40 + "\n")
 
if __name__ == "__main__":
    main()