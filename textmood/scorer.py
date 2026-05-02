from __future__ import annotations

MOOD_WORDS: dict[str, list[str]] = {
    "happy": [
        "amazing", "wonderful", "great", "love", "joy",
        "excited", "fantastic", "brilliant", "happy", "yay",
        "awesome", "delighted", "pleased", "fun", "best",
    ],

    "angry": [
        "hate", "angry", "furious", "stupid", "broken",
        "terrible", "awful", "horrible", "rage", "useless",
        "frustrating", "rediculous", "disgusting",
    ],

    "sad": [
        "sad", "cry", "miss", "lonely", "depressed",
        "heartbroken", "sorry", "unfortunate", "grief", "lost",
        "hopeless", "painful", "tears",
    ],

    "calm": [
        "fine", "okay", "normal", "alright", "usual",
        "standard", "average", "regular", "typical", "mild",
    ],

    "fearful": [
        "scared", "afraid", "fear", "terrified", "worried",
        "anxious", "nervous", "panic", "dread", "horror"
    ]
}


def score_text(text: str) -> tuple[str, dict[str, int]]:
    """Analyze text and return (dominant_mood, scores_per_mood)"""
    words = text.lower().split()
    scores: dict[str, int] = {mood: 0 for mood in MOOD_WORDS}
        
    for word in words:
        clean = word.strip(".,!?;:\"")
        for mood, keywords in MOOD_WORDS.items():
            if clean in keywords:
                scores[mood] += 1

    dominant = max(scores, key=lambda m: scores[m])
    # if all scores are 0, default to calm
    if scores[dominant] == 0:
        dominant = "calm"

    return dominant, scores