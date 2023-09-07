import sys, os, csv
sys.path.append(r'C:\Users\Filipe\Desktop\Python\AI\SPRINT-3\consts')
os.chdir(r'C:\Users\Filipe\Desktop\Python\AI\SPRINT-3\scripts')
import cx_Oracle
import constants

def read_txt_file(txt):
    with open(txt, "r") as f: 
        return f.read()

prompt = read_txt_file('prompt.txt')
def conecta_orcl():
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

                query = "SELECT * FROM CG_TB_PRODUTOS"
                cursor.execute(query)
                
                with open("input_treino.txt", "w", newline="") as txtfile:
                    txtfile.write(prompt)
                    
                    writer = csv.writer(txtfile, delimiter="\t")
                    
                    colunas = [desc[0] for desc in cursor.description]
                    writer.writerow(colunas)
                    
                    for row in cursor:
                        writer.writerow(row)
        
        print('Criação do arquivo input_treino - OK')

    except cx_Oracle.DatabaseError as e:
        print("Erro de banco de dados ocorreu:", e)

    except Exception as e:
        print("Erro ocorreu:", e)