"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd


def pregunta_12():

    tbl2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")

    return (
        tbl2.assign(c5=tbl2["c5a"] + ":" + tbl2["c5b"].astype(str))
        .sort_values(["c0", "c5"])
        .groupby("c0")
        .agg({"c5": ",".join})
        .reset_index()
    )
