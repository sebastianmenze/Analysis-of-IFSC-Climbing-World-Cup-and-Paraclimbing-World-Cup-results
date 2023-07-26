# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:14:17 2023

@author: Administrator
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import glob 
import os
from scipy import stats

#%%






file=r"C:\Users\a5278\Documents\ifscanalysis\athlete_rankings\Sebastian MENZE.csv"

df=pd.read_csv(file,index_col=0)
df['date']=pd.to_datetime(df['date'])

ix_para=df['event'].str.contains('Paraclimbing')
df= df.loc[ix_para,:]

plt.figure(0)
plt.clf()

plt.plot( df['date'],df['rank'] ) 
plt.draw()


file=r"C:\Users\a5278\Documents\ifscanalysis\athlete_rankings\Tomoa NARASAKI.csv"



df=pd.read_csv(file,index_col=0)
df['date']=pd.to_datetime(df['date'])

ix= df['event'].str.contains('World') & ~df['event'].str.contains('Paraclimbing')
df= df.loc[ix,:]


plt.figure(0)
plt.clf()

plt.plot( df['date'],df['rank'] ) 
plt.draw()


slope, intercept, r, p, std_err = stats.linregress(  df['date'].values .astype(float)     ,df['rank'].values)


coeffs = np.polyfit(df['date'].values,df['rank'].values,1)
slope = coeffs[-2]

#%% para world

filelist = glob.glob(r'C:\Users\a5278\Documents\ifscanalysis\athlete_rankings\*.csv')





filelist = glob.glob(r'C:\Users\a5278\Documents\ifscanalysis\athlete_rankings\*.csv')



eventlist=pd.DataFrame([])


for file in filelist:
    
    
    
    df=pd.read_csv(file,index_col=0)
    df['date']=pd.to_datetime(df['date'])
    
    ix_para=df['event'].str.contains('Paraclimbing')
    
    df= df.loc[ix_para,:]
    
    if len(df)>0:

        events = pd.Series( (df['event']+df['para_class'] ).unique() )
        eventlist = pd.concat( [eventlist,events ])
  
        
eventlist= eventlist.reset_index(drop=True)

df_event=pd.DataFrame([])
df_event['name'] = eventlist[0].unique()

i=0
for e in df_event['name'] :
    n = np.sum(eventlist[0]==e)
    df_event.loc[i,'n']=n
    i=i+1

name=[]
mean=[]
std=[]
cat=[]
mean_norm=[]
std_norm =[]
slop=[]

for file in filelist:
    
    
    
    df=pd.read_csv(file,index_col=0)
    df['date']=pd.to_datetime(df['date'])
    
    ix_para=df['event'].str.contains('Paraclimbing')
    
    df= df.loc[ix_para,:]
    df=df.reset_index(drop=True)
    
    events = pd.Series( (df['event']+df['para_class'] ).unique() )
    for k in range(len(df)):
        ixe = events[k] ==df_event['name']
        n= df_event.loc[ixe,'n']
        
        df.loc[k,'rank_norm']= df.loc[k,'rank'] /n.values


    if len(df)>4:
    
        name.append( os.path.basename(file)    )
        mean.append( df['rank'].mean()   )
        std.append( df['rank'].std()     )

        mean_norm.append( df['rank_norm'].mean()   )
        std_norm.append( df['rank_norm'].std()   )
        
        slope, intercept, r, p, std_err = stats.linregress(  df['date'].values .astype(float)     ,df['rank_norm'].values)
        slop.append( slope    )

        
        cat.append( df.loc[0,'para_class']    )

    
    

ifsc_para = pd.DataFrame([])
ifsc_para['name']=name
ifsc_para['mean']=mean
ifsc_para['std']=std
ifsc_para['cat']=cat
ifsc_para['mean_norm']=mean_norm
ifsc_para['std_norm']=std_norm
ifsc_para['slope']=slop



#%% wold normal



filelist = glob.glob(r'C:\Users\a5278\Documents\ifscanalysis\athlete_rankings\*.csv')



eventlist=pd.DataFrame([])


for file in filelist:
    
    
    
    df=pd.read_csv(file,index_col=0)
    df['date']=pd.to_datetime(df['date'])
    
    ix= df['event'].str.contains('World') & ~df['event'].str.contains('Paraclimbing')  & ~df['event'].str.contains('Youth')
    
    df= df.loc[ix,:]
    
    if len(df)>0:

        events = pd.Series( (df['event']+df['para_class'] ).unique() )
        eventlist = pd.concat( [eventlist,events ])
  
        
