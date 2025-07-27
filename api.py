from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)
orders = []

@app.route("/submit-order", methods=["POST"])
def submit_order_api():
    data = request.json
    return jsonify(submit_order(data))

def submit_order(data):
    order_id = str(uuid.uuid4())
    eta = "30 دقيقة"
    orders.append({**data, "order_id": order_id, "eta": eta})
    return {"order_id": order_id, "eta": eta}

if __name__ == "__main__":
    app.run(debug=True)
