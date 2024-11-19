from flask import Flask, render_template, request, url_for, redirect, Response
from models import db, Missoes
import json
from datetime import datetime
from decimal import Decimal

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///missoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    missoes = Missoes.query.all()
    result = [e.to_dict() for e in missoes]

    if request.headers.get('Content-Type') == 'application/json':
        return Response(response=json.dumps(result), status=200, content_type="application/json")
    
    return render_template('index.html', missoes=missoes)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = request.get_json()
        else:
            data = request.form
        
        required_fields = [
            'nome_missao', 'data_lancamento', 'destino', 'estado',
            'tripulacao', 'carga_util', 'duracao', 'custo', 'status_missao'
        ]
        
        for field in required_fields:
            if field not in data:
                return Response(
                    response=json.dumps({"error": f"'{field}' is required"}), 
                    status=400, 
                    content_type="application/json"
                )
        
        try:
            nome_missao = data['nome_missao']
            data_lancamento = datetime.strptime(data['data_lancamento'], '%Y-%m-%d').date()
            destino = data['destino']
            estado = data['estado']
            tripulacao = data['tripulacao']
            carga_util = data['carga_util']
            try:
                duracao = datetime.strptime(data['duracao'], '%Y-%m-%dT%H:%M:%S')
            except ValueError:
                duracao = datetime.strptime(data['duracao'], '%Y-%m-%dT%H:%M')
            custo = Decimal(data['custo'])
            status_missao = data['status_missao']
    
            missao = Missoes(
                nome_missao, data_lancamento, destino, estado,
                tripulacao, carga_util, duracao, custo, status_missao
            )
            db.session.add(missao)
            db.session.commit()
            
            if request.content_type == 'application/json':
                return Response(response=json.dumps(missao.to_dict()), status=200, content_type="application/json")
            
            return redirect(url_for('index'))
        except Exception as e:
            return Response(response=json.dumps({"error": str(e)}), status=400, content_type="application/json")
    
    return render_template('add.html')

@app.route('/read/<int:id>', methods=['GET'])
def read(id):
    missao = Missoes.query.get(id)
    if not missao:
        return Response(response=json.dumps({"error": "Mission not found"}), status=404, content_type="application/json")
    
    if request.headers.get('Content-Type') == 'application/json':
        return Response(response=json.dumps(missao.to_dict()), status=200, content_type="application/json")
    
    

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    missao = Missoes.query.get(id)
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = request.get_json()
        else:
            data = request.form
        
        required_fields = [
            'nome_missao', 'data_lancamento', 'destino', 'estado',
            'tripulacao', 'carga_util', 'duracao', 'custo', 'status_missao'
        ]
        
        for field in required_fields:
            if field not in data:
                return Response(
                    response=json.dumps({"error": f"'{field}' is required"}), 
                    status=400, 
                    content_type="application/json"
                )
        
        missao.nome_missao = data['nome_missao']
        missao.data_lancamento = datetime.strptime(data['data_lancamento'], '%Y-%m-%d').date()
        missao.destino = data['destino']
        missao.estado = data['estado']
        missao.tripulacao = data['tripulacao']
        missao.carga_util = data['carga_util']
        try:
            missao.duracao = datetime.strptime(data['duracao'], '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            missao.duracao = datetime.strptime(data['duracao'], '%Y-%m-%dT%H:%M')
        missao.custo = Decimal(data['custo'])
        missao.status_missao = data['status_missao']
        
        db.session.commit()
        
        if request.content_type == 'application/json':
            return Response(response=json.dumps(missao.to_dict()), status=200, content_type="application/json")
        
        return redirect(url_for('index'))
    
    return render_template('edit.html', missao=missao)

@app.route('/delete/<int:id>', methods=['POST', 'DELETE'])
def delete(id):
    missao = Missoes.query.get(id)
    if not missao:
        return Response(response=json.dumps({"error": "Mission not found"}), status=404, content_type="application/json")
    
    db.session.delete(missao)
    db.session.commit()
    
    if request.content_type == 'application/json':
        return Response(response=json.dumps(missao.to_dict()), status=200, content_type="application/json")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
