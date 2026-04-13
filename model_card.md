# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This system recommends 3-5 songs from a catalog based on a user's preferred genre, mood, and musical attributes (energy, valence, tempo, danceability, acousticness). 
 
**Target Users:** Educational demonstration only - designed for classroom exploration of recommendation algorithms, not for real-world deployment.
 
**Use Cases:**
- Understanding how content-based filtering works
- Exploring how feature weights affect recommendations
- Learning about bias in AI systems

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

The recommender analyzes each song in the catalog and calculates a "match score" out of 100 points based on how closely the song's attributes align with the user's preferences.
 
**Scoring Breakdown:**
- **Genre Match** (25 pts): Does the song match the user's favorite genre?
- **Mood Match** (20 pts): Does the song's mood align with what the user wants?
- **Energy Similarity** (20 pts): How close is the song's energy level to the user's target?
- **Valence Similarity** (15 pts): How close is the emotional positivity?
- **Tempo Similarity** (10 pts): How close is the beats-per-minute?
- **Danceability** (5 pts): Minor refinement factor
- **Acousticness** (5 pts): Minor refinement factor
 
Songs are ranked from highest to lowest score, and the top 5 are recommended.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

**Dataset:** `data/songs.csv` containing 20 songs
 
**Original Dataset:** 10 songs (pop, lofi, rock, jazz, ambient, synthwave, indie pop)
 
**Added Songs:** 10 additional songs to increase diversity (country, electronic, chiptune, folk, blues, EDM, classical)
 
**Genre Distribution:**
- Pop: 2 songs (10%)
- Lofi: 3 songs (15%)
- Rock: 1 song (5%)
- Jazz: 2 songs (10%)
- Ambient: 2 songs (10%)
- Synthwave: 2 songs (10%)
- Other genres: 8 songs (40%)
 
**Whose taste does this reflect?**
The dataset reflects a mix of modern streaming preferences with a slight bias toward electronic/digital music production (60% of songs have acousticness < 0.5). Classical, country, and folk are underrepresented compared to real-world listening habits.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

**Transparency:** Users can see exactly why each song was recommended (breakdown of scores)
 
**Works for Clear Preferences:** When a user has a distinct taste (e.g., "chill lofi study music"), the system reliably finds matching songs
 
**No Cold Start Problem:** Unlike collaborative filtering, this system can recommend any song immediately without needing user behavior data
 
**Interpretable Weights:** The scoring logic is simple math - no "black box" neural network
 
**Handles Niche Genres:** Can recommend less popular genres like chiptune or blues if they match the user's profile

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

### Testing Methodology:
 
I tested the system with **6 diverse user profiles**:
 
1. **High-Energy Pop (Workout):** Wants energetic, upbeat pop songs
2. **Chill Lofi (Study):** Wants low-energy, relaxed background music
3. **Deep Intense Rock:** Wants high-energy rock with lower valence
4. **EDGE CASE - Conflicting:** High energy (0.9) + sad mood (moody)
5. **EDGE CASE - Indecisive:** All preferences at 0.5 (neutral)
6. **EDGE CASE - Acoustic Purist:** Extreme acousticness preference (0.95)
 
### Key Findings:
 
**What Worked Well:**
- Clear profiles (High-Energy Pop, Chill Lofi) got relevant, sensible recommendations
- The scoring explanations helped me understand why each song ranked where it did
- Genre match was a strong predictor of user satisfaction
 
**Surprises:**
- "Gym Hero" kept appearing for ANY pop user, even those wanting low energy - the 25-point genre bonus is too powerful
- The "Conflicting" profile (high energy + moody) recommended songs that were energetic but not actually dark/moody - the system prioritized energy over mood
- The "Indecisive" profile had nearly identical scores for all songs (difference of <5 points), making recommendations essentially random
 
### Experiment: Doubling Energy Weight
 
I tested doubling the energy weight (20 → 40) and halving genre weight (25 → 12.5).
 
**Result:** 
- Recommendations became more varied across genres
- Users who wanted high energy got EDM/electronic even if they said "pop"
- Genre purists were unhappy - a pop fan got electronic music
- **Conclusion:** Genre weight should stay high for user satisfaction, but perhaps cap at 20 points instead of 25

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

If I had more time, I would:
 
1. **Add Context-Aware Profiles:** Allow users to have multiple profiles (workout, sleep, commute) that activate based on time/location
2. **Implement Diversity Boosting:** Penalize songs that are too similar to already-recommended tracks to avoid repetitive lists
3. **Hybrid Filtering:** Combine content-based (current system) with collaborative filtering ("users like you also enjoyed...")
4. **Temporal Features:** Boost new releases or songs trending in the user's region
5. **Feedback Loop:** Let users "thumbs up/down" recommendations to refine their profile over time
6. **Expand Dataset:** 500+ songs to enable better long-tail discovery

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

### What Surprised Me:
 
I was surprised by how much **genre weight dominates** the recommendations. Even when I set energy and mood preferences that clearly pointed to a different genre, the system still prioritized genre matches. This made me realize that real-world recommenders like Spotify probably use much more nuanced weighting - maybe genre only counts 10-15% of the score, not 25%.
 
The **"conflicting preferences" edge case** was eye-opening. When I set high energy (0.9) + moody mood, the system couldn't find songs that were BOTH energetic AND dark. It defaulted to prioritizing energy. This made me realize that some combinations of preferences are just rare in music - or at least in my small dataset.
 
### How This Changed My View of Real Recommenders:
 
Building this made me appreciate how much **invisible work** goes into systems like Spotify Discover Weekly. My system uses 7 features and already has edge cases and biases - Spotify probably uses 100+ features (listening history, skip rate, playlist context, lyrics, artist similarity, social signals). 
 
I also realized that **"accuracy" is subjective**. My system could technically be "accurate" (matching features correctly) but still feel wrong to users if the weights don't match their mental model of importance. A user might say "I want pop music" but what they really mean is "I want upbeat, singable music" - and my system takes "pop" too literally.
 
### Where Human Judgment Still Matters:
 
Even if my model gets "better" with more data and tuning, humans still matter for:
 
1. **Defining "good" recommendations:** Is a good recommendation what you EXPECT, or what you DISCOVER? My system optimizes for expected matches, not serendipity.
 
2. **Handling context:** I can't capture "I want this for my toddler" vs "I want this for a party" without human input.
 
3. **Cultural sensitivity:** My system doesn't know that recommending sad breakup songs to someone going through a breakup might be hurtful, not helpful.
 
4. **Novelty vs. Comfort:** Only humans can decide when they want to hear "more of the same" vs. "something different" - my system always assumes "more of the same."
 
The biggest lesson: **Recommenders are opinionated**. My weighting choices (25 for genre, 20 for energy) reflect MY beliefs about what matters in music. A different developer would make different choices, and both systems could be "correct" while producing totally different recommendations.