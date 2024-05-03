from flask import request
from flask_restful import Resource,reqparse
from project.scripts.tclive import main
import json
import math

class TcliveResource(Resource):
    def get(self):
        try : 
            result=main("get")
            return{
                'status':"Success",
                "message":"",
                "data":result
            }
        except Exception as err : 
            return{
                'status':"Failed",
                "message":str(err),
                "data":None
            }

    def post(self):
        try:
            req_data=request.get_json()
            _type=req_data.get('type')
            domain=req_data.get('domain')
            if _type and domain : 
                if _type == "disable" : 
                    result=main("disable",domain)
                    return {
                        "status":"Success",
                        "message":f"{domain} is disabled.",
                        "data":None
                    }
                
                elif _type == "enable" : 
                    result=main("enable",domain)
                    return {
                        "status":"Success",
                        "message":f"{domain} is enabled.",
                        "data":None
                    }
            else : 
                return {
                    "status":"Failed",
                    "message":f"Please provide the correct type/domain.",
                    "data":None
                }

        except Exception as err : 
                return{
                    'status':"Failed",
                    "message":str(err),
                    "data":None
                }