eventlist= eventlist.reset_index(drop=True)

df_event=pd.DataFrame([])
df_event['name'] = eventlist[0].unique()

i=0
for e in df_event['name'] :
    n = np.sum(eventlist[0]==e)
    df_event.loc[i,'n']=n
    i=i+1

name=[]
mean=[]
std=[]
cat=[]
mean_norm=[]
std_norm =[]
slop=[]



for file in filelist:
    
    
    
    df=pd.read_csv(file,index_col=0)
    df['date']=pd.to_datetime(df['date'])

    ix= df['event'].str.contains('World') & ~df['event'].str.contains('Paraclimbing')  & ~df['event'].str.contains('Youth')
    df= df.loc[ix,:]
    
    ix= df['date']>pd.Timestamp(2000,1,1)
    df= df.loc[ix,:]
    
    df=df.reset_index(drop=True)
    
    events = pd.Series( (df['event']+df['para_class'] ).unique() )
    for k in range(len(df)):
        try:
            ixe = events[k] ==df_event['name']
            n= df_event.loc[ixe,'n']
            df.loc[k,'rank_norm']= df.loc[k,'rank'] /n.values

        except:
            df.loc[k,'rank_norm']= np.nan

    
    if len(df)>4:
    
        name.append( os.path.basename(file)    )
        mean.append( df['rank'].mean()   )
        std.append( df['rank'].std()     )
        cat.append( df.loc[0,'para_class']    )
    
        mean_norm.append( df['rank_norm'].mean()   )
        std_norm.append( df['rank_norm'].std()   )
        slope, intercept, r, p, std_err = stats.linregress(  df['date'].values .astype(float)     ,df['rank_norm'].values)
        slop.append( slope    )       

ifsc_norm = pd.DataFrame([])
ifsc_norm['name']=name
ifsc_norm['mean']=mean
ifsc_norm['std']=std
ifsc_norm['cat']=cat
ifsc_norm['mean_norm']=mean_norm
ifsc_norm['std_norm']=std_norm
ifsc_norm['slope']=slop




#%% rank by cat




cats= ifsc_norm['cat'].unique()
c=cats[0]
for c in cats:
    ix = ifsc_norm['cat']==c
    x=   ifsc_norm.loc[ix,'mean']
    x= x / x.mean()
    ifsc_norm.loc[ix,'mean_norm2']=x

    x=   ifsc_norm.loc[ix,'std']
    x= x / x.mean()
    ifsc_norm.loc[ix,'std_norm2']=x
    

cats= ifsc_para['cat'].unique()
c=cats[0]
for c in cats:
    ix = ifsc_para['cat']==c
    
    x=   ifsc_para.loc[ix,'mean']
    x= x / x.mean()
    ifsc_para.loc[ix,'mean_norm2']=x

    x=   ifsc_para.loc[ix,'std']
    x= x / x.mean()
    ifsc_para.loc[ix,'std_norm2']=x
    

    
    
#%%



plt.figure(1)
plt.clf()

plt.hist2d(ifsc_para['mean_norm'],ifsc_para['std_norm'],20 )
plt.plot(ifsc_para['mean_norm'],ifsc_para['std_norm'],'.k' )

# for i in range(len(mean)):
#     plt.annotate(name[i], (mean[i],std[i]))


plt.draw()



plt.figure(2)
plt.clf()

plt.hist2d(ifsc_norm['mean_norm'],ifsc_norm['std_norm'],20 )
plt.plot(ifsc_norm['mean_norm'],ifsc_norm['std_norm'],'.k' )

# for i in range(len(mean)):
#     plt.annotate(name[i], (mean[i],std[i]))


plt.draw()

#%%
plt.figure(4)
plt.clf()

plt.plot(ifsc_para['mean_norm'],ifsc_para['std_norm'],'.b' )
plt.plot(ifsc_norm['mean_norm'],ifsc_norm['std_norm'],'.r' )

for i in range(len(ifsc_para)):
    plt.annotate(ifsc_para.loc[i,'name'], ( ifsc_para.loc[i,'mean_norm'], ifsc_para.loc[i,'std_norm'] )  )


