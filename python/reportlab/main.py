"""
Estudo sobre a biblioteca ReportLab
Geração de PDFs com o Python

Observações:
As dimensões da folha A4 são 210 x 297 mm
"""

# Imports

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

# Constants

FACTOR2CONVERTION = 0.3527777778

# Directory

path = os.path.dirname(__file__)

# Auxiliary Functions

def mm2points(valor: float) -> float:
    return valor/FACTOR2CONVERTION

# Report

cnv = canvas.Canvas(path+'\\report.pdf', pagesize=A4)
cnv.drawImage(path+'\\logo_python.png', mm2points(0), mm2points(0), width=mm2points(50), height=mm2points(50))
cnv.drawString(mm2points(100), mm2points(100), 'Meu primeiro relatório')
cnv.save()
