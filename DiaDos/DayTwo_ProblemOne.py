def solve_gift_shop(input_data):
    """
    Calcula la suma de IDs inválidos basándose en rangos proporcionados.
    Un ID es inválido si consiste en una secuencia de dígitos repetida dos veces (ej. 1212).
    """
    
    # 1. Limpieza y parseo de la entrada
    # Eliminamos saltos de línea si existen y dividimos por comas
    ranges = input_data.replace('\n', '').split(',')
    
    total_invalid_sum = 0
    invalid_ids_found = []

    # 2. Iterar sobre cada rango
    for r in ranges:
        if not r.strip(): continue # Saltar entradas vacías
        
        # Obtener inicio y fin del rango
        start_str, end_str = r.split('-')
        start = int(start_str)
        end = int(end_str)
        
        # 3. Analizar números dentro del rango
        # Usamos range(start, end + 1) para inclusión
        for num in range(start, end + 1):
            s_num = str(num)
            length = len(s_num)
            
            # Condición 1: La longitud debe ser par
            if length % 2 != 0:
                continue
            
            # Condición 2: La primera mitad debe ser igual a la segunda
            half_index = length // 2
            first_half = s_num[:half_index]
            second_half = s_num[half_index:]
            
            if first_half == second_half:
                total_invalid_sum += num
                invalid_ids_found.append(num)

    return total_invalid_sum, invalid_ids_found

# --- Ejecución con los datos del ejemplo ---

input_string = """5529687-5587329,50-82,374-560,83-113,226375-287485,293169-368713,2034-2634,9945560-9993116,4872472-4904227,3218-5121,1074-1357,15451-26093,483468003-483498602,51513-85385,1466-1992,7600-13034,710570-789399,407363-480868,3996614725-3996662113,3-17,5414907798-5414992881,86274-120443,828669-909588,607353-700604,4242340614-4242556443,28750-44009,935177-1004747,20-41,74678832-74818251,8484825082-8484860878,2784096938-2784156610,5477-7589,621-952,2424167145-2424278200,147085-217900,93043740-93241586"""

# Limpieza inicial para que coincida con el formato de "una sola línea" mencionado
input_cleaned = input_string.replace('\n', '')

result_sum, ids = solve_gift_shop(input_cleaned)

print(f"IDs Inválidos encontrados: {ids}")
print(f"Suma Total: {result_sum}")