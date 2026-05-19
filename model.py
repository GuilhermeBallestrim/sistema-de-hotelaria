from dao import connection
from datetime import datetime

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

    if not nome or not email or not telefone or not cpf:
        return "Preencha todos os campos"

    conexao = connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        sql = "SELECT * FROM hospedes WHERE cpf = %s"
        cursor.execute(sql, (cpf,))

        if cursor.fetchone():
            return "CPF já cadastrado"

        sql = """
            INSERT INTO hospedes(nome, email, telefone, cpf)
            VALUES(%s, %s, %s, %s)
        """

        cursor.execute(sql, (nome, email, telefone, cpf))

        conexao.commit()

        return True

    except Exception:
        return "Erro ao cadastrar hóspede"

    finally:
        cursor.close()
        conexao.close()

def update_hospede(id, nome=None, email=None, telefone=None, cpf=None):

    hospede = consulta_hospede_id(id)

    if not hospede:
        return "Hóspede não encontrado"

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

    try:

        sql = """
            SELECT *
            FROM hospedes
            WHERE cpf = %s
            AND id != %s
        """

        cursor.execute(sql, (cpf, id))

        if cursor.fetchone():
            return "CPF já cadastrado"

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

        return True

    except Exception:
        return "Erro ao atualizar hóspede"

    finally:
        cursor.close()
        conexao.close()
        
def delete_hospede(id):

    if not consulta_hospede_id(id):
        return "Hóspede não encontrado"

    conexao = connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = "SELECT * FROM reservas WHERE hospede_id = %s"
        cursor.execute(sql, (id,))

        if cursor.fetchone():
            cursor.close()
            conexao.close()

            return "Hóspede possui reservas"

        sql = "DELETE FROM hospedes WHERE id = %s"
        cursor.execute(sql, (id,))

        conexao.commit()

        return True
    except Exception:
        return "Erro ao excluir hóspede"
    
    finally:
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
    
    status_validos = [
        "Disponível",
        "Ocupado",
        "Manutenção"
    ]

    if numero is None or not tipo or not status:
        return "Preencha todos os campos"
    
    if status not in status_validos:
        return "Status inválido"

    if valor_diaria <= 0:
        return "Valor da diária inválido"
    
    conexao = connection()
    cursor = conexao.cursor()
    
    try:
        
        sql = "SELECT * FROM quartos WHERE numero = %s"
        cursor.execute(sql, (numero,))

        if cursor.fetchone():
            return "Quarto já existe"
        
        
        sql = """
            INSERT INTO quartos(numero, tipo, valor_diaria, status)
            VALUES(%s, %s, %s, %s)
        """
        
        cursor.execute(sql, (numero, tipo, valor_diaria, status))
        
        conexao.commit()
        
        return True
    
    except Exception:
        return "Erro ao adicionar quarto"

    finally:
        cursor.close()
        conexao.close()

def update_quarto(id, numero=None, tipo=None, valor_diaria=None, status=None):
    
    quarto = consulta_quarto_id(id)
    
    if not quarto:
        return "Quarto não existe"
    
    if numero is None:
        numero = quarto['numero']
    
    if tipo is None:
        tipo = quarto['tipo']
    
    if valor_diaria is None:
        valor_diaria = quarto['valor_diaria']
    
    if status is None:
        status = quarto['status']
    
    status_validos = [
        "Disponível",
        "Ocupado",
        "Manutenção"
    ]

    if status not in status_validos:
        return "Status inválido"
    
    if valor_diaria <= 0:
        return "Valor da diária inválido"
    
    conexao = connection()
    cursor = conexao.cursor()
        
    try:
        sql = """
            SELECT *
            FROM quartos
            WHERE numero = %s
            AND id != %s
        """

        cursor.execute(sql, (numero, id))

        if cursor.fetchone():
            return "Número de quarto já existe"
        
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
        
        return True
    
    except Exception:
        return "Erro ao atualizar quarto"

    finally:
        cursor.close()
        conexao.close()

def delete_quarto(id):

    if not consulta_quarto_id(id):
        return "Quarto não encontrado"

    conexao = connection()
    cursor = conexao.cursor(dictionary=True)


    try:
        sql = "SELECT * FROM reservas WHERE quarto_id = %s"
        cursor.execute(sql, (id,))

        if cursor.fetchone():
            cursor.close()
            conexao.close()

            return "Quarto possui reservas"

        sql = "DELETE FROM quartos WHERE id = %s"
        cursor.execute(sql, (id,))

        conexao.commit()

        return True
    
    except Exception:
        return "Erro ao excluir quarto"

    finally:
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
            hospedes.cpf,
            hospedes.telefone,
            hospedes.email,

            quartos.numero AS quarto,
            quartos.tipo,
            quartos.valor_diaria,
            quartos.status,

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

    if dados:

        if dados["data_entrada"]:
            dados["data_entrada_formatada"] = (
                dados["data_entrada"]
                .strftime("%d/%m/%Y")
            )

        else:
            dados["data_entrada_formatada"] = ""

        if dados["data_saida"]:
            dados["data_saida_formatada"] = (
                dados["data_saida"]
                .strftime("%d/%m/%Y")
            )

        else:
            dados["data_saida_formatada"] = ""

    cursor.close()
    conexao.close()

    return dados

def add_reserva(hospede_id, quarto_id, data_entrada, data_saida):

    if not consulta_hospede_id(hospede_id):
        return "Hóspede não encontrado"

    quarto = consulta_quarto_id(quarto_id)

    if not quarto:
        return "Quarto não encontrado"

    if quarto["status"] == "Manutenção":
        return "Quarto em manutenção"

    try:
        entrada = datetime.strptime(data_entrada, "%Y-%m-%d")
        saida = datetime.strptime(data_saida, "%Y-%m-%d")

    except:
        return "Data inválida"

    if saida <= entrada:
        return "Data de saída inválida"

    if not verificar_disponibilidade(
        quarto_id,
        data_entrada,
        data_saida
    ):
        return "Quarto indisponível nesta data"

    conexao = connection()
    cursor = conexao.cursor()


    try:
        sql = """
            INSERT INTO reservas(
                hospede_id,
                quarto_id,
                data_entrada,
                data_saida
            )
            VALUES(%s, %s, %s, %s)
        """

        cursor.execute(sql, (
            hospede_id,
            quarto_id,
            data_entrada,
            data_saida
        ))

        conexao.commit()

        return True    
    
    except Exception:
        return "Erro ao adicionar reserva"

    finally:
        cursor.close()
        conexao.close()

def update_reserva(
    id,
    hospede_id=None,
    quarto_id=None,
    data_entrada=None,
    data_saida=None
):

    reserva = consulta_reserva_id(id)

    if not reserva:
        return "Reserva não existe"

    if hospede_id is None:
        hospede_id = reserva['hospede_id']

    if quarto_id is None:
        quarto_id = reserva['quarto_id']

    if data_entrada is None:
        data_entrada = reserva['data_entrada']

    if data_saida is None:
        data_saida = reserva['data_saida']
        
    if not verificar_disponibilidade(
        quarto_id,
        data_entrada,
        data_saida,
        id
    ):
        return "Quarto não está disponível"
    
    if not consulta_hospede_id(hospede_id):
        return "Hóspede não encontrado"

    quarto = consulta_quarto_id(quarto_id)

    if not quarto:
        return "Quarto não encontrado"

    if quarto["status"] == "Manutenção":
        return "Quarto em manutenção"

    try:
        entrada = datetime.strptime(str(data_entrada), "%Y-%m-%d")
        saida = datetime.strptime(str(data_saida), "%Y-%m-%d")
    except:
        return "Data inválida"
    
    if saida <= entrada:
        return "Data inválida"

    conexao = connection()
    cursor = conexao.cursor()


    try:
        sql = """
            UPDATE reservas
            SET hospede_id = %s,
                quarto_id = %s,
                data_entrada = %s,
                data_saida = %s
            WHERE id = %s
        """

        cursor.execute(sql, (
            hospede_id,
            quarto_id,
            data_entrada,
            data_saida,
            id
        ))

        conexao.commit()

        return True

    except Exception:
        return "Erro ao atualizar reserva"

    finally:
        cursor.close()
        conexao.close()


def delete_reserva(id):
    
    if not consulta_reserva_id(id):
        return "Reserva não existe"
    
    conexao = connection()
    cursor = conexao.cursor()
    
    try:
        
        sql = "DELETE FROM reservas WHERE id = %s"
        cursor.execute(sql, (id,))
        
        conexao.commit()
        
        return True
    
    except Exception:
        return "Erro ao excluir reserva"

    finally:
        cursor.close()
        conexao.close()
    
def verificar_disponibilidade(
    quarto_id,
    data_entrada,
    data_saida,
    reserva_id=None
):

    conexao = connection()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM reservas
        WHERE quarto_id = %s
        AND (
            data_entrada < %s
            AND data_saida > %s
        )
    """

    valores = [
        quarto_id,
        data_saida,
        data_entrada
    ]

    if reserva_id is not None:
        sql += " AND id != %s"
        valores.append(reserva_id)

    cursor.execute(sql, tuple(valores))

    reserva = cursor.fetchone()

    cursor.close()
    conexao.close()

    return reserva is None