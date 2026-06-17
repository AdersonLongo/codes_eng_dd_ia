import os
import sys
from datetime import datetime


def obter_info_sistema() -> dict:
    return {
        "sistema: ": sys.platform,
        "diretorio: : os.getcwd,
        "data: ": datetime.now().isoformat(),
    }
