# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 07:50:09 2023

@author: wurst
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import glob 
import os
from scipy import stats


filelist = glob.glob(r'athlete_rankings_2\*.csv')

#file=r"C:\Users\wurst\Downloads\Analysis-of-IFSC-Climbing-World-Cup-and-Paraclimbing-World-Cup-results-main\athlete_rankings\Abigail ROBINSON.csv"


eventlist=pd.DataFrame([])

df_event=pd.DataFrame([])

for file in filelist:
    
    
    
    df=pd.read_csv(file,index_col=0)
    df['date']=pd.to_datetime(df['date'])
    
    df['age_at_event'] =  df['age']  - (2023 - df['date'].dt.year)
    
    # ix_para=df['event'].str.contains('Para')
    
    # df= df.loc[ix_para,:]
    
    if len(df)>0:

         
        # events = pd.Series( (df['event'] ).unique() )
        
        # ix_uni = df['event'].isin(events)
        
        
        
        eventlist = pd.concat( [eventlist,  df ])
  
        
eventlist= eventlist.reset_index(drop=True)

# df_event['name'] = eventlist[0].unique()


# i=0
# for e in df_event['name'] :
#     n = np.sum(eventlist[0]==e)
#     df_event.loc[i,'n']=n
#     i=i+1

#eventlist.to_csv('eventlist.csv')
#%%

# eventlist = pd.read_csv( 'eventlist.csv' )
# eventlist = pd.read_csv( 'eventlist.csv' )
   # eventlist['date']=pd.to_datetime(eventlist['date'])

print( pd.Series( ( eventlist['para_class']  ).unique() ) )
 
 
ix = eventlist['para_class'] == 'MEN AMPUTEE LEG PD'
eventlist.loc[ix,'para_class'] = 'MEN AL2'

ix = eventlist['para_class'] == 'MEN AL-2'
eventlist.loc[ix,'para_class'] = 'MEN AL2'

ix = eventlist['para_class'] == 'WOMEN VISUAL IMPAIRMENT B2'
eventlist.loc[ix,'para_class'] = 'WOMEN B2'

ix = eventlist['para_class'] == 'MEN VISUAL IMPAIRMENT B1'
eventlist.loc[ix,'para_class'] = 'MEN B1'

ix = eventlist['para_class'] == 'WOMEN VISUAL IMPAIRMENT B3'
eventlist.loc[ix,'para_class'] = 'WOMEN B3'

ix = eventlist['para_class'] == 'WOMEN VISUAL IMPAIRMENT B1'
eventlist.loc[ix,'para_class'] = 'WOMEN B1'

ix = eventlist['para_class'] == 'MEN AU-2 (FOREARM AMPUTEE)'
eventlist.loc[ix,'para_class'] = 'MEN AU2'

ix = eventlist['para_class'] == 'MEN AU-1 (ARM AMPUTEE)'
eventlist.loc[ix,'para_class'] = 'MEN AU1'

ix = eventlist['para_class'] == 'MEN AL-1 (SEATING)'
eventlist.loc[ix,'para_class'] = 'MEN AL1'

ix = eventlist['para_class'] == 'WOMEN AU-2 (FOREARM AMPUTEE)'
eventlist.loc[ix,'para_class'] = 'WOMEN AU2'

ix = eventlist['para_class'] == 'WOMEN AMPUTEE LEG PD'
eventlist.loc[ix,'para_class'] = 'WOMEN AL2'

ix = eventlist['para_class'] == 'MEN VISUAL IMPAIRMENT B2'
eventlist.loc[ix,'para_class'] = 'MEN B2'

ix = eventlist['para_class'] == 'MEN VISUAL IMPAIRMENT B3'
eventlist.loc[ix,'para_class'] = 'MEN B3'

ix = eventlist['para_class'] == 'MEN SEATING'
eventlist.loc[ix,'para_class'] = 'MEN AL1'

ix = eventlist['para_class'] == 'MEN AMPUTEE ARM PD'
eventlist.loc[ix,'para_class'] = 'MEN AU2'

