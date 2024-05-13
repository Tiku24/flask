
from flask import Flask,request,jsonify
from db.create import createTables,createUser
from db.getUsers import getAllUsers,getSpecificUser
from db.updateOperation import updateUserAccess
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

port =int(os.getenv('PORT', 5000))

@app.route('/getSpecificUser',methods=['GET'])
def get_specific_user():
    userID = request.form['userID']
    return getSpecificUser(userId=userID)

@app.route("/getAllUsers",methods=['GET'])
def get_all_users():
    return getAllUsers()

@app.route("/createUser",methods=['POST'])
def create_user():
    name =request.form['name']
    password=request.form['password']
    email=request.form['email']
    address=request.form['address']
    phone=request.form['phone']
    pincode=request.form['pincode']
    dbres=createUser(name=name,Email=email,Address=address,Phone=phone,password=password,PinCode=pincode)
    if dbres==True:
        return jsonify({'success':'200','message':'Successfully created'})
    else:
        return jsonify({'failed':'400','message':'unable to create user'})
    

@app.route("/updateUser_Access",methods=['PATCH']) #for partial update
def update_user():
    userId=request.form['userID']
    approved=request.form['approved']
    blocked=request.form['blocked']
    updateUserAccess(id=userId,approved=approved,blocked=blocked)
    return "access updated successfully"

if __name__ == "__main__":
    createTables()
    app.run(port=port)
