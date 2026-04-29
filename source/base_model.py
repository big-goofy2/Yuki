from memory import Memory

class BaseModel:
  def __init__(self):
    self.model = "Numa-1"
    self.memory = Memory()
    self.memory.load()
    self.nicknames = []
    
  def add_nickname(self,nickname):
    self.nicknames.append(nickname)
    return self.nicknames
