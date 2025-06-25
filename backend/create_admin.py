#!/usr/bin/env python3
import os
import sys

# Ajustar sys.path para incluir o diretório src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from flask import Flask
from config import Config
from database import db
from models.user import User

def create_admin():
    """Criar usuário admin padrão"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar banco de dados
    db.init_app(app)
    
    with app.app_context():
        # Criar todas as tabelas
        db.create_all()
        
        # Verificar se já existe usuário admin
        admin_user = User.find_by_email("admin@vip.com.br")
        if admin_user:
            print("Usuário admin já existe: admin@vip.com.br")
            return
        
        # Criar usuário admin
        try:
            new_user = User(
                email="admin@vip.com.br",
                name="Administrador VIP",
                role="admin"
            )
            new_user.set_password("123456")
            db.session.add(new_user)
            db.session.commit()
            print("✅ Usuário admin criado com sucesso!")
            print("Email: admin@vip.com.br")
            print("Senha: 123456")
        except Exception as e:
            print(f"❌ Erro ao criar usuário admin: {e}")

if __name__ == '__main__':
    create_admin()

