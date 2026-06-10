import hashlib
import time

class Block:
    def __init__(self, index: int, data: str, previous_hash: str):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        # 1. Unimos todos los datos del bloque en un solo texto (string)
        block_string = f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'

        # 2. Convertimos el texto a bytes y aplicamos el algoritmo matemático SHA-256
        encoded_block = block_string.encode('utf-8')
        return hashlib.sha256(encoded_block).hexdigest()
    
# --- Zona de Pruebas ---
if __name__ == "__main__":
    # 1. Crear el "Bloque Genesis o Primer Bloque"
    # Parametros: index=0, data="Bloque Genesis", previous_hash="0"
    bloque_genesis = Block(0, 'Primer bloque de mi Blockchain', '0')

    # 2. Imprimir las propiedades para verlas en la terminal
    print('=== Bloque Genesis Creado ===')
    print(f'Indice: {bloque_genesis.index}')
    print(f'Timestamp: {bloque_genesis.timestamp}')
    print(f'Datos: {bloque_genesis.data}')
    print(f'Hash Anterior: {bloque_genesis.previous_hash}')
    print(f'Hash del Bloque (La Magia!): {bloque_genesis.hash}')