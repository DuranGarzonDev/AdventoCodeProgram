import sys
import re
import numpy as np
from scipy.optimize import linprog
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def solve_machine(line):
    """
    Parsea y resuelve una sola máquina usando Programación Lineal Entera.
    Retorna el número mínimo de pulsaciones o 0 si no hay solución.
    """
    if not line.strip():
        return 0

    # 1. Parsing (Extracción de datos)
    # Formato ejemplo: ... (0,2) (0,1) {3,5,4,7}
    # Ignoramos la parte de luces [...] para la Parte 2
    
    # Extraer botones (las tuplas en paréntesis)
    buttons_str = re.findall(r'\(([\d,]+)\)', line)
    # Extraer objetivos (la tupla en llaves)
    targets_match = re.search(r'\{([\d,]+)\}', line)
    
    if not buttons_str or not targets_match:
        return 0

    # Convertir objetivos a vector b
    b_eq = np.array([int(x) for x in targets_match.group(1).split(',')])
    num_counters = len(b_eq)
    
    # Construir Matriz A
    # A tiene dimensiones (num_contadores x num_botones)
    num_buttons = len(buttons_str)
    A_eq = np.zeros((num_counters, num_buttons))
    
    for col_idx, btn_str in enumerate(buttons_str):
        indices = [int(x) for x in btn_str.split(',')]
        for row_idx in indices:
            if row_idx < num_counters:
                A_eq[row_idx, col_idx] = 1

    # 2. Configuración del Solver (ILP)
    # Queremos minimizar la suma de pulsaciones: sum(x_i)
    # Por lo tanto, el vector de costos 'c' es todo 1s.
    c = np.ones(num_buttons)
    
    # Restricciones de variables: 0 a Infinito, y deben ser Enteros
    # integrality=1 fuerza a que la solución sea entera
    res = linprog(c, 
                  A_eq=A_eq, 
                  b_eq=b_eq, 
                  bounds=(0, None),
                  method='highs', 
                  integrality=np.ones(num_buttons)) # 1 = entero

    # 3. Verificación y Retorno
    if res.success:
        # Redondeamos para evitar errores de punto flotante infinitesimales
        return int(round(res.fun))
    else:
        # Si el sistema es inconsistente o no tiene solución entera
        return 0

def main():
    # Leer entrada desde un archivo o stdin
    # Para pruebas, puedes cambiar esto a abrir un archivo: open('input.txt').read()
    input_data = sys.stdin.read().strip().split('\n')
    
    print(f"Procesando {len(input_data)} máquinas...")

    # Paralelización: Usar todos los CPUs disponibles
    # chunksize ayuda a reducir el overhead de comunicación entre procesos
    total_presses = 0
    
    # max_workers=None usa por defecto el número de procesadores lógicos
    with ProcessPoolExecutor() as executor:
        # Mapear la función solve_machine a cada línea de datos
        results = executor.map(solve_machine, input_data, chunksize=100)
        
        for res in results:
            total_presses += res

    print(f"--- Solución Parte 2 ---")
    print(f"Pulsaciones totales mínimas requeridas: {total_presses}")

if __name__ == "__main__":
    main()