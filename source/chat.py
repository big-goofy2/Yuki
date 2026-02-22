import json
import uuid
from datetime import datetime
import os

class Chat:
    def __init__(self, filename="chats.json"):
        self.chat_id = str(uuid.uuid4())
        self.memory = []
        self.filename = filename
        self.loadChat()

    def addMemory(self, sender, message, intent="unknown"):
        data = {
            "id": str(uuid.uuid4()),
            "chat_id": self.chat_id,
            "sender": sender,
            "message": message,
            "intent": intent,
            "timestamp": datetime.now().isoformat()
        }

        self.memory.append(data)

        if len(self.memory) % 5 == 0:
            self.saveChat()

        return data

    def saveChat(self):
        all_chats = []

        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    all_chats = json.load(f)
            except json.JSONDecodeError:
                all_chats = []

        # Remove old version of this chat if it exists
        all_chats = [c for c in all_chats if c["chat_id"] != self.chat_id]

        all_chats.append({
            "chat_id": self.chat_id,
            "memory": self.memory,
            "last_updated": datetime.now().isoformat()
        })

        with open(self.filename, "w") as f:
            json.dump(all_chats, f, indent=4)

    def loadChat(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r") as f:
                all_chats = json.load(f)
                for chat in all_chats:
                    if chat["chat_id"] == self.chat_id:
                        self.memory = chat["memory"]
                        return
        except json.JSONDecodeError:
            pass

    def get_last_subject(self):
        keywords = {"game", "python", "pygame", "ai", "code", "bug", "chat"}

        for entry in reversed(self.memory):
            words = entry["message"].lower().split()
            for word in words:
                if word in keywords:
                    return word
        return None
