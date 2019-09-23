import flask
from flask import json, jsonify,request
import mysql.connector as Connection
app=flask.Flask(__name__)
app.config['DEBUG']=True
conn=Connection.connect(user='root',password='SPARCLab1',host='localhost',db='Airsense')

@app.route('/',methods=['GET'])
def home():
    return "Welcome to SPARCLab Airsense Server"
@app.route('/airsense/extended',methods=['GET'])
def Extended():
    curExte=conn.cursor()
    #return "ok"
    queryExe="SELECT NodeId,Time,CO,CO2,SO2,NO2,O3 FROM ExtendedData"
    
    curExte.execute(queryExe)
    valExten=curExte.fetchall()
    Extenlist=[]
    #return "{}".format(valExten)
    #return "ok"
    for row in valExten:
        #return "ok"
        airsensedata={
            
                "NodeId":row[0],
                "Time":row[1],
                "CO":row[2],
                "CO2":row[3],
                "SO2":row[4],
                "NO2":row[5],
                "O3":row[6]
            
        }
        Extenlist.append(airsensedata)
    #return jsonify(Extenlist)
    #JsonData=json.dumps(Extenlist)
    if 'NodeId' in request.args:
        #return "ok"
        NodeId=int(request.args['NodeId'])
    else:
        return jsonify(Extenlist)
    result=[]
    for dataextend in Extenlist:
        if dataextend['NodeId']==NodeId:
            result.append(dataextend)
    return jsonify(result)
@app.route('/airsense/data', methods=['GET'])
def data():
    #return "OK"
    curdata=conn.cursor()
    querydata="SELECT NodeId,Time,PM2p5,PM10,PM1,Temperature,Humidity FROM Data"
    dataall=[]
    curdata.execute(querydata)
    #return "{}".format(val)
    val=curdata.fetchall()
    for row in val:
        #return "ok"
        airsensedata={
               
                "Time":row[1],
                "PM2.5":row[2],
                "PM10":row[3],
                "PM1":row[4],
                "Tem":row[5],
                "Hum":row[6],
                "NodeId":row[0]
            
        }
        dataall.append(airsensedata)
    #return "okok"
    if 'NodeId'in request.args:
        NodeId=int(request.args['NodeId'])
    else: 
        return jsonify(dataall)
    #return type(request.arg['NodeId'])
    result=[]
    for intdata in dataall:
        if intdata['NodeId']==NodeId:
            result.append(intdata)
    return jsonify(result)

app.run(host='0.0.0.0',port=4000)
