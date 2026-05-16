from dao import connection

def consulta_hospedes():
    conexao = connection()
    cursor = conexao.cursor(dictionary=True)
    
    sql = "SELECT * FROM hospedes"
    cursor.execute(sql)
    
    dados = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    return dados

def consulta_hospede_id(id):
    conexao = connection()
    cursor = conexao.cursor(dictionary=True)
    
    sql = "SELECT * FROM hospedes WHERE id = %s"
    cursor.execute(sql, (id,))
    
    dados = cursor.fetchone()
    
    cursor.close()
    conexao.close()
    
    return dados

def add_hospede(nome, email, telefone, cpf):
    
    conexao = connection()
    cursor = conexao.cursor()
    
    sql = """
        INSERT INTO hospedes(nome, email, telefone, cpf)
        VALUES(%s, %s, %s, %s)
    """
    
    cursor.execute(sql, (nome, email, telefone, cpf))
    
    conexao.commit()
    
    cursor.close()
    conexao.close()

def update_hospede(id, nome=None, email=None, telefone=None, cpf=None):
    
    hospede = consulta_hospede_id(id)
    
    if not hospede:
        return False
    
    if nome is None:
        nome = hospede['nome']
    
    if email is None:
        email = hospede['email']
    
    if telefone is None:
        telefone = hospede['telefone']
    
    if cpf is None:
        cpf = hospede['cpf']
    
    conexao = connection()
    cursor = conexao.cursor()
    
    sql = """
        UPDATE hospedes
        SET nome = %s, 
            email = %s, 
            telefone = %s, 
            cpf = %s 
        WHERE id = %s
    """
    
    cursor.execute(sql, (nome, email, telefone, cpf, id))
    
    conexao.commit()
    
    cursor.close()
    conexao.close()

def delete_hospede(id):
      
    if not consulta_hospede_id(id):
        return False
    
    conexao = connection()
    cursor = conexao.cursor()
    
    sql = "DELETE FROM hospedes WHERE id = %s"
    cursor.execute(sql, (id,))
    
    conexao.commit()
    
    cursor.close()
    conexao.close()


def consulta_quartos():
    conexao = connection()
    cursor = conexao.cursor(dictionary=True)
    
    sql = "SELECT * FROM quartos"
    cursor.execute(sql)
    
    dados = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    return dados

def consulta_quarto_id(id):
    conexao = connection()
    cursor = conexao.cursor(dictionary=True)
    
    sql = "SELECT * FROM quartos WHERE id = %s"
    cursor.execute(sql, (id,))
    
    dados = cursor.fetchone()
    
    cursor.close()
    conexao.close()
    
    return dados

def add_quarto(numero, tipo, valor_diaria, status):
    
    conexao = connection()
    cursor = conexao.cursor()
    
    sql = """
        INSERT INTO quartos(numero, tipo, valor_diaria, status)
        VALUES(%s, %s, %s, %s)
    """
    
    cursor.execute(sql, (numero, tipo, valor_diaria, status))
    
    conexao.commit()
    
    cursor.close()
    conexao.close()

def update_quarto(id, numero=None, tipo=None, valor_diaria=None, status=None):
    
    quarto = consulta_quarto_id(id)
    
    if not quarto:
        return False
    
    if numero is None:
        numero = quarto['numero']
    
    if tipo is None:
        tipo = quarto['tipo']
    
    if valor_diaria is None:
        valor_diaria = quarto['valor_diaria']
    
    if status is None:
        status = quarto['status']
    
    conexao = connection()
    cursor = conexao.cursor()
    
    sql = """
        UPDATE quartos
        SET numero = %s, 
            tipo = %s, 
            valor_diaria = %s, 
            status = %s 
        WHERE id = %s
    """
    
    cursor.execute(sql, (numero, tipo, valor_diaria, status, id))
    
    conexao.commit()
    
    cursor.close()
    conexao.close()

def delete_quarto(id):
    
    if not consulta_quarto_id(id):
        return False
    
    conexao = connection()
    cursor = conexao.cursor()
    
    sql = "DELETE FROM quartos WHERE id = %s"
    cursor.execute(sql, (id,))
    
    conexao.commit()
    
    cursor.close()
    conexao.close()


def consulta_reservas():
    
    conexao = connection()
    cursor = conexao.cursor(dictionary=True)
    
    sql = """
        SELECT 
            reservas.id,
            hospedes.nome AS hospede,
            quartos.numero AS quarto,
            reservas.data_entrada,
            reservas.data_saida
        FROM reservas
        JOIN hospedes
            ON reservas.hospede_id = hospedes.id
        JOIN quartos
            ON reservas.quarto_id = quartos.id
    """
    
    cursor.execute(sql)
    
    dados = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    return dados

def consulta_reserva_id(id):
    
    conexao = connection()
    cursor = conexao.cursor(dictionary=True)
    
    sql = """
        SELECT 
            reservas.id,
            reservas.hospede_id,
            reservas.quarto_id,
            hospedes.nome AS hospede,
            quartos.numero AS quarto,
            reservas.data_entrada,
            reservas.data_saida
        FROM reservas
        JOIN hospedes
            ON reservas.hospede_id = hospedes.id
        JOIN quartos
            ON reservas.quarto_id = quartos.id
        WHERE reservas.id = %s
    """
    
    cursor.execute(sql, (id,))
    
    dados = cursor.fetchone()
    
    cursor.close()
    conexao.close()
    
    return dados

def add_reserva(hospede_id, quarto_id, data_entrada, data_saida):
    
    if not consulta_hospede_id(hospede_id):
     return False

    if not consulta_quarto_id(quarto_id):
      return False
    
    if data_saida <= data_entrada:
        return False
    
    conexao = connection()
    cursor = conexao.cursor()
    
    sql = """
        INSERT INTO reservas(hospede_id, quarto_id, data_entrada, data_saida)
        VALUES(%s, %s, %s, %s)
    """
    
    cursor.execute(sql, (hospede_id, quarto_id, data_entrada, data_saida))
    
    conexao.commit()
    
    cursor.close()
    conexao.close()
    
def update_reserva(id, hospede_id=None, quarto_id=None, data_entrada=None, data_saida=None):
    
    reserva = consulta_reserva_id(id)
    
    if not consulta_hospede_id(hospede_id):
        return False

    if not consulta_quarto_id(quarto_id):
        return False
    
    if not reserva:
        return False
    
    if data_saida <= data_entrada:
        return False
    
    if hospede_id is None:
        hospede_id = reserva['hospede_id']
    
    if quarto_id is None:
        quarto_id = reserva['quarto_id']
    
    if data_entrada is None:
        data_entrada = reserva['data_entrada']
    
    if data_saida is None:
        data_saida = reserva['data_saida']
        
    conexao = connection()
    cursor = conexao.cursor()
    
    sql = """
        UPDATE reservas
        SET hospede_id = %s, 
            quarto_id = %s, 
            data_entrada = %s, 
            data_saida = %s 
        WHERE id = %s
    """
    
    cursor.execute(sql, (hospede_id, quarto_id, data_entrada, data_saida, id))
    
    conexao.commit()
    
    cursor.close()
    conexao.close()

def delete_reserva(id):
    
    if not consulta_reserva_id(id):
        return False
    
    conexao = connection()
    cursor = conexao.cursor()
    
    sql = "DELETE FROM reservas WHERE id = %s"
    cursor.execute(sql, (id,))
    
    conexao.commit()
    
    cursor.close()
    conexao.close()