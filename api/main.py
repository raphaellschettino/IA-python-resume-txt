import os
from dotenv import load_dotenv

# CARREGAR .ENV MANUALMENTE
ENV_PATH = r"C:\Users\rapha\OneDrive\Área de Trabalho\estudos-ia\api\.env"
load_dotenv(ENV_PATH)
print("MAIN.LOAD_OK =", os.getenv("OPENAI_API_KEY"))

from fastapi import FastAPI, UploadFile, File
from routes.resumo_route import router as resumo_router
from routes.txt_route import router as txt_router
from routes.pdf_route import router as pdf_router
from logging_config import logger

app = FastAPI()

app.include_router(resumo_router)
app.include_router(txt_router)
app.include_router(pdf_router)
