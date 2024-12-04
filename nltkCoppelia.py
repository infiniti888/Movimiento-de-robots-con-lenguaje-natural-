import re
from nltk.corpus import wordnet
import sys
sys.path.append(r'C:\...\zmqRemoteApi-master\zmqRemoteApi-master\clients\python') #path de zmqRemoteApi
import time
from zmqRemoteApi import RemoteAPIClient

# Función para obtener el mapeo de sinónimos a las formas base de las direcciones
def get_synonym_mapping():
    """
    Crea un diccionario que mapea sinónimos a sus palabras base relacionadas solo con direcciones,
    incluyendo 'left', 'right', 'back' y 'forward'.
    """
    # Mapeo de palabras base de direcciones a sus sinónimos en direcciones
    synonym_mapping = {}

    # Mapeo para 'left' y 'right' (sin sinónimos)
    synonym_mapping['left'] = 'left'
    synonym_mapping['right'] = 'right'
    
    # Sinónimos específicos de 'back' y 'forward' de los synsets seleccionados
    # Sinónimos de "back" del synset 'back.r.02'
    back_synset = wordnet.synset('back.r.02')
    for lemma in back_synset.lemmas():
        synonym_mapping[lemma.name().lower()] = 'back'  # Usamos "back" como base

    # Sinónimos de "forward" del synset 'ahead.r.03'
    forward_synset = wordnet.synset('ahead.r.03')
    for lemma in forward_synset.lemmas():
        synonym_mapping[lemma.name().lower()] = 'forward'  # Usamos "forward" como base

    return synonym_mapping

# Función para encontrar las direcciones en el texto y normalizarlas a las formas base
def find_directions_with_base(text):
    """
    Encuentra las palabras de direcciones en el texto y las normaliza
    a las formas base: "back", "forward", "left", "right".
    """
    synonym_mapping = get_synonym_mapping()

    # Crear un patrón de búsqueda que coincida con las palabras clave o sinónimos
    pattern = r'\b(' + '|'.join(re.escape(word) for word in synonym_mapping.keys()) + r')\b'

    # Buscar las coincidencias de las palabras en el texto
    matches = re.findall(pattern, text, flags=re.IGNORECASE)

    # Normalizar las palabras encontradas utilizando el mapeo de sinónimos
    normalized = [synonym_mapping[match.lower()] for match in matches]

    return normalized

# Conexión de prueba con CoppeliaSim
sys.path.append(r'C:\Users\isaac\Desktop\materials varis\curs IA\robotica-con-python-main\zmqRemoteApi-master\zmqRemoteApi-master\clients\python')
from zmqRemoteApi import RemoteAPIClient

# Conecta con CoppeliaSim
client = RemoteAPIClient()  # Utiliza el puerto por defecto (23000)
sim = client.getObject('sim')  # Obtenemos el objeto principal

# Obtenemos el handle del robot
handle = sim.getObject('/MiRobot')  # Especifica el nombre del objeto
print(f"Handle obtenido: {handle}")
print(sim.getObjectPosition(handle, -1))

# Función para mover el robot basado en las direcciones
def move_robot(direction, handle, sim):
    """
    Mueve el robot según la dirección dada.
    """
    # Obtener la posición actual
    position = sim.getObjectPosition(handle, -1)
    
    # Mover el robot en la dirección adecuada
    if direction == 'left':
        position[0] -= 0.1  # Movimiento a la izquierda
    elif direction == 'right':
        position[0] += 0.1  # Movimiento a la derecha
    elif direction == 'back':
        position[1] -= 0.1  # Movimiento hacia atrás
    elif direction == 'forward':
        position[1] += 0.1  # Movimiento hacia adelante
    
    # Establecer la nueva posición
    sim.setObjectPosition(handle, -1, position)
    print(f"Moviendo a la posición: {position}")
    time.sleep(1)  # Pausa para observar el movimiento

# Solicitar texto al usuario
text = input("Ingresa un texto con direcciones en inglés (por ejemplo, 'go ahead then turn right then go backwards and do a left turn'):\n")

# Detectar las direcciones en el texto y normalizarlas
directions = find_directions_with_base(text)
print(f"Direcciones detectadas: {directions}")

# Mover el robot según las direcciones detectadas
for direction in directions:
    move_robot(direction, handle, sim)

print("¡Movimiento completado!")
