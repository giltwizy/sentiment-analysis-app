from transformers import pipeline

# Geting pipelineAPI for sentiment analysis

classifier = pipeline("sentiment-analysis")
def func(utterance):
  return classifier(utterance)

  # UI App
import gradio as gr
descriptions = "This is an AI sentiment analyser which checks and get the emotions in a particular sentence."

app = gr.Interface(fn=func, inputs="text", outputs="text", title="Sentiment Analayser", description=descriptions)
app.launch()