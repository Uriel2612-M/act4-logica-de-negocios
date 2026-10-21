# act4-logica-de-negocios

# TechStore - API de Lógica de Negocio (DDD)

Este repositorio contiene la implementación de una arquitectura de software basada en el Diseño Orientado a Dominios (DDD) para la gestión de pedidos de una tienda tecnológica. Se aislaron las reglas de negocio en una capa de dominio independiente, utilizando patrones como Aggregate Roots, Value Objects y Specification, exponiendo la funcionalidad a través de una API REST con FastAPI.

## Pasos de Instalación

1. Clona este repositorio en tu máquina local:
   git clone <url-de-tu-repositorio>
Accede a la carpeta del proyecto y crea un entorno virtual:

python -m venv .venv
Activa el entorno virtual:

Windows: .venv\Scripts\activate

Mac/Linux: source .venv/bin/activate

Instala las dependencias necesarias:

pip install fastapi uvicorn pytest
Ejecución
El proyecto cuenta con múltiples formas de interacción:

1. Carga inicial de datos (Consola):
Para verificar la inicialización de los objetos en memoria a partir del archivo CSV:

python cargar_csv.py
2. Levantar la API REST:
Para iniciar el servidor web y habilitar los endpoints:

uvicorn app.api:app --reload
Una vez en ejecución, la interfaz de documentación interactiva (Swagger) estará disponible en: http://127.0.0.1:8000/docs

3. Ejecutar pruebas unitarias:
Para correr la suite de pruebas automatizadas que validan las invariantes del dominio:

python -m pytest
Reglas de Negocio Implementadas
El sistema valida de forma estricta las siguientes políticas comerciales mediante el patrón Specification:

Límite de unidades: Un pedido no puede superar las 20 unidades físicas en total, independientemente del número de renglones.

Moneda: Solo se aceptan transacciones en pesos mexicanos (MXN).

Descuento del 10%: Requiere que el cliente sea VIP, un monto superior a $500.00 MXN, un mínimo de 4 unidades y la ausencia de promociones previas.

Descuento del 5%: Requiere un monto superior a $5,000.00 MXN y la ausencia de promociones previas.

Integridad de transiciones: Los eventos de dominio (Domain Events) solo se emiten si la transición de estado (DRAFT -> CONFIRMED, etc.) es matemáticamente y lógicamente válida.

Endpoints Disponibles
La API expone los siguientes recursos HTTP para interactuar con los pedidos:

GET /orders: Lista los identificadores de todos los pedidos cargados en memoria.

GET /orders/{order_id}: Consulta el estado, unidades y datos actuales de un pedido específico.

POST /orders/{order_id}/confirm: Intenta confirmar un pedido en estado DRAFT. Valida inventario y reglas antes de transicionar.

POST /orders/{order_id}/ship: Marca un pedido confirmado como enviado, requiere un número de guía.

POST /orders/{order_id}/cancel: Cancela un pedido confirmado, requiere un motivo de cancelación.