#!/usr/bin/env python
# coding: utf-8

# # kg_to_lbs converter and miles_to_kilometers

# In[ ]:


def kg_to_lbs(kg):
    
    divider = 0.45359237 # this is the value we use to change KGs to pounds 
    return kg/divider


# In[5]:


kg_to_lbs(50)


# In[6]:


def miles_to_kilometers(miles):
    kilometers = miles*1.60934
    # 1.6093 changes miles to kilometers
    if kilometers >10 and kilometers <20:
        print("You can use a car or walk.")
    elif kilometers <10:
        print("You can walk")
    elif kilometers >20:
        print("Use a car")
    return kilometers


# In[7]:


miles_to_kilometers(2)


# # fizz_buzz_question

# In[8]:


def fizz_buzz_question(number):
   if number %3==0 and number %5==0:
       print("Fizz Buzz")
   elif number %3==0:
       print("Fizz")
   elif number %5==0:
       print("Buzz")
   return number


# In[12]:


fizz_buzz_question(120)


# # Alpha's classes and inheritance's demstration

# In[2]:



class humans:
   def __init__(self, name, age, sex):
       self.name = name
       self.age = age
       self.sex = sex 
       
   def walk(self):
       if self.age < 2:
           print(f"{self.name} cannot walk")
       else:
           print(f" {self.name} is walking and the {self.sex} is {self.age}")
       
   def eat(self):
       print(f"{self.name} is eating")
       
   def sleep(self):  
       print(f"{self.name} is sleeping")
       
class dog(humans):
   def __init__(self, name, age, sex, color):
       self.color = color
       super().__init__(name, age, sex)
       
   def skin_color(self):
       print(f"{self.name} is having a {self.color} skin torn")
       
class cat(dog,humans):
   def __init__(self, name, age, sex, color,breed):
       self.breed = breed
       super().__init__(name, age, sex, color)
       
   def skin_color(self):
       print(f" The cat is having a {self.color} fur color and its a {self.breed}")
       
   def walk(self):
       if self.age < 0.5:
           print(f"{self.name} cannot walk")
       else:
           print(f" {self.name} is walking and the cat is {self.age}")
   
   

       
   


# In[12]:


r4 = cat("bruno", 1, "Male dog", "black", "italian")
r4.walk()
r4.eat()
r4.sleep()
r4.skin_color()


# In[ ]:


r4 = dog("max", 3, "Male_cat", "brown")
r4.walk()
r4.eat()
r4.sleep()


# In[ ]:




