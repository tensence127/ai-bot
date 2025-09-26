from config import SYSTEM_MESSAGE

def trim_messages(messages):
    if len(messages) <= 15:
        return messages
    else:
        return [SYSTEM_MESSAGE] + messages[-14:]