ix = eventlist['para_class'] == 'WOMEN AMPUTEE ARM PD'
eventlist.loc[ix,'para_class'] = 'WOMEN AU2'

ix = eventlist['para_class'] == 'WOMEN AU-1 (ARM AMPUTEE)'
eventlist.loc[ix,'para_class'] = 'WOMEN AU1'

#%%

plt.figure(1)
plt.clf()



plt.plot( eventlist['age_at_event'] , eventlist['rank'],'.b')


plt.grid()


plt.tight_layout()   
plt.draw()

# plt.savefig('class_participation_timseries.png',dpi=200)


#%%


cla =pd.Series( ( eventlist['para_class']  ).unique() )

df_age=pd.DataFrame([],columns = cla)
bins = np.arange(10,51)
df_age['age'] = bins[:-1]

i=0
c=cla[0]


for c in cla:
        
    ixx = eventlist['para_class'] ==c
    
    ixhead= df_age.columns==c

    x = eventlist.loc[ixx,'age_at_event']
    
    y = np.histogram( x,bins)
    
    
    df_age.loc[:,ixhead]=y[0] 
    
    
#%%

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:31:29 2023

@author: a5278
"""



plt.figure(1)
plt.clf()


plt.subplot(431)
plt.plot( df_age['age'] , df_age['MEN AL2'],'.-b',label='Men')
plt.plot( df_age['age'] , df_age['WOMEN AL2'],'.-r',label='Women')
plt.title('AL2')
plt.legend()
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')
plt.subplot(432)
plt.plot( df_age['age'], df_age['MEN AL1'],'.-b')
#plt.plot( df_age['age'], df_age['WOMEN AL1'],'.-r')
plt.title('AL1')
plt.xlabel('Age at competition')
plt.ylabel('count')

plt.grid()

plt.subplot(433)
plt.plot( df_age['age'], df_age['MEN AU2'],'.-b')
plt.plot( df_age['age'], df_age['WOMEN AU2'],'.-r')
plt.title('AU2')
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')
plt.subplot(434)
plt.plot( df_age['age'], df_age['MEN AU1'],'.-b')
plt.plot( df_age['age'], df_age['WOMEN AU1'],'.-r')
plt.title('AU1')
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')
plt.subplot(435)
plt.plot( df_age['age'], df_age['MEN B1'],'.-b')
plt.plot( df_age['age'], df_age['WOMEN B1'],'.-r')
plt.title('B1')
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')
plt.subplot(436)
plt.plot( df_age['age'], df_age['MEN B2'],'.-b')
plt.plot( df_age['age'], df_age['WOMEN B2'],'.-r')
plt.title('B2')
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')

plt.subplot(437)
plt.plot( df_age['age'], df_age['MEN B3'],'.-b')
plt.plot( df_age['age'], df_age['WOMEN B3'],'.-r')
plt.title('B3')
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')
plt.subplot(438)
plt.plot( df_age['age'], df_age['MEN RP1'],'.-b')
plt.plot( df_age['age'], df_age['WOMEN RP1'],'.-r')
plt.title('RP1')
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')
plt.subplot(439)
plt.plot( df_age['age'], df_age['MEN RP2'],'.-b')
plt.plot( df_age['age'], df_age['WOMEN RP2'],'.-r')
plt.title('RP2')
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')
plt.subplot(4,3,10)
plt.plot( df_age['age'], df_age['MEN RP3'],'.-b')
plt.plot( df_age['age'], df_age['WOMEN RP3'],'.-r')
plt.title('RP3')
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')
plt.subplot(4,3,11)
plt.plot( df_age['age'], df_age['MEN'],'.-b')
plt.plot( df_age['age'], df_age['WOMEN'],'.-r')
plt.title('Regular')
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')

plt.subplot(4,3,12)

ix_para= df_age.columns.isin( ['MEN AU2','MEN AU1','MEN AL2','MEN AL1','MEN B1','MEN B2','MEN B3','MEN RP1','MEN RP2','MEN RP3'] )
plt.plot( df_age['age'], df_age.iloc[:,ix_para].sum(axis=1)  ,'.-b')

ix_para= df_age.columns.isin( ['WOMEN AU2','WOMEN AU1','WOMEN AL2','WOMEN AL1','WOMEN B1','WOMEN B2','WOMEN B3','WOMEN RP1','WOMEN RP2','WOMEN RP3'] )
plt.plot( df_age['age'], df_age.iloc[:,ix_para].sum(axis=1)  ,'.-r')


plt.title('All para categories')
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')

plt.tight_layout()   
plt.draw()

# plt.savefig('class_age_distribution.png',dpi=200)

#%%

#%%
years= np.arange(2010,2024)

# y=2023
# c=cla[7]


cla =pd.Series( ( eventlist['para_class']  ).unique() )

he = pd.concat( [ pd.Series( ['year']) ,cla]  )

dfts=pd.DataFrame([],columns = he)

dfts['date'] = years

dfts_new=dfts.copy()

i=0
for y in years:
    

    for c in cla:
        
        ix1 = eventlist['date'].dt.year == y
        ix2 = eventlist['para_class'] ==c
        ix= ix1 & ix2
        
        nam = pd.Series(  eventlist.loc[ix,'name'].unique() )
        
        ix1 = eventlist['date'].dt.year == y-1
        ix2 = eventlist['para_class'] ==c
        ix= ix1 & ix2        
        nam_old =  pd.Series(   eventlist.loc[ix,'name'].unique() )
        
        # newthatyear =  len(nam) - nam.isin(nam_old).sum() 
        newthatyear =   nam.isin(nam_old).sum() 
        


        
        ixhead= dfts.columns==c
    
        dfts.loc[i,ixhead]= len(nam)
        dfts_new.loc[i,ixhead]= newthatyear

    i=i+1


#%%




plt.figure(2)
plt.clf()


plt.subplot(431)
plt.plot( dfts['date'] , dfts['MEN AL2'],'.-b',label='Men')
plt.plot( dfts['date'] , dfts['WOMEN AL2'],'.-r',label='Women')


plt.title('AL2')
plt.legend()
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')



plt.subplot(432)
plt.plot( dfts['date'] , dfts['MEN AL1'],'.-b')
#plt.plot( dfts['date'] , dfts['WOMEN AL1'],'.-r')
plt.title('AL1')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(433)
plt.plot( dfts['date'] , dfts['MEN AU2'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN AU2'],'.-r')
plt.title('AU2')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')


plt.subplot(434)
plt.plot( dfts['date'] , dfts['MEN AU1'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN AU1'],'.-r')
plt.title('AU1')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')
plt.subplot(435)
plt.plot( dfts['date'] , dfts['MEN B1'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN B1'],'.-r')
plt.title('B1')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(436)
plt.plot( dfts['date'] , dfts['MEN B2'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN B2'],'.-r')
plt.title('B2')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(437)
plt.plot( dfts['date'] , dfts['MEN B3'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN B3'],'.-r')
plt.title('B3')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(438)
plt.plot( dfts['date'] , dfts['MEN RP1'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN RP1'],'.-r')
plt.title('RP1')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(439)
plt.plot( dfts['date'] , dfts['MEN RP2'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN RP2'],'.-r')
plt.title('RP2')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(4,3,10)
plt.plot( dfts['date'] , dfts['MEN RP3'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN RP3'],'.-r')
plt.title('RP3')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(4,3,11)
plt.plot( dfts['date'] , dfts['MEN'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN'],'.-r')
plt.title('Regular')
plt.grid()
plt.ylabel('N athletes')


plt.tight_layout()   
plt.draw()

# plt.savefig('athletes_per_year.png',dpi=200)

# dfts.to_csv('athletes_per_year.csv')
    
#%%


plt.figure(2)
plt.clf()


plt.subplot(431)
plt.plot( dfts['date'] , dfts['MEN AL2'],'.-b',label='Men')
plt.plot( dfts['date'] , dfts['WOMEN AL2'],'.-r',label='Women')
plt.plot( dfts_new['date'] , dfts_new['MEN AL2'],'.--b',label='Competed in previous year - Men')
plt.plot( dfts_new['date'] , dfts_new['WOMEN AL2'],'.--r',label='Competed in previous year - Women')

plt.title('AL2')
plt.grid()

plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(432)
plt.plot( dfts['date'] , dfts['MEN AL1'],'.-b')
plt.plot( dfts_new['date'] , dfts_new['MEN AL1'],'.--b')
#plt.plot( dfts['date'] , dfts['WOMEN AL1'],'.-r')
plt.title('AL1')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(433)
plt.plot( dfts['date'] , dfts['MEN AU2'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN AU2'],'.-r')
plt.plot( dfts['date'] , dfts_new['MEN AU2'],'.--b')
plt.plot( dfts['date'] , dfts_new['WOMEN AU2'],'.--r')
plt.title('AU2')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')


plt.subplot(434)
plt.plot( dfts['date'] , dfts['MEN AU1'],'.-b',label='Men')
plt.plot( dfts['date'] , dfts['WOMEN AU1'],'.-r',label='Women')
plt.plot( dfts['date'] , dfts_new['MEN AU1'],'.--b',label='Competed in previous year - Men')
plt.plot( dfts['date'] , dfts_new['WOMEN AU1'],'.--r',label='Competed in previous year - Women')
plt.title('AU1')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')
plt.legend()


plt.subplot(435)
plt.plot( dfts['date'] , dfts['MEN B1'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN B1'],'.-r')
plt.plot( dfts['date'] , dfts_new['MEN B1'],'.--b')
plt.plot( dfts['date'] , dfts_new['WOMEN B1'],'.--r')
plt.title('B1')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(436)
plt.plot( dfts['date'] , dfts['MEN B2'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN B2'],'.-r')
plt.plot( dfts['date'] , dfts_new['MEN B2'],'.--b')
plt.plot( dfts['date'] , dfts_new['WOMEN B2'],'.--r')
plt.title('B2')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(437)
plt.plot( dfts['date'] , dfts['MEN B3'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN B3'],'.-r')
plt.plot( dfts['date'] , dfts_new['MEN B3'],'.--b')
plt.plot( dfts['date'] , dfts_new['WOMEN B3'],'.--r')
plt.title('B3')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(438)
plt.plot( dfts['date'] , dfts['MEN RP1'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN RP1'],'.-r')
plt.plot( dfts['date'] , dfts_new['MEN RP1'],'.--b')
plt.plot( dfts['date'] , dfts_new['WOMEN RP1'],'.--r')
plt.title('RP1')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(439)
plt.plot( dfts['date'] , dfts['MEN RP2'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN RP2'],'.-r')
plt.plot( dfts['date'] , dfts_new['MEN RP2'],'.--b')
plt.plot( dfts['date'] , dfts_new['WOMEN RP2'],'.--r')
plt.title('RP2')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(4,3,10)
plt.plot( dfts['date'] , dfts['MEN RP3'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN RP3'],'.-r')
plt.plot( dfts['date'] , dfts_new['MEN RP3'],'.--b')
plt.plot( dfts['date'] , dfts_new['WOMEN RP3'],'.--r')
plt.title('RP3')
plt.grid()
plt.ylim([0,25])
plt.ylabel('N athletes')

plt.subplot(4,3,11)
plt.plot( dfts['date'] , dfts['MEN'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN'],'.-r')
plt.plot( dfts['date'] , dfts_new['MEN'],'.--b')
plt.plot( dfts['date'] , dfts_new['WOMEN'],'.--r')
plt.title('Regular')
plt.grid()
plt.ylabel('N athletes')


plt.subplot(4,3,12)

ix_para1= dfts.columns.isin( ['MEN AU2','MEN AU1','MEN AL2','MEN AL1','MEN B1','MEN B2','MEN B3','MEN RP1','MEN RP2','MEN RP3'] )

ix_para2= dfts.columns.isin( ['WOMEN AU2','WOMEN AU1','WOMEN AL2','WOMEN AL1','WOMEN B1','WOMEN B2','WOMEN B3','WOMEN RP1','WOMEN RP2','WOMEN RP3'] )

plt.plot( dfts['date'] , dfts.iloc[:,ix_para1].sum(axis=1),'.-b')
plt.plot( dfts['date'] , dfts.iloc[:,ix_para2].sum(axis=1),'.-r')
plt.plot( dfts['date'] , dfts_new.iloc[:,ix_para1].sum(axis=1),'.--b')
plt.plot( dfts['date'] , dfts_new.iloc[:,ix_para2].sum(axis=1),'.--r')
plt.title('All para categories')
plt.grid()
plt.ylabel('N athletes')





plt.tight_layout()   
plt.draw()

# plt.savefig('athletes_per_year2.png',dpi=200)

# dfts.to_csv('athletes_per_year.csv')
    

#%%


plt.figure(3)
plt.clf()

plt.subplot(2,2,1)
plt.plot( dfts['date'] , dfts['MEN'],'.-b')
plt.plot( dfts['date'] , dfts['WOMEN'],'.-r')
plt.plot( dfts['date'] , dfts_new['MEN'],'.--b')
plt.plot( dfts['date'] , dfts_new['WOMEN'],'.--r')
plt.title('Regular')
plt.grid()
plt.ylabel('N athletes')
plt.xlabel('Year')


plt.subplot(2,2,3)

ix_para1= dfts.columns.isin( ['MEN AU2','MEN AU1','MEN AL2','MEN AL1','MEN B1','MEN B2','MEN B3','MEN RP1','MEN RP2','MEN RP3'] )

ix_para2= dfts.columns.isin( ['WOMEN AU2','WOMEN AU1','WOMEN AL2','WOMEN AL1','WOMEN B1','WOMEN B2','WOMEN B3','WOMEN RP1','WOMEN RP2','WOMEN RP3'] )

plt.plot( dfts['date'] , dfts.iloc[:,ix_para1].sum(axis=1),'.-b',label='Men')
plt.plot( dfts['date'] , dfts.iloc[:,ix_para2].sum(axis=1),'.-r',label='Women')
plt.plot( dfts['date'] , dfts_new.iloc[:,ix_para1].sum(axis=1),'.--b',label='Competed in previous year - Men')
plt.plot( dfts['date'] , dfts_new.iloc[:,ix_para2].sum(axis=1),'.--r',label='Competed in previous year - Women')
plt.title('Paraclimbing')
plt.grid()
plt.ylabel('N athletes')
plt.xlabel('Year')
plt.legend()




plt.subplot(2,2,2)
plt.plot( df_age['age'], df_age['MEN'],'.-b')
plt.plot( df_age['age'], df_age['WOMEN'],'.-r')
plt.title('Regular')
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')

plt.subplot(2,2,4)

ix_para= df_age.columns.isin( ['MEN AU2','MEN AU1','MEN AL2','MEN AL1','MEN B1','MEN B2','MEN B3','MEN RP1','MEN RP2','MEN RP3'] )
plt.plot( df_age['age'], df_age.iloc[:,ix_para].sum(axis=1)  ,'.-b')

ix_para= df_age.columns.isin( ['WOMEN AU2','WOMEN AU1','WOMEN AL2','WOMEN AL1','WOMEN B1','WOMEN B2','WOMEN B3','WOMEN RP1','WOMEN RP2','WOMEN RP3'] )
plt.plot( df_age['age'], df_age.iloc[:,ix_para].sum(axis=1)  ,'.-r')


plt.title('Paraclimbing')
plt.grid()
plt.xlabel('Age at competition')
plt.ylabel('count')

plt.tight_layout()   
plt.draw()

# plt.savefig('para_vs_regular.png',dpi=200)