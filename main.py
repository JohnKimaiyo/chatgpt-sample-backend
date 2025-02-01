from flask import Flask, request, jsonify
import your_custom_model  # Your custom NLP model

app = Flask(__name__)

@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    # Process the message with your custom NLP model
    bot_response = your_custom_model.generate_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(port=5000)