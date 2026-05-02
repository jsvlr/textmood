from rich import print as rprint
from rich.text import Text
from .scorer import score_text

MOOD_COLOURS: dict[str, str] = {
    "happy": "bold yellow",
    "angry": "bold red",
    "sad":   "blue",
    "calm":  "cyan",
    "fearful": "magenta"
}

MOOD_LABELS: dict[str, str] = {
    "happy": "Happy :)",
    "angry": "Angry >:(",
    "sad":   "Sad :(",
    "calm":  "Calm :|",
    "fearful": "Fearful :O",
}

def print_mood(text: str, show_scores: bool = False) -> str:
    mood, scores = score_text(text)
    colour = MOOD_COLOURS[mood]
    label = MOOD_LABELS[mood]

    styled = Text(text, style=colour)
    rprint(styled)
    rprint(Text(f" mood: {label}", style=f"dim {colour}"))

    if show_scores:
        for m, s in scores.items():
            rprint(Text(f"  {m}: {s}", style="dim"))
    
    return mood