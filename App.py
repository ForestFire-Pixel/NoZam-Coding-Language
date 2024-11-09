from flask import Flask, request, jsonify
from compiler import NoZamCompiler
from libraries import AlertBetter, apihide, ThreeDee
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

# Define a model for WorldStorage
class WorldStorage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), unique=True, nullable=False)
    value = db.Column(db.String(120), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to compile and execute NoZam code
@app.route('/execute', methods=['POST'])
def execute_code():
    data = request.json
    nozam_code = data.get('code')
    
    # Compile and execute code
    compiled_code = NoZamCompiler.compile(nozam_code)
    result = eval(compiled_code)  # Executes in Python runtime (CAUTION: Secure this in production)
    
    return jsonify({'result': result})

# Endpoint to store and retrieve WorldStorage
@app.route('/storage', methods=['POST'])
def save_to_world_storage():
    data = request.json
    key = data['key']
    value = data['value']
    
    entry = WorldStorage(key=key, value=value)
    db.session.add(entry)
    db.session.commit()
    
    return jsonify({'message': 'Stored successfully'})

@app.route('/storage/<key>', methods=['GET'])
def get_from_world_storage(key):
    entry = WorldStorage.query.filter_by(key=key).first()
    if entry:
        return jsonify({'key': entry.key, 'value': entry.value})
    else:
        return jsonify({'error': 'Key not found'}), 404

# Additional endpoints for specific libraries like AlertBetter
@app.route('/alert', methods=['POST'])
def better_alert():
    message = request.json.get('message')
    alert_message = AlertBetter.show_alert(message)
    return jsonify({'alert': alert_message})

if __name__ == '__main__':
    app.run(debug=True)
  
