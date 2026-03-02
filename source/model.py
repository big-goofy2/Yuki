class Model:
    def __init__(self,name):
        self.model = name
        self.memory = []
        self.knowledge = {}
    
    def get_knowlage(self,data):
        self.knowledge = data
    
    def clear_memory(self):
        self.memory.clear()
        return self.memory
    
