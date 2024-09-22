import time

def medir_tiempo(func):
    def wrapper(**kwargs):
        start_time = time.time()  # Inicia el cronómetro
        result = func(**kwargs)   # Ejecuta la función decorada
        end_time = time.time()    # Termina el cronómetro
        elapsed_time = end_time - start_time


        suma = sum(kwargs.values())
        print(f"Suma de los elementos: {suma}")
        print(f"Tiempo de ejecución: {elapsed_time:.6f} segundos")
        return result
    return wrapper

@medir_tiempo
def encontrar_mayor(**kwargs):
    mayor = max(kwargs.values())
    return f"El número mayor es: {mayor}"

print(encontrar_mayor(a=10, b=20, c=30, d=40))
