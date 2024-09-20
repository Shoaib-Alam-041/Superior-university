#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Model_agent:
    def __init__(self, desirde_temp):
        self.desirde_temp = desirde_temp  
        self.previous_act = None  

    def act(self, current_temp):
        if current_temp < self.desirde_temp and self.previous_act != "on":
            self.previous_act = "on"
            return "Heater ON"
        
        elif current_temp >= self.desirde_temp and self.previous_act != "off":
            self.previous_act = "off"
            return "Heater OFF"
        
        return "No action needed"


agent = Model_agent(desirde_temp=22)
print(agent.act(20))  
print(agent.act(21))  
print(agent.act(23))  


# In[ ]:




