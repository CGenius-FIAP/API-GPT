import cx_Oracle
import sys, os
sys.path.append(r'C:\Users\Filipe\Desktop\Python\AI\SPRINT-3\consts')
os.chdir(r'C:\Users\Filipe\Desktop\Python\AI\SPRINT-3\scripts')

import constants

class InvalidDSNError(Exception):
    pass

def criar_tabelas():
    try:
        
        try:
            dsn = cx_Oracle.makedsn(
                constants.ORACLE_HOST,
                constants.ORACLE_PORT,
                constants.ORACLE_SID
            )
        except cx_Oracle.DatabaseError as e:
            raise InvalidDSNError("O DSN fornecido é inválido.") from e
        
        with cx_Oracle.connect(
            user = constants.ORACLE_USER,
            password = constants.ORACLE_PASSWORD,
            dsn = dsn) as conn:
            with conn.cursor() as cursor:

                create_table = """
                    CREATE TABLE CG_TB_PRODUTOS (
                        --ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        NOME VARCHAR2(255),
                        MARCA VARCHAR2(255),
                        DESCRICAO VARCHAR2(255),
                        PRECO NUMBER(12,2)
                    )
                """
                
                cursor.execute(create_table)
                print('Criação da tabela produtos - OK')

    except cx_Oracle.DatabaseError as e:
        print('Criação da tabela de produtos - ERRO\n\n')
        print(f'Log =>  {e}')
