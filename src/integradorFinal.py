"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src
Fecha de generacion: 2025-11-05 09:49:44
Total de archivos integrados: 110
Total de directorios procesados: 27
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. constantes.py
#   2. main.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades/clientes
#   4. __init__.py
#   5. cliente.py
#   6. cliente_frecuente.py
#   7. nivel_de_fidelidad.py
#
# DIRECTORIO: entidades/cocina
#   8. __init__.py
#   9. estacion_bebidas.py
#   10. estacion_cocina.py
#   11. estacion_cocina_general.py
#   12. estacion_parrilla.py
#   13. estacion_pastas.py
#   14. estacion_postres.py
#   15. estado_orden.py
#   16. orden_cocina.py
#
# DIRECTORIO: entidades/inventario
#   17. __init__.py
#   18. alerta_stock.py
#   19. categoria_ingrediente.py
#   20. ingrediente.py
#   21. unidad_medida.py
#
# DIRECTORIO: entidades/menu
#   22. __init__.py
#   23. bebida.py
#   24. categoria_item.py
#   25. entrada.py
#   26. item_menu.py
#   27. plato_principal.py
#   28. postre.py
#   29. tipo_coccion.py
#
# DIRECTORIO: entidades/pedidos
#   30. __init__.py
#   31. estado_pedido.py
#   32. item_pedido.py
#   33. pedido.py
#   34. tipo_servicio.py
#
# DIRECTORIO: entidades/personal
#   35. __init__.py
#   36. cajero.py
#   37. chef.py
#   38. cocinero.py
#   39. empleado.py
#   40. especialidad_chef.py
#   41. mozo.py
#   42. turno.py
#
# DIRECTORIO: entidades/salon
#   43. __init__.py
#   44. estado_mesa.py
#   45. estado_reserva.py
#   46. mesa.py
#   47. reserva.py
#   48. zona_salon.py
#
# DIRECTORIO: excepciones
#   49. __init__.py
#   50. ingrediente_agotado_exception.py
#   51. mesa_ocupada_exception.py
#   52. pedido_invalido_exception.py
#   53. persistencia_exception.py
#   54. restaurante_exception.py
#
# DIRECTORIO: monitoreo
#   55. __init__.py
#
# DIRECTORIO: monitoreo/control
#   56. __init__.py
#   57. monitor_base_task.py
#   58. monitor_cocina_task.py
#   59. monitor_inventario_task.py
#
# DIRECTORIO: monitoreo/sensores
#   60. __init__.py
#   61. sensor_base_task.py
#   62. sensor_stock_task.py
#   63. sensor_temperatura_cocina_task.py
#   64. sensor_tiempo_de_espera_task.py
#
# DIRECTORIO: patrones
#   65. __init__.py
#
# DIRECTORIO: patrones/decorator
#   66. __init__.py
#   67. descuento_decorator.py
#   68. precio_decorator.py
#   69. recargo_decorator.py
#
# DIRECTORIO: patrones/factory
#   70. __init__.py
#   71. estacion_factory.py
#   72. item_menu_factory.py
#
# DIRECTORIO: patrones/observer
#   73. __init__.py
#   74. observable.py
#   75. observer.py
#
# DIRECTORIO: patrones/state
#   76. __init__.py
#   77. pedido_cancelado_state.py
#   78. pedido_en_preparacion_state.py
#   79. pedido_listo_state.py
#   80. pedido_recibidio_state.py
#   81. pedido_servido_state.py
#   82. pedido_state.py
#
# DIRECTORIO: patrones/strategy
#   83. __init__.py
#   84. coccion_fritura_strategy.py
#   85. coccion_horno_strategy.py
#   86. coccion_parrilla_strategy.py
#   87. coccion_plancha_strategy.py
#   88. coccion_vapor_strategy.py
#   89. metodo_coccion_strategy.py
#
# DIRECTORIO: servicios
#   90. __init__.py
#
# DIRECTORIO: servicios/cocina
#   91. __init__.py
#   92. cocina_service.py
#   93. control_calidad_service.py
#   94. distribucion_ordenes_service.py
#
# DIRECTORIO: servicios/inventario
#   95. __init__.py
#   96. inventario_service.py
#   97. proovedor_service.py
#
# DIRECTORIO: servicios/menu
#   98. __init__.py
#   99. item_service_registry.py
#   100. menu_service.py
#
# DIRECTORIO: servicios/pedidos
#   101. __init__.py
#   102. comanda_service.py
#   103. pedido_service.py
#
# DIRECTORIO: servicios/persistencia
#   104. __init__.py
#   105. restaurante_persistence_service.py
#
# DIRECTORIO: servicios/personal
#   106. __init__.py
#   107. personal_service.py
#
# DIRECTORIO: servicios/salon
#   108. __init__.py
#   109. mesa_service.py
#   110. reserva_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/110: constantes.py
# Directorio: .
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/constantes.py
# ==============================================================================

# --- MENU ---
PRECIO_BASE_ENTRADA = 8.50
PRECIO_BASE_PLATO_PRINCIPAL = 15.00
PRECIO_BASE_POSTRE = 6.00
PRECIO_BASE_BEBIDA = 3.50

# --- BEBIDAS - VINOS MENDOCINOS ---
VINOS_MENDOCINOS = {
    "Catena Zapata Malbec": 45.00,
    "Luigi Bosca DOC": 32.00,
    "Rutini Cabernet Sauvignon": 28.00,
    "Trapiche Medalla": 18.00,
    "Alamos Malbec": 15.00
}

# --- BEBIDAS - VINOS SANJUANINOS ---
VINOS_SANJUANINOS = {
    "Graffigna Centenario": 35.00,
    "Callia Alta Syrah": 25.00,
    "Las Marianas Reserva": 22.00,
    "Pedernal Malbec": 20.00,
    "Vinorum Bonarda": 16.00
}

# --- COCINA ---
TIEMPO_PREPARACION_ENTRADA = 10  # minutos
TIEMPO_PREPARACION_PLATO_PRINCIPAL = 25  # minutos
TIEMPO_PREPARACION_POSTRE = 15  # minutos
TIEMPO_PREPARACION_BEBIDA = 2  # minutos

TEMPERATURA_COCINA_MIN = 18  # °C
TEMPERATURA_COCINA_MAX = 30  # °C
TEMPERATURA_PARRILLA = 200  # °C
TEMPERATURA_HORNO = 180  # °C

# --- INVENTARIO ---
STOCK_MINIMO_INGREDIENTE = 10  # unidades/kg/litros según tipo
STOCK_CRITICO = 5
DIAS_VENCIMIENTO_ALERTA = 3

# --- PEDIDOS ---
TIEMPO_MAXIMO_ESPERA = 45  # minutos
TIEMPO_PRIORIDAD_EXPRESS = 20  # minutos
CAPACIDAD_MAXIMA_COCINA = 15  # pedidos simultáneos

# --- MESAS ---
CANTIDAD_MESAS_INTERIOR = 15
CANTIDAD_MESAS_TERRAZA = 10
CANTIDAD_MESAS_VIP = 5
TIEMPO_ROTACION_MESA = 90  # minutos promedio

# --- MONITOREO ---
INTERVALO_SENSOR_TEMPERATURA = 5.0  # segundos
INTERVALO_SENSOR_STOCK = 30.0  # segundos
INTERVALO_SENSOR_TIEMPO_ESPERA = 10.0  # segundos
INTERVALO_MONITOR_COCINA = 3.0  # segundos
THREAD_JOIN_TIMEOUT = 2.0

# --- DESCUENTOS Y RECARGOS ---
DESCUENTO_CLIENTE_FRECUENTE = 10  # %
DESCUENTO_HAPPY_HOUR = 15  # %
RECARGO_DELIVERY = 2.50  # USD
RECARGO_SERVICIO_MESA = 10  # %

# --- PERSONAL ---
CAPACIDAD_MOZOS = 4  # mesas por mozo
TURNOS_POR_DIA = 2  # almuerzo y cena

# --- PERSISTENCIA ---
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

# ==============================================================================
# ARCHIVO 2/110: main.py
# Directorio: .
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/main.py
# ==============================================================================

# src/main.py

import time

# --- IMPORTACIONES DE CONSTANTES ---
from src.constantes import (
    VINOS_MENDOCINOS, 
    VINOS_SANJUANINOS, 
    STOCK_MINIMO_INGREDIENTE
)

# --- IMPORTACIONES DE ENTIDADES ---
from src.entidades.menu.categoria_item import CategoriaItem
from src.entidades.pedidos.item_pedido import ItemPedido
from src.entidades.cocina.orden_cocina import OrdenCocina
from src.entidades.personal.chef import Chef
from src.entidades.personal.mozo import Mozo
from src.entidades.personal.especialidad_chef import EspecialidadChef
from src.entidades.salon.mesa import Mesa
from src.entidades.salon.zona_salon import ZonaSalon
from src.entidades.inventario.ingrediente import Ingrediente
from src.entidades.inventario.categoria_ingrediente import CategoriaIngrediente
from src.entidades.inventario.unidad_medida import UnidadMedida
from src.entidades.pedidos.pedido import Pedido
from src.entidades.pedidos.tipo_servicio import TipoServicio

# --- IMPORTACIONES DE SERVICIOS ---
from src.servicios.menu.menu_service import MenuService
from src.servicios.menu.item_service_registry import ItemServiceRegistry
from src.servicios.pedidos.comanda_service import ComandaService
from src.servicios.pedidos.pedido_service import PedidoService
from src.servicios.cocina.cocina_service import CocinaService
from src.servicios.personal.personal_service import PersonalService
from src.servicios.salon.mesa_service import MesaService
from src.servicios.inventario.inventario_service import InventarioService

# --- IMPORTACIONES DE PATRONES ---
from src.patrones.observer.observer import IObserver
from src.patrones.observer.observable import IObservable


# =============================================================================
# --- CLASES HELPERS PARA LA SIMULACIÓN ---
# =============================================================================

class AlertadorStockConsola(IObserver):
    """
    (Patrón Observer)
    Un observador simple que imprime alertas de stock en la consola
    cuando un ingrediente (Observable) lo notifica.
    """
    def actualizar(self, observable: IObservable):
        if isinstance(observable, Ingrediente):
            ingrediente = observable
            if ingrediente.necesita_reabastecimiento():
                print(f"\n🔔🔔 ALERTA DE STOCK (OBSERVER) 🔔🔔")
                print(f"  > Ingrediente: {ingrediente.get_nombre()}")
                print(f"  > Stock actual: {ingrediente.get_cantidad_actual()} {ingrediente.get_unidad_medida()}")
                print(f"  > Mínimo: {ingrediente.get_cantidad_minima()}")
                print(f"🔔🔔----------------------------------🔔🔔\n")

def distribuir_pedido_a_cocina(pedido: Pedido, cocina_service: CocinaService):
    """
    Helper que simula el servicio de distribución.
    Toma un Pedido, lo divide en Ordenes de Cocina y las envía
    a las estaciones correspondientes.
    """
    print(f"\n--- PASO 2.1: Distribuyendo Pedido #{pedido.get_id()} a Cocina ---")
    
    items_pedido = pedido.get_items() #
    if not items_pedido:
        print(f"Advertencia: Pedido #{pedido.get_id()} no tiene items.")
        return

    for item in items_pedido:
        # 1. Crear la Orden de Cocina para este item
        orden = OrdenCocina(
            item_pedido=item,
            pedido_id=pedido.get_id(),
            mesa_id=pedido.get_mesa_id()
        ) #
        
        # 2. Enviar la orden al servicio de cocina
        try:
            cocina_service.enviar_orden_a_estacion(orden) #
            print(f"  -> '{item.get_item_menu().get_nombre()}' enviado a Estación '{orden.get_estacion_asignada()}'")
        except ValueError as e:
            print(f"Error al enviar orden: {e}")
            
    # 3. Confirmar el pedido (Patrón State)
    pedido_service = PedidoService()
    pedido_service.confirmar_preparacion_pedido(pedido.get_id()) #
    print(f"Estado del Pedido #{pedido.get_id()}: {pedido.get_estado()}")


# =============================================================================
# --- FUNCIONES DE CONFIGURACIÓN ---
# =============================================================================

def inicializar_servicios():
    """Inicializa todos los servicios Singleton."""
    print("--- INICIALIZANDO SERVICIOS ---")
    servicios = {
        "menu": MenuService(),
        "registry": ItemServiceRegistry(),
        "comanda": ComandaService(),
        "pedido": PedidoService(),
        "cocina": CocinaService(),
        "personal": PersonalService(),
        "mesa": MesaService(),
        "inventario": InventarioService()
    }
    print("Servicios inicializados.")
    return servicios

def configurar_menu(menu_service: MenuService):
    """
    (Patrón Factory)
    Crea y registra todos los items del menú.
    """
    print("\n--- 1. CONFIGURANDO MENÚ ---")
    
    # --- VINOS MENDOCINOS ---
    print("Registrando Vinos Mendocinos...")
    for nombre in VINOS_MENDOCINOS: #
        menu_service.crear_y_registrar_item(
            categoria=CategoriaItem.BEBIDA,
            nombre=nombre,
            descripcion="Vino tinto de las prestigiosas bodegas de Mendoza.",
            tipo_bebida="vino",
            tamanio="botella"
        ) #

    # --- VINOS SANJUANINOS ---
    print("Registrando Vinos Sanjuaninos...")
    for nombre in VINOS_SANJUANINOS: #
        menu_service.crear_y_registrar_item(
            categoria=CategoriaItem.BEBIDA,
            nombre=nombre,
            descripcion="Vino de altura proveniente de los valles de San Juan.",
            tipo_bebida="vino",
            tamanio="botella"
        )

    # --- OTROS ITEMS ---
    menu_service.crear_y_registrar_item(
        categoria=CategoriaItem.PLATO_PRINCIPAL,
        nombre="Bife de Chorizo",
        descripcion="Clásico corte argentino a la parrilla.",
        tipo_proteina="carne", # Va a EstacionParrilla
        guarnicion="papas fritas"
    )
    menu_service.crear_y_registrar_item(
        categoria=CategoriaItem.PLATO_PRINCIPAL,
        nombre="Spaghetti Carbonara",
        descripcion="Pasta clásica con huevo, queso y panceta.",
        tipo_proteina="vegetariano", # (Asignación de ejemplo)
        guarnicion="queso parmesano" # Va a EstacionPastas
    )
    menu_service.crear_y_registrar_item(
        categoria=CategoriaItem.ENTRADA,
        nombre="Ensalada Caprese",
        descripcion="Tomate, mozzarella y albahaca.",
        tipo_entrada="ensalada" # Va a EstacionCocinaGeneral
    )

def configurar_personal(personal_service: PersonalService):
    print("\n--- 2. CONFIGURANDO PERSONAL ---")
    chef_parrilla = Chef("Francis", "Mallmann", "123", "555", "f@m.com", 5000, EspecialidadChef.PARRILLA) #
    chef_pastas = Chef("Donato", "De Santis", "456", "555", "d@d.com", 4500, EspecialidadChef.PASTAS)
    personal_service.contratar_empleado(chef_parrilla) #
    personal_service.contratar_empleado(chef_pastas)
    
    mozo1 = Mozo("Juan", "Perez", "789", "555", "j@p.com", 1000) #
    personal_service.contratar_empleado(mozo1)

def configurar_salon(mesa_service: MesaService):
    print("\n--- 3. CONFIGURANDO SALÓN ---")
    mesa_service.agregar_mesa(Mesa(numero=1, capacidad=4, zona=ZonaSalon.INTERIOR)) #
    mesa_service.agregar_mesa(Mesa(numero=2, capacidad=2, zona=ZonaSalon.INTERIOR))
    mesa_service.agregar_mesa(Mesa(numero=5, capacidad=4, zona=ZonaSalon.TERRAZA)) #

def configurar_inventario(inventario_service: InventarioService) -> list:
    print("\n--- 4. CONFIGURANDO INVENTARIO ---")
    ingredientes = [
        Ingrediente("Lomo", CategoriaIngrediente.CARNES, UnidadMedida.KILOGRAMOS, 20.0),
        Ingrediente("Spaghetti", CategoriaIngrediente.CEREALES_GRANOS, UnidadMedida.PAQUETES, 50.0),
        # Ingrediente para la alerta (Patrón Observer)
        Ingrediente("Tomate", CategoriaIngrediente.VERDURAS, UnidadMedida.KILOGRAMOS, 3.0),
        Ingrediente("Queso", CategoriaIngrediente.LACTEOS, UnidadMedida.KILOGRAMOS, 10.0)
    ] #
    
    # Configurar stock mínimo para la alerta
    ingredientes[2].set_cantidad_minima(STOCK_MINIMO_INGREDIENTE / 2) # 5.0 kg

    for ing in ingredientes:
        inventario_service.agregar_ingrediente(ing) #
    
    print("Inventario cargado. Tomate tiene 3.0kg (Mínimo: 5.0kg).")
    return ingredientes

def configurar_monitoreo(inventario_service: InventarioService):
    """
    (Patrón Observer)
    Configura los observadores para reaccionar a cambios en el sistema.
    """
    print("\n--- 5. CONFIGURANDO MONITOREO (OBSERVERS) ---")
    
    # 1. Crear el observador
    alerta_consola = AlertadorStockConsola()
    
    # 2. Registrar el observador en el servicio de inventario
    # El servicio se encargará de adjuntarlo a CADA ingrediente.
    inventario_service.registrar_observador_stock(alerta_consola) #
    print("Observador 'AlertadorStockConsola' registrado en InventarioService.")


# =============================================================================
# --- FUNCIONES DE SIMULACIÓN ---
# =============================================================================

def simular_pedido_mesa_parrilla(servicios: dict):
    """
    Simulación 1: Un pedido estándar en salón (Mesa 5).
    Demuestra: Builder, Factory, State, Decorator (Recargo Servicio).
    """
    print("\n=======================================================")
    print("--- SIMULACIÓN 1: Pedido en Salón (Parrilla + Vino) ---")
    print("=======================================================")
    
    # --- PASO 1: Tomando Pedido (Patrón Builder) ---
    print("\n--- PASO 1: Tomando Pedido (Builder) ---")
    
    # Obtener las plantillas de item del menú
    item_bife = servicios["registry"].get_item_por_nombre("Bife de Chorizo")
    item_vino = servicios["registry"].get_item_por_nombre("Catena Zapata Malbec")

    # Crear los "ItemPedido"
    pedido_bife = ItemPedido(item_bife, 1)
    pedido_bife.set_observaciones_especiales("A punto") #
    pedido_vino = ItemPedido(item_vino, 1)

    # Usar el ComandaService para construir el Pedido
    builder = servicios["comanda"].iniciar_nuevo_pedido(cliente_id=1) #
    builder.para_mesa(mesa_id=5)
    builder.con_mozo(mozo_id=1)
    builder.con_item(pedido_bife)
    builder.con_item(pedido_vino)
    
    pedido = servicios["comanda"].finalizar_pedido(builder)
    servicios["pedido"].registrar_pedido(pedido)
    print(f"Pedido #{pedido.get_id()} creado. Estado: {pedido.get_estado()}")

    # --- PASO 2: Distribuyendo Pedido a Cocina (Patrón Factory) ---
    distribuir_pedido_a_cocina(pedido, servicios["cocina"])

    # --- PASO 3: Simulación de Cocina y Estados (Patrón State) ---
    print("\n--- PASO 3: Simulación de Cocina (State) ---")
    print("...Chefs trabajando...")
    time.sleep(1) # Simula tiempo de preparación
    
    # El Mozo o Chef marca el pedido como listo
    servicios["pedido"].marcar_pedido_listo(pedido.get_id()) #
    print(f"Estado del Pedido #{pedido.get_id()}: {pedido.get_estado()}")
    
    # El Mozo sirve el pedido
    servicios["pedido"].servir_pedido(pedido.get_id())
    print(f"Estado del Pedido #{pedido.get_id()}: {pedido.get_estado()}")

    # --- PASO 4: Cálculo de Precio (Patrón Decorator) ---
    print("\n--- PASO 4: Cálculo de Precio (Decorator) ---")
    # El Pedido es En Salón, por lo que se aplica RecargoServicioMesa
    precio_final = servicios["pedido"].calcular_precio_final_con_cargos(pedido.get_id()) #
    
    print(f"\n--- TICKET PEDIDO #{pedido.get_id()} ---")
    print(f"  Bife de Chorizo:     ${item_bife.get_precio_base():.2f}")
    print(f"  Catena Zapata Malbec: ${item_vino.calcular_precio_final():.2f}")
    print("  -----------------------")
    print(f"  Subtotal:            ${pedido.calcular_subtotal():.2f}")
    print(f"  Recargo Salón (10%): +${pedido.calcular_recargos():.2f}")
    print("  -----------------------")
    print(f"  TOTAL A PAGAR:       ${precio_final:.2f}")

def simular_consumo_inventario(servicios: dict):
    """
    Simulación 2: Un pedido que consume stock y dispara un Observador.
    Demuestra: Observer.
    """
    print("\n=======================================================")
    print("--- SIMULACIÓN 2: Pedido con Alerta de Stock (Observer) ---")
    print("=======================================================")
    
    # 1. Tomar pedido de ensalada
    item_ensalada = servicios["registry"].get_item_por_nombre("Ensalada Caprese")
    builder = servicios["comanda"].iniciar_nuevo_pedido(cliente_id=2)
    builder.para_mesa(mesa_id=2).con_item(ItemPedido(item_ensalada, 1))
    pedido = servicios["comanda"].finalizar_pedido(builder)
    print(f"Pedido #{pedido.get_id()} (Ensalada Caprese) creado.")
    
    # 2. Simular consumo de stock
    # Asumimos que la ensalada usa 0.5kg de Tomate y 0.3kg de Queso
    try:
        print("\nCocinero consume 0.5kg de Tomate...")
        # El stock de Tomate es 3.0kg, Mínimo 5.0kg.
        # Al consumir, el stock NO BAJA del mínimo, pero ya está bajo.
        # El observador se dispara porque (stock <= minimo)
        servicios["inventario"].consumir_stock("Tomate", 0.5) #
        
        print("\nCocinero consume 0.3kg de Queso...")
        servicios["inventario"].consumir_stock("Queso", 0.3)
        # (No debería disparar alerta para el queso)
        
    except ValueError as e:
        print(f"Error en inventario: {e}")

def simular_pedido_delivery_descuento(servicios: dict):
    """
    Simulación 3: Pedido Delivery Y Cliente Frecuente.
    Demuestra: Builder (Delivery), Decorator (Descuento + Recargo).
    """
    print("\n=======================================================")
    print("--- SIMULACIÓN 3: Delivery con Descuento (Decorators) ---")
    print("=======================================================")

    # --- PASO 1: Tomando Pedido (Patrón Builder) ---
    print("\n--- PASO 1: Tomando Pedido (Builder) ---")
    
    item_pasta = servicios["registry"].get_item_por_nombre("Spaghetti Carbonara")
    
    builder = servicios["comanda"].iniciar_nuevo_pedido(cliente_id=3)
    builder.para_delivery(direccion="Calle Falsa 123") #
    builder.con_item(ItemPedido(item_pasta, 2)) # Pide dos porciones
    
    pedido = servicios["comanda"].finalizar_pedido(builder)
    
    # --- PASO 2: Aplicando Lógica de Negocio ---
    print("\n--- PASO 2: Aplicando Lógica de Negocio ---")
    
    # El cliente es frecuente, aplicamos el flag
    pedido.set_cliente_frecuente(True) #
    servicios["pedido"].registrar_pedido(pedido)
    print(f"Pedido #{pedido.get_id()} (Delivery) creado para Cliente Frecuente.")

    # --- PASO 3: Cálculo de Precio (Patrón Decorator Múltiple) ---
    print("\n--- PASO 3: Cálculo de Precio (Multi-Decorator) ---")
    
    # El PedidoService aplicará AMBOS decoradores:
    # 1. DescuentoDecorator (por cliente frecuente)
    # 2. RecargoDecorator (por delivery)
    precio_final = servicios["pedido"].calcular_precio_final_con_cargos(pedido.get_id())
    
    print(f"\n--- TICKET PEDIDO #{pedido.get_id()} ---")
    print(f"  2x Spaghetti Carbonara: ${item_pasta.get_precio_base() * 2:.2f}")
    print("  -----------------------")
    print(f"  Subtotal:               ${pedido.calcular_subtotal():.2f}")
    print(f"  Descuento Cliente (10%): -${pedido.calcular_descuentos():.2f}")
    print(f"  Recargo Delivery:       +${pedido.calcular_recargos():.2f}")
    print("  -----------------------")
    print(f"  TOTAL A PAGAR:          ${precio_final:.2f}")


# =============================================================================
# --- PUNTO DE ENTRADA PRINCIPAL ---
# =============================================================================

