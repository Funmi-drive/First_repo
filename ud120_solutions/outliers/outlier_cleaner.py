#!/usr/bin/env python
# coding: utf-8

# In[5]:


#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    
    cleaned_data = []
   
  
    for i in range(len(predictions)):
        residual_error = predictions[i] - net_worths[i]
        cleaned_data.append((ages[i], net_worths[i], residual_error))
    cleaned_data = sorted(cleaned_data, key=lambda tup: tup[2])


    ### your code goes here

    
    return cleaned_data[: 81]