for i in range(len(ifsc_norm)):
    plt.annotate(ifsc_norm.loc[i,'name'], ( ifsc_norm.loc[i,'mean_norm'], ifsc_norm.loc[i,'std_norm'] )  )


plt.draw()


#%%

plt.figure(5)
plt.clf()

x=ifsc_norm['mean_norm']
y=ifsc_norm['std_norm']

x[x>100]=np.nan
y[y>100]=np.nan

# x= (x-x.min()) / (x.max()-x.min())
# y= (y-y.min()) / (y.max()-y.min())
plt.plot(x,y,'.r' ,label='Normal')

# for i in range(len(ifsc_norm)):
#     plt.annotate(ifsc_norm.loc[i,'name'], (x[i],y[i]))


ixme = ifsc_norm['name'] =='Adam ONDRA.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.r',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_norm.loc[i,'name'], (x[i],y[i])  )



ixme = ifsc_norm['name'] =='Janja GARNBRET.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.r',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_norm.loc[i,'name'], (x[i],y[i])  )

x=ifsc_para['mean_norm']
y=ifsc_para['std_norm']

# x= (x-x.min()) / (x.max()-x.min())
# y= (y-y.min()) / (y.max()-y.min())
plt.plot(x,y,'.b' ,label='Paraclimbing')
# for i in range(len(ifsc_para)):
#     plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i]))

ixme = ifsc_para['name'] =='Sebastian MENZE.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )


# ixme = ifsc_para['name'] =='Isak RIPMAN.csv'
# plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
# i=  np.where( ixme.values )[0][0]
# plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )


# ixme = ifsc_para['name'] =='Dina EIVIK.csv'
# plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
# i=  np.where( ixme.values )[0][0]
# plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )

ixme = ifsc_para['name'] =='Thierry DELARUE.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )


ixme = ifsc_para['name'] =='Solenne PIRET.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )


plt.legend()
plt.grid()
plt.xlabel('Normalized mean World cup result per category')
plt.ylabel('Normalized standard deviation of World cup results per category')
plt.draw()

# plt.savefig('ifsc_worldup_result_analysis_comp.png')

#%%



plt.figure(6)
plt.clf()

# x=ifsc_norm['mean_norm']
# y=ifsc_norm['std_norm']

# x[x>100]=np.nan
# y[y>100]=np.nan

# # x= (x-x.min()) / (x.max()-x.min())
# # y= (y-y.min()) / (y.max()-y.min())
# plt.plot(x,y,'.r' ,label='Normal')

# # for i in range(len(ifsc_norm)):
# #     plt.annotate(ifsc_norm.loc[i,'name'], (x[i],y[i]))


# ixme = ifsc_norm['name'] =='Adam ONDRA.csv'
# plt.plot( x[ixme.values]  ,y[ixme.values],'.r',markersize=30 )
# i=  np.where( ixme.values )[0][0]
# plt.annotate(ifsc_norm.loc[i,'name'], (x[i],y[i])  )



# ixme = ifsc_norm['name'] =='Janja GARNBRET.csv'
# plt.plot( x[ixme.values]  ,y[ixme.values],'.r',markersize=30 )
# i=  np.where( ixme.values )[0][0]
# plt.annotate(ifsc_norm.loc[i,'name'], (x[i],y[i])  )

x=ifsc_para['mean_norm']
y=ifsc_para['std_norm']

# x= (x-x.min()) / (x.max()-x.min())
# y= (y-y.min()) / (y.max()-y.min())
plt.plot(x,y,'.b' ,label='Paraclimbing')
# for i in range(len(ifsc_para)):
#     plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i]))

ixme = ifsc_para['name'] =='Sebastian MENZE.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )


ixme = ifsc_para['name'] =='Isak RIPMAN.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )


ixme = ifsc_para['name'] =='Dina EIVIK.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )

ixme = ifsc_para['name'] =='Thierry DELARUE.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )


ixme = ifsc_para['name'] =='Solenne PIRET.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )


plt.legend()

plt.xlabel('Normalized mean World cup result per category')
plt.ylabel('Normalized standard deviation of World cup results per category')
plt.draw()

# plt.savefig('ifsc_worldup_result_analysis_norm.png')




#%%
plt.figure(6)
plt.clf()

