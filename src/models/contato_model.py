from src.settings.extensions import db

class Contato(db.Model):
    
    __tablename__ = "contatos"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f"Contato: {self.nome} - {self.email} - {self.telefone}"