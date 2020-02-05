from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/setcookie', methods = ['POST', 'GET'])
def set_cookie():
    if request.method == 'POST':
        user = request.form['nm']
        response = make_response(render_template('setcookie.html'))
        response.set_cookie('userID', user)

    return response

@app.route('/readcookie', methods = ['POST', 'GET'])
def read_cookie():
    user_id = request.cookies.get('userID')

    return render_template('readcookie.html', user_id = user_id)
       



if __name__ == '__main__':
    app.run(debug=True)
