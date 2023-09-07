import subprocess, os
os.chdir(r'C:\Users\Filipe\Desktop\Python\AI\SPRINT-3\scripts')


def instala_pacotes():
    packages = ['langchain', 'cx_Oracle', 'chromadb', 'tiktoken', 'unstructured', 'Flask', 'Flask-Bootstrap', 'Flask-Session']
    for package in packages:
        subprocess.run(["pip", "install", package])
