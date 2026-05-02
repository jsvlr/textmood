import pytest
from textmood.scorer import score_text


def test_happy_text():
    mood, _ = score_text("I love this amazing day")
    assert mood == "happy"

def test_angry_text():
    mood, _ = score_text("This is terrible and i hate it")
    assert mood == "angry"

def test_sad_text():
    mood, _ = score_text("I feel so sad and lonely today")
    assert mood == "sad"

def test_natural_defaults_to_calm():
    mood, _ = score_text("The weather today is mild")
    assert mood == "calm"

def test_scores_are_dict():
    _, scores = score_text("hello")
    assert isinstance(scores, dict)
    assert "happy" in scores

def test_punctuation_ignored():
    """Punctuation should not break word matching."""
    mood1, _ = score_text("amazing!")
    mood2, _ = score_text("amazing")

    assert mood1 == mood2