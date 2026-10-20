import argparse
import pandas as pd
import numpy as np
from pathlib import Path

def krippendorff_alpha_nominal(matriz):
    unidades = []
    for ejercicio in matriz.columns:
        valores = matriz[ejercicio].dropna().tolist()
        if len(valores) >= 2:
            unidades.append(valores)

    if not unidades:
        return None

    n_total = 0
    n_coincidencias = 0

    for valores in unidades:
        n = len(valores)
        for i in range(n):
            for j in range(i + 1, n):
                n_total += 1
                if valores[i] == valores[j]:
                    n_coincidencias += 1

    if n_total == 0:
        return None

    Do = 1 - (n_coincidencias / n_total)
    todos = [v for u in unidades for v in u]
    n_obs = len(todos)
    frecuencias = {}
    for v in todos:
        frecuencias[v] = frecuencias.get(v, 0) + 1

    De = 0
    for v1, n1 in frecuencias.items():
        for v2, n2 in frecuencias.items():
            if v1 != v2:
                De += n1 * n2
                
    if n_obs > 1:
        De = De / (n_obs * (n_obs - 1))
    else:
        De = 0

    if De == 0:
        return 1.0 if Do == 0 else 0.0

    alpha = 1 - (Do / De)
    return round(alpha, 4)

def main():
    parser = argparse.ArgumentParser(description="Calcula Krippendorff's Alpha para el proyecto STEV.")
    parser.add_argument("--input", required=True, help="Ruta al archivo CSV consolidado.")
    parser.add_argument("--output", required=True, help="Carpeta donde guardar los resultados.")
    args = parser.parse_args()

    print(f"Cargando datos desde: {args.input}")
    try:
        df = pd.read_csv(args.input)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {args.input}")
        return

    Path(args.output).mkdir(parents=True, exist_ok=True)
    capas = ["l1_motivo_vacio", "l2_codigo_principal", "l3_codigo_principal"]
    
    for capa in capas:
        if capa not in df.columns:
            print(f"Advertencia: La columna '{capa}' no está en el CSV. Saltando...")
            continue
            
        print(f"\n--- Calculando Alpha para {capa.upper()} ---")
        matriz = df.pivot(index='evaluador', columns='ejercicio', values=capa)
        alpha = krippendorff_alpha_nominal(matriz)
        print(f"Alpha: {alpha}")
        
        out_file = Path(args.output) / f"alpha_{capa}.txt"
        with open(out_file, "w") as f:
            f.write(f"Krippendorff's Alpha para {capa}: {alpha}\n")
            
    print(f"\nResultados guardados en: {args.output}")

if __name__ == "__main__":
    main()