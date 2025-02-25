from flask import Flask, json, redirect, flash, jsonify
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

########################
# Microservice IP and Port Configurations
########################
SERVER_ADDRESS = "127.0.0.1"
PORT_NUMBER = 8101


app = Flask(__name__)
db_connection = db.connect_to_database()

# CRUD Routes

# Create
@app.route("/add_experience", methods=['POST'])
def add_task():
    request_data = request.get_json()
    db_connection = db.connect_to_database()    
    rating = request_data['rating']
    details = request_data['details']
    image = request_data['image']
    userID = request_data['userID']
    # Null Handling
    if details == '' and image == '':
        query = 'INSERT INTO Experiences (rating, userID) VALUES (%s, %s)'
        db.execute_query(db_connection, query, (rating, userID))
    elif details == '':
        query= 'INSERT INTO Experiences (rating, userID, image) VALUES (%s, %s, %s)'
        db.execute_query(db_connection, query, (rating, userID, image))
    elif image == '':
        query='INSERT INTO Experiences (rating, userID, details) VALUES (%s, %s, %s)'
        db.execute_query(db_connection, query, (rating, userID, details))
    else:
        query='INSERT INTO Experiences (rating, userID, details, image) VALUES (%s, %s, %s, %s)'
        db.execute_query(db_connection, query, (rating, userID, details, image))
    return "Experience added to database"


# Read
@app.route("/experiences", methods=['GET'])
def retreive_all_experiences():
    db_connection = db.connect_to_database()
    query = 'SELECT * FROM Experiences'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return jsonify(results)

@app.route("/experiences/<int:experienceID>", methods=['GET'])
def retreive_one_experience(experienceID):
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Experiences WHERE experienceID = '%s';"
    cursor = db.execute_query(db_connection, query, (experienceID,))
    results = cursor.fetchall()
    return jsonify(results)

# Update
@app.route('/update_experience/<int:experienceID>', methods=['POST'])
def update_experience(experienceID):
    request_data = request.get_json()
    db_connection = db.connect_to_database()    
    rating = request_data['rating']
    details = request_data['details']
    image = request_data['image']
    userID = request_data['userID']
    if details == '' and image == '':
        query = 'UPDATE Experiences  SET Experiences.rating = %s, Experiences.userID = %s, Experiences.details = NULL, Experiences.image = NULL WHERE experienceID = %s'
        db.execute_query(db_connection, query, (rating, userID, experienceID))
    elif details == '':
        query = 'UPDATE Experiences  SET Experiences.rating = %s, Experiences.userID = %s, Experiences.details = NULL, Experiences.image = %s WHERE experienceID = %s'
        db.execute_query(db_connection, query, (rating, userID, image, experienceID))
    elif image == '':
        query = 'UPDATE Experiences  SET Experiences.rating = %s, Experiences.userID = %s, Experiences.details = %s, Experiences.image = NULL WHERE experienceID = %s'
        db.execute_query(db_connection, query, (rating, userID, details, experienceID))
    else:
        query = 'UPDATE Experiences  SET Experiences.rating = %s, Experiences.userID = %s, Experiences.details = %s, Experiences.image = %s WHERE experienceID = %s'
        db.execute_query(db_connection, query, (rating, userID, details, image, experienceID))
    return "Experience updated"
    

# Delete
@app.route('/delete_experience/<int:experienceID>', methods=['POST'])
def delete_experience(experienceID):
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Experiences WHERE experienceID = '%s';"
    cursor = db.execute_query(db_connection, query, (experienceID,))
    results = cursor.fetchall()
    if results == ():
        return jsonify({'error': 'Invalid experienceID'}), 400, {'Content-Type': 'application/json'}
    else:
        query = "DELETE FROM Experiences WHERE experienceID = '%s';"
        db.execute_query(db_connection, query, (experienceID,))
        return "Deleted experience"

# Listener
if __name__ == "__main__":
    app.run(host=SERVER_ADDRESS, port=PORT_NUMBER, debug=True)
