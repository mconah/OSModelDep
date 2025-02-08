import ollama

response = ollama.generate(
        model="gemma:2b",
        prompt="Hi"
        )

print(response["response"])
