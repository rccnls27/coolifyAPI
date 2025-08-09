from flask import Flask, jsonify

app = Flask(__name__)

# Route 1: The original homepage (still works!)
@app.route('/')
def home():
    return {"message": "Welcome to the complex API!"}

# Route 2: Our new calculator endpoint
# The <int:a> and <int:b> parts are special. They tell Flask:
# 1. Expect two pieces of data in the URL path.
# 2. Automatically convert them to integers for us.
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    # Perform the "complex" logic
    result = a + b

    # Create a dictionary for the JSON response
    response_data = {
        "operation": "addition",
        "a": a,
        "b": b,
        "result": result
    }

    # Use jsonify to properly format the dictionary as a JSON response
    return jsonify(response_data)

# This part is only for local development, Coolify doesn't use it.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
