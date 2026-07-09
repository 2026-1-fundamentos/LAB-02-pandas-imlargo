"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd


def pregunta_10():


    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")

    return (
        tbl0.sort_values(["c1", "c2"])
        .astype({"c2": str})
        .groupby("c1")
        .agg({"c2": ":".join})
    )
