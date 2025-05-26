from datetime import datetime
from database import obter_conexao
from endereco_repo import *
from models.endereco import Endereco
from sql.endereco_sql import CREATE_TABLE_ENDERECO, DELETE_ENDERECO, GET_ENDERECO_BY_ID, INSERT_ENDERECO, UPDATE_ENDERECO

def criar_tabela_enderecos():
    """Cria a tabela Endereco se ela não existir."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(CREATE_TABLE_ENDERECO)
    conexao.commit()
    conexao.close()
def inserir_endereco(endereco: Endereco) -> Endereco:
    """Insere um novo endereco no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(INSERT_ENDERECO, 
        (endereco.logradouro, endereco.numero, endereco.complemento, endereco.bairro, endereco.cidade, endereco.estado, endereco.cep))
    endereco.id = cursor.lastrowid
    conexao.commit()
    conexao.close()
    return endereco
def atualizar_endereco(endereco: Endereco) -> bool:
    """Atualiza um endereco existente no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(UPDATE_ENDERECO, 
        (endereco.logradouro, endereco.numero, endereco.complemento, endereco.bairro, endereco.cidade, endereco.estado, endereco.cep, endereco.id))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)
def excluir_endereco(id: int) -> bool:
    """Exclui um endereco do banco de dados pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(DELETE_ENDERECO, (id,))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)
def obter_endereco_por_id(id: int) -> Endereco:
    """Obtém um endereco pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(GET_ENDERECO_BY_ID, (id,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return Endereco(
            id=resultado[0],
            logradouro=resultado[1],
            numero=resultado[2],
            complemento=resultado[3],
            bairro=resultado[4],
            cidade=resultado[5],
            estado=resultado[6],
            cep=resultado[7]
        )
    return None