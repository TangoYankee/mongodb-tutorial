## Requirements
*Recommend initializing [virtual environment](#virtual-environment) first*  
```pip install -r requirements.txt```
### Flask
The Python web microframework: [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)  
```flask run```  
To run in development mode  
```export FLASK_ENV=development``` 

### MongoDB
NoSQL Database: [Install for Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)  
```service mongod start/status/stop```

### PyMongo
The recommended way to work with MongoDB from Python: [PyMongo Documentation](https://docs.mongodb.com/ecosystem/drivers/pymongo/)
https://flask-pymongo.readthedocs.io/en/latest/


## Virtual Environment
Create environment  
```python3 -m venv api-env```  
Enter environment  
```source api-env/bin/activate```  
Exit environment  
```deactivate```  
Help Menu  
```python3 -h venv```  

## Setup
```
source config-dev.sh
pip install -e .
```

## Run
```python run.py```
