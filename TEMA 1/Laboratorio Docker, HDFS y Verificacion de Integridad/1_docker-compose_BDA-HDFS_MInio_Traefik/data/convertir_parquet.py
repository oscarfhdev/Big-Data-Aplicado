import time
import pyarrow.csv as pv
import pyarrow.parquet as pq

# Rutas relativas locales en tu Host
csv_path = "data/ventas_ecommerce.csv"
parquet_path = "data/ventas_ecommerce.zstd.parquet"

print("Leyendo CSV y convirtiendo a formato columnar Parquet con compresión ZSTD...")
inicio = time.time()

# 1. Leer CSV respetando tipos de datos
tabla = pv.read_csv(csv_path)

# 2. Escribir a Parquet con códec Zstandard
pq.write_table(tabla, parquet_path, compression="zstd")

duracion = round(time.time() - inicio, 2)
print(f"Conversión completada con éxito en {duracion} segundos.")