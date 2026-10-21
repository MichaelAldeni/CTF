from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/listen', methods=['GET', 'POST'])
def listen():
    if request.method == 'POST':
        raw = request.get_data(as_text=True)
        json = request.get_json(silent=True)
        form = request.form.to_dict()
        args = request.args.to_dict()
        print('--- Received POST ---')
        if json is not None:
            print('JSON:', json)
        if form:
            print('Form:', form)
        if raw:
            print('Raw:', raw)
        if args:
            print('Query args:', args)
        print('--- End ---')
        return 'OK', 200
    else:
        args = request.args.to_dict()
        print('--- Received GET ---')
        print('Query args:', args)
        print('--- End ---')
        return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)