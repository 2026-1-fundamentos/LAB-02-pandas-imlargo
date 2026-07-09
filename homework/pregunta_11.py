"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd


def pregunta_11():
    tbl1 = pd.read_csv("files/input/tbl1.tsv", sep="\t")

    return (
        tbl1.sort_values(["c0", "c4"]).groupby("c0").agg({"c4": ",".join}).reset_index()
    )
