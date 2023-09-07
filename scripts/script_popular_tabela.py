import cx_Oracle
import sys, os
sys.path.append(r'C:\Users\Filipe\Desktop\Python\AI\SPRINT-3\consts')
os.chdir(r'C:\Users\Filipe\Desktop\Python\AI\SPRINT-3\scripts')
import constants

import csv

def read_produtos(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 4:
                nome, marca, descricao, preco = row
                yield nome, marca, descricao, float(preco)
            else:
                print(f"Skipping malformed row: {row}")



def popular_tabelas():
    try:
        dsn = cx_Oracle.makedsn(
            constants.ORACLE_HOST,
            constants.ORACLE_PORT,
            constants.ORACLE_SID
        )

        with cx_Oracle.connect(
            user=constants.ORACLE_USER,
            password=constants.ORACLE_PASSWORD,
            dsn=dsn
        ) as conn:
            with conn.cursor() as cursor:
                
                for nome, marca, descricao, preco in read_produtos('script_produtos.txt'):
                    insert_sql = """ 
                    BEGIN
                    INSERT INTO CG_TB_PRODUTOS (NOME, MARCA, DESCRICAO, PRECO)
                    VALUES (:nome, :marca, :descricao, :preco);
                    COMMIT;
                    END;
                    """

                    cursor.execute(insert_sql, nome=nome, marca=marca, descricao=descricao, preco=preco)
                
                print('Inserção de itens na tabela produtos - OK.')

    except cx_Oracle.DatabaseError as e:
        print('Erro ao inserir produtos.')
        print(f"Log => {e}")

