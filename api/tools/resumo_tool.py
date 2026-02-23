from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

@tool
def resumir_tool(texto: str) -> str:
    """Gera um resumo claro e direto do texto fornecido."""
    resposta = llm.invoke([
        HumanMessage(
            content=f"Resuma de maneira clara e direta:\n\n{texto}"
        )
    ])
    return resposta.content