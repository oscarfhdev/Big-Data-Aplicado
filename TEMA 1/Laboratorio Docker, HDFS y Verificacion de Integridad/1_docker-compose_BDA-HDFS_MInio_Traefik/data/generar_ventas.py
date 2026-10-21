import csv
import random
import time
from datetime import datetime, timedelta

NUM_REGISTROS = 100_000
CIUDADES = ["Cordoba", "Sevilla", "Madrid", "Barcelona", "Valencia", "Malaga"]
CATEGORIAS = ["Electronica", "Informatica", "Hogar", "Deportes", "Libros"]
METODOS_PAGO = ["Tarjeta", "Bizum", "PayPal", "Transferencia"]

print(f"Generando dataset con {NUM_REGISTROS} registros...")
inicio = time.time()

fecha_base = datetime(2026, 1, 1)

with open("/opt/hadoop/shared_data/ventas_ecommerce.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Cabecera estructurada
    writer.writerow(["id_venta", "fecha_transaccion", "id_cliente", "ciudad", "categoria", "unidades", "precio_unitario", "metodo_pago"])

    for i in range(1, NUM_REGISTROS + 1):
        fecha = fecha_base + timedelta(minutes=random.randint(0, 390000))
        cliente = random.randint(1000, 9999)
        ciudad = random.choice(CIUDADES)
        categoria = random.choice(CATEGORIAS)
        unidades = random.randint(1, 8)
        precio = round(random.uniform(5.50, 450.00), 2)
        pago = random.choice(METODOS_PAGO)

        writer.writerow([i, fecha.isoformat(), cliente, ciudad, categoria, unidades, precio, pago])

print(f"Dataset generado con éxito en {round(time.time() - inicio, 2)} segundos.")