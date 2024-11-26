import requests

def get_survey_answers(survey_id):
    # URL base de la API
    base_url = "https://qs28.qservus.com/api/surveys/"
    url = f"{base_url}{survey_id}/answers/"
    
    # Token de autenticación
    headers = {
        "Authorization": "Token e7ba35e0954f17aea1e333762ec19a6d091f0903"
    }
    
    try:
        # Solicitud GET
        response = requests.get(url, headers=headers)
        
        # Verificar si la respuesta fue exitosa
        if response.status_code == 200:
            print("Datos obtenidos exitosamente:")
            return response.json()  # Retorna los datos en formato JSON
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None

if __name__ == "__main__":
    # Solicitar ID de la encuesta al usuario
    survey_id = input("Introduce el ID de la encuesta: ")
    data = get_survey_answers(survey_id)
    
    # Mostrar los datos obtenidos
    if data:
        print(data)
        
    print('\n',30 * '*', '* Fin del Proceso *', 30 * '*','\n')