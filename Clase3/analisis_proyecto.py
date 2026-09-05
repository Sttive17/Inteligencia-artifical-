import csv
import os

def cargar_datos_pavia(ruta_archivo):
    """Lee el CSV de daños viales y retorna una lista de diccionarios con tipos de datos correctos."""
    datos = []
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                fila['id_reporte'] = int(fila['id_reporte'])
                fila['severidad'] = int(fila['severidad'])
                fila['area_m2'] = float(fila['area_m2'])
                fila['costo_reparacion_cop'] = float(fila['costo_reparacion_cop'])
                datos.append(fila)
    except FileNotFoundError:
        print(f"Error: No se encontró {ruta_archivo}")
    return datos

def calcular_estadisticas_proyecto(datos):
    """Calcula 5 estadísticas relevantes para el proyecto PAVIA."""
    if not datos:
        return None
        
    total_reportes = len(datos)
    costos = [d['costo_reparacion_cop'] for d in datos]
    severidades = [d['severidad'] for d in datos]
    areas = [d['area_m2'] for d in datos]
    
    # 1. Total de dinero requerido
    costo_total = sum(costos)
    
    # 2. Promedio de costo por reparación
    costo_promedio = costo_total / total_reportes
    
    # 3. Costo máximo de reparación
    costo_maximo = max(costos)
    
    # 4. Severidad promedio de los huecos
    severidad_promedio = sum(severidades) / total_reportes
    
    # 5. Área total afectada en metros cuadrados
    area_total = sum(areas)
    
    # Reportes críticos
    reportes_criticos = sum(1 for d in datos if d['prioridad'] == 'Critica')
    
    return {
        "total_reportes": total_reportes,
        "costo_total": costo_total,
        "costo_promedio": costo_promedio,
        "costo_maximo": costo_maximo,
        "severidad_promedio": severidad_promedio,
        "area_total": area_total,
        "reportes_criticos": reportes_criticos
    }

def generar_informe_markdown(stats, archivo_salida):
    """Genera el informe de resultados en formato Markdown."""
    if not stats:
        return
        
    contenido = f"""# Informe de Análisis de Datos — Proyecto PAVIA

**Plataforma Inteligente para la Gestión del Deterioro Vial en Cartago, Valle del Cauca**  
**Asignatura:** Inteligencia Artificial (Semestre VI)

---

## 1. Descripción de los Datos
El conjunto de datos contiene {stats['total_reportes']} reportes georreferenciados de daños viales en diversos barrios del municipio de Cartago. Cada registro incluye información como el tipo de daño (hueco profundo, grieta, hundimiento), nivel de severidad (1-10), área afectada en metros cuadrados y costo estimado de reparación.

## 2. Estadísticas Calculadas

| Métrica | Valor |
|---------|-------|
| **Total de reportes viales analizados** | {stats['total_reportes']} |
| **Costo total de intervención** | ${stats['costo_total']:,.2f} COP |
| **Costo promedio por reparación** | ${stats['costo_promedio']:,.2f} COP |
| **Daño con mayor costo de reparación** | ${stats['costo_maximo']:,.2f} COP |
| **Nivel de severidad promedio** | {stats['severidad_promedio']:.2f} / 10 |
| **Área total afectada** | {stats['area_total']:.2f} m² |
| **Reportes en prioridad Crítica** | {stats['reportes_criticos']} |

## 3. Interpretación de Resultados
1. **Alta severidad promedio:** Un nivel de severidad de {stats['severidad_promedio']:.2f} sobre 10 indica que los daños reportados representan un riesgo considerable para motociclistas y vehículos particulares.
2. **Impacto económico:** El costo promedio de reparación por hueco asciende a ${stats['costo_promedio']:,.0f} COP. Identificar estos daños tempranamente con IA permitirá a la alcaldía repararlos antes de que el costo aumente.
3. **Casos críticos:** Contamos con {stats['reportes_criticos']} casos de prioridad crítica que requieren atención inmediata. Estos serán los primeros en ser clasificados por nuestro modelo predictivo.
"""
    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.write(contenido)

if __name__ == "__main__":
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_csv = os.path.join(directorio_actual, "datos_pavia.csv")
    archivo_md = os.path.join(directorio_actual, "informe_proyecto.md")
    
    datos = cargar_datos_pavia(archivo_csv)
    estadisticas = calcular_estadisticas_proyecto(datos)
    
    if estadisticas:
        generar_informe_markdown(estadisticas, archivo_md)
        print("El informe del proyecto ha sido generado con éxito en: informe_proyecto.md")
