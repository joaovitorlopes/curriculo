# curriculos-
## Venv
sudo apt install python3-venv

## Pip3
sudo apt install python3-pip

# Pipenv
sudo apt install pipenv

## Criar o ambiente na primeira vez
pipenv --three

## Entrar no ambiente
pipenv shell

## Sair do ambiente
exit

##Instalar individualmente os pacotes
pipenv install Flask

## Instalar todos os pacotes
pipenv install


# Aula 2
## Configurando o banco de dados
sudo mysql -u root -p
create database curriculos;
create user 'aa'@'localhost' identified by 'Senha';
grant all privileges on curriculos.* to 'aa'@'localhost';

## Criar o model

## Configurar a aplicação

## Configurar o Miagrates
### Para inicializar o migrates (rodar somente uma vez)
python3 migrations.py db init

### Ao alterar models
python3 migrations.py db migrate
python3 migrations.py db upgrade

## CRUD (Console interativo)
from app import db
from app.models.tables import Usuario
import bcrypt

### Adicionar um novo usuario
senha_plana = 'teste'
senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
u = Usuario(nome='aa', email='aa', senha=senha_encriptada)
db.session.add(u)
db.session.commit()

### Selecionar todos os usuarios
lista = Usuario.query.all()

### Selecionar usuario pelo ID
u2 = Usuario.query.filter_by(id=1).first()
u2.email = 'novo@gmail.com'
db.session.add(u2)
db.session.commit()

### Deletar usuario
u3 = Usuario.query.filter_by(id=1).first()
db.session.delete(u3)
db.session.commit()
