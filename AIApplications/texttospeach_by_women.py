import pyttsx3

# 1. Initialize the text-to-speech engine
engine = pyttsx3.init()

# 2. Get available voices
voices = engine.getProperty('voices')

# Print all voices to see which are available on your system
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} ({voice.id})")

# 3. Set to female voice (often index 1 on Windows, but may vary)
engine.setProperty('voice', voices[1].id)  # try 0,1,2... until you find a female one

# Optional: Adjust speed and volume
engine.setProperty('rate', 170)   # speed (words per minute)
engine.setProperty('volume', 1.0) # max volume (0.0 to 1.0)

# 4. Text to speak
text = (
    "Hello, This is Girum your Power BI assistant. How can I help you today? "
    "I can assist you with your Power BI reports and dashboards. "
    "I can also help you with data analysis and visualization. "
    "I can answer your questions about Power BI features and functionalities. "
    "I can guide you through the process of creating reports and dashboards. "
    "I can provide tips and best practices for using Power BI effectively. "
    "I can help you troubleshoot common issues in Power BI."
)

# 5. Speak the text
engine.say(text)

# 6. Wait for the speaking to finish
engine.runAndWait()