x=ifsc_norm['mean']
y=ifsc_norm['std']

x[x>100]=np.nan
y[y>100]=np.nan

x= (x-x.min()) / (x.max()-x.min())
y= (y-y.min()) / (y.max()-y.min())
plt.plot(x,y,'.r' ,label='Normal')

# for i in range(len(ifsc_norm)):
#     plt.annotate(ifsc_norm.loc[i,'name'], (x[i],y[i]))


ixme = ifsc_norm['name'] =='Adam ONDRA.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.r',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_norm.loc[i,'name'], (x[i],y[i])  )



ixme = ifsc_norm['name'] =='Janja GARNBRET.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.r',markersize=30 )
i=  np.where( ixme.values )[0][0]
# plt.annotate(ifsc_norm.loc[i,'name'], (x[i],y[i])  )

x=ifsc_para['mean']
y=ifsc_para['std']

x= (x-x.min()) / (x.max()-x.min())
y= (y-y.min()) / (y.max()-y.min())
plt.plot(x,y,'.b' ,label='Paraclimbing')
# for i in range(len(ifsc_para)):
#     plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i]))

ixme = ifsc_para['name'] =='Sebastian MENZE.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )


ixme = ifsc_para['name'] =='Isak RIPMAN.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )


ixme = ifsc_para['name'] =='Dina EIVIK.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )

ixme = ifsc_para['name'] =='Thierry DELARUE.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )


ixme = ifsc_para['name'] =='Solenne PIRET.csv'
plt.plot( x[ixme.values]  ,y[ixme.values],'.b',markersize=30 )
i=  np.where( ixme.values )[0][0]
plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i])  )


plt.legend()

plt.xlabel('Normalized mean World cup result')
plt.ylabel('Normalized standard deviation of World cup results')
plt.draw()

# plt.savefig('ifsc_worldup_result_analysis.png')


#%%
plt.figure(5)
plt.clf()

x=ifsc_para['mean']
y=ifsc_para['std']

x= (x-x.min()) / (x.max()-x.min())
y= (y-y.min()) / (y.max()-y.min())
plt.plot(x,y,'.b' )
for i in range(len(ifsc_para)):
    plt.annotate(ifsc_para.loc[i,'name'], (x[i],y[i]))


x=ifsc_norm['mean']
y=ifsc_norm['std']

x[x>100]=np.nan
y[y>100]=np.nan

x= (x-x.min()) / (x.max()-x.min())
y= (y-y.min()) / (y.max()-y.min())
plt.plot(x,y,'.r' )

for i in range(len(ifsc_norm)):
    plt.annotate(ifsc_norm.loc[i,'name'], (x[i],y[i]))


plt.draw()

#%%


plt.figure(4)
plt.clf()

plt.scatter(ifsc_para['mean_norm'],ifsc_para['std_norm'],40, ifsc_para['slope'],cmap='coolwarm',vmin=-.5e-17,vmax=.5e-17)
plt.colorbar()

for i in range(len(ifsc_para)):
    plt.annotate(ifsc_para.loc[i,'name'], ( ifsc_para.loc[i,'mean_norm'], ifsc_para.loc[i,'std_norm'] )  )


# for i in range(len(ifsc_norm)):
#     plt.annotate(ifsc_norm.loc[i,'name'], ( ifsc_norm.loc[i,'mean_norm'], ifsc_norm.loc[i,'std_norm'] )  )

plt.xlabel('Normalized mean World cup result')
plt.ylabel('Normalized standard deviation of World cup results')
plt.grid()

plt.draw()

# plt.savefig('ifsc_worldup_result_analysis_trendpara.png')


#%%

plt.figure(5)
plt.clf()

plt.scatter(ifsc_norm['mean_norm'],ifsc_norm['std_norm'],40, ifsc_norm['slope'],cmap='coolwarm',vmin=-.5e-17,vmax=.5e-17)
plt.colorbar()


# for i in range(len(ifsc_norm)):
#     plt.annotate(ifsc_norm.loc[i,'name'], ( ifsc_norm.loc[i,'mean_norm'], ifsc_norm.loc[i,'std_norm'] )  )
# 


plt.xlabel('Normalized mean World cup result')
plt.ylabel('Normalized standard deviation of World cup results')
plt.grid()

plt.draw()

