import sys, os
sys.path.append(r'C:\Users\Filipe\Desktop\Python\AI\SPRINT-3\consts')
os.chdir(r'C:\Users\Filipe\Desktop\Python\AI\SPRINT-3\scripts')

from scripts.script_criar_tabelas import criar_tabelas
from scripts.script_popular_tabela import popular_tabelas
from scripts.script_pips import instala_pacotes
from orcl_txt import conecta_orcl


# instala_pacotes()
criar_tabelas()
popular_tabelas()
conecta_orcl()


