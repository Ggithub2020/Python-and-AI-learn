import pyttsx3

#1,Initialize the text-to-speech engine
engine = pyttsx3.init()

#2,Set text to speak
text = "Hello, This is Girum your power BI assistant. How can I help you today? " \
"I can assist you with your Power BI reports and dashboards." \
"I can also help you with data analysis and visualization." \
"I can answer your questions about Power BI features and functionalities." 
" I can guide you through the process of creating reports and dashboards." \
"I can provide tips and best practices for using Power BI effectively." \
"I can help you troubleshoot common issues in Power BI." \
"" \
"" \
#3" speak the text
engine.say(text)

#4,Wait for the speaking to finish
engine.runAndWait()