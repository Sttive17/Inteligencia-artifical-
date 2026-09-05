def calcular_rendimiento(cultivo):
    """
    Retorna la producción por hectárea de un cultivo.
    """
    if cultivo["hectareas"] == 0:
        return 0
    return cultivo["produccion_toneladas"] / cultivo["hectareas"]

def mostrar_cultivos(lista_cultivos):
    """
    Recorre la lista y muestra el nombre y el rendimiento de cada cultivo con un mensaje formateado.
    """
    print("--- Rendimiento de Cultivos ---")
    for cultivo in lista_cultivos:
        rendimiento = calcular_rendimiento(cultivo)
        print(f"Cultivo: {cultivo['nombre']} | Rendimiento: {rendimiento:.2f} ton/ha")
    print("-------------------------------\n")

def cultivo_mayor_rendimiento(lista_cultivos):
    """
    Retorna el nombre del cultivo con mayor rendimiento.
    """
    if not lista_cultivos:
        return None
        
    mayor_cultivo = lista_cultivos[0]
    mayor_rend = calcular_rendimiento(mayor_cultivo)
    
    for cultivo in lista_cultivos[1:]:
        rend = calcular_rendimiento(cultivo)
        if rend > mayor_rend:
            mayor_rend = rend
            mayor_cultivo = cultivo
            
    return mayor_cultivo["nombre"]

if __name__ == "__main__":
    # Lista de diccionarios con datos de cultivos
    cultivos_cartago = [
        {"nombre": "Café", "hectareas": 5, "produccion_toneladas": 3.2},
        {"nombre": "Caña", "hectareas": 10, "produccion_toneladas": 8.5},
        {"nombre": "Maíz", "hectareas": 3, "produccion_toneladas": 1.8},
        {"nombre": "Plátano", "hectareas": 4, "produccion_toneladas": 2.5},
        {"nombre": "Frijol", "hectareas": 2, "produccion_toneladas": 1.1}
    ]

    # Llamar a mostrar_cultivos() para ver todos los datos
    mostrar_cultivos(cultivos_cartago)

    # Llamar a cultivo_mayor_rendimiento() y mostrar el resultado
    mejor_cultivo = cultivo_mayor_rendimiento(cultivos_cartago)
    print(f"El cultivo con mayor rendimiento es: {mejor_cultivo}")
