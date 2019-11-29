from flask import Flask
import flask_restful

# Create an instance of Flask, which is the main backend application in this program
app = Flask(__name__)

# Create the main entry point using the Flask instance
api = flask_restful.Api(app)


# Declare a Resource
class Interviewees(flask_restful.Resource):
    # The function name is "get" because you gonna use http method GET to reach this function
    def get(self):
        db = Connection2DB()
        interviewees = db.getIntervieweesFromDB()
        return interviewees


# The Database part
class Connection2DB:
    def __init__(self):
        print("This part is different according to which DBMS you use")
        print("Let's act like we connect to the database during this initiation process...")

    def getIntervieweesFromDB(self):
        print("You should use SQL to select records in the data table here")
        print("Let's assume we succeed...")
        return [
            {
                "name": "Evan You",
                "GPA": 3.9
            },
            {
                "name": "Ron You",
                "GPA": 2.0
            }
        ]


# Remember to add the resource to your entrypoint
api.add_resource(Interviewees, "/api/interviewees")


# Run from here
if __name__ == "__main__":
    app.run("0.0.0.0")
