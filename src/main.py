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