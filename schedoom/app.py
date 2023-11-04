from flask import Flask, jsonify, make_response, request, json
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)
cors = CORS(app)
app.config.from_object('config.Config')
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://schedoomdb:schedoomdb@schedoomdb:5432/schedoomdb"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String())
    name = db.Column(db.String())
    surname = db.Column(db.String())

    # doors = db.Column(db.Integer())

    def __init__(self, user, name, surname):
        self.user = user
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"<User {self.user}>"


class ProjectModel(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())

api = Api(app)

data = [
       {
                    "id": 789,
                    "name": "Otaner",
                    "description": "Membership from Qela Technologies T(Ltd)",
                    "created_at": "2023-11-02T14:11:00.000000Z",
                    "updated_at": "2023-11-02T19:59:36.000000Z"
                },
                {
                    "id": 792,
                    "name": "William Ng'wininga",
                    "description": "My young brother",
                    "created_at": "2023-11-02T14:52:16.000000Z",
                    "updated_at": "2023-11-02T20:03:11.000000Z"
                },
                {
                    "id": 793,
                    "name": "Gabriel James Mbeke",
                    "description": "Membership from Qela Technologies T(Ltd)",
                    "created_at": "2023-11-02T19:38:29.000000Z",
                    "updated_at": "2023-11-02T20:04:54.000000Z"
                },
                {
                    "id": 794,
                    "name": "Rinward Nkondo",
                    "description": "Hellow, World!",
                    "created_at": "2023-11-02T20:01:28.000000Z",
                    "updated_at": "2023-11-02T20:01:28.000000Z"
                }

]

class Projects(Resource):
    def get(self):
        projects = ProjectModel.query.all()
        results = [
            {
                "id": project.id,
                "name": project.name,
                "description": project.description,
                "created_at": "2023-11-02T20:01:28.000000Z",
                "updated_at": "2023-11-02T20:01:28.000000Z"
                
            } for project in projects]

        return jsonify(results)
    
    def post(self):
        data = request.get_json()
        new_project = ProjectModel(name=data['name'], description=data['description'])
        db.session.add(new_project)
        db.session.commit()
        make_response(jsonify({"msg": "OK"}), 200)

    

   

class Project(Resource):
    def get(self, id):
        ret_obj = ProjectModel.query.get_or_404(id)
        

        return jsonify({
            "id": ret_obj.id,
            "name": ret_obj.name,
            "description": ret_obj.description

        })     
        # make_response(jsonify({"msg":"not found"}), 404)

    def patch(self, id):
        up_data = request.get_json() 
        ret_obj = ProjectModel.query.get(id)
        ret_obj.name = up_data["name"]
        ret_obj.description = up_data["description"]
        db.session.add(ret_obj)
        db.session.commit()
        
        make_response(jsonify({"msg": "OK"}), 201)

    def delete(self, id):
        ret_obj = ProjectModel.query.get_or_404(id)
        db.session.delete(ret_obj)
        db.session.commit()
        make_response(jsonify({"msg": "OK"}), 200)
        

api.add_resource(Projects, '/api/projects')
api.add_resource(Project, '/api/projects/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)