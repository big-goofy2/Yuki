class BaseModel:
  def __init__(self,memory):
    self.model = "Numa-1"
    self.memory = memory
    self.intents = {
      "research": ["what is", "who is", "explain", "how", "why","when"],
      "greeting": ["hello", "hi", "hey"],
      "system": ["who are you"]
    }
    
  def detect_intents(self, user_input):
        text = user_input.lower()
        found = []

        for intent, keywords in self.intents.items():
            for kw in keywords:
                if kw in text:
                    found.append(intent)
                    break

        return found if found else ["unknown"]
