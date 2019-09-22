from flask import Flask, render_template, url_for
import os

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/saigen-0001')
def saigen0001():
    return render_template('saigen-0001.html')

@application.route('/saigen-0002')
def saigen0002():
    return render_template('saigen-0002.html')

@application.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(application.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
    application.debug = True
    application.run()
