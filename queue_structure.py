class Queoe:
    def __init__(self):
        self.data=[]
    def put(self,name):
        self.data.append(name)
    def get(self):
        return  self.data.pop(0)


q1= Queoe()
q1.put(1)
q1.putr(2)
q1.putr(3)
q1.putr(4)
first=q1.put()
print(q1.out())