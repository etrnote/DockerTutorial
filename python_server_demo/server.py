from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbuser:dbpassword@db:5432/messages'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    creator = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Message {self.id}>"


@app.route('/')
def hello():
    return 'Hello, Docker!'


# Define a route to add a new message
@app.route('/messages', methods=['POST'])
def add_message():
    data = request.get_json()
    content = data.get('content')
    creator = data.get('creator')

    message = Message(content=content, creator=creator)
    db.session.add(message)
    db.session.commit()

    return jsonify({'message': 'Message added successfully'})


# Define a route to display all messages
@app.route('/messages', methods=['GET'])
def get_all_messages():
    messages = Message.query.all()
    message_list = []
    for message in messages:
        message_data = {
            'id': message.id,
            'content': message.content,
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'creator': message.creator
        }
        message_list.append(message_data)
    return jsonify(message_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0')