import re

def solve_part_two(file_path):
    # 1. Extracción de datos (reutilizando la lógica robusta)
    with open(file_path, 'r') as f:
        instructions = re.findall(r'([LR])(\d+)', f.read())

    current_pos = 50
    total_zeros = 0
    
    for direction, val_str in instructions:
        amount = int(val_str)
        
        # PASO 1: Contar vueltas completas (Matemáticas)
        # Por cada 100 pasos, cruzamos el 0 exactamente una vez.
        total_zeros += amount // 100
        
        # PASO 2: Simular el resto del movimiento (Precisión)
        # Solo necesitamos simular los pasos que no completan una vuelta (0-99 pasos)
        remainder = amount % 100
        
        for _ in range(remainder):
            if direction == 'R':
                current_pos = (current_pos + 1) % 100
            else: # Direction 'L'
                current_pos = (current_pos - 1) % 100
            
            # Si en este "tick" caemos en 0, cuenta.
            if current_pos == 0:
                total_zeros += 1
                
    return total_zeros

# --- Ejecución ---
if __name__ == "__main__":
    resultado = solve_part_two("input1.txt")
    print(f"La contraseña del método CLICK es: {resultado}")