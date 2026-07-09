"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd


def pregunta_12():

     tabla = pd.read_csv("files/input/tbl2.tsv", sep="\t")
     tabla["c5"] = tabla["c5a"].astype(str) + ":" + tabla["c5b"].astype(str)
     return tabla[["c0", "c5"]]
