from flask import Flask, render_template
from models import db, Cliente

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///exemplo.sqlite"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():

    cliente = Cliente(nome='xxxxx')
    db.session.add(cliente)

    db.session.commit()
    clientes = Cliente.query.all()

    return render_template('index.html', clientes=clientes)


if __name__ == '__main__':
    app.run(debug=True)