import os
import json
import time
import threading
import concurrent.futures

def process_files(directory, file):
    s_file = os.path.join(directory, file)
    c_file = os.path.join(directory, file.replace(".s", ".c"))
    if os.path.exists(c_file):
        try:
            with open(s_file, "r") as s:
                s_content = s.read()
            with open(c_file, "r") as c:
                c_content = c.read()
            json_data = {
                "instruction": "Generates C code from this assembler code",
                "input": s_content,
                "output": c_content,
            }
            return json_data
        except UnicodeDecodeError:
            print(f"Error de decodificación en el archivo {s_file}. Pasando al siguiente archivo.")

def create_json(directory, max_entries):
    start_time = time.time()
    data = []
    i = 1
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".s"):
                    future = executor.submit(process_files, root, file)
                    futures.append(future)
                    thread_id = threading.get_ident()
                    print(f"Procesando entrada {i} en el hilo {thread_id}")
                    i += 1
                    if len(futures) >= max_entries:
                        break
            if len(futures) >= max_entries:
                break
        
        for future in concurrent.futures.as_completed(futures):
            data.append(future.result())
        
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo dedicado a la creación del JSON: {elapsed_time} segundos")
    return data

# Ejemplo de uso
directory_path = "C:\\Users\\dani_\\Documents\\MEGAsync\\UPC\\Q9\\TFG\\Development\\AnghaBench"
max_entries = 1000000  # Definir el número máximo de entradas
json_data = create_json(directory_path, max_entries)

output_file = "output.json"
with open(output_file, "w") as f:
    json.dump(json_data, f, indent=4)

print(f"La salida se ha guardado en el archivo {output_file}")
print(f"Longitud del array: {len(json_data)}")
