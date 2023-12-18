from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
# app.config.from_object('config')
# app.app_context().push()
# db.init_app(app)
# migrate = Migrate(app, db)


@app.route('/')
def index():
    
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)