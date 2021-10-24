#!/usr/bin/env python
# coding: utf-8

# # Wajahat_Hussain (ASSIGNEMENT-3) JAWAN PAKISTAN_PYTHON

# In[25]:


#Write a Python program to print the following string in a specific format (see the output).

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")


# In[37]:


#Write a Python program to get the Python version you are using
from platform import python_version

print(python_version())


# In[46]:


#Write a Python program to display the current date and time.

from datetime import datetime
today = datetime.today()
print("Today's time & date:", today)


# In[53]:


#Write a Python program which accepts the radius of a circle from the user and compute the area.

Radius=int(input("Enter Radius OF Circle"))
Area=3.142*(Radius**2)
print("Area OF Circle is", Area)


# In[64]:


#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
F=(input("Enter First name"))
L=(input("Enter First name"))
print("Your Full Name In Reverse is" ,L,"",F)


# In[68]:


#Write a python program which takes two inputs from user and print them addition
Num1=int(input("Enter Num1 = "))
Num2=int(input("Enter Num2 = "))
Num=Num1+Num2
print("When we add Both Num1&2 = ",Num)


# In[9]:


#Write a program which takes 5 inputs from user for different subject’s marks, total it and generate mark sheet using grades ?

Urdu=int(input("Enter Urdu Marks = "))
English=int(input("Enter English Marks = "))
Islamiat=int(input("Enter Islamiat Marks = "))
Maths=int(input("Enter Maths Marks = "))
Arts=int(input("Enter Arts Marks = "))
print("Islamiat marks =" , Islamiat)
print("English marks =" , English)
print("Maths marks =" , Maths)
print("Urdu marks =" , Urdu)
print("Arts marks =" , Arts)
total_Marks = 500
print(total_Marks)
print("obtained marks = ",Urdu+Islamiat+Maths+English+Arts)
percent=(((Urdu+Islamiat+Maths+English+Arts)/500)*100)
print("percentage is =",(percent),"%"  )

if percent < 100 and percent > 80:
    print("Grade A+");
elif percent < 80 and percent > 70:
    print("Grade A");
elif percent < 70 and percent > 80:
    print("Grade B")
else:
    print("Fail")


# In[14]:


#Write a program which take input from user and identify that the given number is even or odd?
L=int(input("Enter number =  "))
if L%2==0:
    print("Even Number you have Entered")
else:
    print("Odd Number you have Entered")


# In[21]:


#Write a program which print the length of the list?
List=[89,366, "love","pakistan", 96]
print(List)
print("Length Of a list is ",len(List))


# In[71]:


#Write a Python program to sum all the numeric items in a list?
List=[455,123,321,90,595]
add=sum(List)
print(add)


# In[58]:


#Write a Python program to get the largest number from a numeric list.
L=[84,98,99.4,88,41,53,48,66,72,90]
list.sort(L)
print(L[-1])


# In[69]:


#Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_a = []

for i in a:
  
    if i < 5:
        new_a.append(i)
print(new_a)


# In[ ]:





# In[ ]:




