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

## Virtual Environment
Install in bash  
```sudo apt-get update```  
```sudo apt-get install python3-venv```  
Create environment  
```python3 -m venv lending-library-env```  
Enter environment  
```source lending-library-env```  
Exit environment  
```deactivate```  
Help Menu  
```python3 -h venv```  
