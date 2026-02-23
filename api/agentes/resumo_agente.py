import os
from dotenv import load_dotenv

# CARREGAR .ENV COM CAMINHO ABSOLUTO
ENV_PATH = r"C:\Users\rapha\OneDrive\Área de Trabalho\estudos-ia\api\.env"
load_dotenv(ENV_PATH)
print("AGENTE.LOAD_OK =", os.getenv("OPENAI_API_KEY"))

# -----------------------------------

# based on agente.py but trimmed for organization
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, END
from tools.resumo_tool import resumir_tool
from logging_config import logger

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

class State(dict):
    messages: list

def agente_node(state: State):
    texto = state["messages"][-1].content
    logger.info(f"[AGENTE] Recebido texto (300 chars): {texto[:300]}")
    resultado = resumir_tool.invoke({"texto": texto})
    logger.info(f"[AGENTE] Resultado gerado (300 chars): {resultado[:300]}")
    return {"messages": [AIMessage(content=resultado)]}

graph = StateGraph(State)
graph.add_node("agente", agente_node)
graph.set_entry_point("agente")
graph.add_edge("agente", END)
agent_resumo = graph.compile()

def executar_resumo(texto: str):
    result = agent_resumo.invoke({
        "messages": [HumanMessage(content=texto)]
    })
    return result["messages"][-1].content
