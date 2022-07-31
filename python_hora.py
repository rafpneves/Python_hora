from cgitb import enable
import subprocess
import requests
import os
import time
from datetime import datetime
from subprocess import PIPE

# ========================================================================================================
# [global_coleta] pegar o tokem temporario para utilizar na API
def global_hora():
  global time_interval
  path = r"dado.txt"
  ti_m = os.path.getatime(path)
  m_ti = time.ctime(ti_m)
  t_obj = time.strptime(m_ti)
  T_Doc = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)

  # Filtrando hora
  T_Doc = (T_Doc[11:])
  
  # Pegando hora atual
  T_hora = str(datetime.today())
  
  # Filtrando Hora atual
  T_hora = (T_hora[11:19])

  # Convertendo as variaveis para [int]
  time_1 = datetime.strptime(T_Doc, "%H:%M:%S")
  time_2 = datetime.strptime(T_hora, "%H:%M:%S")
  print(f"Dados do arquivo {time_1}")
  print(f"Dados do sistema {time_2}")
  
  time_interval = time_2 - time_1
  time_interval = str(time_interval)

  time_interval2 = (time_interval[:1])
  
  if time_interval2 == "-":
    process = subprocess.Popen("./ping.sh",stdout=PIPE, stderr=PIPE)
  else:
    if time_interval > "0:59:00": # Teste correto e [ < ]
      print("                         ---------------------------------------------------------")
      print("                                      === Verificador de Token_temp ===")
      print(f"                                         Hora do arquivo: {T_Doc}")
      print(f"                                            Hora atual: {T_hora}")
      print(f"                                    Hora de ultima atualização: {time_interval}\n")
      print("                                     { Token Erro - Criando novo Token... }\n")
      process = subprocess.Popen("./ping.sh",stdout=PIPE, stderr=PIPE)
      output, error = process.communicate()
      print("                                          === [ Token Valido ] ===\n")
      subprocess.run(["cat" , "dado.txt"])
      process.kill
    else:
      print("                         ---------------------------------------------------------")
      print("                                     === Verificador de Token_temp ===")
      print(f"                                         Hora do arquivo: {T_Doc}")
      print(f"                                            Hora atual: {T_hora}")
      print(f"                                    Hora de ultima atualização: {time_interval}\n")
      print("                                          === [ Token Valido ] ===\n")
      subprocess.run(["cat" , "dado.txt"])


if __name__ == "__main__":
  global_hora()

  

