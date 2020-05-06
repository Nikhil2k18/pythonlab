#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## theotrical questions
# q1
# we can call it by using super() command
# q3
 people={1:{'name':'John','age':'27','sex':'Male'}
        2:{'name':'Marie','age','22','sex':'Female'}}
 print(people)
# q2
 class Parent:
        pass
 class Child(Parent):
        pass


# In[4]:



items=[]
for i in range(100,401):
    s=str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
print(",".join(items))


# In[5]:


def calculateSum (a,b):
    s=int(a)+int(b)
    return s
# Main code
# take two integral numbers as strings
num1="10"
num2="20"
# calculate sum
sum=calculateSum(num1,num2)
# print sum
print("Sum=",sum)


# In[3]:





# In[ ]:




