from pathlib import Path
import time
import pyarrow.csv as pcsv
import pyarrow.parquet as pq

carpeta = Path(__file__).parent
csv = carpeta / "ventas_ecommerce.csv"
parquet = carpeta / "ventas_ecommerce.zstd.parquet"

inicio = time.perf_counter()
tabla = pcsv.read_csv(csv)
pq.write_table(tabla, parquet, compression="zstd")
duracion = time.perf_counter() - inicio

csv_bytes = csv.stat().st_size
parquet_bytes = parquet.stat().st_size
ahorro = 100 * (csv_bytes - parquet_bytes) / csv_bytes
print(f"CSV: {csv_bytes} bytes")
print(f"Parquet ZSTD: {parquet_bytes} bytes")
print(f"Reducción medida: {ahorro:.2f} %")
print(f"Conversión: {duracion:.3f} s")