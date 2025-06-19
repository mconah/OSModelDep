# Open Source LLM Model Deployment

This repos contains a guide to running opensource Large Language Models and other models made available through Ollama. If you a developer eager to understand teh simple functions used in these simple lines of code [Visit the ollama library on PyPI](https://pypi.org/project/ollama/ "Ollama on PyPI")

### Introduction to Ollama
Ollama is a tool that makes it easy to run large language models(LLMs) locally on your computer. It is also great to note that its functionality can be extended to production. 

###### Note:
+ This tutorial assumes the use of ubuntu linux, while the python code work irrespective of the operating system. The installation of ollama locally may only work on Linux and Mac for more informatio on installing ollama in you operation system [visit this page](https://ollama.com/download "Ollama download page")
+ This tutorial assumes that you have python installed if not [visit this website to download it](https://www.python.org/downloads/ "Donwload python here") Ensure that python is added to your path variable and that pip is also installed. 
+ Ensure that you are running python3 and not python2. This is important to always checkout for mainly Linux and Mac users. 
+ This models where tested on a machine of 4Gb ram and 2VCPU cores, hence it should work on most 4Gb ram systems. 

### Running open source models locally with Ollama:
1. After Ollama installation, [visit the ollama website](https://ollama.com/search "Search a gallery of models") to see all the models available via Ollama. 
2. Run this command to dowload 1.5 billion DeepSeek R1
```bash
ollama pull deepseek-r1:1.5b
```

3. To get the model working in your terminal run the next command
```bash
ollama run deepseek-r1:1.5b
```

That is practically all you need to enjoy the coolness of runing models directly on your termminal, you can download any model available on Ollama website and and tthe power of your machine can sustain/power. 

### Running open source models with python and ollama(Of course)
To make it easy to follow allong even without prior knowledge of python we would take a step by step approach to make the code work for you. All this goodness can not be restricted to a specific number of people. 

1. Clone this repository 
```bash
cd ~
git clone https://github.com/mconah/OSModelDep
```

2. Now that you have the repository install the required libraries. 
```bash
cd ~/OSModelDep
pip install -r requirements.txt
```

> If you are a python developer of feels explorative, you can go through the code and make modifications. Else you can just run each of the code to get different super powers. sentiment.py code simply performs sentiment analysis with an LLM not an actuall sentiment analysis model. basic_use.py just allows you to make just a simple input. As expected, the main.py is the majoy code file that allows you to work with ollama directly through python code. Enjoy all that goodness. 

3. To run each file run the command below. 
```bash
python3 main.py
```
OR
```bash
python main.py
```
OR
```bash
py main.py
```

You can change main.py to to sentiment.py or basic_use.py to run and of those two code. 

> Boooooyaaaaah!!!!!!

Let's see what you can do with this repo. 
