# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project implements a content-based music recommender that suggests songs based on matching musical attributes. The system analyzes a user's listening history to build a taste profile, then scores each song in the catalog by comparing features like genre, mood, energy level, and tempo. Songs with the highest similarity scores are recommended to the user.

---

## How The System Works

This recommender uses **content-based filtering** to match songs to user preferences based on musical attributes.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- Each song uses two types of features:
  - **Categorical attributes**: 'genre', 'mood'
  - **Numerical attributes**: 'energy' (0-1), 'valence' (0-1), 'tempo_bpm', 'danceability' (0-1), 'acousticness (0-1)
- What information does your `UserProfile` store
- 'favorite_genre': Preferred musical style (e.g, "pop", "lofi", "jazz")
- 'favorite_mood': Preferred emotional tone (e.g, "happy", "chilli", "intense")
- 'target_energy': Desired energy level (0.0 = calm, 1.0 = very energetic)
- 'target_valence': Desired positivity (0.0 = sad/dark, 1.0 = happy/bright)
- 'target_tempo': Preferred beats per minute (e.g, 75 for slow, 130 for fast)
- 'target_danceability': How danceable (0-1)
- 'target_acousticness': Preferrence for acoustic vs. wlwctronic (0-1)

- How does your `Recommender` compute a score for each song
Each songs receives a score out of a total of 100 points based on how well it maches the user preferences.
**Categorical Matching (exact match):**
- Genre match: +25 points
- Mood match: +20 points

**Numerical Matching (distance-based):**
- Songs closer to the user's average values score higher using the formula:
- 'Score = Max Points x (1 - |user_preference - song_value|)'

- Energy similarity: up to 20 points
- Valence similarity: up to 15 points
- Tempo similarity: up to 10 points (normalized by dividing BPM difference by 100)
- Danceability similarity: up to 5 points
- Acousticness similarity: up to 5 points

You can include a simple diagram or bullet list if helpful.

- How do you choose which songs to recommend
- Songs are recommended in 4 steps:
1) Load all songs from 'data/songs.csv'
2) For each songs, Calculate total score based on user profile.
3) Rank all songs from highest to lowest score.
4) Return the top 5 songs as recommendations.

**Potential Biases**
- **Genre over-prioritization**: A song  with matching genre gets 25 points automatically, which might exclude great mood matches from other genres.
- **Exact match requirement**: Songs that are "close but not exact" in categorical features get zero points instead of partial credit.
- **Narrow taste assumption**: The system assumes users have a single, consistent taste profile rather than context-dependent preferences (e.g, workout vs. sleep music)
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

