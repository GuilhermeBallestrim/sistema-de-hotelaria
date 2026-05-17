# Sistema de Hotelaria

Sistema de gerenciamento de hotelaria desenvolvido com Flask, MySQL, HTML e CSS.

## Funcionalidades

- Cadastro de hóspedes
- Cadastro de quartos
- Cadastro de reservas
- Edição e exclusão de registros
- Verificação de disponibilidade de quartos
- Dashboard do sistema

---

# Tecnologias Utilizadas

- Python
- Flask
- MySQL
- HTML5
- CSS3
- Jinja2

---

# Instalação

## 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
````

## 2. Criar ambiente virtual

```bash
python -m venv venv
```

## 3. Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

# Instalar dependências

```bash
pip install flask mysql-connector-python
```

---

# Banco de Dados

1. Abra o MySQL
2. Execute o arquivo:

```text
hotelaria.sql
```

---

# Configuração da conexão

No arquivo `dao.py`, configure:

```python
host=""
user=""
password=""
database=""
```

com os dados do seu MySQL.

---

# Executar o projeto

```bash
python app.py
```

O sistema estará disponível em:

```text
http://127.0.0.1:5000
```

```
