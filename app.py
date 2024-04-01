from flask import Flask
import sys
import os


#importing logger from housing folder
from housing.logger import logging

#importing exception from housing folder
from housing.exception import HousingException

app=Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        

    
        logging.info("lets testing logging info.")
    return "hello"




if __name__=="__main__":
    app.run(debug=True)