from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from model import *

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


# ==================================================
# HOME
# ==================================================

@app.get("/")
def home(request: Request):

    qtd_hospedes = len(consulta_hospedes())
    qtd_quartos = len(consulta_quartos())
    qtd_reservas = len(consulta_reservas())

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "request": request,
            "qtd_hospedes": qtd_hospedes,
            "qtd_quartos": qtd_quartos,
            "qtd_reservas": qtd_reservas
        }
    )


# ==================================================
# HOSPEDES
# ==================================================

# LISTAR
@app.get("/hospedes")
def hospedes(request: Request):

    dados = consulta_hospedes()

    return templates.TemplateResponse(
        request,
        "hospedes.html",
        {
            "request": request,
            "hospedes": dados
        }
    )


# PAGINA ADD
@app.get("/add_hospede")
def add_hospede_page(request: Request):

    return templates.TemplateResponse(
        request,
        "add_hospede.html",
        {
            "request": request
        }
    )


# ADD
@app.post("/add_hospede")
def add_hospede_route(
    request: Request,
    nome: str = Form(),
    email: str = Form(),
    telefone: str = Form(),
    cpf: str = Form()
):

    resultado = add_hospede(
        nome,
        email,
        telefone,
        cpf
    )

    if resultado != True:

        return templates.TemplateResponse(
            request,
            "add_hospede.html",
            {
                "request": request,
                "erro": resultado
            }
        )

    return RedirectResponse(
        "/hospedes",
        status_code=303
    )

# PAGINA EDIT
@app.get("/edit_hospede/{id}")
def edit_hospede_page(request: Request, id: int):

    hospede = consulta_hospede_id(id)

    return templates.TemplateResponse(
        request,
        "edit_hospede.html",
        {
            "request": request,
            "hospede": hospede
        }
    )


# EDIT
@app.post("/edit_hospede/{id}")
def edit_hospede_route(
    request: Request,
    id: int,
    nome: str = Form(),
    email: str = Form(),
    telefone: str = Form(),
    cpf: str = Form()
):

    resultado = update_hospede(
        id,
        nome,
        email,
        telefone,
        cpf
    )

    if resultado != True:

        hospede = consulta_hospede_id(id)

        return templates.TemplateResponse(
            request,
            "edit_hospede.html",
            {
                "request": request,
                "erro": resultado,
                "hospede": hospede
            }
        )

    return RedirectResponse(
        "/hospedes",
        status_code=303
    )


# DELETE
@app.get("/delete_hospede/{id}")
def delete_hospede_route(id: int):

    delete_hospede(id)

    return RedirectResponse(
        "/hospedes",
        status_code=303
    )


# ==================================================
# QUARTOS
# ==================================================

# LISTAR
@app.get("/quartos")
def quartos(request: Request):

    dados = consulta_quartos()

    return templates.TemplateResponse(
        request,
        "quartos.html",
        {
            "request": request,
            "quartos": dados
        }
    )


# PAGINA ADD
@app.get("/add_quarto")
def add_quarto_page(request: Request):

    return templates.TemplateResponse(
        request,
        "add_quarto.html",
        {
            "request": request
        }
    )


# ADD
@app.post("/add_quarto")
def add_quarto_route(
    request: Request,
    numero: int = Form(None),
    tipo: str = Form(None),
    valor_diaria: float = Form(None),
    status: str = Form(None)
):
    
    if not numero or not tipo or not valor_diaria or not status:
            
            return RedirectResponse(
                "/add_quarto",
                status_code=303
            )

    resultado = add_quarto(numero, tipo, valor_diaria, status)

    if resultado != True:
        return templates.TemplateResponse(
            request,
            "add_quarto.html",
            {
                "request": request,
                "erro": resultado
            }
        )

    
    return RedirectResponse(
        "/quartos",
        status_code=303
    )


# PAGINA EDIT
@app.get("/edit_quarto/{id}")
def edit_quarto_page(request: Request, id: int):

    quarto = consulta_quarto_id(id)

    return templates.TemplateResponse(
        request,
        "edit_quarto.html",
        {
            "request": request,
            "quarto": quarto
        }
    )


