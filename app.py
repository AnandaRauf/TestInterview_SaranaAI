from flask import Flask, request, jsonify
from ml_model import GeminiModel
from rabbitmq import send_message, receive_message

app = Flask(__name__)
model = GeminiModel()

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json.get('text')
    prediction = model.predict(text)
    
    # Send prediction to another service or log it using RabbitMQ
    send_message('predictions_queue', {'text': text, 'prediction': prediction})

    return jsonify({'prediction': prediction})

def handle_message(message):
    print(f"Received message: {message}")

# Start RabbitMQ listener
if __name__ == '__main__':
    import threading
    listener_thread = threading.Thread(target=receive_message, args=('predictions_queue', handle_message))
    listener_thread.start()

    app.run(host='0.0.0.0', port=5000)
