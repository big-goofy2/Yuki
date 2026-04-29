import json

class Memory:
  def __init__(self):
    self.filename = "memory.json"
    self.short_term = []
    self.long_term = {}
    
  def save(self):
   pass
   
  def load(self):
   with open(self.filename,"r") as f:
    return json.load(f)
