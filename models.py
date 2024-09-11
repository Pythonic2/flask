from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)


    def __repr__(self) -> str:
        return f'<Cliente {self.nome}>'
    