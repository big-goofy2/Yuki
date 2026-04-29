import json

class Memory:
  def __init__(self):
    self.filename = "memory.json"
    self.short_term = []
    self.long_term = {}
    
  def remember(self, key, value):
    self.long_term[key] = value
    
  def recall(self, key):
      return self.long_term.get(key)
  
  def add_short_term(self, message):
      self.short_term.append(message)
      return self.short_term
    
  def save(self):
   with open(self.filename, "w") as f:
    json.dump({"short_term": self.short_term, "long_term": self.long_term}, f, indent=2)
   
  def load(self):
    try:
     with open(self.filename,"r") as f:
      data = json.load(f)
      self.short_term = data.get("short_term", [])
      self.long_term = data.get("long_term", {})
    except FileNotFoundError:
      return
