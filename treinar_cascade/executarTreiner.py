import os

try:
    comando = 'python -m pip install -r requiriments.txt'
    os.system(comando)
except:
    comando = 'py -m pip install -r requiriments.txt'
    os.system(comando)

comando = 'python download.py'
os.system(comando)

comando = 'python imgFeia.py'
os.system(comando)

comando = 'python renomear.py'
os.system(comando)

comando = 'python listar.py'
os.system(comando)

comando = 'python amostras.py'
os.system(comando)

comando = 'python vetores.py'
os.system(comando)

comando = 'python treinar.py'
os.system(comando)

print("CONCLUIDO")