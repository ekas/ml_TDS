# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:07:03 2017

@author: DELL1

Logic_API 'Automation'
"""
import re
import os
#from py2neo import neo4j, Graph
import json
import nltk
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request
from flask_restful import Api,Resource
from nltk.corpus import stopwords,wordnet
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

app = Flask(__name__)
api= Api(app)

corpus=[]
tokenizer = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words('english'))
corpus=[]
log={}


 
@api.resource('/')
class json_data(Resource):  
    def post(self):            
       global log 
       file_path="C:\\Users\\DELL1\\Desktop\\TDS Payable Assurance Tool - Logic Tool.xlsx"
       file_path2="C:\\Users\\DELL1\\Desktop\\Hackathon TDS payable assurance tool base data_3 November.xls"        
       x1=pd.ExcelFile(file_path)
       x2=pd.ExcelFile(file_path2)        
        
       # ap_dump=x1.parse('AP Dump',skiprows=0)
       #tds_returns=x2.parse('TDS Return_Data',skiprows=5)
       logic=x1.parse('Sheet1',skiprows = 6)
       logic.set_index('S. No.')
        
       des=logic['Similar to description of invoice']
       #Tds_head=logic['TDS Head']
       Hsn_head=logic['HSN Head']
       Hsn=logic['HSN code']
          
       for j in range(len(Hsn)):
          log[int(Hsn[j])] = (Hsn_head[j],des[j])

       print(log)
       return jsonify(log)
#api.app_resource('/',tag)  
if __name__ == '__main__':
    app.secret_key=os.urandom(24)
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port) 