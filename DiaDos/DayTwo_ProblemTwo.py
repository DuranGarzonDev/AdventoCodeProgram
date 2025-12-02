def solve_gift_shop_part_two(input_data):
    """
    Calcula la suma de IDs inválidos bajo las reglas de la Parte 2.
    Un ID es inválido si consiste en una secuencia de dígitos repetida 
    AL MENOS dos veces (ej. 123123123 o 55).
    """
    
    # 1. Limpieza y preparación de la entrada
    ranges = input_data.replace('\n', '').split(',')
    
    total_invalid_sum = 0
    invalid_ids_found = []

    # 2. Procesar cada rango
    for r in ranges:
        if not r.strip(): continue
        
        start_str, end_str = r.split('-')
        start = int(start_str)
        end = int(end_str)
        
        # 3. Analizar cada número en el rango
        for num in range(start, end + 1):
            s_num = str(num)
            length = len(s_num)
            
            is_invalid = False
            
            # Buscamos un patrón de longitud 'm'
            # m debe ser menor o igual a la mitad de la longitud total
            for m in range(1, (length // 2) + 1):
                
                # Optimización: La longitud total debe ser divisible por la longitud del patrón
                if length % m == 0:
                    pattern = s_num[:m]
                    repetitions = length // m
                    
                    # Verificamos si el patrón repetido forma el número original
                    if pattern * repetitions == s_num:
                        is_invalid = True
                        break # Encontramos un patrón, no necesitamos buscar más
            
            if is_invalid:
                total_invalid_sum += num
                invalid_ids_found.append(num)

    return total_invalid_sum, invalid_ids_found

# --- Ejecución con los datos del ejemplo ---

input_string = """5529687-5587329,50-82,374-560,83-113,226375-287485,293169-368713,2034-2634,9945560-9993116,4872472-4904227,3218-5121,1074-1357,15451-26093,483468003-483498602,51513-85385,1466-1992,7600-13034,710570-789399,407363-480868,3996614725-3996662113,3-17,5414907798-5414992881,86274-120443,828669-909588,607353-700604,4242340614-4242556443,28750-44009,935177-1004747,20-41,74678832-74818251,8484825082-8484860878,2784096938-2784156610,5477-7589,621-952,2424167145-2424278200,147085-217900,93043740-93241586"""

# Limpieza inicial
input_cleaned = input_string.replace('\n', '')

result_sum, ids = solve_gift_shop_part_two(input_cleaned)

# Mostrar una muestra de los IDs encontrados para verificar contra el problema
print(f"Suma Total (Parte 2): {result_sum}")
print(f"Cantidad de IDs inválidos: {len(ids)}")
print(f"Ejemplos encontrados: {ids[:15]}...") # Mostramos los primeros para no saturar