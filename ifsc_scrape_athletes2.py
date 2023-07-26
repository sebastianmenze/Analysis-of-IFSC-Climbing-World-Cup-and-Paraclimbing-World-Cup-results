# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 22:36:37 2023

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 21:33:34 2023

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import re

import traceback

driver = webdriver.Chrome()

for number in np.arange(30000)+1 :
    
    try:
        url = 'https://www.ifsc-climbing.org/index.php?option=com_ifsc&task=athlete.display&id='+ str(int(number))
        driver.get(url)
        
        climber_name= driver.title
        
        elem = driver.find_element(By.CLASS_NAME, "results")
        text = elem.get_attribute('innerHTML')
        
        
        # match=re.findall(pattern, text)
        pattern = '<div class="event">'
        indices_object = re.finditer(pattern=pattern, string=text)
        i1 = [index.start() for index in indices_object]
        
        pattern = 'RESULTS &gt;&gt'
        indices_object = re.finditer(pattern=pattern, string=text)
        i2 = [index.start() for index in indices_object]
        
        athlete =pd.DataFrame(columns=['event','rank','para_class','date'])
        
        jj =0
        for i in range(len(i1)):
            
            try:
                substr = text[ i1[i] :  i2[i] ]
                
                
                pattern1 = '<div class="event">'
                indices_object = re.finditer(pattern=pattern1, string=substr)
                k1 = [index.start() for index in indices_object]
                
                pattern2 = '</div><div class="date">'
                indices_object = re.finditer(pattern=pattern2, string=substr)
                k2 = [index.start() for index in indices_object]
                    
                event = substr[k1[0]+len( pattern1 ):k2[0]].strip()
                    
                pattern1 = '<div class="rank"><div> <span>'
                indices_object = re.finditer(pattern=pattern1, string=substr)
                k1 = [index.start() for index in indices_object]
                
                pattern2 = '</span> <strong> LEAD </strong>'
                indices_object = re.finditer(pattern=pattern2, string=substr)
                k2 = [index.start() for index in indices_object]
                    
                rank_str = substr[k1[0]+len( pattern1 ):k2[0]].strip()    
                rank= int( re.sub("[^0-9]", "", rank_str) )
            
                pattern1 = '<strong> LEAD </strong>'
                indices_object = re.finditer(pattern=pattern1, string=substr)
                k1 = [index.start() for index in indices_object]
                
                pattern2 = '</div> <a href="/index.php/'
                indices_object = re.finditer(pattern=pattern2, string=substr)
                k2 = [index.start() for index in indices_object]
                    
                para_class = substr[k1[0]+len( pattern1 ):k2[0]].strip()
                
                pattern1 = '<div class="date">'
                indices_object = re.finditer(pattern=pattern1, string=substr)
                k1 = [index.start() for index in indices_object]
                
                pattern2 = '</div><div class="rank"><div>'
                indices_object = re.finditer(pattern=pattern2, string=substr)
                k2 = [index.start() for index in indices_object]
                    
                date_str = substr[k1[0]+len( pattern1 ):k2[0]].strip()   
                
                
            
                athlete.loc[jj,'event']=event            
                athlete.loc[jj,'rank']=rank
                athlete.loc[jj,'para_class']=para_class
                athlete.loc[jj,'date']= pd.to_datetime(date_str)


                jj=jj+1
            except Exception as e:
                print(e)
                print(traceback.format_exc())

                #pass                
        athlete['name']=    climber_name
        
        print(athlete)
        
        athlete.to_csv(climber_name+'.csv')
    
    # text.find('class="event"')
    except:
        pass

driver.close()




