from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/courses')
def show_all_courses():
    courses = [
        'International Finance',
        'Database Design and Implementation',
        'Advanced Corporate Finance',
    ]
    return render_template('mycourses.html', courses=courses)


# https://goo.gl/Pc39w8 explains the following line
if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
