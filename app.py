import gradio as gr
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
def analyze_sentiment(text):
    return classifier(text)
interface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(label="Input Text", placeholder="Enter your text here..."),
    outputs=[gr.Textbox(label="Sentiment Output")],  
    live=False, 
    title="Sentiment Analysis", 
    description="Enter text to analyze its sentiment. The model will predict whether the sentiment is positive or negative.",
    theme="compact" 
)

interface.launch()
