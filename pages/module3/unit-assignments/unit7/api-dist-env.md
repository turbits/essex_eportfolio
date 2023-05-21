---
layout: page
permalink: /pages/module3/unit-assignments/unit7/api-dist-env.html
---

⬅️[Back](/pages/module3/unit-assignments/unit7/m3u7.html)

## Unit 7: Developing an API for a Distributed Environment

Unit assignment questions and answers to follow.

### 📝 Requirements

In this session, you will create a RESTful API which can be used to create and delete user records. Responses to the questions should be recorded in your e-portfolio.

You are advised to use these techniques to create an API for your team’s submission in Unit 11 and be prepared to demonstrate it during next week’s seminar (Unit 10). Remember that you can arrange a session with the tutor during office hours for more support, if required.

Using the Jupyter Notebook workspace, create a file named api.py and copy the following code into it (a copy is provided for upload to Codio/GitHub): You can install Jupyter Notebook on your local machine following these instructions or via the University of Essex Software Hub.

```python

#source of code: https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3


from flask import Flask
from flask_restful import Api, Resource, reqparse
 
app = Flask(__name__)
api = Api(app)
 
users = [
    {
        "name": "James",
        "age": 30,
        "occupation": "Network Engineer"
    },
    {
        "name": "Ann",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jason",
        "age": 22,
        "occupation": "Web Developer"
    }
]
 
class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404
 
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
 
        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400
 
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201
 
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
 
        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201
 
    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200
      
api.add_resource(User, "/user/<string:name>")
 
app.run(debug=True)
```

---

### 🤔 Questions


#### Question 1
- Run the API.py code. Take a screenshot of the terminal output. What command did you use to compile and run the code?

The unit assignment says to use Jupyter notebook in the Codio environment, but it appears that the packages required to run flask are not able to be installed:

pip install flask
```
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.6/dist-packages/itsdangerous'
Consider using the `--user` option or check the permissions.
```

This is the output when run from my local machine after installing `flask` and `flask_restful` and using `python api_dist.py` to start it:

![](/pages/module3/unit-assignments/unit7/api-dist-out.jpg)


#### Question 2
- Run the following command at the terminal prompt: w3m http://127.0.0.1:5000/user/Ann
- What happens when this command is run, and why?

Since I'm not using Linux and I won't be looking for a way to run it on Windows, I'll show the output from Postman instead.

When sending a GET request from Postman to `http://127.0.0.1:5000/user/Ann` I get the following response:

```json
{
    "name": "Ann",
    "age": 32,
    "occupation": "Doctor"
}
```

#### Question 3
- Run the following command at the terminal prompt: w3m http://127.0.0.1:5000/user/Adam
- What happens when this command is run, and why?

```
"User not found"
```

#### Question 4
- What capability is achieved by the flask library?

Flask is a lightweight web framework for Python. It's classified as a microframework, which means that it does not include many built-in features from a more complex framework, such as Django, but it offers a simple and extendable base for building web applications.

Flask has some key features, such as routing, templating, and form handling, that make it quick and easy to build a lightweight web application.

#### Architecture Evolution Activity
- Based on your reading this week, could you write a section that might be appended to this paper, Salah et al, 2016, which would present the next phase of evolution history, from microservices to the technologies which are commonly in use today?

Since this paper was written, there have been several key developments from a software architecture perspective. One of the most significant trends is containerization, using technology such as Docker. Containers are a portable and lightweight way to package software. Another development has been the rise of serverless architecture, a logical progression from the classic model of on premises servers to the cloud. Cloud computing offers a level of scalability, flexibility, and cost-efficiency never seen before. It also has the benefit of exchanging capital expenses for operational expenses, something that most companies would deem a very positive change.
