from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Missoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_missao = db.Column(db.String(100), unique=True, nullable=False)
    data_lancamento = db.Column(db.Date, nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    tripulacao = db.Column(db.String(500), nullable=False)
    carga_util = db.Column(db.String(500), nullable=False)
    duracao = db.Column(db.DateTime, nullable=False)
    custo = db.Column(db.Numeric(precision=15, scale=2), nullable=False)
    status_missao = db.Column(db.Text, nullable=False)

    def __init__(self, nome_missao, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo, status_missao):
        self.nome_missao = nome_missao
        self.data_lancamento = data_lancamento
        self.destino = destino
        self.estado = estado
        self.tripulacao = tripulacao
        self.carga_util = carga_util
        self.duracao = duracao
        self.custo = custo
        self.status_missao = status_missao

    def to_dict(self, columns=[]):
        if not columns:
            return {
                "id": self.id,
                "nome_missao": self.nome_missao,
                "data_lancamento": self.data_lancamento.strftime('%Y-%m-%d'),
                "destino": self.destino,
                "estado": self.estado,
                "tripulacao": self.tripulacao,
                "carga_util": self.carga_util,
                "duracao": self.duracao.strftime('%Y-%m-%dT%H:%M:%S'),
                "custo": str(self.custo),
                "status_missao": self.status_missao
            }
        else:
            return {col: getattr(self, col) for col in columns}
