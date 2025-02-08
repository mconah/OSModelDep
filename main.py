import ollama 

def response(model, prompt):
    try:
        response: ollama.ChatResponse = ollama.chat(model = model, messages = [
            {
                 'role': 'user',
                'content': prompt,
            },
        ])
        return response.message.content
    except ollama.ResponseError as e:
        print("Error:", e.error)
        if e.status_code == 404:
            ollama.pull(model)
    except Exception as e:
        print("Error:", e)


def display_intro():
    return """Welcome to this Demo By Mmaduabuci Onah for NSK.AI
    At NSK.AI we are focused at practical utilization of AI and how it impacts your life

    ENJOY!!! THE POWER OF INTENTIONAL COMMUNITY

    NOTE: This is a simple demo to show how to work with open-source models which can be easily accessed via Ollama.
    
    Input %%instructions to view the instructions

    @NSK.AI Lab
    """

def display_instructions():
   return  """This a command linke interface that allows you to play arround multiple models using ollama

    ENJOY THE COOLNESS OF OPEN-SOURCE MODELS

    These are the prompts to use for certain actions:
     _________________________________________________________________
    | Command          | What does it do?       | Anything to note?   |
    |==================|========================|=====================|
    |%%change model    |Used to change models   | None                |
    |__________________|________________________|_____________________|
    |%%list model      |To list models in your  |None                 |
    |                  |local system            |                     |
    |__________________|________________________|_____________________|
    |%%quit            |To end the session      |                     |
    |------------------|------------------------|---------------------|
    |%%download model  |To download any model on|                     |
    |                  |the ollama website      |                     |
    |------------------|------------------------|---------------------|
    |%%delete model    |Delete any of your model|                     |
    |__________________|________________________|_____________________|
    
    Any other prompt outside these commands would be responded by your default model(qwen2 i.5B).
    """

commands = ["%%change model", "%%list model", "%%quit", "%%download model", "%%delete model", "%%instructions", "%%introduction"]

model = "qwen2:1.5b"

print(display_intro())
while True:
    prompt = input("You: ")
    model = model

    if prompt in commands:
        if prompt == "%%change model":
            pass
        if prompt =="%%list model":
            models = ollama.list()
            print(models.models[].model)
        if prompt == "%%quit":
            break
        if prompt == "%%download model":
            pass
        if prompt == "%%delete model":
            pass
        if prompt == "%%instructions":
            print(display_instructions())
        if prompt == "%%introduction":
            print(display_intro())

    else:
        new_response = response(model, prompt)
        print(new_response)
