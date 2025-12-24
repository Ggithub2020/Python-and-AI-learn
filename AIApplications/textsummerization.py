from transformers import pipeline

#1.Load the summarization pipeline
summarizer = pipeline("summarization",model="facebook/bart-large-cnn")

#2. Long text input
text = """
Artificial Intelligence (AI) is a rapidly evolving field that focuses on creating machines capable of performing tasks
    that typically require human intelligence. This includes understanding natural language, recognizing patterns, solving problems, and making decisions. 
    AI technologies are being integrated into various sectors such as healthcare, finance, transportation, and entertainment, leading to significant advancements and efficiencies.
    """
#3. Summarize the text
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

#4. Print the summary
print("Summary:", summary[0]['summary_text'])