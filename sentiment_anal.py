import ollama

def create_prompt(text):
    return f"""Score the sentiment of the text below, given you response in the format of 'The sentiment is 
(Sentiment which is either negative or positive) with the sentiment score of (Add the score here)'. The text is {text}"""

def sentiment(text):
    sentiment = ollama.generate(
            model = "qwen2:1.5b",
            prompt = create_prompt(text)
            )
    return sentiment

sentiment = sentiment("This product is too bad to be paid for")

print(sentiment["response"])
