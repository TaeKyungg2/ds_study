class queue:
    def __init__(self,len):
        self.len=len
        self.items=[None]*len
    def pop(self):
        value=self.items[0]
        del self.items[0]
        return value
    def push(self,value):
        for i in self.items:
            if i ==None:
                i=value
                break