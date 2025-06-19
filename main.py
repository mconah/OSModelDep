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
    return """Welcome to this Demo By Mmaduabuci Onah 

    NOTE: This is a simple demo to show how to work with open-source models which can be easily accessed via Ollama.
    
    Input %%instructions to view the instructions
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


def list_models() -> list:
    existing_models = ollama.list()
    models_list = []
    print("AVAILABLE MODELS ARE:/n ")
    for models in existing_models.models:
        models_list.append(models.model)
    return models_list

model = "qwen2.5:0.5b"

if model not in list_models():
    ollama.pull(model)

print(display_intro())
while True:
    prompt = input("You: ")
    model = model

    if prompt in commands:
        if prompt == "%%change model":
            for model in list_models():
                print(model)
            model_to_use = input("What model do you want to use? ")
            if model_to_use in list_models():
                model = model_to_use
                print(f"Booyaaah!! /nModels successfully changed to {model}")
            else:
                print("Ooops!! /n Model not in list of models /nTry again")
        if prompt =="%%list model":
            models = ollama.list()
            for model in list_models():
                print(model)
        if prompt == "%%quit":
            break
        if prompt == "%%download model":
            model_to_download = input("What model do you want to download? ")
            try:
                ollama.pull(model_to_download)
                print("Successful")
            except:
                print("Ooops! Failed. Ensure that the model name is correct and try again")
        if prompt == "%%delete model":
            print(list_models())
            model_to_delete = input("What model do you want to delete? ")
            if model_to_delete in list_models():
                ollama.delete(model_to_delete)
                print(f"You have deleted {model_to_delete}")
            else:
                print(f"{model_to_delete} was not found. /nTry again!!")
        if prompt == "%%instructions":
            print(display_instructions())
        if prompt == "%%introduction":
            print(display_intro())

    else:
        new_response = response(model, prompt)
        print(new_response)