# plt.savefig('ifsc_worldup_result_analysis_trendnormo.png')


#%%

plt.figure(6)
plt.clf()

plt.scatter(ifsc_norm['mean_norm'],ifsc_norm['slope'],40, ifsc_norm['std_norm'],cmap='plasma') #,vmin=-.1,vmax=.1)
# plt.colorbar()

plt.scatter(ifsc_para['mean_norm'],ifsc_para['slope'],40, ifsc_para['std_norm'],cmap='plasma') #,vmin=-.1,vmax=.1)
plt.colorbar()

# for i in range(len(ifsc_para)):
#     plt.annotate(ifsc_para.loc[i,'name'], ( ifsc_para.loc[i,'mean_norm'], ifsc_para.loc[i,'std_norm'] )  )


plt.draw()

# plt.savefig('ifsc_worldup_result_analysis_trendpara.png')


#%%

ifsc_norm['slope'].mean()
ifsc_para['slope'].mean()

plt.figure(7)
plt.clf()

plt.subplot(211)

plt.hist( ifsc_norm['slope'],100 )
plt.grid()
plt.title('mean slope: '+str(ifsc_norm['slope'].mean() ))

plt.subplot(212)

plt.hist( ifsc_para['slope'],100 )
plt.grid()
plt.title('mean slope: '+str(ifsc_para['slope'].mean() ))

plt.tight_layout()
plt.draw()

# plt.savefig('ifsc_worldup_result_analysis_trend_hist.png')

#%%




filelist = glob.glob(r'C:\Users\a5278\Documents\ifscanalysis\athlete_rankings\*.csv')



eventlist=pd.DataFrame([])


for file in filelist:
    
    
    
    df=pd.read_csv(file,index_col=0)
    df['date']=pd.to_datetime(df['date'])
    
    ix_para=df['event'].str.contains('Paraclimbing')
    
    df= df.loc[ix_para,:]
    
    if len(df)>0:

        events = pd.Series( (df['event']+df['para_class'] ).unique() )
        eventlist = pd.concat( [eventlist,events ])
  
        
eventlist= eventlist.reset_index(drop=True)

df_event=pd.DataFrame([])
df_event['name'] = eventlist[0].unique()

i=0
for e in df_event['name'] :
    n = np.sum(eventlist[0]==e)
    df_event.loc[i,'n']=n
    i=i+1

name=[]
mean=[]
std=[]
cat=[]
mean_norm=[]
std_norm =[]
slop=[]

athlet_list=[]

for file in filelist:
    
    
    
    df=pd.read_csv(file,index_col=0)
    df['date']=pd.to_datetime(df['date'])
    
    ix_para=df['event'].str.contains('Paraclimbing')
    
    df= df.loc[ix_para,:]
    df=df.reset_index(drop=True)
    
    events = pd.Series( (df['event']+df['para_class'] ).unique() )
    for k in range(len(df)):
        ixe = events[k] ==df_event['name']
        n= df_event.loc[ixe,'n']
        
        df.loc[k,'rank_norm']= df.loc[k,'rank'] /n.values

    if len(df)>1:
        athlet_list.append(df)
    
    if len(df)>4:
    
        name.append( os.path.basename(file)    )
        mean.append( df['rank'].mean()   )
        std.append( df['rank'].std()     )

        mean_norm.append( df['rank_norm'].mean()   )
        std_norm.append( df['rank_norm'].std()   )
        
        slope, intercept, r, p, std_err = stats.linregress(  df['date'].values .astype(float)     ,df['rank_norm'].values)
        slop.append( slope    )

        
        cat.append( df.loc[0,'para_class']    )

    
    

ifsc_para = pd.DataFrame([])
ifsc_para['name']=name
ifsc_para['mean']=mean
ifsc_para['std']=std
ifsc_para['cat']=cat
ifsc_para['mean_norm']=mean_norm
ifsc_para['std_norm']=std_norm
ifsc_para['slope']=slop

#%%


plt.figure(8)
plt.clf()

for a in athlet_list:
    
    
    plt.plot( a['date'] , a['rank_norm'] )
    

plt.plot( a['date'] , a['rank_norm'] )

    
plt.draw()

#%%

# ifsc_para.to_csv('world_cup_stats_para.csv')
# ifsc_norm.to_csv('world_cup_stats_norm.csv')

