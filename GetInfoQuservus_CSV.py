import requests
import csv

# Configuración de la API y token
BASE_URL = "https://qs28.qservus.com/api/surveys/{}/answers/"
TOKEN = "e7ba35e0954f17aea1e333762ec19a6d091f0903"

# Función para obtener los datos de la API
def obtener_datos_api(survey_id):
    url = BASE_URL.format(survey_id)
    headers = {
        "Authorization": f"Token {TOKEN}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanza un error si la respuesta no es 200
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectarse a la API: {e}")
        return None

# Función para guardar los datos en un archivo CSV
def guardar_datos_csv(datos, nombre_archivo):
    if not datos:
        print("No hay datos para guardar.")
        return
    
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=';')
            
            # Escribir encabezados
            encabezados = datos['results'][0].keys().mapping # if isinstance(datos, list) and datos else datos.keys()
            writer.writerow(encabezados)
            
            # Escribir datos
            if isinstance(datos, list):
                for fila in datos:
                    writer.writerow(fila.values())
            else:
                writer.writerow(datos.values())
        
        print(f"Datos guardados en el archivo: {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar los datos en CSV: {e}")

# Main
def main():
    survey_id = input("Ingrese el ID de la encuesta: ")
    datos = obtener_datos_api(survey_id)
    if datos:
        archivo_salida = f"encuesta_{survey_id}.csv"
        guardar_datos_csv(datos, archivo_salida)

if __name__ == "__main__":
    main()
    
    print('\n',30 * '*', '* Fin del Proceso *', 30 * '*','\n')
