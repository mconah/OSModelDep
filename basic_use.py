import ollama

print("""
      This is just a simple interaction with Gemma:2b model, if this model is not installed
      make sure to install i by running the command: ollama pull gemma:2b. 

      Thank you!
      """)
prompt = input("Ask any question: ")
response = ollama.generate(
        model="gemma:2b",
        prompt=prompt
        )

print(response["response"])
