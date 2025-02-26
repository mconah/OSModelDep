import ollama

def create_prompt(text):
    return f"""Score the sentiment of the text below, given you response in the format of 'The sentiment is 
(Sentiment which is either negative or positive or neutral)'. The text is {text}"""

def sentiment(text):
    sentiment = ollama.generate(
            model = "qwen2:1.5b",
            prompt = create_prompt(text)
            )
    return sentiment

print("""
      This is sample uses LLM to perform sentiment analysis through prompting./n""")

prompt = input("What is the input you would want to get the sentiment of? > ")
sentiment = sentiment(prompt) 

print(sentiment["response"])
