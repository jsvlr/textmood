# textmood

Colour your terminal output by emotional tone.

`textmood` analyses the mood of any text and prints it in a matching colour —
happy text in yellow, angry in red, sad in blue, calm in cyan, fearful in magenta.

## Install

```bash
pip install textmood
```

## Quick start

### As a command

```bash
textmood "I can't believe how amazing today was!"
textmood "This is absolutely frustrating and broken."
textmood "The weather is mild. Nothing special."

# Show mood scores
textmood "I love this wonderful day!" --scores
```

### In your Python code

```python
from textmood import print_mood, score_text

# Print text in its mood colour
print_mood("I love this amazing day!")

# Just get the mood without printing
mood, scores = score_text("This is terrible and broken.")
print(mood)     # "angry"
print(scores)   # {"happy": 0, "angry": 2, "sad": 0, ...}
```

## Moods and colours

| Mood    | Colour  | Example words                     |
| ------- | ------- | --------------------------------- |
| Happy   | Yellow  | amazing, love, wonderful, excited |
| Angry   | Red     | hate, terrible, furious, broken   |
| Sad     | Blue    | sad, lonely, heartbroken, grief   |
| Calm    | Cyan    | fine, okay, normal, mild          |
| Fearful | Magenta | scared, anxious, panic, dread     |

## Contributing

1. Fork this repo
2. Create a branch: `git checkout -b my-feature`
3. Make your changes and add tests
4. Run tests: `pytest tests/ -v`
5. Open a pull request

Bug reports and feature ideas are welcome — open an issue anytime.

## License

MIT © 2025 Jose Dalanon
