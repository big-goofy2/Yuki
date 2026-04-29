import json

class Memory:
  def __init__(self):
    self.filename = "memory.json"
    self.short_term = []
    self.long_term = {}
    
  def save(self):
   with open(self.filename, "w") as f:
    json.dump({"short_term": self.short_term, "long_term": self.long_term}, f, indent=2)
   
  def load(self):
   with open(self.filename,"r") as f:
    return json.load(f)