# EDIT
@app.post("/edit_quarto/{id}")
def edit_quarto_route(
    request: Request,
    id: int,
    numero: int = Form(),
    tipo: str = Form(),
    valor_diaria: float = Form(),
    status: str = Form()
):

    resultado = update_quarto(
        id,
        numero,
        tipo,
        valor_diaria,
        status
    )

    if resultado != True:

        quarto = consulta_quarto_id(id)

        return templates.TemplateResponse(
            request,
            "edit_quarto.html",
            {
                "request": request,
                "erro": resultado,
                "quarto": quarto
            }
        )

    return RedirectResponse(
        "/quartos",
        status_code=303
    )


# DELETE
@app.get("/delete_quarto/{id}")
def delete_quarto_route(id: int):

    delete_quarto(id)

    return RedirectResponse(
        "/quartos",
        status_code=303
    )


# ==================================================
# RESERVAS
# ==================================================

# LISTAR
@app.get("/reservas")
def reservas(request: Request):

    dados = consulta_reservas()

    return templates.TemplateResponse(
        request,
        "reservas.html",
        {
            "request": request,
            "reservas": dados
        }
    )


# PAGINA ADD
@app.get("/add_reserva")
def add_reserva_page(request: Request):

    hospedes = consulta_hospedes()
    quartos = consulta_quartos()

    return templates.TemplateResponse(
        request,
        "add_reserva.html",
        {
            "request": request,
            "hospedes": hospedes,
            "quartos": quartos
        }
    )


# ADD
@app.post("/add_reserva")
def add_reserva_route(
    request: Request,
    hospede_id: int = Form(),
    quarto_id: int = Form(),
    data_entrada: str = Form(),
    data_saida: str = Form()
):

    resultado = add_reserva(
        hospede_id,
        quarto_id,
        data_entrada,
        data_saida
    )

    if resultado != True:

        hospedes = consulta_hospedes()
        quartos = consulta_quartos()

        return templates.TemplateResponse(
            request,
            "add_reserva.html",
            {
                "request": request,
                "erro": resultado,
                "hospedes": hospedes,
                "quartos": quartos
            }
        )

    return RedirectResponse(
        "/reservas",
        status_code=303
    )

# PAGINA EDIT
@app.get("/edit_reserva/{id}")
def edit_reserva_page(request: Request, id: int):

    reserva = consulta_reserva_id(id)
    hospedes = consulta_hospedes()
    quartos = consulta_quartos()

    return templates.TemplateResponse(
        request,
        "edit_reserva.html",
        {
            "request": request,
            "reserva": reserva,
            "hospedes": hospedes,
            "quartos": quartos
        }
    )


# EDIT
@app.post("/edit_reserva/{id}")
def edit_reserva_route(
    request: Request,
    id: int,
    hospede_id: int = Form(),
    quarto_id: int = Form(),
    data_entrada: str = Form(),
    data_saida: str = Form()
):

    resultado = update_reserva(
        id,
        hospede_id,
        quarto_id,
        data_entrada,
        data_saida
    )

    if resultado != True:

        reserva = consulta_reserva_id(id)

        hospedes = consulta_hospedes()
        quartos = consulta_quartos()

        return templates.TemplateResponse(
            request,
            "edit_reserva.html",
            {
                "request": request,
                "erro": resultado,
                "reserva": reserva,
                "hospedes": hospedes,
                "quartos": quartos
            }
        )

    return RedirectResponse(
        "/reservas",
        status_code=303
    )


# DELETE
@app.get("/delete_reserva/{id}")
def delete_reserva_route(id: int):

    delete_reserva(id)

    return RedirectResponse(
        "/reservas",
        status_code=303
    )


@app.get("/view_reserva/{id}")
def view_reserva(request: Request, id: int):

    reserva = consulta_reserva_id(id)

    if not reserva:
        return RedirectResponse(
            "/reservas",
            status_code=303
        )

    hospede = consulta_hospede_id(
        reserva["hospede_id"]
    )

    quarto = consulta_quarto_id(
        reserva["quarto_id"]
    )

    if not reserva.get("data_entrada") or not reserva.get("data_saida"):

        dias = 0
        valor_total = 0

    else:

        entrada = reserva["data_entrada"]
        saida = reserva["data_saida"]

        dias = (saida - entrada).days

        valor_total = (
            dias * quarto["valor_diaria"]
        )

    return templates.TemplateResponse(
        request,
        "view_reserva.html",
        {
            "request": request,
            "reserva": reserva,
            "hospede": hospede,
            "quarto": quarto,
            "dias": dias,
            "valor_total": valor_total
        }
    )