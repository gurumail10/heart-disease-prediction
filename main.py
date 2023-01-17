#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 22:04:28 2021

@author: test
"""

import streamlit as st
import joblib

import numpy as np
import pandas as pd
import shap
#import plotly.graph_objects as go
import base64



#st.subheader('Raw data')
st.header("Heart Disease Prediction :")
st.image("im3.jpg",width=300)
st.write("Heart disease occurs mostly after the age of 30 mainly because of some factors such as rate of calcium in our body, poor diet, stretching of blood vessels of the heart, blood pressure, sex, cholesterol problem and lack of proper exercise is also a common problem for heart disease. Heart disease also can be prevented if it can be detected during the early phases. This system helps you to find out the chances of occurrence of heart disease.")

#if st.button('Get Test'):
st.write("Enter Feature Values:")




height=float(st.number_input('Enter Height in metres',min_value=0.5))
weight=float(st.number_input('Enter weight in kg',min_value=5))
BMI=weight/(height)**2
sex = st.radio(
        'Sex',
        ('Select a value',"Male","Female"),index=0)
    
    
CurrentSmoker = st.radio(
        'Current Smoker',
        ('Select a value',"Yes","No"))


    
    
EXSmoker = st.radio(
        'EX-Smoker',
        ('Select a value',"Yes","No"))



chestpain = st.radio(
        'Typical Chest Pain',
        ('Select a value',"Yes","No"))



A_typical = st.radio(
        'Atypical',
        ('Select a value',"Yes","No"))
        


Non_anginal = st.radio(
        'Nonanginal',
        ('Select a value',"Yes","No"))

    
F_H = st.radio(
        'Family History',
        ('Select a value',"Yes","No"))

#VHD = st.sidebar.radio(
 #       'VHD',
 #       ("No","mild","Moderate","Severe"))

#DiastolicMurmur = st.sidebar.radio(
#        'Diastolic Murmur',
 #       ("Yes","No"))
#if DiastolicMurmur=='Yes':
#    Diastolic_Murmur=1
#else:
#    Diastolic_Murmur=0

Age = st.slider('Age')

#BMI=st.slider(
#    'BMI-Body Mass Index in Kg/m2',
#    0.0, 50.0
#)

fbs=st.slider(
    'FBS-Fasting Blood Sugar in mg.dL',
   50.0, 500.0
)
#TG=st.sidebar.slider(
#    'TG',
#    30.0, 1200.0
#)

#Lymph=st.sidebar.slider(
#    'Lymph',
#    0.0, 100.0
#)



PR=st.slider(
    'PR - Pulse Rate in ppm',
    0.0, 200.0
)



BP=st.slider(
    'BP-Blood Pressure mm in Hg',
    50.0, 200.0
)



#HB=st.sidebar.slider(
#    'HB',
#    0.0, 20.0
#)
if CurrentSmoker=='Yes':
        Current_Smoker=1
else:
        Current_Smoker=0    
        
if EXSmoker=='Yes':
        EX_Smoker=1
else:
        EX_Smoker=0   
    
if chestpain=='Yes':
        chest_pain=1
else:
        chest_pain=0
if A_typical=='Yes':
        Atypical=1
else:
        Atypical=0
if Non_anginal=='Yes':
        Nonanginal=1
else:
        Nonanginal=0
if F_H=='Yes':
        FH=1
else:
        FH=0
if sex=='Male':
        Sex=1
else:
        Sex=0

def get_recommend(final_df):
    recom_list=[]
    for col in final_df.features.values:
        if col in ['Typical Chest Pain','Sex','Age','FH','EX-Smoker']:
            recom_list.append('')
        
        elif col=='Atypical':
            if final_df[final_df.features==col]['Actual Values'].values[0] =='Yes':
                recom_list.append('Atypical Chest Pain')
            else:
                recom_list.append('')
        elif col=='Nonanginal':
            if final_df[final_df.features==col]['Actual Values'].values[0] =='Yes':
                recom_list.append('Nonanginal')
            else:
                recom_list.append('')
        elif col=='Current Smoker':
            if final_df[final_df.features==col]['Actual Values'].values[0] =='Yes':
                recom_list.append('Quit smoking to lower the chances of getting heart disease as it affects the pulse rate.')
            else:
                recom_list.append('')
                
            
        elif col=='FBS':
            if final_df[final_df.features==col]['Actual Values'].values[0] < 62:
                recom_list.append('Person has Low FBS')
                
            elif final_df[final_df.features==col]['Actual Values'].values[0]>=100 and final_df[final_df.features==col]['Actual Values'].values[0]<=125:
                recom_list.append('Indicates you have prediabetes, follow healthy food habits to keep the FBS range in control. Normal FBS range is below 99')
                
            elif final_df[final_df.features==col]['Actual Values'].values[0]>126:
                recom_list.append('Indicates you have diabetes, undergo frequent check-up of the FBS and follow healthy food habits, proper medication to keep the FBS levels in control.')
            else:
                recom_list.append('')
                #recom_list.append('Person has Normal FBS')
        
        elif col=='PR':
            if final_df[final_df.features==col]['Actual Values'].values[0]<50:
                recom_list.append('Person has Low Pulse Rate')
                
            elif final_df[final_df.features==col]['Actual Values'].values[0]>100:
                recom_list.append('Exercise is the number one way to lower pulse rate. Regular exercises, maintaining healthy weight, staying hydrated, sleeping well and managing stress would help to keep your pulse rate within normal range (60-100).')
            else:
                recom_list.append('')
                #recom_list.append('Person has Normal Pulse Rate')
        elif col=='BP':
            if final_df[final_df.features==col]['Actual Values'].values[0]<90:
                recom_list.append('Person has Low Blood Pressure')
                
            elif final_df[final_df.features==col]['Actual Values'].values[0]>=140:
                recom_list.append('Person has Hypertension')
                
            elif final_df[final_df.features==col]['Actual Values'].values[0]>120 and final_df[final_df.features==col]['Actual Values'].values[0]<=139:
                recom_list.append('Person has Pre-Hypertension')
            
            else:
                recom_list.append('')
                #recom_list.append('Person has Normal Blood Pressure')
                
        elif col=='BMI':
            if final_df[final_df.features==col]['Actual Values'].values[0]<18.5:
                recom_list.append('Person has Low BMI i.e- Underweight ')
                
            elif final_df[final_df.features==col]['Actual Values'].values[0]>=18.5 and final_df[final_df.features==col]['Actual Values'].values[0]<24.9:
                recom_list.append('')
               # recom_list.append('Person has Normal BMI')
            
            elif final_df[final_df.features==col]['Actual Values'].values[0]>=25 and final_df[final_df.features==col]['Actual Values'].values[0]<29.9:
                recom_list.append('Person has High BMI i.e - Overweight')
            else:
                recom_list.append('Person has very high BMI i.e - Obese')
    #final_df['Recommendations']=recom_list
    return recom_list
                
            
                    
if st.button('Get Prediction'):                   
    
    #values=[chest_pain,Atypical,Nonanginal,fbs,TG,Lymph,Age,PR,Diastolic_Murmur,BP,HB,Sex,Current_Smoker,EX_Smoker,BMI,FH]
    
    #values2=[chestpain,A_typical,Non_anginal,fbs,TG,Lymph,Age,PR,DiastolicMurmur,BP,HB,sex,CurrentSmoker,EXSmoker,BMI,F_H]
    
    values=[chest_pain,Atypical,Nonanginal,fbs,Age,PR,BP,Sex,Current_Smoker,EX_Smoker,BMI,FH]
    values2=[chestpain,A_typical,Non_anginal,fbs,Age,PR,BP,sex,CurrentSmoker,EXSmoker,BMI,F_H]
    val=np.array(values)
    
    col_list=['Typical Chest Pain', 'Atypical', 'Nonanginal', 'FBS', 'Age', 'PR',
           'BP', 'Sex', 'Current Smoker', 'EX-Smoker', 'BMI', 'FH']
    
    df=pd.DataFrame.from_dict({'Typical Chest Pain': "",
     'Atypical': "",
     'Nonanginal': '',
     'FBS':" < 100",
     #'TG': "< 150",
    # 'Lymph': "10-48",
     'Age': "0-100",
    
     'PR': "60-100",
    # 'Diastolic Murmur': '',
     'BP': "< 120",
     
     'HB': "Male: 13.8 to 17.2 g/dL Female: 12.1 to 15.1 g/dL",
     'Sex': "",
     'Current Smoker': '',
     'EX-Smoker': '',
     'BMI': 'Underweight: <18.5 Normal: 18.5-24.9 Overweight:25-29.9 Obese:>30',
     'FH': ''}.items())
    df.columns=['features','Normal Range']
    
#if st.button('Predict'):
    loaded_rf = joblib.load("final_rf_model.joblib")
    pred=loaded_rf.predict(val.reshape(1,-1))[0]
    pred_prob=loaded_rf.predict_proba(val.reshape(1,-1))[0]
    dct={}
    dct['Normal']=pred_prob[1]
    dct['Cad']=pred_prob[0]
    
    st.write("Prediction is:-  ",pred," , With probability :- ",dct[pred])
    #
  
    explainer = shap.TreeExplainer(loaded_rf)
    shap_values = explainer.shap_values(val.reshape(1,-1))
    
    #shap_values=pd.DataFrame(shap_values[0])
   
    shap_values=pd.DataFrame(shap_values[0][0],columns=['Shap Values'])
    shap_values['features']=col_list
    shap_values['Actual Values']=values2
    #final_df=pd.merge(shap_values,df,how='left',left_on='features',right_on='features')[['features','Shap Values','Actual Values','Normal Range']]
    final_df=shap_values.copy()
    
    
    final_df.loc[final_df['Shap Values']>0,'Contribution']='Cad'
    
    final_df.loc[final_df['Shap Values']<=0,'Contribution']='Normal'
    
    import plotly.express as px
  #  df = px.data.tips()
    fig = px.bar(final_df, x="Shap Values", y="features", color='Contribution', orientation='h',
             
             
             title='Feature Contribution towards disease')
    #st.plotly_chart(fig)
    
  
    st.subheader("Features that are contributing towards Disease:- ")
    #st.write(final_df[final_df['Shap Values']>0].sort_values('Shap Values',ascending=False))
    a=final_df[final_df['Shap Values']>0]
    recom=get_recommend(a)
    st.write('Recommendation:- ')
    count=1
    for i in recom:
        if i!='':
            st.write(count,'.',i)
            count +=1
   # st.subheader("Features that are contributing towards Normal:- ")
   # st.write(final_df[final_df['Shap Values']<=0].sort_values('Shap Values',ascending=True))
    #st.write(shap_values[shap_values['Shap Values']<=0].sort_values('Shap Values',ascending=True))
    a=final_df[final_df['Shap Values']<0]
    recom=get_recommend(a)
    #st.write('Recommendation:- ')
    count=1
    for i in recom:
        if i!='':
           # st.write(count,'.',i)
            count +=1


    
   
    
    
    
    
    
    






















