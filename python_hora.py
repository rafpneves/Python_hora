from cgitb import enable
from distutils.command.clean import clean
import subprocess
import requests
import os
import time
from datetime import datetime
from subprocess import PIPE

# ========================================================================================================
# [Clear] 
def Clear():
  subprocess.run(["clear"])

# ========================================================================================================
# [Logo] 
def Logo():
  print("")
  print("                                   888    888                      d8888 ")
  print("                                   888    888                     d88888 ")
  print("                                   888    888                    d88P888 ")
  print("                                   8888888888  .d88b.  888d888  d88P 888 ")
  print("                                   888    888 d88  88b 888P    d88P  888 ")
  print("                                   888    888 888  888 888    d88P   888 ")
  print("                                   888    888 Y88..88P 888   d8888888888 ")
  print("                                   888    888   Y88P   888  d88P     888 ")
  print("")

# ========================================================================================================
# [Hora] pegar o tokem temporario para utilizar na API
def Hora():

  path = r"dado.txt"
  #print(path)
  
  ti_m = os.path.getatime(path)
  #print(f"meta dados:               {ti_m}")
  
  m_ti = time.ctime(ti_m)
  #print(f"Hora do arquivo {path}: {m_ti}")
  
  t_obj = time.strptime(m_ti)
  #print(f"Hora time.struct_time:    {t_obj}")
  
  T_Doc = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
  #print(f"Hora do arquivo {path}: {T_Doc}")

  # Filtrando hora
  T_Doc = (T_Doc[11:])
  #print(f"Hora filtrada:            {T_Doc}")
  
  # Pegando hora atual
  T_hora = str(datetime.today())
  #print(f"Hora do Servidor:         {T_hora}")
  
  # Filtrando Hora atual
  T_hora = (T_hora[11:19])
  #print(f"Hora filtrada:            {T_hora}")

  # Convertendo as variaveis para [int]
  time_1 = datetime.strptime(T_Doc, "%H:%M:%S")
  time_2 = datetime.strptime(T_hora, "%H:%M:%S")  
  time_interval = time_2 - time_1
  time_interval = str(time_interval)
  time_interval2 = (time_interval[:1])
  
  if time_interval2 == "-":
    process = subprocess.Popen("./ping.sh",stdout=PIPE, stderr=PIPE)
  else:
    if time_interval > "0:00:20": # Teste correto e [ < ]
      print("                         ---------------------------------------------------------")
      print("                                        === Verificador de Hora ===")
      print(f"                                         Hora do arquivo: {T_Doc}")
      print(f"                                            Hora atual: {T_hora}")
      print(f"                                    Hora de ultima atualização: {time_interval}\n")
      print("                               { Tempo do arquivo inrregular Exe arquivo... }\n")
      process = subprocess.Popen("./ping.sh",stdout=PIPE, stderr=PIPE)
      output, error = process.communicate()
      print("                                          === [ Script Rodado ] ===\n")
      subprocess.run(["cat" , "dado.txt"])
      process.kill
    else:
      print("                         ---------------------------------------------------------")
      print("                                        === Verificador de Hora ===")
      print(f"                                         Hora do arquivo: {T_Doc}")
      print(f"                                            Hora atual: {T_hora}")
      print(f"                                    Hora de ultima atualização: {time_interval}\n")
      print("                                     === [ Script dentro do tempo ] ===\n")
      subprocess.run(["cat" , "dado.txt"])


if __name__ == "__main__":
  Clear()
  Logo()
  Hora()

  

