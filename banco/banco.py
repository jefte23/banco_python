# importar bibliotecas
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

#intanciando a app
banco = Flask(__name__)

# configurar bd
banco.config['MYSQL_DATABASE_USER'] = 'root'
banco.config['MYSQL_DATABASE_PASSWORD'] = 'root'
banco.config['MYSQL_DATABASE_DB'] = 'banco'

# Instanciar bd
mysql = MySQL()
mysql.init_app(banco)

#rota /
@banco.route('/')
# Metodo para /

def index():
    return render_template('formLogin.html')


#rota para /login
@banco.route('/login')
#metodo que responde /login
def login():
    # Obtendo os parametros do formulário
    cpf_cliente = request.args.get('cpf_cliente')
    senha_cliente = request.args.get('senha_cliente')

    # Cria conexao com bd
    cursor = mysql.connect().cursor()

    # Submeter o comando SQL
    cursor.execute(f"SELECT * FROM banco.cliente where cpfcliente='{cpf_cliente}' and senhacliente='{senha_cliente}'")

    # Recupera os dados
    dados = cursor.fetchone()

    # mysql.connect().close()

    # imprimir nome
    return render_template('logado.html', nome_cliente=str(dados[2]))

# executar a app
banco.run(debug=True)


