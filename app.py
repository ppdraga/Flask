from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route("/")
def home():
    data = request.get_json()
    a=1
    return render_template('home.html')

@app.route("/api")
def api():
    json_data = request.get_json()
    data_args = {}
    for key in request.args.keys():
        data_args[key] = request.args.get(key)
    return jsonify({'message': 'Success', 
                    'json_data': json_data,
                    'data_args': data_args}), 200

if __name__=='__main__':
    app.run(debug=True)