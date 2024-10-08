import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
from moduloPelicula import moduloPelicula
from moduloPersonaje import moduloPersonaje
from moduloVehiculo import moduloVehiculo
from moduloEspecie import moduloEspecie
from moduloNave import moduloNave
from moduloPlaneta import moduloPlaneta
response_especies = requests.get("https://www.swapi.tech/api/species/")
response_peliculas = requests.get("https://www.swapi.tech/api/films")
response_planetas = requests.get("https://www.swapi.tech/api/planets")
response_personajes = requests.get("https://www.swapi.tech/api/people")
response_naves = requests.get("https://www.swapi.tech/api/starships")
response_vehiculos = requests.get("https://www.swapi.tech/api/vehicles")

peliculas = moduloPelicula(response_peliculas)
vehiculos = moduloVehiculo(response_vehiculos)
naves = moduloNave(response_naves)
especies = moduloEspecie(response_especies, peliculas)
personajes = moduloPersonaje(response_personajes, peliculas, especies, naves, vehiculos)
planetas = moduloPlaneta(response_planetas, peliculas, personajes)

class moduloGraficos:
    def __init__(self, planetas, naves):
        self.planetas = planetas
        self.naves = naves

    def menuGraficos (self):
        while True:
            opcion_menu = input("\nBienvenido al módulo de gráficos y tablas. ¿Qué desea visualizar? \n1. Cantidad de personajes originarios de cada planeta \n2. Comparación longitud de naves \n3. Comparación capacidad de carga de naves \n4. Comparación de hiperimpulsor de naves \n5. Comparación MGLT de naves \n6. Estadísticas MGLT \n7. Estadisticas Hiperimpulsores \n8. Estadisticas Velocidad Maxima en Atmosfera \n9. Estadisticas Costos en Creditos \n10. Salir \n")

            if opcion_menu == "1":
                self.planetas.mostrar_grafico()

            elif opcion_menu == "2":
                self.naves.grafico_longitud()

            elif opcion_menu == "3":
                self.naves.grafico_capacidad_carga()

            elif opcion_menu == "4":
                self.naves.grafico_hiperimpulsor()

            elif opcion_menu == "5":
                self.naves.grafico_MGLT()

            elif opcion_menu == "6":
                self.naves.generar_tabla_mglt()

            elif opcion_menu == "7":
                self.naves.generar_tabla_hiperimpulsor()

            elif opcion_menu == "8":
                self.naves.generar_tabla_velocidad()

            elif opcion_menu == "9":
                self.naves.generar_tabla_costo()

            elif opcion_menu == "10":
                print("¡Hasta luego!")
                break

            else: 
                print("\nIngrese una opción válida.")

'''
graficos = moduloGraficos(planetas, naves)
graficos.menuGraficos()
'''


