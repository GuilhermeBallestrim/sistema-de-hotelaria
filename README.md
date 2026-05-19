# 🏨 Sistema de Hotelaria

Sistema de gerenciamento de hotelaria desenvolvido com FastAPI, MySQL, HTML, CSS e Jinja2.

O projeto permite o gerenciamento completo de:

- 👥 Hóspedes
- 🛏️ Quartos
- 📅 Reservas

Além disso, o sistema possui:

- Dashboard inicial
- Validações de formulário
- Mensagens de erro e sucesso
- Interface web responsiva
- Integração com banco de dados MySQL

---

# 🚀 Tecnologias Utilizadas

- Python
- FastAPI
- MySQL
- HTML5
- CSS3
- Jinja2
- Uvicorn

---

# 📁 Estrutura do Projeto

```bash
sistema-de-hotelaria/
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── hospedes.html
│   ├── quartos.html
│   ├── reservas.html
│   └── ...
│
├── app.py
├── model.py
├── dao.py
├── database.sql
├── requirements.txt
└── README.md
```

---

# ⚙️ Instalação do Projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/GuilhermeBallestrim/sistema-de-hotelaria
```

---

## 2. Acessar a pasta do projeto

```bash
cd sistema-de-hotelaria
```

---

## 3. Criar ambiente virtual

### Windows

```bash
python -m venv venv
```

---

## 4. Ativar ambiente virtual

### Windows

```bash
venv\Scripts\Activate.ps1
```

---

## 5. Instalar dependências

```bash
pip install -r requirements.txt
```

---

# 📦 Dependências

O projeto utiliza as seguintes bibliotecas:

```txt
fastapi
uvicorn
jinja2
python-multipart
mysql-connector-python
```

---

# 🗄️ Configuração do Banco de Dados

## 1. Abrir o MySQL Workbench

Ou outro gerenciador MySQL de sua preferência.

---

## 2. Executar o arquivo `hotelaria.sql`

O arquivo irá:

- Criar o banco de dados
- Criar as tabelas
- Criar os relacionamentos
- Inserir dados iniciais para testes

---

# 🔌 Configuração da Conexão MySQL

No arquivo `dao.py`, configure:

```python
host="localhost",
user="root",
password="",
database="hotelaria"
```

---

# ▶️ Executando o Projeto

No terminal, execute:

```bash
uvicorn app:app --reload
```

---

# 🌐 Acesso ao Sistema

Após iniciar o servidor:

```txt
http://127.0.0.1:8000
```

---

# 📌 Funcionalidades

## 👥 Hóspedes

- Listar hóspedes
- Adicionar hóspedes
- Editar hóspedes
- Excluir hóspedes
- Visualizar detalhes

---

## 🛏️ Quartos

- Listar quartos
- Adicionar quartos
- Editar quartos
- Excluir quartos
- Controle de status:
  - Disponível
  - Ocupado
  - Manutenção

---

## 📅 Reservas

- Criar reservas
- Editar reservas
- Excluir reservas
- Verificar disponibilidade
- Calcular diárias
- Calcular valor total

---

# 👨‍💻 Autores

Projeto desenvolvido para trabalho escolar, conduzido pelo professor Carlos.
Integrantes:
Guilherme Ballestrim Sobreira - Nº06
Guilherme Wallace Carturan Falcão - Nº08
João Vitor Alves da Costa - Nº11
John Wayne Gustão Tavares de Melo - Nº12
Lucas Silva Santos Costa - Nº17
Miguel Rosa Arantes - Nº21
