#Aqui irei realizar a atividade extra em criar um script de backup de arquivos

import shutil
import os

#As pastas não existiam, então o Python criou essas, certo? Mas funciona caso tenha um arquivo existente.
pasta_origem = "meus_documentos"
pasta_backup = "backup_sistema"

#Aqui vai ser a pasta de origem e um arquivo de teste.
if not os.path.exists(pasta_origem):
    os.makedirs(pasta_origem)
    with open(f"{pasta_origem}/projeto_video.txt", "w") as f:
        f.write("Pastas & Pressets para os videos.")
        #no caso acho que funcionaria se usase p f.read também.

#Utilizando o tratamento de erros, vamos realizar o backup para não haver erros.
try:
    # Verificamos se a pasta de backup já existe
    if os.path.exists(pasta_backup):
      # Se já existe, removemos para criar uma cópia fresca (opcional)
      shutil.rmtree(pasta_backup)
    
    # Neste comando, ele copia a pasta inteira da origem para o destino
    shutil.copytree(pasta_origem, pasta_backup)

    print(f"\n--- Backup concluído com sucesso! 💾🤙 ---")
    print(f"Arquivos copiados de '{pasta_origem}' para '{pasta_backup}' ")

except Exception as e:
    print(f"\nErro ao realizar o backup: {e}")
