class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_bienvenida(self):
        print(f"\n¡Bienvenido, {self.nombre}! Aquí está nuestra lista de platillos tradicionales mexicanos:\n")

class Menu:
    PRECIO_UNITARIO = 50  # Precio por platillo

    def __init__(self):
        self.platillos = [
            "1. Tacos al Pastor",
            "2. Tamales",
            "3. Chiles en Nogada",
            "4. Pozole",
            "5. Mole Poblano",
            "6. Enchiladas Verdes",
            "7. Sopes",
            "8. Barbacoa de Borrego",
            "9. Cochinita Pibil",
            "10. Pambazos"
        ]

    def mostrar_menu(self):
        for platillo in self.platillos:
            print(platillo)

    def seleccionar_platillo(self, opcion):
        if 1 <= opcion <= len(self.platillos):
            return self.platillos[opcion - 1][3:]  # Retorna solo el nombre del platillo
        else:
            return None

    def calcular_costo(self, cantidad):
        return cantidad * self.PRECIO_UNITARIO

# Función principal
def main():
    print("¡Bienvenido al restaurante de comida tradicional mexicana!\n")
    
    # Ingresar el nombre del usuario
    nombre = input("Por favor, ingresa tu nombre: ")
    usuario = Usuario(nombre)
    usuario.mostrar_bienvenida()

    # Mostrar menú
    menu = Menu()
    menu.mostrar_menu()

    # Seleccionar platillo
    try:
        opcion = int(input("\nSelecciona el número del platillo que deseas ordenar: "))
        platillo = menu.seleccionar_platillo(opcion)
        
        if platillo:
            print(f"\nHas seleccionado: {platillo}")
            
            # Solicitar la cantidad de platillos
            cantidad = int(input(f"¿Cuántos '{platillo}' deseas comprar? "))
            
            if cantidad > 0:
                # Calcular costo total
                costo_total = menu.calcular_costo(cantidad)
                print(f"\nResumen de tu compra:")
                print(f"Platillo: {platillo}")
                print(f"Cantidad: {cantidad}")
                print(f"Precio por unidad: $50")
                print(f"Total a pagar: ${costo_total}")
                print("\n¡Gracias por tu compra! ¡Buen provecho!")
            else:
                print("La cantidad debe ser mayor a 0.")
        else:
            print("Opción no válida. Intenta nuevamente.")
    
    except ValueError:
        print("Error: Debes ingresar un número válido.")

# Ejecutar programa
if __name__ == "__main__":
    main()
