import json
import psycopg2
from flask import Flask, request
from flask_restful import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from flask import jsonify
import os

app = Flask(__name__)
api = Api(app)

Base = declarative_base()
database_url = "postgresql://postgres:1995@localhost:5432/postgres"

engine = create_engine(database_url, echo=True, poolclass=NullPool)

conn = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

class stdInfo(Base):
    __tablename__='std_info'
    nameS=Column('name',String)
    ageS=Column('age',Integer)
    mobileS=Column('mobile_no',Integer,primary_key=True)
    
##@app.route('/create_record',methods=['POST'])
##def std():
##    try:
##        request_body=request.get_json(force=True)
##        for item in request_body:
##            result=stdInfo(nameS==item.get("nameS"),
##                        mobileS=item.get("mobile_no"),
##                           ageS=item.get("age"))
##        session.add_all([result])
##        session.commit()
##        return{"status":"Sucess"}
##    except Exception as err:
##       session.rollback()
##       return {"status":"Failed"}
##app.run(debug=True)
                            
##@app.route('/update_std_info',methods=['PATCH'])
##def std():
##    update_age=request.args.get('age')
##    update_mobile=request.args.get('mobile_no')
##    session.query(stdInfo).filter(stdInfo.ageS==update_age).update({"mobileS":update_mobile})
##    session.commit()
##    return "sucessfully"
##app.run(debug=False)


##@app.route('/fetch_details',methods=['GET'])
##def std():
##    result=session.query(stdInfo).all()
##    proper_result=[item.__dict__ for item in result]
##    for item in proper_result:
##        del item['_sa_instance_state']
##    return json.dumps (proper_result)
##app.run()
       

##@app.route('/fetch_std_info',methods=['GET'])
##def abc():
##    result=session.query(stdInfo).all()
##    proper_result=[item.__dict__ for item in result]
##    for item in proper_result:
##        del item['_sa_instance_state']
##    return json.dumps(proper_result)
##app.run()




##
##@app.route('/fetch_std_info_details',methods=['PATCH'])
##def std_info():
##    update_ageS=request.args.get('age')
##    result=session.query(stdInfo).filter(stdInfo.ageS==update_ageS)
##    proper_result=[item.__dict__ for item in  result]
##    for item in proper_result:
##        del item['_sa_instance_state']
##    return json.dumps(proper_result)
##app.run(debug=False)
##    



##@app.route('/fetch_all_methods_data',methods=['GET'])
##def eee():
##    result=session.query(stdInfo).all()
##    properResult=[item.__dict__ for item in result]
##    for item in properResult:
##        del item['_sa_instance_state']
##    return json.dumps( properResult)
##app.run()


##
##@app.route('/get_std_info',methods=['GET'])
##def abc():
##    response=request.args.get('mobile_no')
##    result=session.query(stdInfo).filter(stdInfo.mobileS==response).all()
##    python_dict=[item.__dict__ for item in result]
##    for my_dict in python_dict:
##        del my_dict['_sa_instance_state']
##    return json.dumps(python_dict)
##        
##app.run(debug=False)


@app.route('/get_std_info',methods=['GET'])
def ABCD():
    request=request.args.get('mobile_mo')
    result=session.query(stdInfo).filter(stdInfo.mobileS==request).all()
    python_dict=[item.__dict__ for item in result]
    for my_dict in python_dict:
        del my_dict['_sa_instance_state']
    return json.dumps(python_dict)

app.run(debug=False)






















