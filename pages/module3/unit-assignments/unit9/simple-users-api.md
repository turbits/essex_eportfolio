---
layout: page
permalink: /pages/module3/unit-assignments/unit9/simple-users-api.html
---

⬅️[Back](/pages/module3/unit-assignments/unit9/m3u9.html)

# Unit 9: Developing an API for a Distributed Environment: Simple Users API Endpoint In Flask

A simple API for a /users endpoint in place of a discussion piece for Unit 9.


```python
from flask import Flask, jsonify, request, abort

# this simple app/api could be extended significantly, such as:
#   - adding IP restriction with Flask's 'before_request' decorator
#   - adding try/except blocks
#   - adding sanitization
#   - adding encryption and decryption
#   - etc.


app = Flask(__name__)

# a set of example users; this would generally be stored in a DB and retrieved in each endpoint
users = [
    { "id": 1, "name": "John Wick"},
    { "id": 2, "name": "Galadriel"},
    { "id": 3, "name": "Rebecca"}
]


@app.route('/users', methods=['GET'])
def get_users():
    # return the list of users
    return jsonify(users)


@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id():
    # check if the request is valid
    user = [user for user in users if user['id'] == id]
    if len(user) == 0:
        abort(404)
    # return the user
    return jsonify({'user': user[0]})


@app.route('/users', methods=['POST'])
def create_user():
    # check if the request is valid
    if not request.json or 'name' not in request.json:
        abort(400)
    user = {
        # get the last id and add 1
        'id': users[-1]['id'] + 1,
        # get the name from the request
        'name': request.json['name'],
    }
    # add the user to the list
    users.append(user)
    # return the user and status code 201 (creation)
    return jsonify({'user': user}), 201


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    # check if the request is valid
    user = [user for user in users if user['id'] == id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    # update the user
    user[0]['name'] = request.json.get('name', user[0]['name'])
    # return the updated user
    return jsonify({'user': user[0]})


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    # check if the request is valid
    user = [user for user in users if user['id'] == id]
    if len(user) == 0:
        abort(404)
    # remove the user from the list
    users.remove(user[0])
    # return the result
    return jsonify({'result': True})


if __name__ == '__main__':
    # run app on 127.0.0.1:8080 with debug on
    app.run(host="127.0.0.1", port=8080, debug=True)

```
