
#adding memory 
class cal_memory:
    def __init__(self):
        self.memory = 0


    def MC(self):
        self.memory = 0
        print("MEMORY CLEARED")


    def MS(self,value):
        self.memory = float(value)
        print("Memory Stored")


    def add_to_memory(self,value):
        self.memory += float(value)
    

    def remove_from_memory(self,value):
        self.memory -= float(value)
        

    def memory_recall(self):
        return self.memory
    
