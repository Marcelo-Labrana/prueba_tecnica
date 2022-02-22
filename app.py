from flask import Flask, render_template, request, jsonify
from numpy import False_
import pandas as pd
import csv
from logging import exception
import json
import sqlite3 as sql


output_csv = ""
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/menu', methods=['GET','POST'])
def menu():
    if request.method == 'POST':
        f = request.form['data']
        funcionData(f)
        
        
    return render_template('menu.html')

@app.route('/api/data', methods=['GET','POST'])
def data_test():
    global output_csv
    if request.method == 'POST':
        f = request.form['csvfile']
        with open(f) as file:
            new_csv = pd.read_csv(file, sep=";")
            new_data = [output_csv, new_csv]
            result = pd.concat(new_data)
            result.reset_index(drop=True, inplace=True)
            result = deleteRepeated(result)
            result.to_csv('output.csv',index=False,sep=';')
            print(result)
            output_csv = pd.read_csv('output.csv', sep=';')
            
        return render_template('post_data.html')
    elif request.method == 'GET':

        try:
            jdata = output_csv.to_json(orient="records", force_ascii=False)
            return jsonify(json.loads(jdata))
        except Exception:
            exception("[SERVER]: Error ->")
            return jsonify({"msg":"Ha ocurrido un error"}), 500

    

def funcionData(data_file):
    #con = sql.connect("data.db")
    con = sql.connect(data_file)
    instruccion = f"SELECT * FROM master_products_configurable"
    df = pd.read_sql_query(instruccion, con)
    configurable_variations = []
    for index, row in df.iterrows():
        configurable_variations.append('sku='+row['sku']+','+'color='+row['attribute_color'])
       
    df['configurable_variations'] = configurable_variations
    del df['sku']
    del df['attribute_color']

    df = deleteRepeated(df)
    print(df)
    f= open("output.csv","w+")
    f.close()
    df.to_csv('output.csv',index=False,sep=';')
    global output_csv
    output_csv = pd.read_csv('output.csv', sep=';')
    

def deleteRepeated(df):
    delete = []
    for index in df.index:
        if index not in delete:
            for index2 in df.index:    
                if index!=index2 and df.loc[index2,'model']==df.loc[index,'model'] and index2 not in delete:
                    delete.append(index2)
                    df.loc[index,'configurable_variations']+='|'+df.loc[index2,'configurable_variations']
    df = df.drop(delete,axis=0)
    df.reset_index(drop=True, inplace=True)
    
    return df

if __name__ == '__main__':
    app.run(debug=True)