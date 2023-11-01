from flask import Flask, request
from flask_restful import Resource, Api
app = Flask("AppStoreAPI")
api = Api(app)

apps = [
     ['Chat App', 'App for chatting', 5.50],
     ['Dating App', 'App for dating', 6.00],
     ['Gaming App', 'App for gaming', 12.00]
]

class AppStore(Resource):
    def get(self, app_id):
        if app_id == "all":
            return apps
        
        return apps[int(app_id)]
    
    def delete(self, app_id):
        app_id = int(app_id)
        if app_id >= 0 and app_id < len(apps):
            del apps[app_id]
        return 200
class AppAdd(Resource):
    def post(self):
        new_app = request.get_json()
        if isinstance(new_app, list):
            apps.append(new_app)
            return new_app, 201
        else:
            return "Not a valid app", 400    

api.add_resource(AppStore, '/apps/<app_id>')
api.add_resource(AppAdd, '/apps')

if __name__=='__main__':
     app.run(port=5000, debug=True, host='0.0.0.0')