import re

def extraer_instrucciones(archivo_path):

    try:
        with open(archivo_path, 'r') as f:
            contenido = f.read()
    
        coincidencias = re.findall(r'([LR])(\d+)', contenido)
        
        instrucciones_limpias = [(dir, int(val)) for dir, val in coincidencias]
        
        return instrucciones_limpias

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_path}")
        return [print("No se pudo Encontrar")]

if __name__ == "__main__":

    datos = extraer_instrucciones("input.txt")
    
    print(f"Se encontraron {len(datos)} instrucciones.")
    print("Primeras 5 para verificar:", datos[:5])

    init = 50
    zero = 0

    for i in range(0,4432):
        if datos[i][0] == 'R':
            init = (init+datos[i][1])%100
            print("R")
        elif datos[i][0] == 'L':
            init = (init-datos[i][1])%100
            print("L")

        if init == 0:
            zero = zero + 1

    print(zero)