# Sample text data
sentences = [
    "I love learning Python",
    "AI is the future",
    "Today is a sunny day",
    "Deep learning is amazing",
    "Python makes AI easy"
]

# Loop through sentences and label if it mentions AI
for sentence in sentences:
    if "AI" in sentence or "learning" in sentence:  # simple keyword detection
        label = "AI-related"
    else:
        label = "Not AI-related"
    print(f"'{sentence}' -> {label}")
