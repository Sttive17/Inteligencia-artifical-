import csv
import os

def leer_datos(ruta_archivo):
    """
    Lee un archivo CSV y lo convierte en una lista de diccionarios.
    """
    datos = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Convertir los valores numéricos a float donde corresponda
                fila["hectareas_sembradas"] = float(fila["hectareas_sembradas"])
                fila["produccion_toneladas"] = float(fila["produccion_toneladas"])
                fila["anio"] = int(fila["anio"])
                datos.append(fila)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta_archivo}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        
    return datos

def mostrar_resumen(datos):
    """
    Muestra la cantidad total de registros y tres estadísticas básicas.
    """
    if not datos:
        print("No hay datos para analizar.")
        return

    total_registros = len(datos)
    
    # Calcular estadísticas básicas de producción
    producciones = [fila["produccion_toneladas"] for fila in datos]
    
    promedio_produccion = sum(producciones) / total_registros
    produccion_maxima = max(producciones)
    produccion_minima = min(producciones)
    
    print("\n--- Resumen de Datos de Cultivos (Cartago) ---")
    print(f"Cantidad total de registros: {total_registros}")
    print(f"Promedio de producción: {promedio_produccion:.2f} toneladas")
    print(f"Producción máxima: {produccion_maxima:.2f} toneladas")
    print(f"Producción mínima: {produccion_minima:.2f} toneladas")
    print("----------------------------------------------\n")

if __name__ == "__main__":
    # Asegurar que buscamos el archivo en el directorio correcto (donde se ejecuta el script)
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(directorio_actual, "datos_cartago.csv")
    
    print("Cargando datos...")
    lista_datos = leer_datos(ruta_csv)
    
    if lista_datos:
        mostrar_resumen(lista_datos)
