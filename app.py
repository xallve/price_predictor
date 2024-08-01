from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/retrain', methods=['POST'])
def retrain():
    # Implement retraining logic here
    # I think to use Celery and trigger retrain every
    # 30 minutes with new data and delete old model
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(port=5000)
