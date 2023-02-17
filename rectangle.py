#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Rectangle:
    
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def Perimeter(self):
        perimeter=2*(self.l+self.b)
        return (perimeter)
    
    def Area(self):
        area=self.l*self.b
        return (area)
    
    def display(self):
        print("length: ",self.l)
        print("breadth: ",self.b)
        print("Area :",self.Area())
        print("Primeter :",self.Permeter())
    


# In[ ]:




