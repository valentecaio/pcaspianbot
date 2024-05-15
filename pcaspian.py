import time, os, sys

# non standard libraries
import telepot
import ollama

WAIT_TIME = 60*60*24 # 24 hours
MODEL_NAME = 'pcaspianllama3'


def msg_handler(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
  print(content_type, chat_type, chat_id)

  if content_type == 'text':
    print(f'Received msg: {msg["text"]}')
    msg = ollama.generate(model=MODEL_NAME, prompt=msg['text'])['response']
    print(f'[send] chat: {chat_id}, msg: {msg}')
    bot.sendMessage(chat_id, msg)


if __name__ == '__main__':
  # instantiate bot
  TOKEN = open(os.path.join(sys.path[0], "token.txt"), "r").read().strip()
  bot = telepot.Bot(TOKEN)
  print(bot.getMe())

  # handling messages
  bot.message_loop(msg_handler)
  print('Listening ...')

  # hanging program execution
  while True:
    time.sleep(60*10)
