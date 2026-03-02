class Model:
    def __init__(self):
        self.model = "Numa-1"
        self.memory = []
        self.knowledge = {}
    
    def get_knowlage(self,data):
        self.knowledge = data
    
    def clear_memory(self):
        self.memory.clear()
        return self.memory
    
