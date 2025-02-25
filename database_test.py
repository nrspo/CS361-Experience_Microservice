import requests

url = 'http://127.0.0.1:8101'

#### Test 1: Create
""" print("Test 1:")
print("create experience")
request_form = {"rating": "5", "details":"", "image":"", "userID":"1"} # add requests include all table columns other than experienceID like an html form would, with blank fields as empty string: ""
database_update = requests.post("http://127.0.0.1:8101/add_experience", json=request_form)
print("test experience POSTed to database microservice") """


#### Test 2: Read All
""" print("Test 2: Read/Get All")
response = requests.get('http://127.0.0.1:8101/experiences')
print(response.json()) # response.json() is a list of jsons, each list element is a table row """


#### Test 3: Read One
print("Test 3: retrieve one experience with experienceID=1")
response = requests.get('http://127.0.0.1:8101/experiences/1') # "/experiences/<int:experienceID>"
print(response.json()) # response is still a list of a singular row, access the 0th element - validate for an empty list, which means no experiences returned for that ID

#### Test 4: Update
""" print("Test 4: Update: adding details to experience 1")
request_form = {"rating": "5", "details":"New details", "image":"", "userID":"1"}
requests.post("http://127.0.0.1:8101/update_experience/1", json=request_form) # request posted to /update_experience/<int:experienceID>

#display change for the test
response = requests.get('http://127.0.0.1:8101/experiences/1') # "/experiences/<int:experienceID>"
print(response.json()[0]) """

# Test 4 reset change
""" request_form = {"rating": "5", "details":"", "image":"", "userID":"1"}
requests.post("http://127.0.0.1:8101/update_experience/1", json=request_form) """

#### Test 5: Delete
""" print("Test 5: Deleting with bad ID")
database_update = requests.post("http://127.0.0.1:8101/delete_experience/1") # "/delete_experience/<int:experienceID>"
print("experienceID not found:", database_update)
# delete error handling: if the requested experienceID is not found, will receive an error code 400
 """