"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded {len(songs)} songs from catalog\n")

     # Define default user profile (pop/happy profile)
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
        "target_valence": 0.80,
        "target_tempo": 120,
        "target_danceability": 0.80,
        "target_acousticness": 0.20
    }

    print("🎵 User Profile:")
    print(f"   Genre: {user_prefs['favorite_genre']}")
    print(f"   Mood: {user_prefs['favorite_mood']}")
    print(f"   Energy: {user_prefs['target_energy']}")
    print(f"   Valence: {user_prefs['target_valence']}")
    print(f"   Tempo: {user_prefs['target_tempo']} BPM")
    print()

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("=" * 80)
    print("🎧 TOP RECOMMENDATIONS")
    print("=" * 80)
    
    for i, (song, score, reasons) in enumerate(recommendations, 1):
        print(f"\n#{i} - {song['title']} by {song['artist']}")
        print(f"   Genre: {song['genre']} | Mood: {song['mood']} | Energy: {song['energy']}")
        print(f"   📊 Total Score: {score:.1f}/100")
        print(f"   Reasons:")
        for reason in reasons:
            print(f"      • {reason}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
