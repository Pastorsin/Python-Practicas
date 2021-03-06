#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import csv
import os


def exportar_csv_a_json(nombre):
    archivo_json = open(os.path.join("archivos", nombre) + ".json", "w")
    archivo_csv = open(os.path.join("archivos", nombre) + ".csv", "r")

    contenido_csv = csv.reader(archivo_csv)
    encabezado_csv = next(contenido_csv)
    lista_json = list()
    for fila in contenido_csv:
        lista_json.append(dict(zip(encabezado_csv, list(map(lambda x: x.strip() if x else '0' ,fila)))))
    json.dump(lista_json, archivo_json, ensure_ascii=False)


    archivo_json.close()
    archivo_csv.close()


def imprimir_json(nombre):
    archivo = open(os.path.join("archivos", nombre) + ".json", "r")
    datos = json.load(archivo)
    print((json.dumps(datos, sort_keys=True, indent=4, ensure_ascii=False)))
    archivo.close()

exportar_csv_a_json("Todas.las.carreras27032018")
imprimir_json("Todas.las.carreras27032018")
