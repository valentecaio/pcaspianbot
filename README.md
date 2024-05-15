# PCaspianBot

This is a basic template for creating chatbot apps for Telegram using `telepot` to interface with Telegram and `ollama` for the bot intelligence.

![alt text](assets/example.jpg?raw=true "Bot example")


## How to Use

### Python Setup

* Clone this repository and install dependencies:

```bash
git clone https://github.com/valentecaio/pcaspianbot && cd pcaspianbot/
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

### Ollama Setup

* Download and install Ollama from [Ollama's website](https://ollama.com).

* Download and install a model from Ollama:
```bash
ollama pull llama3
ollama run llama3
```

* Edit the MODEL_NAME variable in the first lines of pcaspian.py to match the name of your model.
```python
MODEL_NAME = 'llama3'
```

### Telepot Setup

* Talk to the [BotFather](https://t.me/BotFather) to create your bot.

* Save your new bot token in a file named **token.txt** at the root of the project.

### [optional] Customize Model Behavior

You can give some life to your model by setting system prompts for a specific desired behavior.  
  
* In the Ollama prompt interface (`ollama run <modelname>`), type:  
```csharp
/set system For all questions asked, respond as PCaspian. PCaspian is a duck in the Possumland Farm. He is also the Prince of Narnia. He has very nice hair and nice feathers. He quacks and swims in the river. Sage feeds him with hay on rainy days. Use simple English words and do not be too verbose.

/save pcaspian
```

* Remember to edit the MODEL_NAME variable in pcaspian.py to match your new model name.
```python
MODEL_NAME = 'pcaspian'
```


### Run

```bash
python3 pcaspian.py
```

Now your bot should be up and running, ready to quack and swim in the virtual rivers of Telegram!