def main():
    """Función principal del sistema"""
    
    try:
        # --- 1. ARRANQUE ---
        servicios = inicializar_servicios()
        
        # --- 2. CONFIGURACIÓN ---
        configurar_menu(servicios["menu"])
        configurar_personal(servicios["personal"])
        configurar_salon(servicios["mesa"])
        configurar_inventario(servicios["inventario"])
        configurar_monitoreo(servicios["inventario"])
        
        print("\n=======================================================")
        print("--- SISTEMA LISTO Y OPERATIVO ---")
        print("=======================================================")
        
        # --- 3. SIMULACIÓN DE OPERACIONES ---
        
        # Simulación 1: Pedido en mesa
        simular_pedido_mesa_parrilla(servicios)
        
        # Simulación 2: Consumo que dispara alerta
        simular_consumo_inventario(servicios)
        
        # Simulación 3: Pedido delivery con descuento
        simular_pedido_delivery_descuento(servicios)

    except Exception as e:
        print(f"\n--- ERROR CRÍTICO EN MAIN ---")
        print(f"{type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

    finally:
        print("\n...Simulación finalizada. Sistema detenido.")


if __name__ == "__main__":
    main()


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/110: __init__.py
# Directorio: entidades
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/clientes
################################################################################

# ==============================================================================
# ARCHIVO 4/110: __init__.py
# Directorio: entidades/clientes
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/clientes/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/110: cliente.py
# Directorio: entidades/clientes
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/clientes/cliente.py
# ==============================================================================

from datetime import datetime
from typing import Optional

class Cliente:
    """Representa un cliente del restaurante"""
    
    _contador_id = 0
    
    def __init__(self, nombre: str, telefono: str, email: Optional[str] = None):
        Cliente._contador_id += 1
        self._id = Cliente._contador_id
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._fecha_registro = datetime.now()
        self._direccion = ""
        self._notas = ""  # Preferencias, alergias, etc.
        self._activo = True
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_telefono(self) -> str:
        return self._telefono
    
    def get_email(self) -> Optional[str]:
        return self._email
    
    def get_fecha_registro(self) -> datetime:
        return self._fecha_registro
    
    def get_direccion(self) -> str:
        return self._direccion
    
    def get_notas(self) -> str:
        return self._notas
    
    def esta_activo(self) -> bool:
        return self._activo
    
    # --- SETTERS ---
    def set_nombre(self, nombre: str):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre
    
    def set_telefono(self, telefono: str):
        if not telefono or telefono.strip() == "":
            raise ValueError("El teléfono no puede estar vacío")
        self._telefono = telefono
    
    def set_email(self, email: str):
        self._email = email
    
    def set_direccion(self, direccion: str):
        self._direccion = direccion
    
    def set_notas(self, notas: str):
        """Notas sobre preferencias, alergias, etc."""
        self._notas = notas
    
    def set_activo(self, activo: bool):
        self._activo = activo
    
    # --- MÉTODOS ---
    def agregar_nota(self, nota: str):
        """Agrega una nota adicional a las existentes"""
        if self._notas:
            self._notas += f"\n- {nota}"
        else:
            self._notas = f"- {nota}"
    
    def tiempo_como_cliente(self) -> int:
        """Retorna los días desde el registro"""
        delta = datetime.now() - self._fecha_registro
        return delta.days
    
    def es_cliente_frecuente(self) -> bool:
        """Método base - se sobrescribe en ClienteFrecuente"""
        return False
    
    def aplicar_descuento(self) -> float:
        """Método base - clientes normales no tienen descuento"""
        return 0.0
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado = "✅ Activo" if self._activo else "❌ Inactivo"
        email_str = f"\n  Email: {self._email}" if self._email else ""
        direccion_str = f"\n  Dirección: {self._direccion}" if self._direccion else ""
        notas_str = f"\n  Notas: {self._notas}" if self._notas else ""
        
        return (f"👤 Cliente #{self._id}\n"
                f"  Nombre: {self._nombre}\n"
                f"  Teléfono: {self._telefono}"
                f"{email_str}"
                f"{direccion_str}"
                f"  Estado: {estado}\n"
                f"  Cliente desde: {self._fecha_registro.strftime('%d/%m/%Y')}"
                f"{notas_str}")
    
    def __repr__(self) -> str:
        return f"Cliente(id={self._id}, nombre='{self._nombre}')"

# ==============================================================================
# ARCHIVO 6/110: cliente_frecuente.py
# Directorio: entidades/clientes
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/clientes/cliente_frecuente.py
# ==============================================================================

from datetime import datetime
from typing import Optional, List
from src.entidades.clientes.cliente import Cliente
from src.entidades.clientes.nivel_de_fidelidad import NivelDeFidelidad
from src.constantes import DESCUENTO_CLIENTE_FRECUENTE


class ClienteFrecuente(Cliente):
    """Cliente con programa de fidelidad"""
    
    def __init__(self, nombre: str, telefono: str, email: Optional[str] = None):
        super().__init__(nombre, telefono, email)
        self._puntos_acumulados = 0
        self._total_gastado = 0.0
        self._cantidad_visitas = 0
        self._nivel_fidelidad = NivelDeFidelidad.BRONCE
        self._fecha_ultima_visita: Optional[datetime] = None
        self._historial_visitas: List[datetime] = []
        self._codigo_qr = f"QR-{self._id:06d}"  # Código único para el cliente
    
    # --- GETTERS ---
    def get_puntos_acumulados(self) -> int:
        return self._puntos_acumulados
    
    def get_total_gastado(self) -> float:
        return self._total_gastado
    
    def get_cantidad_visitas(self) -> int:
        return self._cantidad_visitas
    
    def get_nivel_fidelidad(self) -> NivelDeFidelidad:
        return self._nivel_fidelidad
    
    def get_fecha_ultima_visita(self) -> Optional[datetime]:
        return self._fecha_ultima_visita
    
    def get_codigo_qr(self) -> str:
        return self._codigo_qr
    
    def get_historial_visitas(self) -> List[datetime]:
        return self._historial_visitas.copy()
    
    # --- MÉTODOS DE PUNTOS Y FIDELIDAD ---
    def agregar_puntos(self, puntos: int):
        """Agrega puntos de fidelidad"""
        if puntos < 0:
            raise ValueError("Los puntos no pueden ser negativos")
        self._puntos_acumulados += puntos
    
    def canjear_puntos(self, puntos: int) -> bool:
        """Canjea puntos por beneficios"""
        if puntos < 0:
            raise ValueError("Los puntos a canjear deben ser positivos")
        if self._puntos_acumulados >= puntos:
            self._puntos_acumulados -= puntos
            return True
        return False
    
    def registrar_visita(self, monto_gastado: float):
        """Registra una nueva visita y actualiza estadísticas"""
        self._cantidad_visitas += 1
        self._total_gastado += monto_gastado
        self._fecha_ultima_visita = datetime.now()
        self._historial_visitas.append(self._fecha_ultima_visita)
        
        # Calcular puntos: 1 punto por cada $10 gastados
        puntos_ganados = int(monto_gastado / 10)
        self.agregar_puntos(puntos_ganados)
        
        # Actualizar nivel de fidelidad
        self._actualizar_nivel_fidelidad()
    
    def _actualizar_nivel_fidelidad(self):
        """Actualiza el nivel de fidelidad según visitas"""
        nuevo_nivel = NivelDeFidelidad.obtener_nivel_por_visitas(self._cantidad_visitas)
        if nuevo_nivel != self._nivel_fidelidad:
            self._nivel_fidelidad = nuevo_nivel
    
    def calcular_promedio_gasto(self) -> float:
        """Calcula el gasto promedio por visita"""
        if self._cantidad_visitas == 0:
            return 0.0
        return self._total_gastado / self._cantidad_visitas
    
    def dias_desde_ultima_visita(self) -> Optional[int]:
        """Retorna los días desde la última visita"""
        if not self._fecha_ultima_visita:
            return None
        delta = datetime.now() - self._fecha_ultima_visita
        return delta.days
    
    def esta_inactivo(self, dias_limite: int = 90) -> bool:
        """Verifica si el cliente está inactivo (sin visitas por X días)"""
        dias = self.dias_desde_ultima_visita()
        if dias is None:
            return True
        return dias > dias_limite
    
    # --- OVERRIDE DE MÉTODOS DE CLIENTE ---
    def es_cliente_frecuente(self) -> bool:
        """Override - siempre retorna True"""
        return True
    
    def aplicar_descuento(self) -> float:
        """Retorna el porcentaje de descuento según nivel de fidelidad"""
        # Puede usar el descuento del nivel o el constante general
        return max(self._nivel_fidelidad.descuento, DESCUENTO_CLIENTE_FRECUENTE)
    
    # --- BENEFICIOS Y RECOMPENSAS ---
    def puede_canjear_comida_gratis(self) -> bool:
        """Verifica si tiene suficientes puntos para comida gratis (500 puntos)"""
        return self._puntos_acumulados >= 500
    
    def puede_canjear_bebida_gratis(self) -> bool:
        """Verifica si tiene suficientes puntos para bebida gratis (200 puntos)"""
        return self._puntos_acumulados >= 200
    
    def puede_canjear_postre_gratis(self) -> bool:
        """Verifica si tiene suficientes puntos para postre gratis (150 puntos)"""
        return self._puntos_acumulados >= 150
    
    def obtener_beneficios_disponibles(self) -> List[str]:
        """Retorna lista de beneficios que puede canjear"""
        beneficios = []
        if self.puede_canjear_comida_gratis():
            beneficios.append("🍽️ Comida gratis (500 pts)")
        if self.puede_canjear_bebida_gratis():
            beneficios.append("🍷 Bebida gratis (200 pts)")
        if self.puede_canjear_postre_gratis():
            beneficios.append("🍰 Postre gratis (150 pts)")
        return beneficios
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        
        ultima_visita = (self._fecha_ultima_visita.strftime('%d/%m/%Y') 
                        if self._fecha_ultima_visita else "Nunca")
        
        beneficios = self.obtener_beneficios_disponibles()
        beneficios_str = "\n    " + "\n    ".join(beneficios) if beneficios else ""
        
        return (f"{base_str}\n"
                f"  {self._nivel_fidelidad}\n"
                f"  Puntos: {self._puntos_acumulados} pts\n"
                f"  Visitas: {self._cantidad_visitas}\n"
                f"  Total gastado: ${self._total_gastado:.2f}\n"
                f"  Promedio por visita: ${self.calcular_promedio_gasto():.2f}\n"
                f"  Última visita: {ultima_visita}\n"
                f"  Descuento: {self.aplicar_descuento()}%\n"
                f"  Código QR: {self._codigo_qr}"
                f"{beneficios_str}")
    
    def __repr__(self) -> str:
        return (f"ClienteFrecuente(id={self._id}, "
                f"nombre='{self._nombre}', "
                f"nivel={self._nivel_fidelidad.nombre_nivel})")

# ==============================================================================
# ARCHIVO 7/110: nivel_de_fidelidad.py
# Directorio: entidades/clientes
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/clientes/nivel_de_fidelidad.py
# ==============================================================================

from enum import Enum

class NivelDeFidelidad(Enum):
    """Niveles de fidelidad para clientes frecuentes"""
    BRONCE = ("Bronce", 5, "🥉")      # nivel, descuento%, emoji
    PLATA = ("Plata", 10, "🥈")
    ORO = ("Oro", 15, "🥇")
    PLATINO = ("Platino", 20, "💎")
    
    def __init__(self, nombre: str, descuento: int, emoji: str):
        self._nombre_nivel = nombre
        self._descuento = descuento
        self._emoji = emoji
    
    @property
    def nombre_nivel(self) -> str:
        return self._nombre_nivel
    
    @property
    def descuento(self) -> int:
        """Porcentaje de descuento"""
        return self._descuento
    
    @property
    def emoji(self) -> str:
        return self._emoji
    
    def __str__(self):
        return f"{self._emoji} {self._nombre_nivel}"
    
    @classmethod
    def obtener_nivel_por_visitas(cls, cantidad_visitas: int):
        """Determina el nivel según la cantidad de visitas"""
        if cantidad_visitas >= 50:
            return cls.PLATINO
        elif cantidad_visitas >= 30:
            return cls.ORO
        elif cantidad_visitas >= 15:
            return cls.PLATA
        else:
            return cls.BRONCE


################################################################################
# DIRECTORIO: entidades/cocina
################################################################################

# ==============================================================================
# ARCHIVO 8/110: __init__.py
# Directorio: entidades/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 9/110: estacion_bebidas.py
# Directorio: entidades/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estacion_bebidas.py
# ==============================================================================

from datetime import datetime
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.orden_cocina import OrdenCocina

class EstacionBebidas(EstacionCocina):
    """Estación especializada en bebidas (barra)"""
    
    def __init__(self):
        super().__init__(nombre_estacion="Bebidas", capacidad_maxima=10)
        self._hielo_disponible_kg = 50.0
        self._copas_limpias = 100
        self._vasos_limpios = 150
        self._maquina_cafe_encendida = True
        self._ultima_limpieza = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_hielo_disponible(self) -> float:
        return self._hielo_disponible_kg
    
    def get_copas_limpias(self) -> int:
        return self._copas_limpias
    
    def get_vasos_limpios(self) -> int:
        return self._vasos_limpios
    
    def esta_maquina_cafe_encendida(self) -> bool:
        return self._maquina_cafe_encendida
    
    # --- OPERACIONES ---
    def agregar_hielo(self, cantidad_kg: float):
        """Agrega hielo"""
        if cantidad_kg <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._hielo_disponible_kg += cantidad_kg
    
    def consumir_hielo(self, cantidad_kg: float = 0.2):
        """Consume hielo al preparar bebida"""
        if self._hielo_disponible_kg < cantidad_kg:
            raise ValueError("No hay suficiente hielo")
        self._hielo_disponible_kg -= cantidad_kg
    
    def usar_copa(self):
        """Usa una copa"""
        if self._copas_limpias <= 0:
            raise ValueError("No hay copas limpias")
        self._copas_limpias -= 1
    
    def usar_vaso(self):
        """Usa un vaso"""
        if self._vasos_limpios <= 0:
            raise ValueError("No hay vasos limpios")
        self._vasos_limpios -= 1
    
    def lavar_cristaleria(self, copas: int = 0, vasos: int = 0):
        """Agrega copas y vasos limpios"""
        self._copas_limpias += copas
        self._vasos_limpios += vasos
    
    # --- OVERRIDE DE MÉTODOS ABSTRACTOS ---
    def verificar_equipamiento(self) -> bool:
        """Verifica que se pueda preparar bebidas"""
        if not self._maquina_cafe_encendida:
            return False
        if self._hielo_disponible_kg < 1.0:
            return False
        if self._copas_limpias + self._vasos_limpios < 10:
            return False
        return True
    
    def realizar_mantenimiento(self):
        """Realiza limpieza de la barra"""
        self._ultima_limpieza = datetime.now()
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Rango óptimo de temperatura"""
        return (18, 25)  # °C
    
    # --- VALIDACIONES ---
    def necesita_hielo(self) -> bool:
        """Verifica si necesita hielo"""
        return self._hielo_disponible_kg < 10.0
    
    def necesita_cristaleria(self) -> bool:
        """Verifica si necesita lavar cristalería"""
        return (self._copas_limpias < 20 or self._vasos_limpios < 30)
    
    def puede_preparar_bebidas(self) -> bool:
        """Verifica si puede preparar bebidas"""
        return (self._hielo_disponible_kg >= 0.2 and 
                (self._copas_limpias > 0 or self._vasos_limpios > 0))
    
    # --- OVERRIDE DE COMPLETAR ORDEN ---
    def completar_orden(self, orden_id: int):
        """Override para consumir recursos"""
        resultado = super().completar_orden(orden_id)
        if resultado:
            # Lógica simplificada: alternamos entre copa y vaso
            if self._copas_limpias > 0:
                self.usar_copa()
            else:
                self.usar_vaso()
            self.consumir_hielo(0.1)
        return resultado
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        
        hielo_alerta = "⚠️ BAJO" if self.necesita_hielo() else "✓"
        cristal_alerta = "⚠️ LAVAR" if self.necesita_cristaleria() else "✓"
        cafe = "☕ Encendida" if self._maquina_cafe_encendida else "☕ Apagada"
        
        return (f"{base_str}\n"
                f"  Máquina café: {cafe}\n"
                f"  Hielo: {self._hielo_disponible_kg:.1f} kg {hielo_alerta}\n"
                f"  Copas: {self._copas_limpias} | Vasos: {self._vasos_limpios} {cristal_alerta}")
    
    def __repr__(self) -> str:
        return f"EstacionBebidas(ordenes={self.contar_ordenes_totales()}, hielo={self._hielo_disponible_kg:.1f}kg)"

# ==============================================================================
# ARCHIVO 10/110: estacion_cocina.py
# Directorio: entidades/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estacion_cocina.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from src.entidades.cocina.orden_cocina import OrdenCocina
from src.entidades.cocina.estado_orden import EstadoOrden


class EstacionCocina(ABC):
    """Clase base abstracta para todas las estaciones de cocina"""
    
    def __init__(self, nombre_estacion: str, capacidad_maxima: int):
        self._nombre_estacion = nombre_estacion
        self._capacidad_maxima = capacidad_maxima  # Órdenes simultáneas
        self._ordenes_pendientes: List[OrdenCocina] = []
        self._ordenes_en_preparacion: List[OrdenCocina] = []
        self._ordenes_completadas: List[OrdenCocina] = []
        self._activa = True
        self._temperatura_actual = 20.0  # °C
        self._chef_responsable_id: Optional[int] = None
    
    # --- GETTERS ---
    def get_nombre_estacion(self) -> str:
        return self._nombre_estacion
    
    def get_capacidad_maxima(self) -> int:
        return self._capacidad_maxima
    
    def get_ordenes_pendientes(self) -> List[OrdenCocina]:
        return self._ordenes_pendientes.copy()
    
    def get_ordenes_en_preparacion(self) -> List[OrdenCocina]:
        return self._ordenes_en_preparacion.copy()
    
    def get_ordenes_completadas(self) -> List[OrdenCocina]:
        return self._ordenes_completadas.copy()
    
    def esta_activa(self) -> bool:
        return self._activa
    
    def get_temperatura_actual(self) -> float:
        return self._temperatura_actual
    
    def get_chef_responsable_id(self) -> Optional[int]:
        return self._chef_responsable_id
    
    # --- SETTERS ---
    def set_activa(self, activa: bool):
        self._activa = activa
    
    def set_temperatura_actual(self, temperatura: float):
        self._temperatura_actual = temperatura
    
    def set_chef_responsable(self, chef_id: int):
        self._chef_responsable_id = chef_id
    
    # --- GESTIÓN DE ÓRDENES ---
    def recibir_orden(self, orden: OrdenCocina):
        """Recibe una nueva orden en la estación"""
        if not self._activa:
            raise ValueError(f"La estación {self._nombre_estacion} no está activa")
        
        if orden.get_estacion_asignada() != self._nombre_estacion:
            raise ValueError(f"Esta orden no pertenece a la estación {self._nombre_estacion}")
        
        self._ordenes_pendientes.append(orden)
        self._ordenes_pendientes.sort(key=lambda o: (-o.get_prioridad(), o.get_id()))
    
    def iniciar_orden(self, orden_id: int) -> bool:
        """Inicia la preparación de una orden pendiente"""
        if not self.puede_iniciar_orden():
            return False
        
        for i, orden in enumerate(self._ordenes_pendientes):
            if orden.get_id() == orden_id:
                orden.iniciar_preparacion()
                self._ordenes_en_preparacion.append(orden)
                self._ordenes_pendientes.pop(i)
                return True
        return False
    
    def completar_orden(self, orden_id: int):
        """Marca una orden como completada"""
        for i, orden in enumerate(self._ordenes_en_preparacion):
            if orden.get_id() == orden_id:
                orden.marcar_como_lista()
                self._ordenes_completadas.append(orden)
                self._ordenes_en_preparacion.pop(i)
                return True
        return False
    
    def cancelar_orden(self, orden_id: int, motivo: str = ""):
        """Cancela una orden"""
        # Buscar en pendientes
        for i, orden in enumerate(self._ordenes_pendientes):
            if orden.get_id() == orden_id:
                orden.cancelar(motivo)
                self._ordenes_pendientes.pop(i)
                return True
        
        # Buscar en preparación
        for i, orden in enumerate(self._ordenes_en_preparacion):
            if orden.get_id() == orden_id:
                orden.cancelar(motivo)
                self._ordenes_en_preparacion.pop(i)
                return True
        
        return False
    
    # --- VALIDACIONES ---
    def puede_iniciar_orden(self) -> bool:
        """Verifica si hay capacidad para iniciar otra orden"""
        return len(self._ordenes_en_preparacion) < self._capacidad_maxima
    
    def tiene_ordenes_pendientes(self) -> bool:
        """Verifica si hay órdenes pendientes"""
        return len(self._ordenes_pendientes) > 0
    
    def esta_saturada(self) -> bool:
        """Verifica si la estación está a máxima capacidad"""
        return len(self._ordenes_en_preparacion) >= self._capacidad_maxima
    
    # --- ESTADÍSTICAS ---
    def contar_ordenes_totales(self) -> int:
        """Cuenta todas las órdenes en la estación"""
        return (len(self._ordenes_pendientes) + 
                len(self._ordenes_en_preparacion) + 
                len(self._ordenes_completadas))
    
    def calcular_tiempo_promedio_preparacion(self) -> float:
        """Calcula el tiempo promedio de preparación de órdenes completadas"""
        if not self._ordenes_completadas:
            return 0.0
        
        tiempos = [o.calcular_tiempo_preparacion() 
                   for o in self._ordenes_completadas 
                   if o.calcular_tiempo_preparacion() is not None]
        
        if not tiempos:
            return 0.0
        
        return sum(tiempos) / len(tiempos)
    
    def obtener_ordenes_retrasadas(self) -> List[OrdenCocina]:
        """Retorna lista de órdenes retrasadas"""
        return [o for o in self._ordenes_en_preparacion if o.esta_retrasada()]
    
    def limpiar_ordenes_completadas(self):
        """Limpia las órdenes completadas (para mantenimiento)"""
        self._ordenes_completadas.clear()
    
    # --- MÉTODOS ABSTRACTOS ---
    @abstractmethod
    def verificar_equipamiento(self) -> bool:
        """Verifica que el equipamiento esté funcionando correctamente"""
        pass
    
    @abstractmethod
    def realizar_mantenimiento(self):
        """Realiza tareas de mantenimiento específicas de la estación"""
        pass
    
    @abstractmethod
    def obtener_temperatura_operacion(self) -> tuple:
        """Retorna (temp_minima, temp_maxima) de operación"""
        pass
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado = "✅ Activa" if self._activa else "❌ Inactiva"
        saturacion = "🔴 SATURADA" if self.esta_saturada() else "🟢 OK"
        
        retrasadas = self.obtener_ordenes_retrasadas()
        alerta_retrasos = f"\n  ⚠️ {len(retrasadas)} órdenes retrasadas" if retrasadas else ""
        
        return (f"🏭 Estación: {self._nombre_estacion}\n"
                f"  Estado: {estado} - {saturacion}\n"
                f"  Capacidad: {len(self._ordenes_en_preparacion)}/{self._capacidad_maxima}\n"
                f"  Pendientes: {len(self._ordenes_pendientes)}\n"
                f"  En preparación: {len(self._ordenes_en_preparacion)}\n"
                f"  Completadas (hoy): {len(self._ordenes_completadas)}\n"
                f"  Temperatura: {self._temperatura_actual}°C\n"
                f"  Tiempo promedio: {self.calcular_tiempo_promedio_preparacion():.1f} min"
                f"{alerta_retrasos}")
    
    def __repr__(self) -> str:
        return f"EstacionCocina(nombre='{self._nombre_estacion}', ordenes={self.contar_ordenes_totales()})"

# ==============================================================================
# ARCHIVO 11/110: estacion_cocina_general.py
# Directorio: entidades/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estacion_cocina_general.py
# ==============================================================================

# src/entidades/cocina/estacion_cocina_general.py

from datetime import datetime
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.constantes import TEMPERATURA_COCINA_MIN, TEMPERATURA_COCINA_MAX

class EstacionCocinaGeneral(EstacionCocina):
    """
    Estación de cocina general para items que no tienen
    una estación especializada (ej. Entradas, Pescados).
    Implementación concreta de EstacionCocina.
    """
    
    def __init__(self):
        # Llama al init de la clase base con sus valores
        super().__init__(nombre_estacion="Cocina", capacidad_maxima=10)
        self._ultima_limpieza = None
        # Asumimos que la cocina general empieza encendida
        self.set_activa(True) 
        self.set_temperatura_actual(22.0) # Temperatura ambiente
    
    # --- Implementación de métodos abstractos ---
    
    def verificar_equipamiento(self) -> bool:
        """
        Implementación simple: Asume que la cocina general
        siempre está operativa si está activa y en temperatura.
        """
        temp_ok = (TEMPERATURA_COCINA_MIN <= 
                   self.get_temperatura_actual() <= 
                   TEMPERATURA_COCINA_MAX)
        
        if not temp_ok:
            print(f"ALERTA: Temperatura fuera de rango en {self.get_nombre_estacion()}")
            
        return self.esta_activa() and temp_ok
    
    def realizar_mantenimiento(self):
        """Implementación simple: solo limpia órdenes completadas."""
        print(f"Realizando mantenimiento en {self.get_nombre_estacion()}...")
        self._ultima_limpieza = datetime.now()
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Retorna el rango estándar de temperatura ambiente de cocina."""
        return (TEMPERATURA_COCINA_MIN, TEMPERATURA_COCINA_MAX)

# ==============================================================================
# ARCHIVO 12/110: estacion_parrilla.py
# Directorio: entidades/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estacion_parrilla.py
# ==============================================================================

from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.constantes import TEMPERATURA_PARRILLA


class EstacionParrilla(EstacionCocina):
    """Estación especializada en parrilla (carnes y pollo)"""
    
    def __init__(self):
        super().__init__(nombre_estacion="Parrilla", capacidad_maxima=8)
        self._temperatura_parrilla = TEMPERATURA_PARRILLA
        self._carbon_disponible = 100.0  # kg
        self._parrilla_encendida = False
        self._ultima_limpieza = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_temperatura_parrilla(self) -> float:
        return self._temperatura_parrilla
    
    def get_carbon_disponible(self) -> float:
        return self._carbon_disponible
    
    def esta_parrilla_encendida(self) -> bool:
        return self._parrilla_encendida
    
    # --- SETTERS ESPECÍFICOS ---
    def set_temperatura_parrilla(self, temperatura: float):
        if temperatura < 150 or temperatura > 300:
            raise ValueError("Temperatura de parrilla fuera de rango (150-300°C)")
        self._temperatura_parrilla = temperatura
    
    def encender_parrilla(self):
        """Enciende la parrilla"""
        if self._carbon_disponible < 5:
            raise ValueError("No hay suficiente carbón para encender la parrilla")
        self._parrilla_encendida = True
        self._temperatura_parrilla = TEMPERATURA_PARRILLA
    
    def apagar_parrilla(self):
        """Apaga la parrilla"""
        self._parrilla_encendida = False
        self._temperatura_parrilla = self._temperatura_actual
    
    def agregar_carbon(self, cantidad: float):
        """Agrega carbón a la parrilla"""
        if cantidad <= 0:
            raise ValueError("La cantidad de carbón debe ser positiva")
        self._carbon_disponible += cantidad
    
    def consumir_carbon(self, cantidad: float = 2.0):
        """Consume carbón durante la cocción"""
        if self._carbon_disponible < cantidad:
            raise ValueError("No hay suficiente carbón")
        self._carbon_disponible -= cantidad
    
    # --- OVERRIDE DE MÉTODOS ABSTRACTOS ---
    def verificar_equipamiento(self) -> bool:
        """Verifica que la parrilla esté en condiciones de operar"""
        if not self._parrilla_encendida:
            return False
        
        if self._carbon_disponible < 10:
            return False
        
        if self._temperatura_parrilla < 150:
            return False
        
        return True
    
    def realizar_mantenimiento(self):
        """Realiza limpieza y mantenimiento de la parrilla"""
        from datetime import datetime
        self._ultima_limpieza = datetime.now()
        # Limpiar órdenes completadas
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Retorna rango de temperatura óptima de operación"""
        return (180, 220)  # °C
    
    # --- MÉTODOS ESPECÍFICOS ---
    def puede_cocinar_a_la_parrilla(self) -> bool:
        """Verifica si se puede cocinar (parrilla encendida y con carbón)"""
        return (self._parrilla_encendida and 
                self._carbon_disponible >= 5 and 
                self._temperatura_parrilla >= 150)
    
    def necesita_carbon(self) -> bool:
        """Verifica si necesita reposición de carbón"""
        return self._carbon_disponible < 20
    
    def ajustar_temperatura(self, incremento: float):
        """Ajusta la temperatura de la parrilla"""
        nueva_temp = self._temperatura_parrilla + incremento
        self.set_temperatura_parrilla(nueva_temp)
    
    # --- OVERRIDE DE RECIBIR ORDEN ---
    def recibir_orden(self, orden):
        """Override para verificar que la parrilla esté lista"""
        if not self.puede_cocinar_a_la_parrilla():
            raise ValueError("La parrilla no está lista para cocinar")
        super().recibir_orden(orden)
    
    # --- OVERRIDE DE COMPLETAR ORDEN ---
    def completar_orden(self, orden_id: int):
        """Override para consumir carbón al completar"""
        resultado = super().completar_orden(orden_id)
        if resultado:
            self.consumir_carbon(1.5)  # Consume carbón por orden
        return resultado
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        
        parrilla_estado = "🔥 Encendida" if self._parrilla_encendida else "⚫ Apagada"
        carbon_alerta = "⚠️ BAJO" if self.necesita_carbon() else "✓"
        
        return (f"{base_str}\n"
                f"  Parrilla: {parrilla_estado}\n"
                f"  Temp. Parrilla: {self._temperatura_parrilla}°C\n"
                f"  Carbón: {self._carbon_disponible:.1f} kg {carbon_alerta}")
    
    def __repr__(self) -> str:
        return f"EstacionParrilla(ordenes={self.contar_ordenes_totales()}, carbon={self._carbon_disponible:.1f}kg)"

# ==============================================================================
# ARCHIVO 13/110: estacion_pastas.py
# Directorio: entidades/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estacion_pastas.py
# ==============================================================================

from datetime import datetime
from typing import Optional
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.orden_cocina import OrdenCocina

class EstacionPastas(EstacionCocina):
    """Estación especializada en pastas"""
    
    def __init__(self):
        super().__init__(nombre_estacion="Pastas", capacidad_maxima=6)
        self._agua_hirviendo = False
        self._ollas_disponibles = 4
        self._cantidad_pasta_kg = 50.0  # kg disponibles
        self._ultima_limpieza = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_ollas_disponibles(self) -> int:
        return self._ollas_disponibles
    
    def get_cantidad_pasta(self) -> float:
        return self._cantidad_pasta_kg
    
    def esta_agua_hirviendo(self) -> bool:
        return self._agua_hirviendo
    
    # --- OPERACIONES ---
    def calentar_agua(self):
        """Calienta el agua para cocinar"""
        self._agua_hirviendo = True
        self._temperatura_actual = 100.0
    
    def enfriar_agua(self):
        """Enfría el agua"""
        self._agua_hirviendo = False
        self._temperatura_actual = 20.0
    
    def agregar_pasta(self, cantidad_kg: float):
        """Agrega pasta al inventario"""
        if cantidad_kg <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._cantidad_pasta_kg += cantidad_kg
    
    def consumir_pasta(self, cantidad_kg: float = 0.3):
        """Consume pasta al preparar un plato"""
        if self._cantidad_pasta_kg < cantidad_kg:
            raise ValueError("No hay suficiente pasta")
        self._cantidad_pasta_kg -= cantidad_kg
    
    def usar_olla(self):
        """Marca una olla como en uso"""
        if self._ollas_disponibles <= 0:
            raise ValueError("No hay ollas disponibles")
        self._ollas_disponibles -= 1
    
    def liberar_olla(self):
        """Libera una olla"""
        if self._ollas_disponibles >= 4:
            raise ValueError("Todas las ollas ya están libres")
        self._ollas_disponibles += 1
    
    # --- OVERRIDE DE MÉTODOS ABSTRACTOS ---
    def verificar_equipamiento(self) -> bool:
        """Verifica que se pueda cocinar pasta"""
        if not self._agua_hirviendo:
            return False
        if self._ollas_disponibles <= 0:
            return False
        if self._cantidad_pasta_kg < 1.0:
            return False
        return True
    
    def realizar_mantenimiento(self):
        """Realiza limpieza de la estación"""
        self._ultima_limpieza = datetime.now()
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Rango óptimo de temperatura"""
        return (18, 28)  # °C ambiente
    
    # --- VALIDACIONES ---
    def necesita_pasta(self) -> bool:
        """Verifica si necesita reposición de pasta"""
        return self._cantidad_pasta_kg < 10.0
    
    def puede_cocinar_pasta(self) -> bool:
        """Verifica si puede cocinar pasta"""
        return (self._agua_hirviendo and 
                self._ollas_disponibles > 0 and 
                self._cantidad_pasta_kg >= 0.3)
    
    # --- OVERRIDE DE COMPLETAR ORDEN ---
    def completar_orden(self, orden_id: int):
        """Override para liberar olla y consumir pasta"""
        resultado = super().completar_orden(orden_id)
        if resultado:
            self.liberar_olla()
            self.consumir_pasta()
        return resultado
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        agua_estado = "💧 Hirviendo" if self._agua_hirviendo else "💧 Fría"
        pasta_alerta = "⚠️ BAJO" if self.necesita_pasta() else "✓"
        
        return (f"{base_str}\n"
                f"  Agua: {agua_estado}\n"
                f"  Ollas disponibles: {self._ollas_disponibles}/4\n"
                f"  Pasta: {self._cantidad_pasta_kg:.1f} kg {pasta_alerta}")
    
    def __repr__(self) -> str:
        return f"EstacionPastas(ordenes={self.contar_ordenes_totales()}, pasta={self._cantidad_pasta_kg:.1f}kg)"


# ==============================================================================
# ARCHIVO 14/110: estacion_postres.py
# Directorio: entidades/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estacion_postres.py
# ==============================================================================

from datetime import datetime
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.orden_cocina import OrdenCocina

class EstacionPostres(EstacionCocina):
    """Estación especializada en postres"""
    
    def __init__(self):
        super().__init__(nombre_estacion="Postres", capacidad_maxima=5)
        self._heladera_encendida = True
        self._temperatura_heladera = -5.0  # °C
        self._horno_encendido = False
        self._temperatura_horno = 0.0
        self._ultima_limpieza = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_temperatura_heladera(self) -> float:
        return self._temperatura_heladera
    
    def get_temperatura_horno(self) -> float:
        return self._temperatura_horno
    
    def esta_heladera_encendida(self) -> bool:
        return self._heladera_encendida
    
    def esta_horno_encendido(self) -> bool:
        return self._horno_encendido
    
    # --- OPERACIONES ---
    def encender_horno(self, temperatura: float = 180.0):
        """Enciende el horno de postres"""
        if temperatura < 100 or temperatura > 250:
            raise ValueError("Temperatura fuera de rango (100-250°C)")
        self._horno_encendido = True
        self._temperatura_horno = temperatura
    
    def apagar_horno(self):
        """Apaga el horno"""
        self._horno_encendido = False
        self._temperatura_horno = 0.0
    
    def ajustar_temperatura_horno(self, temperatura: float):
        """Ajusta la temperatura del horno"""
        if not self._horno_encendido:
            raise ValueError("El horno no está encendido")
        if temperatura < 100 or temperatura > 250:
            raise ValueError("Temperatura fuera de rango")
        self._temperatura_horno = temperatura
    
    def ajustar_temperatura_heladera(self, temperatura: float):
        """Ajusta la temperatura de la heladera"""
        if temperatura > 5:
            raise ValueError("La heladera debe estar bajo 5°C")
        self._temperatura_heladera = temperatura
    
    # --- OVERRIDE DE MÉTODOS ABSTRACTOS ---
    def verificar_equipamiento(self) -> bool:
        """Verifica que el equipamiento esté funcionando"""
        if not self._heladera_encendida:
            return False
        if self._temperatura_heladera > 5:
            return False
        return True
    
    def realizar_mantenimiento(self):
        """Realiza mantenimiento de la estación"""
        self._ultima_limpieza = datetime.now()
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Rango óptimo de temperatura ambiente"""
        return (18, 24)  # °C
    
    # --- VALIDACIONES ---
    def puede_hacer_postres_frios(self) -> bool:
        """Verifica si puede hacer postres fríos"""
        return self._heladera_encendida and self._temperatura_heladera <= 0
    
    def puede_hornear(self) -> bool:
        """Verifica si puede hornear postres"""
        return self._horno_encendido and self._temperatura_horno >= 150
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        
        heladera_estado = f"❄️ {self._temperatura_heladera}°C" if self._heladera_encendida else "❄️ Apagada"
        horno_estado = f"🔥 {self._temperatura_horno}°C" if self._horno_encendido else "🔥 Apagado"
        
        return (f"{base_str}\n"
                f"  Heladera: {heladera_estado}\n"
                f"  Horno: {horno_estado}")
    
    def __repr__(self) -> str:
        return f"EstacionPostres(ordenes={self.contar_ordenes_totales()})"

# ==============================================================================
# ARCHIVO 15/110: estado_orden.py
# Directorio: entidades/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estado_orden.py
# ==============================================================================

from enum import Enum

class EstadoOrden(Enum):
    """Estados posibles de una orden en cocina"""
    PENDIENTE = "Pendiente"
    EN_PREPARACION = "En Preparación"
    LISTA = "Lista"
    ENTREGADA = "Entregada"
    CANCELADA = "Cancelada"
    
    def __str__(self):
        return self.value

# ==============================================================================
# ARCHIVO 16/110: orden_cocina.py
# Directorio: entidades/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/orden_cocina.py
# ==============================================================================

from datetime import datetime
from typing import Optional
from src.entidades.cocina.estado_orden import EstadoOrden
from src.entidades.pedidos.item_pedido import ItemPedido


class OrdenCocina:
    """Representa una orden individual en la cocina para un item específico"""
    
    _contador_id = 0
    
    def __init__(self, item_pedido: ItemPedido, pedido_id: int, mesa_id: Optional[int] = None):
        OrdenCocina._contador_id += 1
        self._id = OrdenCocina._contador_id
        self._item_pedido = item_pedido
        self._pedido_id = pedido_id
        self._mesa_id = mesa_id
        self._estado = EstadoOrden.PENDIENTE
        self._estacion_asignada = item_pedido.get_item_menu().get_estacion_cocina()
        self._prioridad = 1  # 1=normal, 2=alta, 3=urgente
        self._chef_asignado_id: Optional[int] = None
        
        # Tiempos
        self._fecha_hora_creacion = datetime.now()
        self._fecha_hora_inicio: Optional[datetime] = None
        self._fecha_hora_fin: Optional[datetime] = None
        
        # Observaciones
        self._notas_chef = ""
        self._observaciones_cliente = item_pedido.get_observaciones_especiales()
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_item_pedido(self) -> ItemPedido:
        return self._item_pedido
    
    def get_pedido_id(self) -> int:
        return self._pedido_id
    
    def get_mesa_id(self) -> Optional[int]:
        return self._mesa_id
    
    def get_estado(self) -> EstadoOrden:
        return self._estado
    
    def get_estacion_asignada(self) -> str:
        return self._estacion_asignada
    
    def get_prioridad(self) -> int:
        return self._prioridad
    
    def get_chef_asignado_id(self) -> Optional[int]:
        return self._chef_asignado_id
    
    def get_fecha_hora_creacion(self) -> datetime:
        return self._fecha_hora_creacion
    
    def get_notas_chef(self) -> str:
        return self._notas_chef
    
    def get_observaciones_cliente(self) -> str:
        return self._observaciones_cliente
    
    # --- SETTERS ---
    def set_prioridad(self, prioridad: int):
        """Establece la prioridad: 1=normal, 2=alta, 3=urgente"""
        if prioridad not in [1, 2, 3]:
            raise ValueError("La prioridad debe ser 1, 2 o 3")
        self._prioridad = prioridad
    
    def set_chef_asignado(self, chef_id: int):
        self._chef_asignado_id = chef_id
    
    def agregar_nota_chef(self, nota: str):
        """Agrega una nota del chef sobre la preparación"""
        if self._notas_chef:
            self._notas_chef += f"\n- {nota}"
        else:
            self._notas_chef = f"- {nota}"
    
    # --- GESTIÓN DE ESTADO ---
    def iniciar_preparacion(self):
        """Marca la orden como en preparación"""
        if self._estado != EstadoOrden.PENDIENTE:
            raise ValueError(f"No se puede iniciar una orden en estado {self._estado}")
        self._estado = EstadoOrden.EN_PREPARACION
        self._fecha_hora_inicio = datetime.now()
    
    def marcar_como_lista(self):
        """Marca la orden como lista para servir"""
        if self._estado != EstadoOrden.EN_PREPARACION:
            raise ValueError(f"No se puede marcar como lista una orden en estado {self._estado}")
        self._estado = EstadoOrden.LISTA
        self._fecha_hora_fin = datetime.now()
    
    def marcar_como_entregada(self):
        """Marca la orden como entregada al cliente"""
        if self._estado != EstadoOrden.LISTA:
            raise ValueError(f"No se puede entregar una orden en estado {self._estado}")
        self._estado = EstadoOrden.ENTREGADA
    
    def cancelar(self, motivo: str = ""):
        """Cancela la orden"""
        if self._estado == EstadoOrden.ENTREGADA:
            raise ValueError("No se puede cancelar una orden ya entregada")
        self._estado = EstadoOrden.CANCELADA
        if motivo:
            self.agregar_nota_chef(f"CANCELADA: {motivo}")
    
    # --- CÁLCULOS DE TIEMPO ---
    def calcular_tiempo_preparacion(self) -> Optional[int]:
        """Calcula el tiempo real de preparación en minutos"""
        if not self._fecha_hora_inicio or not self._fecha_hora_fin:
            return None
        delta = self._fecha_hora_fin - self._fecha_hora_inicio
        return int(delta.total_seconds() / 60)
    
    def calcular_tiempo_espera_actual(self) -> int:
        """Calcula el tiempo de espera desde la creación hasta ahora"""
        delta = datetime.now() - self._fecha_hora_creacion
        return int(delta.total_seconds() / 60)
    
    def get_tiempo_estimado(self) -> int:
        """Retorna el tiempo estimado de preparación del item"""
        return self._item_pedido.get_item_menu().get_tiempo_preparacion()
    
    def esta_retrasada(self) -> bool:
        """Verifica si la orden está retrasada respecto al tiempo estimado"""
        if self._estado in [EstadoOrden.LISTA, EstadoOrden.ENTREGADA, EstadoOrden.CANCELADA]:
            return False
        return self.calcular_tiempo_espera_actual() > self.get_tiempo_estimado()
    
    # --- VALIDACIONES ---
    def puede_iniciarse(self) -> bool:
        """Verifica si la orden puede iniciarse"""
        return self._estado == EstadoOrden.PENDIENTE and self._chef_asignado_id is not None
    
    def esta_en_progreso(self) -> bool:
        """Verifica si la orden está siendo preparada"""
        return self._estado == EstadoOrden.EN_PREPARACION
    
    def esta_completada(self) -> bool:
        """Verifica si la orden está completada (lista o entregada)"""
        return self._estado in [EstadoOrden.LISTA, EstadoOrden.ENTREGADA]
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado_emoji = {
            EstadoOrden.PENDIENTE: "⏳",
            EstadoOrden.EN_PREPARACION: "👨‍🍳",
            EstadoOrden.LISTA: "✅",
            EstadoOrden.ENTREGADA: "🍽️",
            EstadoOrden.CANCELADA: "❌"
        }
        
        prioridad_str = "🔴 URGENTE" if self._prioridad == 3 else "🟡 ALTA" if self._prioridad == 2 else "🟢 NORMAL"
        
        mesa_str = f"Mesa {self._mesa_id}" if self._mesa_id else "Para llevar"
        
        tiempo_info = ""
        if self._estado == EstadoOrden.EN_PREPARACION:
            tiempo_info = f"\n  ⏱️ Tiempo transcurrido: {self.calcular_tiempo_espera_actual()} min"
            if self.esta_retrasada():
                tiempo_info += " ⚠️ RETRASADA"
        elif self._fecha_hora_fin:
            tiempo_real = self.calcular_tiempo_preparacion()
            tiempo_info = f"\n  ✓ Tiempo de preparación: {tiempo_real} min"
        
        obs_cliente = f"\n  💬 Cliente: {self._observaciones_cliente}" if self._observaciones_cliente else ""
        notas_chef = f"\n  📝 Chef: {self._notas_chef}" if self._notas_chef else ""
        
        return (f"{estado_emoji.get(self._estado, '📋')} Orden #{self._id} - {prioridad_str}\n"
                f"  Pedido #{self._pedido_id} - {mesa_str}\n"
                f"  Item: {self._item_pedido.get_item_menu().get_nombre()} x{self._item_pedido.get_cantidad()}\n"
                f"  Estación: {self._estacion_asignada}\n"
                f"  Estado: {self._estado.value}\n"
                f"  Estimado: {self.get_tiempo_estimado()} min"
                f"{tiempo_info}"
                f"{obs_cliente}"
                f"{notas_chef}")
    
    def __repr__(self) -> str:
        return (f"OrdenCocina(id={self._id}, "
                f"pedido={self._pedido_id}, "
                f"estado={self._estado}, "
                f"estacion={self._estacion_asignada})")


################################################################################
# DIRECTORIO: entidades/inventario
################################################################################

# ==============================================================================
# ARCHIVO 17/110: __init__.py
# Directorio: entidades/inventario
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/inventario/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 18/110: alerta_stock.py
# Directorio: entidades/inventario
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/inventario/alerta_stock.py
# ==============================================================================

from datetime import datetime
from enum import Enum
from typing import Optional


class TipoAlerta(Enum):
    """Tipos de alertas de stock"""
    STOCK_BAJO = ("Stock Bajo", "🟡", 2)  # tipo, emoji, prioridad
    STOCK_CRITICO = ("Stock Crítico", "🟠", 3)
    AGOTADO = ("Agotado", "🔴", 5)
    POR_VENCER = ("Por Vencer", "⏰", 3)
    VENCIDO = ("Vencido", "⚠️", 5)
    SOBRESTOCK = ("Sobrestock", "📈", 1)
    
    def __init__(self, descripcion: str, emoji: str, prioridad: int):
        self._descripcion = descripcion
        self._emoji = emoji
        self._prioridad = prioridad
    
    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @property
    def emoji(self) -> str:
        return self._emoji
    
    @property
    def prioridad(self) -> int:
        """Prioridad de 1 (baja) a 5 (crítica)"""
        return self._prioridad
    
    def __str__(self):
        return f"{self._emoji} {self._descripcion}"


class AlertaStock:
    """Representa una alerta del sistema de inventario"""
    
    _contador_id = 0
    
    def __init__(self, ingrediente_id: int, ingrediente_nombre: str, 
                 tipo_alerta: TipoAlerta, mensaje: str):
        AlertaStock._contador_id += 1
        self._id = AlertaStock._contador_id
        self._ingrediente_id = ingrediente_id
        self._ingrediente_nombre = ingrediente_nombre
        self._tipo_alerta = tipo_alerta
        self._mensaje = mensaje
        self._fecha_hora_generacion = datetime.now()
        self._resuelta = False
        self._fecha_hora_resolucion: Optional[datetime] = None
        self._accion_tomada = ""
        self._usuario_responsable_id: Optional[int] = None
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_ingrediente_id(self) -> int:
        return self._ingrediente_id
    
    def get_ingrediente_nombre(self) -> str:
        return self._ingrediente_nombre
    
    def get_tipo_alerta(self) -> TipoAlerta:
        return self._tipo_alerta
    
    def get_mensaje(self) -> str:
        return self._mensaje
    
    def get_fecha_hora_generacion(self) -> datetime:
        return self._fecha_hora_generacion
    
    def esta_resuelta(self) -> bool:
        return self._resuelta
    
    def get_fecha_hora_resolucion(self) -> Optional[datetime]:
        return self._fecha_hora_resolucion
    
    def get_accion_tomada(self) -> str:
        return self._accion_tomada
    
    def get_prioridad(self) -> int:
        """Retorna la prioridad de la alerta"""
        return self._tipo_alerta.prioridad
    
    # --- SETTERS ---
    def resolver(self, accion_tomada: str, usuario_id: Optional[int] = None):
        """Marca la alerta como resuelta"""
        if self._resuelta:
            raise ValueError("La alerta ya está resuelta")
        
        self._resuelta = True
        self._fecha_hora_resolucion = datetime.now()
        self._accion_tomada = accion_tomada
        self._usuario_responsable_id = usuario_id
    
    def reabrir(self):
        """Reabre una alerta resuelta"""
        if not self._resuelta:
            raise ValueError("La alerta no está resuelta")
        
        self._resuelta = False
        self._fecha_hora_resolucion = None
        self._accion_tomada = ""
        self._usuario_responsable_id = None
    
    # --- CÁLCULOS ---
    def calcular_tiempo_sin_resolver(self) -> int:
        """Calcula los minutos desde que se generó la alerta"""
        if self._resuelta:
            return 0
        delta = datetime.now() - self._fecha_hora_generacion
        return int(delta.total_seconds() / 60)
    
    def calcular_tiempo_resolucion(self) -> Optional[int]:
        """Calcula los minutos que tomó resolver la alerta"""
        if not self._resuelta or not self._fecha_hora_resolucion:
            return None
        delta = self._fecha_hora_resolucion - self._fecha_hora_generacion
        return int(delta.total_seconds() / 60)
    
    def es_critica(self) -> bool:
        """Verifica si la alerta es de prioridad crítica (4 o 5)"""
        return self._tipo_alerta.prioridad >= 4
    
    def es_antigua(self, horas_limite: int = 24) -> bool:
        """Verifica si la alerta lleva mucho tiempo sin resolver"""
        if self._resuelta:
            return False
        horas = self.calcular_tiempo_sin_resolver() / 60
        return horas > horas_limite
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado = "✅ Resuelta" if self._resuelta else "⏳ Pendiente"
        
        tiempo_info = ""
        if self._resuelta:
            tiempo_resol = self.calcular_tiempo_resolucion()
            if tiempo_resol is not None:
                tiempo_info = f"\n  ⏱️ Tiempo de resolución: {tiempo_resol} min"
                tiempo_info += f"\n  ✓ Acción: {self._accion_tomada}"
        else:
            minutos = self.calcular_tiempo_sin_resolver()
            tiempo_info = f"\n  ⏱️ Sin resolver: {minutos} min"
            if self.es_antigua():
                tiempo_info += " ⚠️ ANTIGUA"
        
        return (f"{self._tipo_alerta} - Alerta #{self._id}\n"
                f"  Ingrediente: {self._ingrediente_nombre}\n"
                f"  {self._mensaje}\n"
                f"  Estado: {estado}\n"
                f"  Prioridad: {self._tipo_alerta.prioridad}/5\n"
                f"  Generada: {self._fecha_hora_generacion.strftime('%d/%m/%Y %H:%M')}"
                f"{tiempo_info}")
    
    def __repr__(self) -> str:
        return (f"AlertaStock(id={self._id}, "
                f"tipo={self._tipo_alerta.descripcion}, "
                f"ingrediente='{self._ingrediente_nombre}', "
                f"resuelta={self._resuelta})")
    
    # --- COMPARACIÓN PARA ORDENAMIENTO ---
    def __lt__(self, other):
        """Permite ordenar alertas por prioridad (mayor prioridad primero)"""
        if not isinstance(other, AlertaStock):
            return NotImplemented
        return self._tipo_alerta.prioridad > other._tipo_alerta.prioridad

# ==============================================================================
# ARCHIVO 19/110: categoria_ingrediente.py
# Directorio: entidades/inventario
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/inventario/categoria_ingrediente.py
# ==============================================================================

from enum import Enum

class CategoriaIngrediente(Enum):
    """Categorías de ingredientes para el inventario"""
    CARNES = "Carnes"
    PESCADOS_MARISCOS = "Pescados y Mariscos"
    VERDURAS = "Verduras"
    FRUTAS = "Frutas"
    LACTEOS = "Lácteos"
    CEREALES_GRANOS = "Cereales y Granos"
    ESPECIAS_CONDIMENTOS = "Especias y Condimentos"
    ACEITES_SALSAS = "Aceites y Salsas"
    BEBIDAS = "Bebidas"
    PANADERIA = "Panadería"
    POSTRES_DULCES = "Postres y Dulces"
    OTROS = "Otros"
    
    def __str__(self):
        return self.value
    
    @classmethod
    def obtener_categorias(cls):
        """Retorna lista de todas las categorías"""
        return [cat.value for cat in cls]

# ==============================================================================
# ARCHIVO 20/110: ingrediente.py
# Directorio: entidades/inventario
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/inventario/ingrediente.py
# ==============================================================================

from datetime import datetime, timedelta
from typing import Optional
from src.entidades.inventario.unidad_medida import UnidadMedida
from src.entidades.inventario.categoria_ingrediente import CategoriaIngrediente
from src.constantes import STOCK_MINIMO_INGREDIENTE, STOCK_CRITICO, DIAS_VENCIMIENTO_ALERTA
from src.patrones.observer.observable import Observable


class Ingrediente(Observable):
    """Representa un ingrediente en el inventario del restaurante"""
    
    _contador_id = 0
    
    def __init__(self, nombre: str, categoria: CategoriaIngrediente, 
                 unidad_medida: UnidadMedida, cantidad_actual: float):
        super().__init__()
        Ingrediente._contador_id += 1
        self._id = Ingrediente._contador_id
        self._nombre = nombre
        self._categoria = categoria
        self._unidad_medida = unidad_medida
        self._cantidad_actual = cantidad_actual
        self._cantidad_minima = STOCK_MINIMO_INGREDIENTE
        self._cantidad_maxima = cantidad_actual * 3  # Por defecto, 3x el stock inicial
        self._precio_unitario = 0.0
        self._proveedor = ""
        self._fecha_ultimo_reabastecimiento: Optional[datetime] = None
        self._fecha_vencimiento: Optional[datetime] = None
        self._ubicacion_almacen = ""
        self._requiere_refrigeracion = False
        self._notas = ""
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_categoria(self) -> CategoriaIngrediente:
        return self._categoria
    
    def get_unidad_medida(self) -> UnidadMedida:
        return self._unidad_medida
    
    def get_cantidad_actual(self) -> float:
        return self._cantidad_actual
    
    def get_cantidad_minima(self) -> float:
        return self._cantidad_minima
    
    def get_cantidad_maxima(self) -> float:
        return self._cantidad_maxima
    
    def get_precio_unitario(self) -> float:
        return self._precio_unitario
    
    def get_proveedor(self) -> str:
        return self._proveedor
    
    def get_fecha_vencimiento(self) -> Optional[datetime]:
        return self._fecha_vencimiento
    
    def get_ubicacion_almacen(self) -> str:
        return self._ubicacion_almacen
    
    def requiere_refrigeracion(self) -> bool:
        return self._requiere_refrigeracion
    
    def get_notas(self) -> str:
        return self._notas
    
    # --- SETTERS ---
    def set_nombre(self, nombre: str):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre
    
    def set_cantidad_minima(self, cantidad: float):
        if cantidad < 0:
            raise ValueError("La cantidad mínima no puede ser negativa")
        self._cantidad_minima = cantidad
    
    def set_cantidad_maxima(self, cantidad: float):
        if cantidad < self._cantidad_minima:
            raise ValueError("La cantidad máxima no puede ser menor a la mínima")
        self._cantidad_maxima = cantidad
    
    def set_precio_unitario(self, precio: float):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio_unitario = precio
    
    def set_proveedor(self, proveedor: str):
        self._proveedor = proveedor
    
    def set_fecha_vencimiento(self, fecha: datetime):
        self._fecha_vencimiento = fecha
    
    def set_ubicacion_almacen(self, ubicacion: str):
        self._ubicacion_almacen = ubicacion
    
    def set_requiere_refrigeracion(self, requiere: bool):
        self._requiere_refrigeracion = requiere
    
    def set_notas(self, notas: str):
        self._notas = notas
    
    # --- GESTIÓN DE STOCK ---
    def agregar_stock(self, cantidad: float):
            """Agrega stock al ingrediente"""
            if cantidad <= 0:
                raise ValueError("La cantidad a agregar debe ser positiva")
            
            self._cantidad_actual += cantidad
            self._fecha_ultimo_reabastecimiento = datetime.now()
            
            self.notificar()
    
    def consumir_stock(self, cantidad: float):
        """Consume stock del ingrediente"""
        if cantidad <= 0:
            raise ValueError("La cantidad a consumir debe ser positiva")
        
        if cantidad > self._cantidad_actual:
            raise ValueError(f"Stock insuficiente. Disponible: {self._cantidad_actual} {self._unidad_medida}")
        
        self._cantidad_actual -= cantidad
        
        self.notificar() #
    
    def esta_agotado(self) -> bool:
        """Verifica si el ingrediente está agotado"""
        return self._cantidad_actual == 0
    
    def necesita_reabastecimiento(self) -> bool:
        """Verifica si el stock está por debajo del mínimo"""
        return self._cantidad_actual <= self._cantidad_minima
    
    def esta_en_stock_critico(self) -> bool:
        """Verifica si el stock está en nivel crítico"""
        return self._cantidad_actual <= STOCK_CRITICO
    
    def calcular_porcentaje_stock(self) -> float:
        """Calcula el porcentaje de stock actual respecto al máximo"""
        if self._cantidad_maxima == 0:
            return 0.0
        return (self._cantidad_actual / self._cantidad_maxima) * 100
    
    def calcular_cantidad_sugerida_reabastecimiento(self) -> float:
        """Calcula la cantidad sugerida para reabastecer hasta el máximo"""
        return max(0, self._cantidad_maxima - self._cantidad_actual)
    
    # --- VENCIMIENTO ---
    def esta_vencido(self) -> bool:
        """Verifica si el ingrediente está vencido"""
        if not self._fecha_vencimiento:
            return False
        return datetime.now() > self._fecha_vencimiento
    
    def esta_por_vencer(self) -> bool:
        """Verifica si el ingrediente está por vencer"""
        if not self._fecha_vencimiento:
            return False
        dias_restantes = (self._fecha_vencimiento - datetime.now()).days
        return 0 < dias_restantes <= DIAS_VENCIMIENTO_ALERTA
    
    def dias_hasta_vencimiento(self) -> Optional[int]:
        """Retorna los días hasta el vencimiento"""
        if not self._fecha_vencimiento:
            return None
        delta = self._fecha_vencimiento - datetime.now()
        return max(0, delta.days)
    
    # --- COSTOS ---
    def calcular_valor_stock(self) -> float:
        """Calcula el valor total del stock actual"""
        return self._cantidad_actual * self._precio_unitario
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        # Estado del stock
        if self.esta_agotado():
            estado_stock = "🔴 AGOTADO"
        elif self.esta_en_stock_critico():
            estado_stock = "🟠 CRÍTICO"
        elif self.necesita_reabastecimiento():
            estado_stock = "🟡 BAJO"
        else:
            estado_stock = "🟢 OK"
        
        # Vencimiento
        vencimiento_str = ""
        if self._fecha_vencimiento:
            if self.esta_vencido():
                vencimiento_str = f"\n  ⚠️ VENCIDO: {self._fecha_vencimiento.strftime('%d/%m/%Y')}"
            elif self.esta_por_vencer():
                dias = self.dias_hasta_vencimiento()
                vencimiento_str = f"\n  ⏰ Vence en {dias} días"
        
        # Refrigeración
        refrig = " ❄️" if self._requiere_refrigeracion else ""
        
        return (f"📦 {self._nombre}{refrig}\n"
                f"  Categoría: {self._categoria.value}\n"
                f"  Stock: {self._cantidad_actual:.2f} {self._unidad_medida} - {estado_stock}\n"
                f"  Mínimo: {self._cantidad_minima} | Máximo: {self._cantidad_maxima}\n"
                f"  Precio unitario: ${self._precio_unitario:.2f}\n"
                f"  Valor total: ${self.calcular_valor_stock():.2f}\n"
                f"  Proveedor: {self._proveedor if self._proveedor else 'N/A'}"
                f"{vencimiento_str}")
    
    def __repr__(self) -> str:
        return (f"Ingrediente(id={self._id}, "
                f"nombre='{self._nombre}', "
                f"stock={self._cantidad_actual}{self._unidad_medida})")

# ==============================================================================
# ARCHIVO 21/110: unidad_medida.py
# Directorio: entidades/inventario
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/inventario/unidad_medida.py
# ==============================================================================

from enum import Enum

class UnidadMedida(Enum):
    """Unidades de medida para ingredientes"""
    KILOGRAMOS = ("kg", "Kilogramos")
    GRAMOS = ("g", "Gramos")
    LITROS = ("L", "Litros")
    MILILITROS = ("mL", "Mililitros")
    UNIDADES = ("u", "Unidades")
    PORCIONES = ("porc", "Porciones")
    PAQUETES = ("paq", "Paquetes")
    
    def __init__(self, abreviatura: str, nombre_completo: str):
        self._abreviatura = abreviatura
        self._nombre_completo = nombre_completo
    
    @property
    def abreviatura(self) -> str:
        return self._abreviatura
    
    @property
    def nombre_completo(self) -> str:
        return self._nombre_completo
    
    def __str__(self):
        return self._abreviatura
    
    @classmethod
    def obtener_por_abreviatura(cls, abrev: str):
        """Busca una unidad por su abreviatura"""
        for unidad in cls:
            if unidad.abreviatura == abrev:
                return unidad
        return None


################################################################################
# DIRECTORIO: entidades/menu
################################################################################

# ==============================================================================
# ARCHIVO 22/110: __init__.py
# Directorio: entidades/menu
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 23/110: bebida.py
# Directorio: entidades/menu
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/bebida.py
# ==============================================================================

from src.entidades.menu.item_menu import ItemMenu
from src.constantes import (
    PRECIO_BASE_BEBIDA, 
    TIEMPO_PREPARACION_BEBIDA,
    VINOS_MENDOCINOS,
    VINOS_SANJUANINOS
)

class Bebida(ItemMenu):
    """Bebidas del menú"""
    
    def __init__(self, nombre: str, descripcion: str, 
                 tipo_bebida: str, tamanio: str = "mediano"):
        super().__init__(
            nombre=nombre,
            descripcion=descripcion,
            precio_base=PRECIO_BASE_BEBIDA,
            tiempo_preparacion=TIEMPO_PREPARACION_BEBIDA
        )
        self._tipo_bebida = tipo_bebida  # "gaseosa", "jugo", "vino", "cerveza", "agua"
        self._tamanio = tamanio  # "chico", "mediano", "grande"
        self._es_alcoholica = False
        self._con_hielo = True
        self._origen_vino = None  # "mendocino" o "sanjuanino"
    
    def calcular_precio_final(self) -> float:
        """Precio base según tamaño, tipo y vinos específicos"""
        
        # Si es un vino mendocino o sanjuanino, usar precio específico
        if self._nombre in VINOS_MENDOCINOS:
            self._origen_vino = "mendocino"
            return VINOS_MENDOCINOS[self._nombre]
        
        if self._nombre in VINOS_SANJUANINOS:
            self._origen_vino = "sanjuanino"
            return VINOS_SANJUANINOS[self._nombre]
        
        # Para otras bebidas, usar lógica estándar
        precio = self._precio_base
        
        # Ajuste por tamaño
        if self._tamanio == "chico":
            precio *= 0.7
        elif self._tamanio == "grande":
            precio *= 1.5
        
        # Recargo por bebidas alcohólicas (cervezas, otros)
        if self._es_alcoholica:
            precio += 4.00
        
        return precio
    
    def get_estacion_cocina(self) -> str:
        """Todas las bebidas van a la barra"""
        return "Bebidas"
    
    def set_alcoholica(self, es_alcoholica: bool):
        self._es_alcoholica = es_alcoholica
    
    def es_alcoholica(self) -> bool:
        return self._es_alcoholica
    
    def set_con_hielo(self, con_hielo: bool):
        self._con_hielo = con_hielo
    
    def get_tamanio(self) -> str:
        return self._tamanio
    
    def get_origen_vino(self) -> str:
        """Retorna 'mendocino', 'sanjuanino' o None"""
        return self._origen_vino
    
    def es_vino_regional(self) -> bool:
        """Verifica si es un vino de la región (Mendoza o San Juan)"""
        return self._origen_vino is not None
    
    def __str__(self) -> str:
        base_str = super().__str__()
        
        # Agregar información de origen si es vino regional
        if self._origen_vino:
            origen_emoji = "🍷"
            origen_texto = f"\n  {origen_emoji} Vino {self._origen_vino.capitalize()}"
            return base_str + origen_texto
        
        return base_str

# ==============================================================================
# ARCHIVO 24/110: categoria_item.py
# Directorio: entidades/menu
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/categoria_item.py
# ==============================================================================

from enum import Enum

class CategoriaItem(Enum):
    ENTRADA = "Entrada"
    PLATO_PRINCIPAL = "Plato Principal"
    POSTRE = "Postre"
    BEBIDA = "Bebida"
    OTRO = "Otro"

    def __str__(self):
        return self.value

# ==============================================================================
# ARCHIVO 25/110: entrada.py
# Directorio: entidades/menu
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/entrada.py
# ==============================================================================

from src.entidades.menu.item_menu import ItemMenu
from src.constantes import PRECIO_BASE_ENTRADA, TIEMPO_PREPARACION_ENTRADA

class Entrada(ItemMenu):
    """Entradas/Aperitivos del menú"""
    
    def __init__(self, nombre: str, descripcion: str, tipo_entrada: str):
        super().__init__(
            nombre=nombre,
            descripcion=descripcion,
            precio_base=PRECIO_BASE_ENTRADA,
            tiempo_preparacion=TIEMPO_PREPARACION_ENTRADA
        )
        self._tipo_entrada = tipo_entrada  # "ensalada", "sopa", "tabla", etc.
    
    def calcular_precio_final(self) -> float:
        """Precio base sin modificaciones"""
        return self._precio_base
    
    def get_estacion_cocina(self) -> str:
        """Todas las entradas se preparan en la estación de cocina general"""
        return "Cocina"
    
    def get_tipo_entrada(self) -> str:
        return self._tipo_entrada

# ==============================================================================
# ARCHIVO 26/110: item_menu.py
# Directorio: entidades/menu
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/item_menu.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import List, Dict

class ItemMenu(ABC):
    """Clase base abstracta para todos los items del menú"""
    
    _contador_id = 0
    
    def __init__(self, nombre: str, descripcion: str, precio_base: float, # en pesos argentinos
                 tiempo_preparacion: int):
        ItemMenu._contador_id += 1
        self._id = ItemMenu._contador_id
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio_base = precio_base
        self._tiempo_preparacion = tiempo_preparacion  # en minutos
        self._ingredientes: Dict[str, float] = {}  # {nombre_ingrediente: cantidad/peso
        self._disponible = True
        self._imagen_url = ""
        self._vegetariano = False
        self._vegano = False
        self._sin_gluten = False
    
    # Getters
    def get_id(self) -> int:
        return self._id
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_descripcion(self) -> str:
        return self._descripcion
    
    def get_precio_base(self) -> float:
        return self._precio_base
    
    def get_tiempo_preparacion(self) -> int:
        return self._tiempo_preparacion
    
    def get_ingredientes(self) -> Dict[str, float]:
        return self._ingredientes.copy()  # Defensive copy
    
    def esta_disponible(self) -> bool:
        return self._disponible
    
    def es_vegetariano(self) -> bool:
        return self._vegetariano
    
    def es_vegano(self) -> bool:
        return self._vegano
    
    def es_sin_gluten(self) -> bool:
        return self._sin_gluten
    
    # Setters
    def set_disponible(self, disponible: bool):
        self._disponible = disponible
    
    def set_precio_base(self, precio: float):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self._precio_base = precio
    
    def agregar_ingrediente(self, nombre_ingrediente: str, cantidad: float):
        """Agrega un ingrediente necesario para este item"""
        self._ingredientes[nombre_ingrediente] = cantidad
    
    def set_vegetariano(self, es_vegetariano: bool):
        self._vegetariano = es_vegetariano
    
    def set_vegano(self, es_vegano: bool):
        self._vegano = es_vegano
        if es_vegano:
            self._vegetariano = True  # Vegano implica vegetariano
    
    def set_sin_gluten(self, sin_gluten: bool):
        self._sin_gluten = sin_gluten
    
    @abstractmethod
    def calcular_precio_final(self) -> float:
        """Cada tipo de item puede tener lógica de precio diferente"""
        pass
    
    @abstractmethod
    def get_estacion_cocina(self) -> str:
        """Define qué estación de cocina prepara este item"""
        pass
    
    def __str__(self) -> str:
        etiquetas = []
        if self._vegetariano:
            etiquetas.append("🌱 Vegetariano")
        if self._vegano:
            etiquetas.append("🥬 Vegano")
        if self._sin_gluten:
            etiquetas.append("🌾 Sin Gluten")
        
        etiquetas_str = " | ".join(etiquetas) if etiquetas else ""
        
        return (f"{self._nombre} - ${self.calcular_precio_final():.2f}\n"
                f"  {self._descripcion}\n"
                f"  {etiquetas_str}\n"
                f"  Tiempo de preparación: {self._tiempo_preparacion} min")

# ==============================================================================
# ARCHIVO 27/110: plato_principal.py
# Directorio: entidades/menu
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/plato_principal.py
# ==============================================================================

# src/entidades/menu/plato_principal.py

from src.entidades.menu.item_menu import ItemMenu
from src.constantes import PRECIO_BASE_PLATO_PRINCIPAL, TIEMPO_PREPARACION_PLATO_PRINCIPAL

class PlatoPrincipal(ItemMenu):
    """Platos principales del menú"""
    
    def __init__(self, nombre: str, descripcion: str, 
                 tipo_proteina: str, guarnicion: str):
        super().__init__(
            nombre=nombre,
            descripcion=descripcion,
            precio_base=PRECIO_BASE_PLATO_PRINCIPAL,
            tiempo_preparacion=TIEMPO_PREPARACION_PLATO_PRINCIPAL
        )
        self._tipo_proteina = tipo_proteina  # "carne", "pollo", "pescado", "vegetariano"
        self._guarnicion = guarnicion  # "papas fritas", "ensalada", "arroz"
        self._punto_coccion = "medio"  # Para carnes
        self._salsa = None

        if self._tipo_proteina == "carne":
            self._punto_coccion = "medio"
    
    def calcular_precio_final(self) -> float:
        """Precio base + extras por tipo de proteína"""
        precio = self._precio_base
        
        # Recargo por tipo de proteína
        if self._tipo_proteina == "pescado":
            precio += 5.00
        elif self._tipo_proteina == "carne":
            precio += 4.00
        elif self._tipo_proteina == "pollo":
            precio += 3.00
        
        # Recargo por salsa premium
        if self._salsa and "premium" in self._salsa.lower():
            precio += 2.00
        
        return precio
    
    def get_estacion_cocina(self) -> str:
        """Define qué estación prepara este plato"""
        if self._tipo_proteina in ["carne", "pollo"]:
            return "Parrilla"
        
        elif self._tipo_proteina == "pescado":
            return "Cocina" # Antes decía "Plancha"
        
        else:
            # Asumimos que "vegetariano" va a Pastas o Cocina
            # Si "vegetariano" es el único 'else', va a Pastas.
            # Si quieres que vaya a Cocina General, cambia esto:
            if self._tipo_proteina == "vegetariano":
                 return "Cocina" # O "Pastas" si prefieres
            return "Pastas"  
    
    def set_punto_coccion(self, punto: str):
        PUNTOS_COCCION_CARNE = ["bleu", "jugoso", "a_punto", "bien_cocido"]
        if self._tipo_proteina != "carne":
            raise ValueError("El punto de cocción solo aplica para carnes")
        if punto not in PUNTOS_COCCION_CARNE:
            raise ValueError(f"Punto debe ser uno de: {PUNTOS_COCCION_CARNE}")
        self._punto_coccion = punto
    
    def get_punto_coccion(self) -> str:
        return self._punto_coccion
    
    def set_salsa(self, salsa: str):
        self._salsa = salsa
    
    def get_tipo_proteina(self) -> str:
        return self._tipo_proteina
    
    def get_guarnicion(self) -> str:
        return self._guarnicion

# ==============================================================================
# ARCHIVO 28/110: postre.py
# Directorio: entidades/menu
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/postre.py
# ==============================================================================

from src.entidades.menu.item_menu import ItemMenu
from src.constantes import PRECIO_BASE_POSTRE, TIEMPO_PREPARACION_POSTRE

class Postre(ItemMenu):
    """Postres del menú"""
    
    def __init__(self, nombre: str, descripcion: str, 
                 tipo_postre: str, temperatura: str):
        super().__init__(
            nombre=nombre,
            descripcion=descripcion,
            precio_base=PRECIO_BASE_POSTRE,
            tiempo_preparacion=TIEMPO_PREPARACION_POSTRE
        )
        self._tipo_postre = tipo_postre  # "torta", "helado", "flan", etc.
        self._temperatura = temperatura  # "frío", "caliente"
        self._contiene_alcohol = False
    
    def calcular_precio_final(self) -> float:
        """Precio base + recargo por alcohol"""
        precio = self._precio_base
        
        if self._contiene_alcohol:
            precio += 3.00
        
        return precio
    
    def get_estacion_cocina(self) -> str:
        """Todos los postres van a la estación de postres"""
        return "Postres"
    
    def set_contiene_alcohol(self, contiene: bool):
        self._contiene_alcohol = contiene
    
    def contiene_alcohol(self) -> bool:
        return self._contiene_alcohol
    
    def get_tipo_postre(self) -> str:
        return self._tipo_postre
    
    def get_temperatura(self) -> str:
        return self._temperatura

# ==============================================================================
# ARCHIVO 29/110: tipo_coccion.py
# Directorio: entidades/menu
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/tipo_coccion.py
# ==============================================================================

from enum import Enum

class TipoCoccion(Enum):
    """Métodos de cocción disponibles en el restaurante"""
    PARRILLA = "Parrilla"
    PLANCHA = "Plancha"
    HORNO = "Horno"
    FRITURA = "Fritura"
    VAPOR = "Vapor"
    HERVIDO = "Hervido"
    CRUDO = "Crudo"  # Para ensaladas, ceviches, etc.
    
    @classmethod
    def valores_validos(cls):
        """Retorna lista de valores válidos"""
        return [e.value for e in cls]
    
    def __str__(self):
        return self.value


################################################################################
# DIRECTORIO: entidades/pedidos
################################################################################

# ==============================================================================
# ARCHIVO 30/110: __init__.py
# Directorio: entidades/pedidos
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/pedidos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/110: estado_pedido.py
# Directorio: entidades/pedidos
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/pedidos/estado_pedido.py
# ==============================================================================

from enum import Enum

class EstadoPedido(Enum):
    """Estados posibles de un pedido"""
    RECIBIDO = "Recibido"
    EN_PREPARACION = "En Preparación"
    LISTO = "Listo"
    SERVIDO = "Servido"
    CANCELADO = "Cancelado"
    
    def __str__(self):
        return self.value

# ==============================================================================
# ARCHIVO 32/110: item_pedido.py
# Directorio: entidades/pedidos
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/pedidos/item_pedido.py
# ==============================================================================

from src.entidades.menu.item_menu import ItemMenu

class ItemPedido:
    """Representa un item individual dentro de un pedido con su cantidad"""
    
    _contador_id = 0
    
    def __init__(self, item_menu: ItemMenu, cantidad: int = 1):
        ItemPedido._contador_id += 1
        self._id = ItemPedido._contador_id
        self._item_menu = item_menu
        self._cantidad = cantidad
        self._observaciones_especiales = ""
        self._precio_unitario_congelado = None  # Para guardar precio al momento del pedido
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_item_menu(self) -> ItemMenu:
        return self._item_menu
    
    def get_cantidad(self) -> int:
        return self._cantidad
    
    def get_observaciones_especiales(self) -> str:
        return self._observaciones_especiales
    
    def get_precio_unitario(self) -> float:
        """Retorna el precio unitario (congelado o actual)"""
        if self._precio_unitario_congelado is not None:
            return self._precio_unitario_congelado
        return self._item_menu.calcular_precio_final()
    
    # --- SETTERS ---
    def set_cantidad(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        self._cantidad = cantidad
    
    def set_observaciones_especiales(self, observaciones: str):
        """Ej: 'sin cebolla', 'bien cocido', 'sin hielo'"""
        self._observaciones_especiales = observaciones
    
    def congelar_precio(self):
        """Congela el precio actual para que no cambie si el menú se actualiza"""
        self._precio_unitario_congelado = self._item_menu.calcular_precio_final()
    
    # --- OPERACIONES ---
    def aumentar_cantidad(self, incremento: int = 1):
        """Aumenta la cantidad del item"""
        if incremento <= 0:
            raise ValueError("El incremento debe ser positivo")
        self._cantidad += incremento
    
    def disminuir_cantidad(self, decremento: int = 1):
        """Disminuye la cantidad del item"""
        if decremento <= 0:
            raise ValueError("El decremento debe ser positivo")
        if self._cantidad - decremento < 1:
            raise ValueError("La cantidad no puede ser menor a 1")
        self._cantidad -= decremento
    
    # --- CÁLCULOS ---
    def calcular_precio_total(self) -> float:
        """Calcula el precio total (precio unitario * cantidad)"""
        return self.get_precio_unitario() * self._cantidad
    
    def calcular_tiempo_preparacion_total(self) -> int:
        """Retorna el tiempo de preparación (no se multiplica por cantidad)"""
        return self._item_menu.get_tiempo_preparacion()
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        obs = f" ({self._observaciones_especiales})" if self._observaciones_especiales else ""
        return (f"{self._cantidad}x {self._item_menu.get_nombre()} - "
                f"${self.calcular_precio_total():.2f}{obs}")
    
    def __repr__(self) -> str:
        return (f"ItemPedido(id={self._id}, "
                f"item={self._item_menu.get_nombre()}, "
                f"cantidad={self._cantidad})")

# ==============================================================================
# ARCHIVO 33/110: pedido.py
# Directorio: entidades/pedidos
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/pedidos/pedido.py
# ==============================================================================

# src/entidades/pedidos/pedido.py

# --- IMPORTACIONES DE PATRONES ---
from src.patrones.state.pedido_state import IPedidoState
from src.patrones.state.pedido_recibidio_state import PedidoRecibidoState
# --- Faltaban estas importaciones para que la clase funcione ---
from src.patrones.state.pedido_listo_state import PedidoListoState
from src.patrones.state.pedido_servido_state import PedidoServidoState
# -------------------------------------------------------------
from src.patrones.decorator.precio_decorator import ICalculablePrecio
from src.entidades.pedidos.item_pedido import ItemPedido
from src.entidades.pedidos.estado_pedido import EstadoPedido
from src.entidades.pedidos.tipo_servicio import TipoServicio
from src.constantes import (
    DESCUENTO_CLIENTE_FRECUENTE,
    DESCUENTO_HAPPY_HOUR,
    RECARGO_DELIVERY,
    RECARGO_SERVICIO_MESA
)
from datetime import datetime
from typing import List, Optional

# La clase ahora implementa la interfaz ICalculablePrecio para el Decorator
class Pedido(ICalculablePrecio):
    """Representa un pedido completo del restaurante"""
    
    _contador_id = 0
    
    def __init__(self, cliente_id: int, mesa_id: Optional[int] = None, 
                 tipo_servicio: TipoServicio = TipoServicio.EN_SALON):
        Pedido._contador_id += 1
        self._id = Pedido._contador_id
        self._cliente_id = cliente_id
        self._mesa_id = mesa_id
        self._tipo_servicio = tipo_servicio
        self._items: List[ItemPedido] = []
        
        # --- CAMBIO A PATRÓN STATE ---
        # El estado ya no es un Enum, es un objeto de estado
        self._estado: IPedidoState = PedidoRecibidoState(self)
        # -----------------------------
        
        self._fecha_hora_pedido = datetime.now()
        self._fecha_hora_listo: Optional[datetime] = None
        self._fecha_hora_servido: Optional[datetime] = None
        self._mozo_id: Optional[int] = None
        self._observaciones = ""
        self._descuento_aplicado = 0.0
        self._recargo_aplicado = 0.0
        self._es_cliente_frecuente = False
        self._es_happy_hour = False
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_cliente_id(self) -> int:
        return self._cliente_id
    
    def get_mesa_id(self) -> Optional[int]:
        return self._mesa_id
        
    def get_tipo_servicio(self) -> TipoServicio:
        return self._tipo_servicio

    # --- MÉTODO AÑADIDO QUE FALTABA ---
    def get_items(self) -> List[ItemPedido]:
        """Retorna una copia de la lista de items del pedido"""
        return self._items.copy()
    # -------------------------------------
    
    def get_estado(self) -> IPedidoState:
        """Retorna el objeto de estado actual"""
        return self._estado

    # --- SETTERS ---

    # Este método es usado INTERNAMENTE por los objetos State
    def set_estado_interno(self, nuevo_estado: IPedidoState):
        """ Setter para que los estados puedan cambiar el estado del pedido """
        self._estado = nuevo_estado
        
        # Lógica de fechas que estaba en el setter anterior
        # (Asegúrate de tener importadas PedidoListoState y PedidoServidoState)
        if isinstance(nuevo_estado, PedidoListoState):
            self._fecha_hora_listo = datetime.now()
        elif isinstance(nuevo_estado, PedidoServidoState):
            self._fecha_hora_servido = datetime.now()

    def set_mozo_id(self, mozo_id: int):
        self._mozo_id = mozo_id
    
    def set_observaciones(self, observaciones: str):
        self._observaciones = observaciones
    
    def set_cliente_frecuente(self, es_frecuente: bool):
        self._es_cliente_frecuente = es_frecuente
    
    def set_happy_hour(self, es_happy_hour: bool):
        self._es_happy_hour = es_happy_hour
    
    # --- GESTIÓN DE ITEMS (Delegada al Estado) ---
    def agregar_item(self, item: ItemPedido):
        """Delega la lógica de agregar item al estado actual"""
        self._estado.agregar_item(item)
    
    def eliminar_item(self, item_id: int) -> bool:
        # La lógica de eliminar también debería ser manejada por el estado
        # (Omitido por brevedad, pero seguiría el mismo patrón que agregar_item)
        pass

    # --- CÁLCULOS (Implementa ICalculablePrecio) ---
    def calcular_subtotal(self) -> float:
        """Calcula el subtotal sin descuentos ni recargos"""
        return sum(item.calcular_precio_total() for item in self._items)
    
    def calcular_descuentos(self) -> float:
        # Esta lógica ahora será manejada por Decorators,
        # pero la dejamos como base.
        subtotal = self.calcular_subtotal()
        descuento_total = 0.0
        
        if self._es_cliente_frecuente:
            descuento_total += subtotal * (DESCUENTO_CLIENTE_FRECUENTE / 100)
        
        if self._es_happy_hour:
             descuento_total += subtotal * (DESCUENTO_HAPPY_HOUR / 100)
             
        return descuento_total

    def calcular_recargos(self) -> float:
        # Esta lógica ahora será manejada por Decorators
        recargo_total = self._recargo_aplicado
        
        if self._tipo_servicio == TipoServicio.DELIVERY:
            recargo_total += RECARGO_DELIVERY
        elif self._tipo_servicio == TipoServicio.EN_SALON:
             subtotal = self.calcular_subtotal()
             recargo_total += subtotal * (RECARGO_SERVICIO_MESA / 100)
             
        return recargo_total
    
    def calcular_total(self) -> float:
        """
        Calcula el total base. 
        Este es el método que será "envuelto" por los Decorators.
        """
        subtotal = self.calcular_subtotal()
        descuentos = self.calcular_descuentos()
        recargos = self.calcular_recargos()
        return subtotal - descuentos + recargos

    
    def aplicar_descuento_personalizado(self, porcentaje: float):
        """Aplica un descuento personalizado adicional"""
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        self._descuento_aplicado = porcentaje
    
    def aplicar_recargo_personalizado(self, monto: float):
        """Aplica un recargo personalizado adicional"""
        if monto < 0:
            raise ValueError("El recargo no puede ser negativo")
        self._recargo_aplicado = monto
    
    # --- TIEMPOS ---
    def calcular_tiempo_espera(self) -> Optional[int]:
        """Calcula el tiempo de espera en minutos desde que se hizo el pedido"""
        if self._fecha_hora_listo:
            delta = self._fecha_hora_listo - self._fecha_hora_pedido
            return int(delta.total_seconds() / 60)
        return None
    
    def calcular_tiempo_estimado_preparacion(self) -> int:
        """Calcula el tiempo estimado total de preparación"""
        if not self._items:
            return 0
        # Retorna el tiempo máximo entre todos los items
        return max(item.get_item_menu().get_tiempo_preparacion() 
                   for item in self._items)
    
    # --- VALIDACIONES ---
    def esta_completo(self) -> bool:
        """Verifica si el pedido tiene al menos un item"""
        return len(self._items) > 0
    
    def puede_cancelarse(self) -> bool:
        """Verifica si el pedido puede ser cancelado"""
        # Compara el tipo de estado (clase)
        return isinstance(self._estado, (PedidoRecibidoState)) # Solo Recibido
    
    def esta_listo(self) -> bool:
        """Verifica si el pedido está listo para servir"""
        return isinstance(self._estado, PedidoListoState)
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        # Usa el __str__ del objeto de estado
        estado_str = str(self._estado) 
        
        items_str = "\n".join([f"  - {item}" for item in self._items])
        
        return (f"\n📋 Pedido #{self._id}\n"
                f"Estado: {estado_str}\n"
                f"Tipo: {self._tipo_servicio.value}\n"
                f"Mesa: {self._mesa_id if self._mesa_id else 'N/A'}\n"
                f"Items:\n{items_str}\n"
                f"Subtotal: ${self.calcular_subtotal():.2f}\n"
                f"Descuentos: -${self.calcular_descuentos():.2f}\n"
                f"Recargos: +${self.calcular_recargos():.2f}\n"
                f"TOTAL: ${self.calcular_total():.2f}\n"
                f"Hora pedido: {self._fecha_hora_pedido.strftime('%H:%M:%S')}")
    
    def __repr__(self) -> str:
        return f"Pedido(id={self._id}, cliente={self._cliente_id}, estado={str(self._estado)})"
    


# ==============================================================================
# ARCHIVO 34/110: tipo_servicio.py
# Directorio: entidades/pedidos
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/pedidos/tipo_servicio.py
# ==============================================================================

from enum import Enum

class TipoServicio(Enum):
    """Tipos de servicio disponibles"""
    EN_SALON = "En Salón"
    TERRAZA = "Terraza"
    VIP = "VIP"
    DELIVERY = "Delivery"
    PARA_LLEVAR = "Para Llevar"
    
    def __str__(self):
        return self.value


################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 35/110: __init__.py
# Directorio: entidades/personal
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/110: cajero.py
# Directorio: entidades/personal
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/cajero.py
# ==============================================================================

from typing import List, Optional
from src.entidades.personal.empleado import Empleado

class Cajero(Empleado):
    """Cajero del restaurante"""
    
    def __init__(self, nombre: str, apellido: str, dni: str, 
                 telefono: str, email: str, salario_base: float):
        super().__init__(nombre, apellido, dni, telefono, email, salario_base)
        self._transacciones_procesadas = 0
        self._monto_total_procesado = 0.0
        self._caja_asignada: Optional[int] = None
    
    def set_caja_asignada(self, numero_caja: int):
        self._caja_asignada = numero_caja
    
    def registrar_transaccion(self, monto: float):
        """Registra una transacción procesada"""
        self._transacciones_procesadas += 1
        self._monto_total_procesado += monto
    
    def calcular_salario_total(self) -> float:
        """Salario base + bono por volumen"""
        bono = 0.0
        if self._transacciones_procesadas > 500:
            bono = self._salario_base * 0.15
        elif self._transacciones_procesadas > 300:
            bono = self._salario_base * 0.1
        return self._salario_base + bono
    
    def obtener_rol(self) -> str:
        return "Cajero"
    
    def __str__(self) -> str:
        base_str = super().__str__()
        caja = f"\n  Caja: #{self._caja_asignada}" if self._caja_asignada else ""
        return (f"{base_str}\n"
                f"  Transacciones: {self._transacciones_procesadas}\n"
                f"  Monto procesado: ${self._monto_total_procesado:.2f}"
                f"{caja}")

# ==============================================================================
# ARCHIVO 37/110: chef.py
# Directorio: entidades/personal
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/chef.py
# ==============================================================================

from typing import List, Optional
from src.entidades.personal.empleado import Empleado
from src.entidades.personal.especialidad_chef import EspecialidadChef

class Chef(Empleado):
    """Chef del restaurante"""
    
    def __init__(self, nombre: str, apellido: str, dni: str, 
                 telefono: str, email: str, salario_base: float,
                 especialidad: EspecialidadChef):
        super().__init__(nombre, apellido, dni, telefono, email, salario_base)
        self._especialidad = especialidad
        self._estacion_asignada: Optional[str] = None
        self._ordenes_preparadas = 0
        self._ordenes_rechazadas = 0
        self._certificaciones: List[str] = []
    
    # --- GETTERS ESPECÍFICOS ---
    def get_especialidad(self) -> EspecialidadChef:
        return self._especialidad
    
    def get_estacion_asignada(self) -> Optional[str]:
        return self._estacion_asignada
    
    def get_ordenes_preparadas(self) -> int:
        return self._ordenes_preparadas
    
    def get_certificaciones(self) -> List[str]:
        return self._certificaciones.copy()
    
    # --- SETTERS ESPECÍFICOS ---
    def set_estacion_asignada(self, estacion: str):
        self._estacion_asignada = estacion
    
    # --- OPERACIONES ---
    def registrar_orden_preparada(self):
        """Incrementa el contador de órdenes preparadas"""
        self._ordenes_preparadas += 1
    
    def registrar_orden_rechazada(self):
        """Incrementa el contador de órdenes rechazadas"""
        self._ordenes_rechazadas += 1
    
    def agregar_certificacion(self, certificacion: str):
        """Agrega una certificación al chef"""
        if certificacion not in self._certificaciones:
            self._certificaciones.append(certificacion)
    
    # --- CÁLCULOS ---
    def calcular_salario_total(self) -> float:
        """Salario base + bono por especialidad + bono por desempeño"""
        bono_especialidad = 0.0
        
        if self._especialidad == EspecialidadChef.CHEF_EJECUTIVO:
            bono_especialidad = self._salario_base * 0.5
        elif self._especialidad == EspecialidadChef.SOUS_CHEF:
            bono_especialidad = self._salario_base * 0.3
        else:
            bono_especialidad = self._salario_base * 0.15
        
        # Bono por desempeño (basado en evaluaciones)
        promedio = self.calcular_promedio_evaluaciones()
        bono_desempeno = 0.0
        if promedio >= 9.0:
            bono_desempeno = self._salario_base * 0.2
        elif promedio >= 8.0:
            bono_desempeno = self._salario_base * 0.1
        
        return self._salario_base + bono_especialidad + bono_desempeno
    
    def calcular_tasa_exito(self) -> float:
        """Calcula el porcentaje de órdenes exitosas"""
        total = self._ordenes_preparadas + self._ordenes_rechazadas
        if total == 0:
            return 100.0
        return (self._ordenes_preparadas / total) * 100
    
    def obtener_rol(self) -> str:
        return f"Chef ({self._especialidad})"
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        estacion = f"\n  Estación: {self._estacion_asignada}" if self._estacion_asignada else ""
        certs = f"\n  Certificaciones: {', '.join(self._certificaciones)}" if self._certificaciones else ""
        
        return (f"{base_str}\n"
                f"  Especialidad: {self._especialidad.value}\n"
                f"  Órdenes preparadas: {self._ordenes_preparadas}\n"
                f"  Tasa de éxito: {self.calcular_tasa_exito():.1f}%"
                f"{estacion}"
                f"{certs}")


# ==============================================================================
# ARCHIVO 38/110: cocinero.py
# Directorio: entidades/personal
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/cocinero.py
# ==============================================================================

from typing import List, Optional
from src.entidades.personal.empleado import Empleado

class Cocinero(Empleado):
    """Cocinero asistente"""
    
    def __init__(self, nombre: str, apellido: str, dni: str, 
                 telefono: str, email: str, salario_base: float):
        super().__init__(nombre, apellido, dni, telefono, email, salario_base)
        self._chef_supervisor_id: Optional[int] = None
        self._estacion_asignada: Optional[str] = None
        self._tareas_completadas = 0
    
    def set_chef_supervisor(self, chef_id: int):
        self._chef_supervisor_id = chef_id
    
    def set_estacion_asignada(self, estacion: str):
        self._estacion_asignada = estacion
    
    def registrar_tarea_completada(self):
        self._tareas_completadas += 1
    
    def calcular_salario_total(self) -> float:
        """Salario base + bono por productividad"""
        bono = 0.0
        if self._tareas_completadas > 100:
            bono = self._salario_base * 0.1
        return self._salario_base + bono
    
    def obtener_rol(self) -> str:
        return "Cocinero"
    
    def __str__(self) -> str:
        base_str = super().__str__()
        estacion = f"\n  Estación: {self._estacion_asignada}" if self._estacion_asignada else ""
        return (f"{base_str}\n"
                f"  Tareas completadas: {self._tareas_completadas}"
                f"{estacion}")


# ==============================================================================
# ARCHIVO 39/110: empleado.py
# Directorio: entidades/personal
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/empleado.py
# ==============================================================================

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from src.entidades.personal.turno import Turno

class Empleado(ABC):
    """Clase base abstracta para todos los empleados"""
    
    _contador_id = 0
    
    def __init__(self, nombre: str, apellido: str, dni: str, 
                 telefono: str, email: str, salario_base: float):
        Empleado._contador_id += 1
        self._id = Empleado._contador_id
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._telefono = telefono
        self._email = email
        self._salario_base = salario_base
        self._fecha_contratacion = datetime.now()
        self._turno_asignado = Turno.COMPLETO
        self._activo = True
        self._dias_trabajados = 0
        self._evaluaciones: List[float] = []  # Calificaciones de desempeño
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_nombre_completo(self) -> str:
        return f"{self._nombre} {self._apellido}"
    
    def get_dni(self) -> str:
        return self._dni
    
    def get_telefono(self) -> str:
        return self._telefono
    
    def get_email(self) -> str:
        return self._email
    
    def get_salario_base(self) -> float:
        return self._salario_base
    
    def get_turno_asignado(self) -> Turno:
        return self._turno_asignado
    
    def esta_activo(self) -> bool:
        return self._activo
    
    def get_dias_trabajados(self) -> int:
        return self._dias_trabajados
    
    # --- SETTERS ---
    def set_turno_asignado(self, turno: Turno):
        self._turno_asignado = turno
    
    def set_activo(self, activo: bool):
        self._activo = activo
    
    def set_salario_base(self, salario: float):
        if salario <= 0:
            raise ValueError("El salario debe ser positivo")
        self._salario_base = salario
    
    # --- MÉTODOS ---
    def registrar_dia_trabajado(self):
        """Registra un día de trabajo"""
        self._dias_trabajados += 1
    
    def agregar_evaluacion(self, calificacion: float):
        """Agrega una evaluación de desempeño (0-10)"""
        if calificacion < 0 or calificacion > 10:
            raise ValueError("La calificación debe estar entre 0 y 10")
        self._evaluaciones.append(calificacion)
    
    def calcular_promedio_evaluaciones(self) -> float:
        """Calcula el promedio de evaluaciones"""
        if not self._evaluaciones:
            return 0.0
        return sum(self._evaluaciones) / len(self._evaluaciones)
    
    def calcular_antiguedad_dias(self) -> int:
        """Calcula la antigüedad en días"""
        delta = datetime.now() - self._fecha_contratacion
        return delta.days
    
    @abstractmethod
    def calcular_salario_total(self) -> float:
        """Calcula el salario total incluyendo bonos"""
        pass
    
    @abstractmethod
    def obtener_rol(self) -> str:
        """Retorna el rol del empleado"""
        pass
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado = "✅ Activo" if self._activo else "❌ Inactivo"
        promedio = self.calcular_promedio_evaluaciones()
        
        return (f"👤 {self.obtener_rol()}: {self.get_nombre_completo()}\n"
                f"  DNI: {self._dni}\n"
                f"  Estado: {estado}\n"
                f"  Turno: {self._turno_asignado}\n"
                f"  Salario: ${self._salario_base:.2f}\n"
                f"  Antigüedad: {self.calcular_antiguedad_dias()} días\n"
                f"  Evaluación promedio: {promedio:.1f}/10")
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self._id}, nombre='{self.get_nombre_completo()}')"


# ==============================================================================
# ARCHIVO 40/110: especialidad_chef.py
# Directorio: entidades/personal
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/especialidad_chef.py
# ==============================================================================

# src/entidades/personal/especialidad_chef.py

from enum import Enum

class EspecialidadChef(Enum):
    """
    Define las especialidades y rangos de los chefs en la cocina.
    """
    
    # Rangos jerárquicos
    CHEF_EJECUTIVO = "Chef Ejecutivo"
    SOUS_CHEF = "Sous Chef"
    
    # Especialidades de estación
    PARRILLA = "Parrilla"
    PASTAS = "Pastas"
    REPOSTERIA = "Repostería"
    GARDE_MANGER = "Garde Manger (Fríos)"
    COCINA_GENERAL = "Cocina General"
    
    def __str__(self):
        """Retorna el valor legible de la especialidad."""
        return self.value

# ==============================================================================
# ARCHIVO 41/110: mozo.py
# Directorio: entidades/personal
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/mozo.py
# ==============================================================================

from typing import List, Optional
from src.entidades.personal.empleado import Empleado

class Mozo(Empleado):
    """Mozo del restaurante"""
    
    def __init__(self, nombre: str, apellido: str, dni: str, 
                 telefono: str, email: str, salario_base: float):
        super().__init__(nombre, apellido, dni, telefono, email, salario_base)
        self._mesas_asignadas: List[int] = []  # IDs de mesas
        self._propinas_acumuladas = 0.0
        self._pedidos_atendidos = 0
        self._zona_asignada: Optional[str] = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_mesas_asignadas(self) -> List[int]:
        return self._mesas_asignadas.copy()
    
    def get_propinas_acumuladas(self) -> float:
        return self._propinas_acumuladas
    
    def get_pedidos_atendidos(self) -> int:
        return self._pedidos_atendidos
    
    def get_zona_asignada(self) -> Optional[str]:
        return self._zona_asignada
    
    # --- SETTERS ESPECÍFICOS ---
    def set_zona_asignada(self, zona: str):
        self._zona_asignada = zona
    
    # --- OPERACIONES ---
    def asignar_mesa(self, mesa_id: int):
        """Asigna una mesa al mozo"""
        if mesa_id not in self._mesas_asignadas:
            self._mesas_asignadas.append(mesa_id)
    
    def desasignar_mesa(self, mesa_id: int):
        """Desasigna una mesa del mozo"""
        if mesa_id in self._mesas_asignadas:
            self._mesas_asignadas.remove(mesa_id)
    
    def registrar_propina(self, monto: float):
        """Registra una propina recibida"""
        if monto < 0:
            raise ValueError("La propina no puede ser negativa")
        self._propinas_acumuladas += monto
    
    def registrar_pedido_atendido(self):
        """Incrementa el contador de pedidos atendidos"""
        self._pedidos_atendidos += 1
    
    # --- CÁLCULOS ---
    def calcular_salario_total(self) -> float:
        """Salario base + 50% de propinas"""
        return self._salario_base + (self._propinas_acumuladas * 0.5)
    
    def calcular_promedio_propina(self) -> float:
        """Calcula el promedio de propina por pedido"""
        if self._pedidos_atendidos == 0:
            return 0.0
        return self._propinas_acumuladas / self._pedidos_atendidos
    
    def obtener_rol(self) -> str:
        return "Mozo"
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        zona = f"\n  Zona: {self._zona_asignada}" if self._zona_asignada else ""
        return (f"{base_str}\n"
                f"  Mesas asignadas: {len(self._mesas_asignadas)}\n"
                f"  Pedidos atendidos: {self._pedidos_atendidos}\n"
                f"  Propinas: ${self._propinas_acumuladas:.2f} (Promedio: ${self.calcular_promedio_propina():.2f})"
                f"{zona}")



# ==============================================================================
# ARCHIVO 42/110: turno.py
# Directorio: entidades/personal
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/turno.py
# ==============================================================================

from typing import List, Optional
from enum import Enum
from datetime import time


class Turno(Enum):
    """Turnos de trabajo"""
    MAÑANA = ("Mañana", time(6, 0), time(14, 0))
    TARDE = ("Tarde", time(14, 0), time(22, 0))
    NOCHE = ("Noche", time(22, 0), time(6, 0))
    COMPLETO = ("Completo", time(9, 0), time(21, 0))
    
    def __init__(self, nombre: str, hora_inicio: time, hora_fin: time):
        self._nombre_turno = nombre
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin
    
    @property
    def nombre_turno(self) -> str:
        return self._nombre_turno
    
    @property
    def hora_inicio(self) -> time:
        return self._hora_inicio
    
    @property
    def hora_fin(self) -> time:
        return self._hora_fin
    
    def __str__(self):
        return f"{self._nombre_turno} ({self._hora_inicio.strftime('%H:%M')} - {self._hora_fin.strftime('%H:%M')})"


################################################################################
# DIRECTORIO: entidades/salon
################################################################################

# ==============================================================================
# ARCHIVO 43/110: __init__.py
# Directorio: entidades/salon
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/salon/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 44/110: estado_mesa.py
# Directorio: entidades/salon
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/salon/estado_mesa.py
# ==============================================================================

from enum import Enum

class EstadoMesa(Enum):
    """Estados posibles de una mesa"""
    DISPONIBLE = "Disponible"
    OCUPADA = "Ocupada"
    RESERVADA = "Reservada"
    EN_LIMPIEZA = "En Limpieza"
    FUERA_DE_SERVICIO = "Fuera de Servicio"
    
    def __str__(self):
        return self.value

# ==============================================================================
# ARCHIVO 45/110: estado_reserva.py
# Directorio: entidades/salon
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/salon/estado_reserva.py
# ==============================================================================

from enum import Enum

class EstadoReserva(Enum):
    """Estados posibles de una reserva"""
    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    EN_CURSO = "En Curso"
    COMPLETADA = "Completada"
    CANCELADA = "Cancelada"
    NO_SHOW = "No Show"
    
    def __str__(self):
        return self.value

# ==============================================================================
# ARCHIVO 46/110: mesa.py
# Directorio: entidades/salon
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/salon/mesa.py
# ==============================================================================

from datetime import datetime
from typing import Optional
from src.entidades.salon.estado_mesa import EstadoMesa
from src.entidades.salon.zona_salon import ZonaSalon

class Mesa:
    """Representa una mesa del restaurante"""
    
    _contador_id = 0
    
    def __init__(self, numero: int, capacidad: int, zona: ZonaSalon):
        Mesa._contador_id += 1
        self._id = Mesa._contador_id
        self._numero = numero
        self._capacidad = capacidad
        self._zona = zona
        self._estado = EstadoMesa.DISPONIBLE
        self._comensales_actuales = 0
        self._mozo_asignado_id: Optional[int] = None
        self._pedido_actual_id: Optional[int] = None
        self._reserva_actual_id: Optional[int] = None
        self._fecha_hora_ocupacion: Optional[datetime] = None
        self._observaciones = ""
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_numero(self) -> int:
        return self._numero
    
    def get_capacidad(self) -> int:
        return self._capacidad
    
    def get_zona(self) -> ZonaSalon:
        return self._zona
    
    def get_estado(self) -> EstadoMesa:
        return self._estado
    
    def get_comensales_actuales(self) -> int:
        return self._comensales_actuales
    
    def get_mozo_asignado_id(self) -> Optional[int]:
        return self._mozo_asignado_id
    
    def get_pedido_actual_id(self) -> Optional[int]:
        return self._pedido_actual_id
    
    def get_reserva_actual_id(self) -> Optional[int]:
        return self._reserva_actual_id
    
    def get_observaciones(self) -> str:
        return self._observaciones
    
    # --- SETTERS ---
    def set_estado(self, estado: EstadoMesa):
        self._estado = estado
    
    def set_mozo_asignado(self, mozo_id: int):
        self._mozo_asignado_id = mozo_id
    
    def set_observaciones(self, observaciones: str):
        self._observaciones = observaciones
    
    # --- OPERACIONES ---
    def ocupar(self, cantidad_comensales: int, pedido_id: Optional[int] = None):
        """Marca la mesa como ocupada"""
        if self._estado != EstadoMesa.DISPONIBLE:
            raise ValueError(f"La mesa no está disponible (Estado: {self._estado})")
        
        if cantidad_comensales > self._capacidad:
            raise ValueError(f"Cantidad de comensales ({cantidad_comensales}) excede capacidad ({self._capacidad})")
        
        self._estado = EstadoMesa.OCUPADA
        self._comensales_actuales = cantidad_comensales
        self._pedido_actual_id = pedido_id
        self._fecha_hora_ocupacion = datetime.now()
    
    def liberar(self):
        """Libera la mesa"""
        if self._estado != EstadoMesa.OCUPADA:
            raise ValueError("La mesa no está ocupada")
        
        self._estado = EstadoMesa.EN_LIMPIEZA
        self._comensales_actuales = 0
        self._pedido_actual_id = None
        self._fecha_hora_ocupacion = None
    
    def marcar_disponible(self):
        """Marca la mesa como disponible después de limpieza"""
        self._estado = EstadoMesa.DISPONIBLE
        self._reserva_actual_id = None
    
    def reservar(self, reserva_id: int):
        """Marca la mesa como reservada"""
        if self._estado != EstadoMesa.DISPONIBLE:
            raise ValueError("La mesa no está disponible para reservar")
        
        self._estado = EstadoMesa.RESERVADA
        self._reserva_actual_id = reserva_id
    
    def cancelar_reserva(self):
        """Cancela la reserva de la mesa"""
        if self._estado != EstadoMesa.RESERVADA:
            raise ValueError("La mesa no está reservada")
        
        self._estado = EstadoMesa.DISPONIBLE
        self._reserva_actual_id = None
    
    def marcar_fuera_de_servicio(self, motivo: str):
        """Marca la mesa como fuera de servicio"""
        self._estado = EstadoMesa.FUERA_DE_SERVICIO
        self.set_observaciones(motivo)
    
    def poner_en_servicio(self):
        """Vuelve a poner la mesa en servicio"""
        self._estado = EstadoMesa.DISPONIBLE
        self._observaciones = ""
    
    # --- CÁLCULOS ---
    def calcular_tiempo_ocupacion(self) -> Optional[int]:
        """Retorna el tiempo de ocupación en minutos"""
        if not self._fecha_hora_ocupacion:
            return None
        delta = datetime.now() - self._fecha_hora_ocupacion
        return int(delta.total_seconds() / 60)
    
    def calcular_porcentaje_ocupacion(self) -> float:
        """Retorna el porcentaje de ocupación actual"""
        if self._comensales_actuales == 0:
            return 0.0
        return (self._comensales_actuales / self._capacidad) * 100
    
    # --- VALIDACIONES ---
    def esta_disponible(self) -> bool:
        return self._estado == EstadoMesa.DISPONIBLE
    
    def esta_ocupada(self) -> bool:
        return self._estado == EstadoMesa.OCUPADA
    
    def esta_reservada(self) -> bool:
        return self._estado == EstadoMesa.RESERVADA
    
    def puede_aceptar_comensales(self, cantidad: int) -> bool:
        """Verifica si la mesa puede aceptar X comensales"""
        return self.esta_disponible() and cantidad <= self._capacidad
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado_emoji = {
            EstadoMesa.DISPONIBLE: "🟢",
            EstadoMesa.OCUPADA: "🔴",
            EstadoMesa.RESERVADA: "🟡",
            EstadoMesa.EN_LIMPIEZA: "🧹",
            EstadoMesa.FUERA_DE_SERVICIO: "⚠️"
        }
        
        zona_emoji = {
            ZonaSalon.INTERIOR: "🏠",
            ZonaSalon.TERRAZA: "🌳",
            ZonaSalon.VIP: "👑",
            ZonaSalon.BARRA: "🍺"
        }
        
        ocupacion = ""
        if self._estado == EstadoMesa.OCUPADA:
            tiempo = self.calcular_tiempo_ocupacion()
            ocupacion = f"\n  👥 Comensales: {self._comensales_actuales}/{self._capacidad}\n  ⏱️ Tiempo: {tiempo} min"
        
        obs = f"\n  📝 {self._observaciones}" if self._observaciones else ""
        
        return (f"{estado_emoji.get(self._estado, '❓')} Mesa #{self._numero}\n"
                f"  {zona_emoji.get(self._zona, '')} Zona: {self._zona.value}\n"
                f"  Estado: {self._estado.value}\n"
                f"  Capacidad: {self._capacidad} personas"
                f"{ocupacion}"
                f"{obs}")
    
    def __repr__(self) -> str:
        return f"Mesa(numero={self._numero}, zona={self._zona}, estado={self._estado})"

# ==============================================================================
# ARCHIVO 47/110: reserva.py
# Directorio: entidades/salon
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/salon/reserva.py
# ==============================================================================

from typing import Optional
from datetime import datetime, timedelta
from src.entidades.salon.estado_reserva import EstadoReserva    

class Reserva:
    """Representa una reserva de mesa"""
    
    _contador_id = 0
    
    def __init__(self, cliente_id: int, fecha_hora: datetime, 
                 cantidad_personas: int, nombre_contacto: str, telefono_contacto: str):
        Reserva._contador_id += 1
        self._id = Reserva._contador_id
        self._cliente_id = cliente_id
        self._fecha_hora = fecha_hora
        self._cantidad_personas = cantidad_personas
        self._nombre_contacto = nombre_contacto
        self._telefono_contacto = telefono_contacto
        self._estado = EstadoReserva.PENDIENTE
        self._mesa_asignada_id: Optional[int] = None
        self._fecha_hora_creacion = datetime.now()
        self._fecha_hora_confirmacion: Optional[datetime] = None
        self._fecha_hora_llegada: Optional[datetime] = None
        self._observaciones = ""
        self._ocasion_especial = ""  # cumpleaños, aniversario, etc.
        self._tiempo_tolerancia = 15  # minutos
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_cliente_id(self) -> int:
        return self._cliente_id
    
    def get_fecha_hora(self) -> datetime:
        return self._fecha_hora
    
    def get_cantidad_personas(self) -> int:
        return self._cantidad_personas
    
    def get_nombre_contacto(self) -> str:
        return self._nombre_contacto
    
    def get_telefono_contacto(self) -> str:
        return self._telefono_contacto
    
    def get_estado(self) -> EstadoReserva:
        return self._estado
    
    def get_mesa_asignada_id(self) -> Optional[int]:
        return self._mesa_asignada_id
    
    def get_observaciones(self) -> str:
        return self._observaciones
    
    def get_ocasion_especial(self) -> str:
        return self._ocasion_especial
    
    # --- SETTERS ---
    def set_observaciones(self, observaciones: str):
        self._observaciones = observaciones
    
    def set_ocasion_especial(self, ocasion: str):
        """Ej: 'Cumpleaños', 'Aniversario', 'Cita romántica'"""
        self._ocasion_especial = ocasion
    
    def set_mesa_asignada(self, mesa_id: int):
        self._mesa_asignada_id = mesa_id
    
    def set_fecha_hora(self, nueva_fecha_hora: datetime):
        """Modifica la fecha/hora de la reserva"""
        if self._estado not in [EstadoReserva.PENDIENTE, EstadoReserva.CONFIRMADA]:
            raise ValueError("No se puede modificar una reserva en este estado")
        self._fecha_hora = nueva_fecha_hora
    
    def set_cantidad_personas(self, cantidad: int):
        """Modifica la cantidad de personas"""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        if self._estado not in [EstadoReserva.PENDIENTE, EstadoReserva.CONFIRMADA]:
            raise ValueError("No se puede modificar una reserva en este estado")
        self._cantidad_personas = cantidad
    
    # --- GESTIÓN DE ESTADO ---
    def confirmar(self):
        """Confirma la reserva"""
        if self._estado != EstadoReserva.PENDIENTE:
            raise ValueError("Solo se pueden confirmar reservas pendientes")
        self._estado = EstadoReserva.CONFIRMADA
        self._fecha_hora_confirmacion = datetime.now()
    
    def registrar_llegada(self):
        """Registra la llegada del cliente"""
        if self._estado != EstadoReserva.CONFIRMADA:
            raise ValueError("La reserva debe estar confirmada")
        self._estado = EstadoReserva.EN_CURSO
        self._fecha_hora_llegada = datetime.now()
    
    def completar(self):
        """Marca la reserva como completada"""
        if self._estado != EstadoReserva.EN_CURSO:
            raise ValueError("La reserva debe estar en curso")
        self._estado = EstadoReserva.COMPLETADA
    
    def cancelar(self, motivo: str = ""):
        """Cancela la reserva"""
        if self._estado in [EstadoReserva.COMPLETADA, EstadoReserva.NO_SHOW]:
            raise ValueError("No se puede cancelar una reserva completada o no show")
        self._estado = EstadoReserva.CANCELADA
        if motivo:
            self.set_observaciones(f"Cancelada: {motivo}")
    
    def marcar_no_show(self):
        """Marca como no presentado"""
        if self._estado != EstadoReserva.CONFIRMADA:
            raise ValueError("Solo se puede marcar no show reservas confirmadas")
        
        # Verificar que ya pasó la hora + tolerancia
        if not self.esta_vencida():
            raise ValueError("Aún no ha vencido el tiempo de tolerancia")
        
        self._estado = EstadoReserva.NO_SHOW
    
    # --- VALIDACIONES ---
    def esta_vigente(self) -> bool:
        """Verifica si la reserva está vigente (no cancelada, no vencida)"""
        if self._estado in [EstadoReserva.CANCELADA, EstadoReserva.NO_SHOW, EstadoReserva.COMPLETADA]:
            return False
        return not self.esta_vencida()
    
    def esta_vencida(self) -> bool:
        """Verifica si ya pasó la hora de la reserva + tolerancia"""
        hora_limite = self._fecha_hora + timedelta(minutes=self._tiempo_tolerancia)
        return datetime.now() > hora_limite
    
    def puede_cancelarse(self) -> bool:
        """Verifica si la reserva puede cancelarse"""
        return self._estado in [EstadoReserva.PENDIENTE, EstadoReserva.CONFIRMADA]
    
    def esta_proxima(self, minutos: int = 60) -> bool:
        """Verifica si la reserva está próxima (dentro de X minutos)"""
        if self._estado not in [EstadoReserva.CONFIRMADA]:
            return False
        delta = self._fecha_hora - datetime.now()
        return 0 <= delta.total_seconds() / 60 <= minutos
    
    # --- CÁLCULOS ---
    def calcular_tiempo_anticipacion(self) -> int:
        """Calcula con cuántos días de anticipación se hizo la reserva"""
        delta = self._fecha_hora - self._fecha_hora_creacion
        return delta.days
    
    def calcular_tiempo_hasta_reserva(self) -> Optional[int]:
        """Retorna minutos hasta la hora de la reserva (negativo si ya pasó)"""
        if self._estado not in [EstadoReserva.PENDIENTE, EstadoReserva.CONFIRMADA]:
            return None
        delta = self._fecha_hora - datetime.now()
        return int(delta.total_seconds() / 60)
    
    def calcular_retraso_llegada(self) -> Optional[int]:
        """Calcula el retraso en minutos respecto a la hora de reserva"""
        if not self._fecha_hora_llegada:
            return None
        delta = self._fecha_hora_llegada - self._fecha_hora
        return int(delta.total_seconds() / 60)
    
    # --- NOTIFICACIONES ---
    def necesita_recordatorio(self) -> bool:
        """Verifica si necesita enviar recordatorio (24hs antes)"""
        if self._estado != EstadoReserva.CONFIRMADA:
            return False
        
        tiempo_hasta = self.calcular_tiempo_hasta_reserva()
        if tiempo_hasta is None:
            return False
        
        # Recordatorio entre 24hs y 23hs antes
        return 1380 <= tiempo_hasta <= 1440  # minutos
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado_emoji = {
            EstadoReserva.PENDIENTE: "⏳",
            EstadoReserva.CONFIRMADA: "✅",
            EstadoReserva.EN_CURSO: "🍽️",
            EstadoReserva.COMPLETADA: "✔️",
            EstadoReserva.CANCELADA: "❌",
            EstadoReserva.NO_SHOW: "👻"
        }
        
        mesa_str = f"Mesa #{self._mesa_asignada_id}" if self._mesa_asignada_id else "Sin asignar"
        ocasion_str = f"\n  🎉 Ocasión: {self._ocasion_especial}" if self._ocasion_especial else ""
        obs_str = f"\n  📝 {self._observaciones}" if self._observaciones else ""
        
        tiempo_hasta = self.calcular_tiempo_hasta_reserva()
        tiempo_str = ""
        if tiempo_hasta is not None:
            if tiempo_hasta > 0:
                tiempo_str = f"\n  ⏰ Faltan {tiempo_hasta} minutos"
            elif tiempo_hasta < 0:
                tiempo_str = f"\n  ⚠️ Retrasada {abs(tiempo_hasta)} minutos"
        
        return (f"{estado_emoji.get(self._estado, '📅')} Reserva #{self._id}\n"
                f"  Estado: {self._estado.value}\n"
                f"  Contacto: {self._nombre_contacto} - {self._telefono_contacto}\n"
                f"  Fecha: {self._fecha_hora.strftime('%d/%m/%Y %H:%M')}\n"
                f"  Personas: {self._cantidad_personas}\n"
                f"  {mesa_str}"
                f"{ocasion_str}"
                f"{tiempo_str}"
                f"{obs_str}")
    
    def __repr__(self) -> str:
        return (f"Reserva(id={self._id}, "
                f"cliente={self._cliente_id}, "
                f"fecha={self._fecha_hora.strftime('%d/%m/%Y')}, "
                f"estado={self._estado})")

# ==============================================================================
# ARCHIVO 48/110: zona_salon.py
# Directorio: entidades/salon
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/salon/zona_salon.py
# ==============================================================================

from enum import Enum

class ZonaSalon(Enum):
    """Zonas del salón"""
    INTERIOR = "Interior"
    TERRAZA = "Terraza"
    VIP = "VIP"
    BARRA = "Barra"
    
    def __str__(self):
        return self.value



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 49/110: __init__.py
# Directorio: excepciones
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 50/110: ingrediente_agotado_exception.py
# Directorio: excepciones
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones/ingrediente_agotado_exception.py
# ==============================================================================

from src.excepciones.restaurante_exception import RestauranteException

# ============= EXCEPCIONES DE INGREDIENTES =============

class IngredienteAgotadoException(RestauranteException):
    """Se lanza cuando un ingrediente está agotado"""
    
    def __init__(self, nombre_ingrediente: str, cantidad_requerida: float = 0):
        mensaje = f"El ingrediente '{nombre_ingrediente}' está agotado"
        if cantidad_requerida > 0:
            mensaje += f" (se requieren {cantidad_requerida} unidades)"
        super().__init__(mensaje, "ERR_INGREDIENTE_AGOTADO")
        self.nombre_ingrediente = nombre_ingrediente
        self.cantidad_requerida = cantidad_requerida


class IngredienteVencidoException(RestauranteException):
    """Se lanza cuando se intenta usar un ingrediente vencido"""
    
    def __init__(self, nombre_ingrediente: str, fecha_vencimiento):
        mensaje = f"El ingrediente '{nombre_ingrediente}' está vencido (venció el {fecha_vencimiento})"
        super().__init__(mensaje, "ERR_INGREDIENTE_VENCIDO")
        self.nombre_ingrediente = nombre_ingrediente
        self.fecha_vencimiento = fecha_vencimiento


class StockInsuficienteException(RestauranteException):
    """Se lanza cuando no hay suficiente stock de un ingrediente"""
    
    def __init__(self, nombre_ingrediente: str, cantidad_disponible: float, cantidad_requerida: float):
        mensaje = (f"Stock insuficiente de '{nombre_ingrediente}'. "
                   f"Disponible: {cantidad_disponible}, Requerido: {cantidad_requerida}")
        super().__init__(mensaje, "ERR_STOCK_INSUFICIENTE")
        self.nombre_ingrediente = nombre_ingrediente
        self.cantidad_disponible = cantidad_disponible
        self.cantidad_requerida = cantidad_requerida



# ==============================================================================
# ARCHIVO 51/110: mesa_ocupada_exception.py
# Directorio: excepciones
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones/mesa_ocupada_exception.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 52/110: pedido_invalido_exception.py
# Directorio: excepciones
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones/pedido_invalido_exception.py
# ==============================================================================

from src.excepciones.restaurante_exception import RestauranteException

# ============= EXCEPCIONES DE PEDIDOS =============

class PedidoInvalidoException(RestauranteException):
    """Se lanza cuando un pedido es inválido"""
    
    def __init__(self, pedido_id: int, razon: str):
        mensaje = f"El pedido #{pedido_id} es inválido: {razon}"
        super().__init__(mensaje, "ERR_PEDIDO_INVALIDO")
        self.pedido_id = pedido_id
        self.razon = razon


class PedidoVacioException(RestauranteException):
    """Se lanza cuando se intenta procesar un pedido sin items"""
    
    def __init__(self, pedido_id: int):
        mensaje = f"El pedido #{pedido_id} no tiene items"
        super().__init__(mensaje, "ERR_PEDIDO_VACIO")
        self.pedido_id = pedido_id


class EstadoPedidoInvalidoException(RestauranteException):
    """Se lanza cuando se intenta realizar una operación con un estado inválido"""
    
    def __init__(self, pedido_id: int, estado_actual: str, estado_requerido: str):
        mensaje = (f"El pedido #{pedido_id} está en estado '{estado_actual}', "
                   f"se requiere estado '{estado_requerido}'")
        super().__init__(mensaje, "ERR_ESTADO_PEDIDO_INVALIDO")
        self.pedido_id = pedido_id
        self.estado_actual = estado_actual
        self.estado_requerido = estado_requerido


class ItemNoDisponibleException(RestauranteException):
    """Se lanza cuando un item del menú no está disponible"""
    
    def __init__(self, nombre_item: str):
        mensaje = f"El item '{nombre_item}' no está disponible en este momento"
        super().__init__(mensaje, "ERR_ITEM_NO_DISPONIBLE")
        self.nombre_item = nombre_item


# ==============================================================================
# ARCHIVO 53/110: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones/persistencia_exception.py
# ==============================================================================

from src.excepciones.restaurante_exception import RestauranteException

# ============= EXCEPCIONES DE PERSISTENCIA =============

class PersistenciaException(RestauranteException):
    """Se lanza cuando hay un error en la persistencia de datos"""
    
    def __init__(self, operacion: str, detalle: str):
        mensaje = f"Error en operación de persistencia '{operacion}': {detalle}"
        super().__init__(mensaje, "ERR_PERSISTENCIA")
        self.operacion = operacion
        self.detalle = detalle


class ArchivoNoEncontradoException(PersistenciaException):
    """Se lanza cuando no se encuentra un archivo"""
    
    def __init__(self, ruta_archivo: str):
        super().__init__("lectura", f"No se encontró el archivo: {ruta_archivo}")
        self.ruta_archivo = ruta_archivo


class ErrorSerializacionException(PersistenciaException):
    """Se lanza cuando hay un error al serializar/deserializar datos"""
    
    def __init__(self, tipo_dato: str, detalle: str):
        super().__init__("serialización", f"Error al serializar '{tipo_dato}': {detalle}")
        self.tipo_dato = tipo_dato


# ==============================================================================
# ARCHIVO 54/110: restaurante_exception.py
# Directorio: excepciones
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones/restaurante_exception.py
# ==============================================================================


# ============= EXCEPCIONES BASE =============

class RestauranteException(Exception):
    """Excepción base para todas las excepciones del restaurante"""
    
    def __init__(self, mensaje: str, codigo_error: str = "ERR_GENERAL"):
        self.mensaje = mensaje
        self.codigo_error = codigo_error
        super().__init__(self.mensaje)
    
    def __str__(self):
        return f"[{self.codigo_error}] {self.mensaje}"



################################################################################
# DIRECTORIO: monitoreo
################################################################################

# ==============================================================================
# ARCHIVO 55/110: __init__.py
# Directorio: monitoreo
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: monitoreo/control
################################################################################

# ==============================================================================
# ARCHIVO 56/110: __init__.py
# Directorio: monitoreo/control
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/control/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 57/110: monitor_base_task.py
# Directorio: monitoreo/control
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/control/monitor_base_task.py
# ==============================================================================

import threading
from abc import ABC, abstractmethod
import time
from src.constantes import THREAD_JOIN_TIMEOUT

class MonitorBase(threading.Thread, ABC):
    """
    Clase base abstracta para un monitor que corre en un hilo.
    """
    def __init__(self, intervalo_segundos: float):
        super().__init__(daemon=True)  # Daemons mueren si el hilo principal muere
        self._intervalo = intervalo_segundos
        self._stop_event = threading.Event()

    @abstractmethod
    def verificar_estado(self):
        """
        Método abstracto que cada monitor implementará
        para chequear lo que necesite.
        """
        pass

    def run(self):
        """
        Método principal del hilo. Corre en bucle hasta que
        se llama a stop().
        """
        print(f"▶️ Iniciando monitor: {self.__class__.__name__}")
        while not self._stop_event.is_set():
            try:
                self.verificar_estado()
            except Exception as e:
                print(f"Error en monitor {self.__class__.__name__}: {e}")
            
            # Esperar el intervalo (o hasta que el evento de stop se active)
            self._stop_event.wait(self._intervalo)
        
        print(f"⏹️ Deteniendo monitor: {self.__class__.__name__}")

    def stop(self):
        """Señala al hilo que debe detenerse"""
        self._stop_event.set()
    
    def join_safe(self):
        """Intenta unirse al hilo de forma segura"""
        self.stop()
        super().join(THREAD_JOIN_TIMEOUT) #

# ==============================================================================
# ARCHIVO 58/110: monitor_cocina_task.py
# Directorio: monitoreo/control
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/control/monitor_cocina_task.py
# ==============================================================================

from typing import List
from src.monitoreo.control.monitor_base_task import MonitorBase #
from src.entidades.cocina.estacion_cocina import EstacionCocina #
from src.entidades.cocina.estacion_parrilla import EstacionParrilla #
from src.entidades.cocina.estacion_bebidas import EstacionBebidas #
from src.entidades.cocina.estacion_pastas import EstacionPastas #

class MonitorCocina(MonitorBase):
    
    def __init__(self, estaciones: List[EstacionCocina], intervalo_segundos: float):
        super().__init__(intervalo_segundos)
        self._estaciones = estaciones

    def verificar_estado(self):
        """
        Verifica el estado de todas las estaciones de cocina.
        """
        # print("Monitoreando cocina...") # Descomentar para debug
        for est in self._estaciones:
            
            if not est.verificar_equipamiento(): #
                print(f"ALERTA EQUIPAMIENTO: {est.get_nombre_estacion()} no operativo")

            if est.esta_saturada(): #
                print(f"ALERTA SATURACIÓN: {est.get_nombre_estacion()} está saturada")
            
            retrasadas = est.obtener_ordenes_retrasadas() #
            if retrasadas:
                print(f"ALERTA RETRASOS: {est.get_nombre_estacion()} tiene {len(retrasadas)} órdenes retrasadas")

            # Chequeos específicos por tipo de estación
            if isinstance(est, EstacionParrilla):
                if est.necesita_carbon(): #
                    print(f"ALERTA RECURSOS: {est.get_nombre_estacion()} necesita carbón")
            
            elif isinstance(est, EstacionBebidas):
                if est.necesita_hielo(): #
                    print(f"ALERTA RECURSOS: {est.get_nombre_estacion()} necesita hielo")
                if est.necesita_cristaleria(): #
                    print(f"ALERTA RECURSOS: {est.get_nombre_estacion()} necesita cristalería")
            
            elif isinstance(est, EstacionPastas):
                if est.necesita_pasta(): #
                    print(f"ALERTA RECURSOS: {est.get_nombre_estacion()} necesita pasta")

# ==============================================================================
# ARCHIVO 59/110: monitor_inventario_task.py
# Directorio: monitoreo/control
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/control/monitor_inventario_task.py
# ==============================================================================

from typing import List
from src.monitoreo.control.monitor_base_task import MonitorBase
from src.entidades.inventario.ingrediente import Ingrediente
from src.entidades.inventario.alerta_stock import AlertaStock, TipoAlerta
# Asumimos que tienes un gestor que maneja las alertas
# from src.gestores.gestor_alertas import GestorDeAlertas 

class MonitorInventario(MonitorBase):
    
    def __init__(self, ingredientes: List[Ingrediente], intervalo_segundos: float):
        super().__init__(intervalo_segundos)
        self._ingredientes = ingredientes
        # self._gestor_alertas = GestorDeAlertas() # O se recibe por parámetro

    def verificar_estado(self):
        """
        Verifica el estado de todos los ingredientes y genera alertas.
        """
        # print("Monitoreando inventario...") # Descomentar para debug
        for ing in self._ingredientes:
            
            if ing.esta_vencido(): #
                # Lógica para generar una alerta de vencimiento
                # self._gestor_alertas.crear_alerta(ing, TipoAlerta.VENCIDO, ...)
                print(f"ALERTA VENCIDO: {ing.get_nombre()}")
                
            elif ing.esta_por_vencer(): #
                # Lógica para alerta "por vencer"
                print(f"ALERTA POR VENCER: {ing.get_nombre()}")

            if ing.esta_agotado(): #
                print(f"ALERTA AGOTADO: {ing.get_nombre()}")
            
            elif ing.esta_en_stock_critico(): #
                print(f"ALERTA STOCK CRITICO: {ing.get_nombre()}")

            elif ing.necesita_reabastecimiento(): #
                print(f"ALERTA STOCK BAJO: {ing.get_nombre()}")


################################################################################
# DIRECTORIO: monitoreo/sensores
################################################################################

# ==============================================================================
# ARCHIVO 60/110: __init__.py
# Directorio: monitoreo/sensores
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/sensores/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 61/110: sensor_base_task.py
# Directorio: monitoreo/sensores
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/sensores/sensor_base_task.py
# ==============================================================================

import threading
from abc import ABC, abstractmethod
from src.constantes import THREAD_JOIN_TIMEOUT

class SensorBase(threading.Thread, ABC):
    """
    Clase base abstracta para un sensor que corre en un hilo.
    """
    def __init__(self, intervalo_segundos: float):
        super().__init__(daemon=True)
        self._intervalo = intervalo_segundos
        self._stop_event = threading.Event()

    @abstractmethod
    def tomar_lectura(self):
        """
        Método abstracto que cada sensor implementará
        para tomar una lectura o simular un dato.
        """
        pass

    def run(self):
        """
        Método principal del hilo. Corre en bucle hasta que
        se llama a stop().
        """
        print(f"▶️ Iniciando sensor: {self.__class__.__name__}")
        while not self._stop_event.is_set():
            try:
                self.tomar_lectura()
            except Exception as e:
                print(f"Error en sensor {self.__class__.__name__}: {e}")
            
            self._stop_event.wait(self._intervalo)
        
        print(f"⏹️ Deteniendo sensor: {self.__class__.__name__}")

    def stop(self):
        """Señala al hilo que debe detenerse"""
        self._stop_event.set()
    
    def join_safe(self):
        """Intenta unirse al hilo de forma segura"""
        self.stop()
        super().join(THREAD_JOIN_TIMEOUT) #

# ==============================================================================
# ARCHIVO 62/110: sensor_stock_task.py
# Directorio: monitoreo/sensores
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/sensores/sensor_stock_task.py
# ==============================================================================

from src.patrones.observer import IObserver
from src.patrones.observer import IObservable
from src.entidades.inventario.ingrediente import Ingrediente
from src.entidades.inventario.alerta_stock import AlertaStock, TipoAlerta

class SensorStockObserver(IObserver):
    """
    Implementación del Patrón Observer. Escucha a los
    ingredientes (Observables).
    """
    def __init__(self):
        # self._gestor_alertas = GestorDeAlertas() # Idealmente
        pass

    def actualizar(self, observable: IObservable):
        if not isinstance(observable, Ingrediente):
            return

        # El 'observable' es el ingrediente que cambió
        ing = observable
        
        # print(f"DEBUG: SensorStockObserver notificado por {ing.get_nombre()}") # Debug
        
        if ing.esta_agotado():
            self.generar_alerta(ing, TipoAlerta.AGOTADO, "Stock en cero")
        elif ing.esta_en_stock_critico():
            msg = f"Stock crítico: {ing.get_cantidad_actual()} {ing.get_unidad_medida()}"
            self.generar_alerta(ing, TipoAlerta.STOCK_CRITICO, msg)
        elif ing.necesita_reabastecimiento():
            msg = f"Stock bajo: {ing.get_cantidad_actual()} {ing.get_unidad_medida()}"
            self.generar_alerta(ing, TipoAlerta.STOCK_BAJO, msg)
    
    def generar_alerta(self, ingrediente: Ingrediente, tipo: TipoAlerta, mensaje: str):
        alerta = AlertaStock(
            ingrediente_id=ingrediente.get_id(),
            ingrediente_nombre=ingrediente.get_nombre(),
            tipo_alerta=tipo,
            mensaje=mensaje
        )
        print("\n--- 🚨 ALERTA DE STOCK (OBSERVER) 🚨 ---")
        print(str(alerta))
        print("---------------------------------------\n")

# ==============================================================================
# ARCHIVO 63/110: sensor_temperatura_cocina_task.py
# Directorio: monitoreo/sensores
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/sensores/sensor_temperatura_cocina_task.py
# ==============================================================================

import random
from typing import List
from src.monitoreo.sensores.sensor_base_task import SensorBase #
from src.entidades.cocina.estacion_cocina import EstacionCocina #
from src.constantes import TEMPERATURA_COCINA_MIN, TEMPERATURA_COCINA_MAX #

class SensorTemperatura(SensorBase):
    
    def __init__(self, estaciones: List[EstacionCocina], intervalo_segundos: float):
        super().__init__(intervalo_segundos)
        self._estaciones = estaciones

    def tomar_lectura(self):
        """
        Simula una lectura de temperatura y la actualiza
        en la estación de cocina correspondiente.
        """
        for estacion in self._estaciones:
            if not estacion.esta_activa(): #
                continue
            
            # Simular una fluctuación de temperatura
            temp_actual = estacion.get_temperatura_actual() #
            fluctuacion = random.uniform(-0.5, 0.5)
            
            # (No aplica fluctuación a estaciones especiales como parrilla o postres 
            # que fijan su propia temp, solo a la temp. ambiente de la estación)
            if temp_actual >= TEMPERATURA_COCINA_MIN and temp_actual <= TEMPERATURA_COCINA_MAX: #
                nueva_temp = max(TEMPERATURA_COCINA_MIN, min(TEMPERATURA_COCINA_MAX, temp_actual + fluctuacion))
                estacion.set_temperatura_actual(nueva_temp) #

# ==============================================================================
# ARCHIVO 64/110: sensor_tiempo_de_espera_task.py
# Directorio: monitoreo/sensores
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/sensores/sensor_tiempo_de_espera_task.py
# ==============================================================================

from typing import List
from src.monitoreo.sensores.sensor_base_task import SensorBase #
from src.entidades.cocina.estacion_cocina import EstacionCocina #

class SensorTiempoEspera(SensorBase):
    
    def __init__(self, estaciones: List[EstacionCocina], intervalo_segundos: float):
        super().__init__(intervalo_segundos)
        self._estaciones = estaciones
        # self._gestor_alertas = GestorDeAlertas() # O se recibe por parámetro

    def tomar_lectura(self):
        """
        Verifica todas las órdenes en preparación y busca retrasos.
        """
        # print("Sensor de tiempo verificando...") # Descomentar para debug
        
        for estacion in self._estaciones:
            if not estacion.esta_activa(): #
                continue
                
            ordenes_retrasadas = estacion.obtener_ordenes_retrasadas() #
            
            for orden in ordenes_retrasadas:
                # Generar una alerta para esta orden
                # (Aquí también usarías tu GestorDeAlertas)
                
                # Simulación con print:
                tiempo_espera = orden.calcular_tiempo_espera_actual() #
                print(f"\n--- SENSOR DE TIEMPO ---")
                print(f"ALERTA RETRASO: Orden #{orden.get_id()} en {estacion.get_nombre_estacion()}") #
                print(f"  Tiempo actual: {tiempo_espera} min (Estimado: {orden.get_tiempo_estimado()} min)") #
                print("--------------------------\n")


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 65/110: __init__.py
# Directorio: patrones
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/decorator
################################################################################

# ==============================================================================
# ARCHIVO 66/110: __init__.py
# Directorio: patrones/decorator
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/decorator/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 67/110: descuento_decorator.py
# Directorio: patrones/decorator
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/decorator/descuento_decorator.py
# ==============================================================================

from src.patrones.decorator.precio_decorator import PrecioDecoratorBase, ICalculablePrecio

class DescuentoDecorator(PrecioDecoratorBase):
    """
    Decorador concreto: Aplica un descuento porcentual.
    """
    def __init__(self, componente: ICalculablePrecio, porcentaje: float):
        super().__init__(componente)
        self._porcentaje_descuento = porcentaje # Ej: 10 para 10%
        
    def calcular_total(self) -> float:
        # 1. Obtiene el total del componente envuelto
        precio_base = self._componente.calcular_total()
        
        # 2. Calcula el descuento sobre el subtotal
        #    (Importante: usar subtotal para no descontar sobre otros decoradores)
        subtotal = self.calcular_subtotal()
        descuento = subtotal * (self._porcentaje_descuento / 100.0)
        
        # 3. Aplica su propia lógica
        return precio_base - descuento

# ==============================================================================
# ARCHIVO 68/110: precio_decorator.py
# Directorio: patrones/decorator
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/decorator/precio_decorator.py
# ==============================================================================

from abc import ABC, abstractmethod

class ICalculablePrecio(ABC):
    """
    Interfaz Componente: Define la operación que será decorada.
    Tu clase 'Pedido' implementará esta interfaz.
    """
    @abstractmethod
    def calcular_subtotal(self) -> float:
        pass
        
    @abstractmethod
    def calcular_total(self) -> float:
        pass

class PrecioDecoratorBase(ICalculablePrecio):
    """
    Clase Decorador Abstracta.
    Mantiene una referencia al componente que envuelve.
    """
    def __init__(self, componente: ICalculablePrecio):
        self._componente = componente
    
    @property
    def componente(self) -> ICalculablePrecio:
        return self._componente
        
    def calcular_subtotal(self) -> float:
        # Delega al componente envuelto
        return self._componente.calcular_subtotal()

    @abstractmethod
    def calcular_total(self) -> float:
        # Delega al componente envuelto (las subclases lo modificarán)
        pass

# ==============================================================================
# ARCHIVO 69/110: recargo_decorator.py
# Directorio: patrones/decorator
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/decorator/recargo_decorator.py
# ==============================================================================

from src.patrones.decorator.precio_decorator import PrecioDecoratorBase, ICalculablePrecio

class RecargoDecorator(PrecioDecoratorBase):
    """
    Decorador concreto: Aplica un recargo fijo (ej. Delivery).
    """
    def __init__(self, componente: ICalculablePrecio, monto_fijo: float):
        super().__init__(componente)
        self._monto_recargo = monto_fijo
        
    def calcular_total(self) -> float:
        # 1. Obtiene el total del componente envuelto
        precio_base = self._componente.calcular_total()
        
        # 2. Aplica su propia lógica
        return precio_base + self._monto_recargo


################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 70/110: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 71/110: estacion_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/factory/estacion_factory.py
# ==============================================================================

# src/patrones/factory/estacion_factory.py

from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.estacion_parrilla import EstacionParrilla 
from src.entidades.cocina.estacion_pastas import EstacionPastas 
from src.entidades.cocina.estacion_postres import EstacionPostres 
from src.entidades.cocina.estacion_bebidas import EstacionBebidas 

# --- IMPORTACIÓN AÑADIDA ---
# Importamos la nueva clase CONCRETA
from src.entidades.cocina.estacion_cocina_general import EstacionCocinaGeneral
# (Asegúrate de que la ruta de importación sea correcta según dónde guardaste el archivo)


class EstacionFactory:
    """
    Patrón Simple Factory para crear instancias de EstacionCocina.
    """
    
    @staticmethod
    def crear_estacion(nombre_estacion: str) -> EstacionCocina:
        """
        Crea y retorna un objeto EstacionCocina basado en su nombre.
        
        El 'nombre_estacion' proviene de los métodos 
        get_estacion_cocina() de tus ItemMenu.
        """
        nombre_normalizado = nombre_estacion.lower()
        
        if nombre_normalizado == "parrilla":
            return EstacionParrilla()
        
        elif nombre_normalizado == "pastas":
            return EstacionPastas()
            
        elif nombre_normalizado == "postres":
            return EstacionPostres()
        
        elif nombre_normalizado == "bebidas":
            return EstacionBebidas()
        
        # --- LÍNEA CORREGIDA ---
        elif nombre_normalizado == "cocina":
            # Para 'Entrada' y ahora 'Pescado'
            return EstacionCocinaGeneral() # Usamos la clase concreta
        
        # El caso "plancha" se ha eliminado
        
        else:
            raise ValueError(f"Tipo de estación desconocida: {nombre_estacion}")

# ==============================================================================
# ARCHIVO 72/110: item_menu_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/factory/item_menu_factory.py
# ==============================================================================

from src.entidades.menu.categoria_item import CategoriaItem
from src.entidades.menu.item_menu import ItemMenu
from src.entidades.menu.entrada import Entrada
from src.entidades.menu.plato_principal import PlatoPrincipal
from src.entidades.menu.postre import Postre
from src.entidades.menu.bebida import Bebida

class ItemMenuFactory:
    """
    Patrón Simple Factory para crear instancias de ItemMenu.
    """
    
    @staticmethod
    def crear_item(categoria: CategoriaItem, **kwargs) -> ItemMenu:
        """
        Crea y retorna un objeto ItemMenu basado en la categoría.
        'kwargs' debe contener los argumentos necesarios.
        """
        try:
            if categoria == CategoriaItem.ENTRADA:
                return Entrada(
                    nombre=kwargs['nombre'],
                    descripcion=kwargs['descripcion'],
                    tipo_entrada=kwargs['tipo_entrada']
                ) #
            
            elif categoria == CategoriaItem.PLATO_PRINCIPAL:
                return PlatoPrincipal(
                    nombre=kwargs['nombre'],
                    descripcion=kwargs['descripcion'],
                    tipo_proteina=kwargs['tipo_proteina'],
                    guarnicion=kwargs['guarnicion']
                ) #
            
            elif categoria == CategoriaItem.POSTRE:
                return Postre(
                    nombre=kwargs['nombre'],
                    descripcion=kwargs['descripcion'],
                    tipo_postre=kwargs['tipo_postre'],
                    temperatura=kwargs['temperatura']
                ) #
            
            elif categoria == CategoriaItem.BEBIDA:
                return Bebida(
                    nombre=kwargs['nombre'],
                    descripcion=kwargs['descripcion'],
                    tipo_bebida=kwargs['tipo_bebida'],
                    tamanio=kwargs.get('tamanio', 'mediano')
                ) #
            
            else:
                raise ValueError(f"Categoría de item desconocida: {categoria}")
        
        except KeyError as e:
            raise AttributeError(f"Falta el argumento '{e}' para crear un '{categoria}'")


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 73/110: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 74/110: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/observer/observable.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import List
from src.patrones.observer.observer import IObserver

class IObservable(ABC):
    """
    Interfaz del Sujeto Observable.
    """
    
    @abstractmethod
    def agregar_observador(self, observador: IObserver):
        pass
        
    @abstractmethod
    def quitar_observador(self, observador: IObserver):
        pass
        
    @abstractmethod
    def notificar(self):
        pass

class Observable(IObservable):
    """
    Clase base concreta que implementa la lógica de
    manejo de observadores.
    
    Tus entidades (Ej. Ingrediente, Mesa) pueden heredar de aquí.
    """
    
    def __init__(self):
        self._observadores: List[IObserver] = []
        
    def agregar_observador(self, observador: IObserver):
        if observador not in self._observadores:
            self._observadores.append(observador)
            
    def quitar_observador(self, observador: IObserver):
        if observador in self._observadores:
            self._observadores.remove(observador)
            
    def notificar(self):
        """Notifica a todos los observadores en la lista"""
        for obs in self._observadores:
            obs.actualizar(self)

# ==============================================================================
# ARCHIVO 75/110: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/observer/observer.py
# ==============================================================================

from abc import ABC, abstractmethod

class IObserver(ABC):
    """
    Interfaz del Observador.
    """
    
    @abstractmethod
    def actualizar(self, observable: 'IObservable'):
        """
        Método llamado por el observable cuando su estado cambia.
        """
        pass


################################################################################
# DIRECTORIO: patrones/state
################################################################################

# ==============================================================================
# ARCHIVO 76/110: __init__.py
# Directorio: patrones/state
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 77/110: pedido_cancelado_state.py
# Directorio: patrones/state
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/pedido_cancelado_state.py
# ==============================================================================

from src.patrones.state.pedido_state import IPedidoState
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import PedidoInvalidoException

class PedidoCanceladoState(IPedidoState):
    """
    Estado: Cancelado (Final).
    No permite más acciones.
    """
    
    def _error(self):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "El pedido está cancelado y no admite cambios."
        )

    def agregar_item(self, item: ItemPedido):
        self._error()
    
    def cancelar(self):
        print(f"Pedido {self._pedido.get_id()} ya está cancelado.")
    
    def confirmar_preparacion(self):
        self._error()

    def marcar_listo(self):
        self._error()
        
    def servir(self):
        self._error()

# ==============================================================================
# ARCHIVO 78/110: pedido_en_preparacion_state.py
# Directorio: patrones/state
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/pedido_en_preparacion_state.py
# ==============================================================================

from src.patrones.state.pedido_state import IPedidoState
from src.patrones.state.pedido_listo_state import PedidoListoState
from src.patrones.state.pedido_cancelado_state import PedidoCanceladoState
from src.entidades.pedidos.estado_pedido import EstadoPedido
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import PedidoInvalidoException, EstadoPedidoInvalidoException

class PedidoEnPreparacionState(IPedidoState):
    """
    Estado: En Preparación.
    Permite: cancelar o marcar como listo.
    NO permite: agregar items.
    """
    
    def agregar_item(self, item: ItemPedido):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "No se pueden agregar items a un pedido en preparación"
        )
    
    def cancelar(self):
        print(f"Pedido {self._pedido.get_id()} CANCELADO (en preparación).")
        self._pedido.set_estado_interno(PedidoCanceladoState(self._pedido))
    
    def confirmar_preparacion(self):
        # Ya está en este estado, no hacer nada o lanzar error leve
        print(f"Pedido {self._pedido.get_id()} ya está en preparación.")

    def marcar_listo(self):
        print(f"Pedido {self._pedido.get_id()} está LISTO.")
        self._pedido.set_estado_interno(PedidoListoState(self._pedido))
        
    def servir(self):
        raise EstadoPedidoInvalidoException(
            self._pedido.get_id(), EstadoPedido.EN_PREPARACION.value, EstadoPedido.SERVIDO.value
        )

# ==============================================================================
# ARCHIVO 79/110: pedido_listo_state.py
# Directorio: patrones/state
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/pedido_listo_state.py
# ==============================================================================

from src.patrones.state.pedido_state import IPedidoState
from src.patrones.state.pedido_servido_state import PedidoServidoState
from src.entidades.pedidos.estado_pedido import EstadoPedido
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import PedidoInvalidoException, EstadoPedidoInvalidoException

class PedidoListoState(IPedidoState):
    """
    Estado: Listo.
    Permite: servir.
    NO permite: agregar, cancelar, etc.
    """
    
    def agregar_item(self, item: ItemPedido):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "No se pueden agregar items a un pedido listo"
        )
    
    def cancelar(self):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "No se puede cancelar un pedido listo para servir"
        )
    
    def confirmar_preparacion(self):
        raise EstadoPedidoInvalidoException(
            self._pedido.get_id(), EstadoPedido.LISTO.value, EstadoPedido.EN_PREPARACION.value
        )

    def marcar_listo(self):
        print(f"Pedido {self._pedido.get_id()} ya está listo.")
        
    def servir(self):
        print(f"Pedido {self._pedido.get_id()} SERVIDO.")
        self._pedido.set_estado_interno(PedidoServidoState(self._pedido))

# ==============================================================================
# ARCHIVO 80/110: pedido_recibidio_state.py
# Directorio: patrones/state
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/pedido_recibidio_state.py
# ==============================================================================

from src.patrones.state.pedido_state import IPedidoState
from src.patrones.state.pedido_en_preparacion_state import PedidoEnPreparacionState
from src.patrones.state.pedido_cancelado_state import PedidoCanceladoState
from src.entidades.pedidos.estado_pedido import EstadoPedido
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import EstadoPedidoInvalidoException

class PedidoRecibidoState(IPedidoState):
    """
    Estado: Pedido Recibido.
    Permite: agregar items, cancelar, o pasar a preparación.
    """
    
    def agregar_item(self, item: ItemPedido):
        # En estado RECIBIDO, sí se pueden agregar items
        self._pedido._items.append(item)
    
    def cancelar(self):
        print(f"Pedido {self._pedido.get_id()} CANCELADO.")
        self._pedido.set_estado_interno(PedidoCanceladoState(self._pedido))
    
    def confirmar_preparacion(self):
        print(f"Pedido {self._pedido.get_id()} pasa a EN PREPARACIÓN.")
        self._pedido.set_estado_interno(PedidoEnPreparacionState(self._pedido))

    def marcar_listo(self):
        raise EstadoPedidoInvalidoException(
            self._pedido.get_id(), EstadoPedido.RECIBIDO.value, EstadoPedido.LISTO.value
        )
        
    def servir(self):
        raise EstadoPedidoInvalidoException(
            self._pedido.get_id(), EstadoPedido.RECIBIDO.value, EstadoPedido.SERVIDO.value
        )

# ==============================================================================
# ARCHIVO 81/110: pedido_servido_state.py
# Directorio: patrones/state
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/pedido_servido_state.py
# ==============================================================================

from src.patrones.state.pedido_state import IPedidoState
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import PedidoInvalidoException

class PedidoServidoState(IPedidoState):
    """
    Estado: Servido (Final).
    No permite más acciones.
    """
    
    def _error(self):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "El pedido ya fue servido y no admite más cambios."
        )

    def agregar_item(self, item: ItemPedido):
        self._error()
    
    def cancelar(self):
        self._error()
    
    def confirmar_preparacion(self):
        self._error()

    def marcar_listo(self):
        self._error()
        
    def servir(self):
        print(f"Pedido {self._pedido.get_id()} ya fue servido.")

# ==============================================================================
# ARCHIVO 82/110: pedido_state.py
# Directorio: patrones/state
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/pedido_state.py
# ==============================================================================

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Importación circular: Pedido necesita Estado, Estado necesita Pedido
if TYPE_CHECKING:
    from src.entidades.pedidos.pedido import Pedido
    from src.entidades.pedidos.item_pedido import ItemPedido

class IPedidoState(ABC):
    """
    Interfaz (Patrón State) para los estados del Pedido.
    Define las operaciones que pueden variar según el estado.
    """
    
    def __init__(self, pedido: Pedido):
        self._pedido = pedido

    @abstractmethod
    def agregar_item(self, item: ItemPedido):
        """Intenta agregar un item al pedido"""
        pass

    @abstractmethod
    def cancelar(self):
        """Intenta cancelar el pedido"""
        pass
    
    @abstractmethod
    def confirmar_preparacion(self):
        """Intenta pasar el pedido a preparación"""
        pass
        
    @abstractmethod
    def marcar_listo(self):
        """Intenta marcar el pedido como listo para servir"""
        pass
        
    @abstractmethod
    def servir(self):
        """Intenta servir el pedido"""
        pass
        
    def __str__(self) -> str:
        return self.__class__.__name__


################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 83/110: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 84/110: coccion_fritura_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/coccion_fritura_strategy.py
# ==============================================================================

from src.patrones.strategy.metodo_coccion_strategy import IMetodoCoccionStrategy
from src.entidades.cocina.orden_cocina import OrdenCocina

class CoccionFrituraStrategy(IMetodoCoccionStrategy):
    """
    Estrategia concreta para cocinar por fritura.
    """
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        item = orden.get_item_pedido().get_item_menu().get_nombre()
        mensaje = f"🍟 {item} preparado por Fritura."
        orden.agregar_nota_chef(mensaje)
        return mensaje

# ==============================================================================
# ARCHIVO 85/110: coccion_horno_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/coccion_horno_strategy.py
# ==============================================================================

from src.patrones.strategy.metodo_coccion_strategy import IMetodoCoccionStrategy
from src.entidades.cocina.orden_cocina import OrdenCocina

class CoccionHornoStrategy(IMetodoCoccionStrategy):
    """
    Estrategia concreta para cocinar al horno.
    """
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        item = orden.get_item_pedido().get_item_menu().get_nombre()
        mensaje = f"🍞 {item} cocinado al Horno."
        orden.agregar_nota_chef(mensaje)
        return mensaje

# ==============================================================================
# ARCHIVO 86/110: coccion_parrilla_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/coccion_parrilla_strategy.py
# ==============================================================================

from src.patrones.strategy.metodo_coccion_strategy import IMetodoCoccionStrategy
from src.entidades.cocina.orden_cocina import OrdenCocina

class CoccionParrillaStrategy(IMetodoCoccionStrategy):
    """
    Estrategia concreta para cocinar a la parrilla.
    """
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        item = orden.get_item_pedido().get_item_menu().get_nombre()
        # Aquí podría ir lógica más compleja, como verificar
        # el punto de cocción de la orden.
        mensaje = f"🔥 {item} cocinado a la Parrilla."
        orden.agregar_nota_chef(mensaje)
        return mensaje

# ==============================================================================
# ARCHIVO 87/110: coccion_plancha_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/coccion_plancha_strategy.py
# ==============================================================================

from src.patrones.strategy.metodo_coccion_strategy import IMetodoCoccionStrategy
from src.entidades.cocina.orden_cocina import OrdenCocina

class CoccionPlanchaStrategy(IMetodoCoccionStrategy):
    """
    Estrategia concreta para cocinar a la plancha.
    """
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        item = orden.get_item_pedido().get_item_menu().get_nombre()
        mensaje = f"🍳 {item} cocinado a la Plancha."
        orden.agregar_nota_chef(mensaje)
        return mensaje

# ==============================================================================
# ARCHIVO 88/110: coccion_vapor_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/coccion_vapor_strategy.py
# ==============================================================================

from src.patrones.strategy.metodo_coccion_strategy import IMetodoCoccionStrategy
from src.entidades.cocina.orden_cocina import OrdenCocina

class CoccionVaporStrategy(IMetodoCoccionStrategy):
    """
    Estrategia concreta para cocinar al vapor.
    """
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        item = orden.get_item_pedido().get_item_menu().get_nombre()
        mensaje = f"💨 {item} cocinado al Vapor."
        orden.agregar_nota_chef(mensaje)
        return mensaje

# ==============================================================================
# ARCHIVO 89/110: metodo_coccion_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/metodo_coccion_strategy.py
# ==============================================================================

from abc import ABC, abstractmethod
from src.entidades.cocina.orden_cocina import OrdenCocina

class IMetodoCoccionStrategy(ABC):
    """
    Interfaz abstracta (Patrón Strategy) para definir un método de cocción.
    """
    
    @abstractmethod
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        """
        Ejecuta la lógica de cocción específica y retorna un
        mensaje del resultado.
        """
        pass
    
    def __str__(self):
        return self.__class__.__name__.replace("Coccion", "").replace("Strategy", "")


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 90/110: __init__.py
# Directorio: servicios
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/cocina
################################################################################

# ==============================================================================
# ARCHIVO 91/110: __init__.py
# Directorio: servicios/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/cocina/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 92/110: cocina_service.py
# Directorio: servicios/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/cocina/cocina_service.py
# ==============================================================================

# src/servicios/cocina/cocina_service.py

from typing import List, Dict, Optional
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.orden_cocina import OrdenCocina
from src.patrones.factory.estacion_factory import EstacionFactory

class CocinaService:
    """
    Servicio Singleton que gestiona todas las estaciones de cocina.
    Utiliza el EstacionFactory para crear las estaciones.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Evita la re-inicialización
        if hasattr(self, '_inicializado'):
            return
        
        self._estaciones: Dict[str, EstacionCocina] = {}
        self._inicializar_estaciones_std()
        self._inicializado = True
        
    def _inicializar_estaciones_std(self):
        """Crea las estaciones de cocina estándar al inicio."""
        
        # --- LÍNEA CORREGIDA ---
        # Eliminamos "Plancha" de la lista
        nombres_estaciones = ["Parrilla", "Pastas", "Postres", "Bebidas", "Cocina"]
        
        for nombre in nombres_estaciones:
            try:
                estacion = EstacionFactory.crear_estacion(nombre)
                self.registrar_estacion(estacion)
            except ValueError as e:
                print(f"Advertencia: No se pudo crear la estación {nombre}: {e}")

    def registrar_estacion(self, estacion: EstacionCocina):
        nombre = estacion.get_nombre_estacion()
        if nombre not in self._estaciones:
            self._estaciones[nombre] = estacion
            print(f"Estación registrada: {nombre}")
        
    def get_estacion(self, nombre: str) -> Optional[EstacionCocina]:
        return self._estaciones.get(nombre)

    def get_todas_las_estaciones(self) -> List[EstacionCocina]:
        return list(self._estaciones.values())

    def enviar_orden_a_estacion(self, orden: OrdenCocina):
        """
        Envía una OrdenCocina a su estación correspondiente.
        """
        nombre_estacion = orden.get_estacion_asignada()
        estacion = self.get_estacion(nombre_estacion)
        
        if not estacion:
            # Esta excepción ahora se lanzará si un item devuelve "Plancha"
            raise ValueError(f"No se encontró la estación '{nombre_estacion}' para la orden #{orden.get_id()}")
            
        estacion.recibir_orden(orden)
        print(f"Orden #{orden.get_id()} enviada a {nombre_estacion}")

# ==============================================================================
# ARCHIVO 93/110: control_calidad_service.py
# Directorio: servicios/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/cocina/control_calidad_service.py
# ==============================================================================

from src.patrones.observer.observer import IObserver
from src.patrones.observer.observable import IObservable
from src.entidades.cocina.orden_cocina import OrdenCocina
from src.entidades.cocina.estado_orden import EstadoOrden

class ControlCalidadService(IObserver):
    """
    Servicio Singleton que actúa como Observador.
    Puede "observar" órdenes de cocina y reaccionar cuando
    pasan al estado LISTA para verificar la calidad.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._inicializado = True
        print("Servicio de Control de Calidad inicializado.")

    def actualizar(self, observable: IObservable):
        """
        Método de IObserver. Se activa cuando un observable
        (ej. una OrdenCocina) notifica un cambio.
        """
        if not isinstance(observable, OrdenCocina):
            return
            
        orden = observable
        
        # Si la orden está LISTA, simular una verificación
        if orden.get_estado() == EstadoOrden.LISTA:
            self.verificar_orden(orden)
            
    def verificar_orden(self, orden: OrdenCocina):
        """
        Simula la lógica de control de calidad.
        """
        # Lógica de QC: ¿El plato cumple los estándares?
        # ¿Tiene las observaciones correctas?
        print(f"QC: Verificando Orden #{orden.get_id()}...")
        
        # Simulación de falla
        if "extra" in orden.get_observaciones_cliente().lower() and "extra" not in orden.get_notas_chef().lower():
             print(f"QC FALLIDO: Orden #{orden.get_id()} no tiene las notas de 'extra' aplicadas.")
             # Aquí se podría devolver la orden a EN_PREPARACION
        else:
             print(f"QC APROBADO: Orden #{orden.get_id()} lista para entregar.")

# ==============================================================================
# ARCHIVO 94/110: distribucion_ordenes_service.py
# Directorio: servicios/cocina
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/cocina/distribucion_ordenes_service.py
# ==============================================================================

from src.entidades.pedidos.pedido import Pedido
from src.entidades.cocina.orden_cocina import OrdenCocina
from src.servicios.cocina.cocina_service import CocinaService

class DistribucionOrdenesService:
    """
    Servicio Singleton que toma un Pedido y lo divide en
    múltiples OrdenCocina, enviándolas al CocinaService.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._cocina_service = CocinaService()
        self._inicializado = True

    def distribuir_pedido(self, pedido: Pedido):
        """
        Toma un pedido, crea las órdenes de cocina y las distribuye.
        """
        if not pedido.get_items():
            print(f"Advertencia: Pedido #{pedido.get_id()} no tiene items para distribuir.")
            return

        print(f"Distribuyendo Pedido #{pedido.get_id()} en órdenes de cocina...")
        
        for item_pedido in pedido.get_items():
            # Crear una OrdenCocina para cada ItemPedido
            orden = OrdenCocina(
                item_pedido=item_pedido,
                pedido_id=pedido.get_id(),
                mesa_id=pedido.get_mesa_id()
            )
            
            # Usar el CocinaService para enviar la orden
            try:
                self._cocina_service.enviar_orden_a_estacion(orden)
            except ValueError as e:
                print(f"Error al distribuir orden: {e}")
                # Aquí se podría manejar la lógica de un item que no
                # tiene estación (ej. cancelar la orden)


################################################################################
# DIRECTORIO: servicios/inventario
################################################################################

# ==============================================================================
# ARCHIVO 95/110: __init__.py
# Directorio: servicios/inventario
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/inventario/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 96/110: inventario_service.py
# Directorio: servicios/inventario
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/inventario/inventario_service.py
# ==============================================================================

from typing import List, Dict, Optional
from src.entidades.inventario.ingrediente import Ingrediente
from src.patrones.observer.observer import IObserver

class InventarioService:
    """
    Servicio Singleton para gestionar el inventario de ingredientes.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._ingredientes: Dict[str, Ingrediente] = {}
        self._observadores_stock: List[IObserver] = []
        self._inicializado = True
        print("Servicio de Inventario inicializado.")
        
    def agregar_ingrediente(self, ingrediente: Ingrediente):
        """
        Agrega un nuevo ingrediente al inventario y le
        adjunta todos los observadores de stock (ej. Sensores).
        """
        if ingrediente.get_nombre() not in self._ingredientes:
            self._ingredientes[ingrediente.get_nombre()] = ingrediente
            # Adjuntar observadores existentes al nuevo ingrediente
            for obs in self._observadores_stock:
                ingrediente.agregar_observador(obs)
        else:
            # Si ya existe, solo suma el stock
            self.agregar_stock(ingrediente.get_nombre(), ingrediente.get_cantidad_actual())

    def get_ingrediente(self, nombre: str) -> Optional[Ingrediente]:
        return self._ingredientes.get(nombre)

    def consumir_stock(self, nombre: str, cantidad: float):
        ingrediente = self.get_ingrediente(nombre)
        if not ingrediente:
            raise ValueError(f"Ingrediente '{nombre}' no encontrado en inventario.")
        
        ingrediente.consumir_stock(cantidad) # Esto notificará a los observadores

    def agregar_stock(self, nombre: str, cantidad: float):
        ingrediente = self.get_ingrediente(nombre)
        if not ingrediente:
            raise ValueError(f"Ingrediente '{nombre}' no encontrado en inventario.")
            
        ingrediente.agregar_stock(cantidad) # Esto notificará a los observadores
        
    def registrar_observador_stock(self, observador: IObserver):
        """
        Registra un observador (ej. SensorStock) que será notificado
        CADA VEZ que CUALQUIER ingrediente cambie.
        """
        if observador not in self._observadores_stock:
            self._observadores_stock.append(observador)
            # Agrega este observador a todos los ingredientes ya existentes
            for ing in self._ingredientes.values():
                ing.agregar_observador(observador)

# ==============================================================================
# ARCHIVO 97/110: proovedor_service.py
# Directorio: servicios/inventario
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/inventario/proovedor_service.py
# ==============================================================================

class ProveedorService:
    """
    Servicio Singleton para gestionar la información de proveedores
    y órdenes de compra.
    (Implementación placeholder)
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        # self._proveedores = {} # Dict[str, Proveedor]
        self._inicializado = True
        print("Servicio de Proveedores inicializado.")

    def generar_orden_de_compra(self, nombre_ingrediente: str, cantidad: float):
        # Lógica para contactar al proveedor del ingrediente
        print(f"ORDEN DE COMPRA: Solicitando {cantidad} de {nombre_ingrediente}...")
        
    def get_info_proveedor(self, nombre_ingrediente: str) -> Optional[dict]:
        # Lógica para buscar qué proveedor vende un ingrediente
        pass


################################################################################
# DIRECTORIO: servicios/menu
################################################################################

# ==============================================================================
# ARCHIVO 98/110: __init__.py
# Directorio: servicios/menu
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/menu/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 99/110: item_service_registry.py
# Directorio: servicios/menu
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/menu/item_service_registry.py
# ==============================================================================

from typing import Dict, Optional
from src.entidades.menu.item_menu import ItemMenu

class ItemServiceRegistry:
    """
    Patrón Registry (como Singleton) para mantener una
    referencia a todas las plantillas de ItemMenu disponibles.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._items_menu: Dict[str, ItemMenu] = {}
        self._inicializado = True
        print("Registro de Items de Menú inicializado.")

    def registrar_item(self, item: ItemMenu):
        if item.get_nombre() not in self._items_menu:
            self._items_menu[item.get_nombre()] = item
            
    def get_item_por_nombre(self, nombre: str) -> Optional[ItemMenu]:
        item = self._items_menu.get(nombre)
        if not item:
            raise ValueError(f"Item '{nombre}' no encontrado en el registro.")
        
        return item

# ==============================================================================
# ARCHIVO 100/110: menu_service.py
# Directorio: servicios/menu
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/menu/menu_service.py
# ==============================================================================

from src.patrones.factory.item_menu_factory import ItemMenuFactory
from src.servicios.menu.item_service_registry import ItemServiceRegistry
from src.entidades.menu.categoria_item import CategoriaItem
from src.entidades.menu.item_menu import ItemMenu

class MenuService:
    """
    Servicio Singleton que utiliza el Factory para crear
    items y los registra en el Registry.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._factory = ItemMenuFactory()
        self._registry = ItemServiceRegistry()
        self._inicializado = True
        print("Servicio de Menú inicializado.")

    def crear_y_registrar_item(self, categoria: CategoriaItem, **kwargs) -> ItemMenu:
        """
        Paso 1: Usa la Factory para crear el item.
        Paso 2: Usa el Registry para registrarlo.
        """
        try:
            item = self._factory.crear_item(categoria, **kwargs)
            self._registry.registrar_item(item)
            print(f"Item creado y registrado: {item.get_nombre()}")
            return item
        except (AttributeError, ValueError) as e:
            print(f"Error al crear item: {e}")
            raise
            
    def get_item_del_menu(self, nombre: str) -> ItemMenu:
        """
        Obtiene una plantilla de item desde el registro.
        """
        return self._registry.get_item_por_nombre(nombre)


################################################################################
# DIRECTORIO: servicios/pedidos
################################################################################

# ==============================================================================
# ARCHIVO 101/110: __init__.py
# Directorio: servicios/pedidos
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/pedidos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 102/110: comanda_service.py
# Directorio: servicios/pedidos
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/pedidos/comanda_service.py
# ==============================================================================

from typing import Optional
from src.entidades.pedidos.pedido import Pedido
from src.entidades.pedidos.item_pedido import ItemPedido
from src.entidades.pedidos.tipo_servicio import TipoServicio


class PedidoBuilder:
    """
    Patrón Builder para construir un objeto Pedido complejo
    paso a paso.
    """
    def __init__(self, cliente_id: int):
        self._cliente_id = cliente_id
        self._mesa_id: Optional[int] = None
        self._tipo_servicio: TipoServicio = TipoServicio.EN_SALON
        self._items: List[ItemPedido] = []
        self._mozo_id: Optional[int] = None
        self._observaciones: str = ""
        self._es_happy_hour: bool = False
        self._es_frecuente: bool = False
    
    def para_mesa(self, mesa_id: int):
        self._mesa_id = mesa_id
        self._tipo_servicio = TipoServicio.EN_SALON
        return self
        
    def para_delivery(self, direccion: str):
        self._mesa_id = None
        self._tipo_servicio = TipoServicio.DELIVERY
        self.con_observacion(f"Enviar a: {direccion}")
        return self
        
    def con_mozo(self, mozo_id: int):
        self._mozo_id = mozo_id
        return self
        
    def con_item(self, item: ItemPedido):
        self._items.append(item)
        return self
        
    def con_observacion(self, observacion: str):
        self._observaciones = observacion
        return self

    def construir(self) -> Pedido:
        if not self._items:
            raise ValueError("No se puede construir un pedido sin items")
        
        pedido = Pedido(
            cliente_id=self._cliente_id,
            mesa_id=self._mesa_id,
            tipo_servicio=self._tipo_servicio
        )
        
        for item in self._items:
            # Usamos el método delegado al Estado
            pedido.agregar_item(item) 
            
        if self._mozo_id:
            pedido.set_mozo_id(self._mozo_id)
            
        pedido.set_observaciones(self._observaciones)
        
        # (Aquí se podrían setear también _es_happy_hour, etc.)
        
        return pedido

# --- Servicio Comanda ---

class ComandaService:
    """
    Servicio Singleton para la TOMA de pedidos.
    Su principal función es exponer el PedidoBuilder.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._inicializado = True
        print("Servicio de Comandas inicializado.")

    def iniciar_nuevo_pedido(self, cliente_id: int) -> PedidoBuilder:
        """
        Retorna un Builder para construir un nuevo pedido.
        """
        print(f"Iniciando nuevo pedido para cliente {cliente_id}...")
        return PedidoBuilder(cliente_id)

    def finalizar_pedido(self, builder: PedidoBuilder) -> Pedido:
        """
        Construye el pedido desde el builder.
        Aquí se podría registrar en PedidoService.
        """
        pedido = builder.construir()
        print(f"Pedido #{pedido.get_id()} creado y listo para preparación.")
        return pedido

# ==============================================================================
# ARCHIVO 103/110: pedido_service.py
# Directorio: servicios/pedidos
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/pedidos/pedido_service.py
# ==============================================================================

from src.entidades.pedidos.pedido import Pedido
from src.patrones.decorator.precio_decorator import ICalculablePrecio
from src.patrones.decorator.descuento_decorator import DescuentoDecorator
from src.patrones.decorator.recargo_decorator import RecargoDecorator
from src.constantes import DESCUENTO_CLIENTE_FRECUENTE, RECARGO_DELIVERY
from src.entidades.pedidos.tipo_servicio import TipoServicio
from typing import Dict

class PedidoService:
    """
    Servicio Singleton para gestionar el CICLO DE VIDA de un Pedido
    y aplicar lógicas de negocio (como Decorators de precio).
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._pedidos_activos: Dict[int, Pedido] = {}
        self._inicializado = True
        print("Servicio de Pedidos inicializado.")
        
    def registrar_pedido(self, pedido: Pedido):
        self._pedidos_activos[pedido.get_id()] = pedido

    def get_pedido(self, pedido_id: int) -> Pedido:
        return self._pedidos_activos[pedido_id]

    # --- Métodos que delegan al PATRÓN STATE ---
    
    def confirmar_preparacion_pedido(self, pedido_id: int):
        pedido = self.get_pedido(pedido_id)
        pedido.get_estado().confirmar_preparacion()

    def marcar_pedido_listo(self, pedido_id: int):
        pedido = self.get_pedido(pedido_id)
        pedido.get_estado().marcar_listo()

    def servir_pedido(self, pedido_id: int):
        pedido = self.get_pedido(pedido_id)
        pedido.get_estado().servir()

    def cancelar_pedido(self, pedido_id: int):
        pedido = self.get_pedido(pedido_id)
        pedido.get_estado().cancelar()

    # --- Método que usa el PATRÓN DECORATOR ---

    def calcular_precio_final_con_cargos(self, pedido_id: int) -> float:
        """
        Calcula el precio final aplicando dinámicamente
        descuentos y recargos usando Decorators.
        """
        pedido = self.get_pedido(pedido_id)
        
        # 1. El componente base es el propio pedido
        componente_precio: ICalculablePrecio = pedido
        
        # 2. Envolver con decoradores según la lógica
        if pedido._es_cliente_frecuente:
            componente_precio = DescuentoDecorator(
                componente=componente_precio,
                porcentaje=DESCUENTO_CLIENTE_FRECUENTE
            )
            
        if pedido.get_tipo_servicio() == TipoServicio.DELIVERY:
            componente_precio = RecargoDecorator(
                componente=componente_precio,
                monto_fijo=RECARGO_DELIVERY
            )
        
        # (Se podrían agregar más, ej. Happy Hour, Recargo Servicio Mesa)
        
        # 3. El cálculo final es polimórfico
        precio_final = componente_precio.calcular_total()
        
        return precio_final


################################################################################
# DIRECTORIO: servicios/persistencia
################################################################################

# ==============================================================================
# ARCHIVO 104/110: __init__.py
# Directorio: servicios/persistencia
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/persistencia/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 105/110: restaurante_persistence_service.py
# Directorio: servicios/persistencia
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/persistencia/restaurante_persistence_service.py
# ==============================================================================

import pickle
from typing import Any
from src.excepciones.persistencia_exception import PersistenciaException, ArchivoNoEncontradoException

class RestaurantePersistenceService:
    """
    Servicio Singleton para guardar y cargar el estado
    del restaurante (usando pickle como ejemplo).
    (Implementación placeholder)
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, archivo_data: str = "data/restaurante_estado.dat"):
        if hasattr(self, '_inicializado'):
            return
        self._archivo_data = archivo_data
        self._inicializado = True
        print(f"Servicio de Persistencia inicializado (archivo: {self._archivo_data})")
        
    def guardar_estado(self, data: Any):
        """Guarda un objeto (ej. un dict con todos los servicios) en un archivo."""
        try:
            with open(self._archivo_data, 'wb') as f:
                pickle.dump(data, f)
            print(f"Estado del restaurante guardado en {self._archivo_data}")
        except IOError as e:
            raise PersistenciaException("escritura", str(e))

    def cargar_estado(self) -> Any:
        """Carga el estado del restaurante desde un archivo."""
        try:
            with open(self._archivo_data, 'rb') as f:
                data = pickle.load(f)
            print(f"Estado del restaurante cargado desde {self._archivo_data}")
            return data
        except FileNotFoundError:
            raise ArchivoNoEncontradoException(self._archivo_data)
        except (IOError, pickle.PickleError) as e:
            raise PersistenciaException("lectura", str(e))


################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 106/110: __init__.py
# Directorio: servicios/personal
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 107/110: personal_service.py
# Directorio: servicios/personal
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/personal/personal_service.py
# ==============================================================================

from typing import Dict, List, Optional
from src.entidades.personal.empleado import Empleado
from src.entidades.personal.chef import Chef
from src.entidades.personal.mozo import Mozo
from src.entidades.personal.cajero import Cajero

class PersonalService:
    """
    Servicio Singleton para gestionar todos los empleados.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._empleados: Dict[int, Empleado] = {}
        self._inicializado = True
        print("Servicio de Personal inicializado.")

    def contratar_empleado(self, empleado: Empleado):
        if empleado.get_id() not in self._empleados:
            self._empleados[empleado.get_id()] = empleado
            print(f"Empleado contratado: {empleado.get_nombre_completo()} ({empleado.obtener_rol()})")
        
    def get_empleado(self, empleado_id: int) -> Optional[Empleado]:
        return self._empleados.get(empleado_id)
        
    def get_all_empleados(self) -> List[Empleado]:
        return list(self._empleados.values())
        
    def get_mozos_disponibles(self) -> List[Mozo]:
        return [
            e for e in self._empleados.values() 
            if isinstance(e, Mozo) and e.esta_activo()
        ]
        
    def get_chefs_disponibles(self) -> List[Chef]:
        return [
            e for e in self._empleados.values() 
            if isinstance(e, Chef) and e.esta_activo()
        ]


################################################################################
# DIRECTORIO: servicios/salon
################################################################################

# ==============================================================================
# ARCHIVO 108/110: __init__.py
# Directorio: servicios/salon
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/salon/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 109/110: mesa_service.py
# Directorio: servicios/salon
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/salon/mesa_service.py
# ==============================================================================

from typing import Dict, List, Optional
from src.entidades.salon.mesa import Mesa
from src.entidades.salon.estado_mesa import EstadoMesa

class MesaService:
    """
    Servicio Singleton para gestionar las mesas del salón.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._mesas: Dict[int, Mesa] = {} # Por ID de mesa
        self._inicializado = True
        print("Servicio de Mesas inicializado.")
        
    def agregar_mesa(self, mesa: Mesa):
        if mesa.get_id() not in self._mesas:
            self._mesas[mesa.get_id()] = mesa

    def get_mesa(self, mesa_id: int) -> Optional[Mesa]:
        return self._mesas.get(mesa_id)
        
    def get_mesas_por_estado(self, estado: EstadoMesa) -> List[Mesa]:
        return [m for m in self._mesas.values() if m.get_estado() == estado]
        
    def buscar_mesa_disponible(self, cantidad_personas: int) -> Optional[Mesa]:
        disponibles = self.get_mesas_por_estado(EstadoMesa.DISPONIBLE)
        # Ordenar por capacidad (la más ajustada primero)
        disponibles.sort(key=lambda m: m.get_capacidad())
        
        for mesa in disponibles:
            if mesa.puede_aceptar_comensales(cantidad_personas):
                return mesa
        return None # No hay mesas disponibles

    def ocupar_mesa(self, mesa_id: int, cantidad: int, pedido_id: int):
        mesa = self.get_mesa(mesa_id)
        if mesa:
            mesa.ocupar(cantidad, pedido_id)
            print(f"Mesa #{mesa.get_numero()} ocupada.")
        
    def liberar_mesa(self, mesa_id: int):
        mesa = self.get_mesa(mesa_id)
        if mesa:
            mesa.liberar()
            print(f"Mesa #{mesa.get_numero()} liberada (en limpieza).")

# ==============================================================================
# ARCHIVO 110/110: reserva_service.py
# Directorio: servicios/salon
# Ruta completa: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/salon/reserva_service.py
# ==============================================================================

from typing import Dict, List, Optional
from datetime import datetime
from src.entidades.salon.reserva import Reserva
from src.entidades.salon.estado_reserva import EstadoReserva
from src.servicios.salon.mesa_service import MesaService

class ReservaService:
    """
    Servicio Singleton para gestionar las reservas.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._reservas: Dict[int, Reserva] = {}
        self._mesa_service = MesaService() # Usa el servicio de mesas
        self._inicializado = True
        print("Servicio de Reservas inicializado.")
        
    def crear_reserva(self, cliente_id: int, fecha_hora: datetime, 
                      cantidad: int, nombre: str, telefono: str) -> Reserva:
        
        # 1. Buscar si hay mesa disponible para esa hora
        # (Aquí iría una lógica compleja de disponibilidad vs. reservas existentes)
        
        # 2. Si hay, buscar una mesa adecuada
        mesa = self._mesa_service.buscar_mesa_disponible(cantidad) # Simplificación
        
        if not mesa:
            raise ValueError("No hay mesas disponibles para esa cantidad de personas")
            
        # 3. Crear la reserva
        reserva = Reserva(cliente_id, fecha_hora, cantidad, nombre, telefono)
        
        # 4. Asignar y reservar la mesa
        reserva.set_mesa_asignada(mesa.get_id())
        mesa.reservar(reserva.get_id())
        
        self._reservas[reserva.get_id()] = reserva
        print(f"Reserva #{reserva.get_id()} creada para Mesa #{mesa.get_numero()}")
        return reserva

    def get_reserva(self, reserva_id: int) -> Optional[Reserva]:
        return self._reservas.get(reserva_id)
        
    def confirmar_llegada(self, reserva_id: int):
        reserva = self.get_reserva(reserva_id)
        if not reserva:
            raise ValueError("Reserva no encontrada")
            
        reserva.registrar_llegada()
        
        # Ocupar la mesa
        mesa_id = reserva.get_mesa_asignada_id()
        if mesa_id:
            mesa = self._mesa_service.get_mesa(mesa_id)
            if mesa and mesa.esta_reservada():
                # Asumimos que se crea un pedido en este momento
                # (Lógica de PedidoService iría aquí)
                pedido_id_nuevo = 999 # ID de pedido simulado
                
                mesa.ocupar(reserva.get_cantidad_personas(), pedido_id_nuevo)
                print(f"Reserva #{reserva_id} registrada. Mesa #{mesa.get_numero()} ocupada.")
            else:
                print(f"Advertencia: Mesa #{mesa_id} no estaba en estado 'Reservada'.")


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 110
# Generado: 2025-11-05 09:49:44
################################################################################
