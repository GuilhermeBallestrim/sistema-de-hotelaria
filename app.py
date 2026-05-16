from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Form
from fastapi.responses import RedirectResponse
from model import *
app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "request": request
        }
    )

    
@app.get("/add_hospede")
def add_hospede_page(request: Request):

    return templates.TemplateResponse(
        request,
        "add_hospede.html",
        {
            "request": request
        }
    )
    
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

    
@app.post("/add_hospede")
def add_hospede_route(
    nome: str = Form(),
    email: str = Form(),
    telefone: str = Form(),
    cpf: str = Form()
):

    add_hospede(nome, email, telefone, cpf)

    return RedirectResponse(
        "/hospedes",
        status_code=303
    )
    
@app.get("/delete_hospede/{id}")
def delete_hospede_route(id: int):

    delete_hospede(id)

    return RedirectResponse(
        "/hospedes",
        status_code=303
    )    

    
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
    
@app.get("/add_quarto")
def add_quarto_page(request: Request):

    return templates.TemplateResponse(
        request,
        "add_quarto.html",
        {
            "request": request
        }
    )
    
@app.post("/add_quarto")
def add_quarto_route(
    numero: int = Form(),
    tipo: str = Form(),
    valor_diaria: float = Form(),
    status: str = Form()
):

    add_quarto(numero, tipo, valor_diaria, status)

    return RedirectResponse(
        "/quartos",
        status_code=303
    )
    
@app.get("/delete_quarto")
def delete_quarto_page(request: Request):

    return templates.TemplateResponse(
        request,
        "delete_quarto.html",
        {
            "request": request
        }
    )

@app.post("/delete_quarto")
def delete_quarto_route(
    id: int = Form()
):

    delete_quarto(id)

    return RedirectResponse(
        "/quartos",
        status_code=303
    )