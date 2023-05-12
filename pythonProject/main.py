# Clase para representar los elementos del menú
class MenuItem:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def calculate_price_with_tax(self):
        tax_rate = 0.16  # Tasa de impuesto (16%)
        return self.price * (1 + tax_rate)

    def __str__(self):
        return f"{self.name} - ${self.calculate_price_with_tax():.2f}\n{self.description}"


# Lista de elementos del menú
menu = []

# Función para agregar un elemento al menú
def add_to_menu(name, price, description):
    menu.append(MenuItem(name, price, description))

# Función para mostrar el menú completo
def show_menu():
    print("~~~ MENÚ ~~~")
    for index, item in enumerate(menu):
        print(f"{index + 1}. {item}")
        print("--------------")

# Función para tomar el pedido del cliente
def take_order():
    order = []
    while True:
        choice = input("Selecciona un número de opción (0 para finalizar): ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(menu):
                order.append(menu[choice - 1])
                print(f"Has añadido '{menu[choice - 1].name}' a tu pedido.")
            else:
                print("Opción inválida. Intenta de nuevo.")
        except ValueError:
            print("Opción inválida. Intenta de nuevo.")
    return order

# Función para mostrar el pedido del cliente
def show_order(order):
    print("~~~ TU PEDIDO ~~~")
    if order:
        total = 0
        for item in order:
            print(item)
            print("--------------")
            total += item.calculate_price_with_tax()
        print(f"TOTAL: ${total:.2f}")
    else:
        print("Tu pedido está vacío.")

# Agregar elementos al menú
add_to_menu("Hamburguesa", 50,"Una deliciosa hamburguesa con queso, lechuga y tomate.")
add_to_menu("Pizza", 10.99, "Pizza de pepperoni con queso fundido y salsa de tomate.")
add_to_menu("Ensalada César", 6.99, "Ensalada fresca con pollo a la parrilla, crutones y aderezo César.")
add_to_menu("Pasta Alfredo", 9.99, "Pasta con salsa Alfredo, champiñones y espinacas.")
add_to_menu("Botana Clasica", 120.00, "Boneles Bufalo, Dedos de queso y papas.")
add_to_menu("Tacos de Bisteck", 80.00, "4 tacos de bisteck.")
add_to_menu("Hot dogs", 35.00, "Hot dog sencillo.")
add_to_menu("Gringa", 50.00, "Gringa con carne de trompo.")
add_to_menu("Gorditas", 20.00, "Gorditas de maiz con discada.")
add_to_menu("Limonada mineral", "Agua de limón con agua mineral.")
add_to_menu("Refresco de cola", "Coca Cola.")
add_to_menu("Jugo", "Jugo de naranja.")
add_to_menu("Alcohol ", "Cerveza Indio.")
add_to_menu("Alcohol ", "Cerveza Corona.")
add_to_menu("Alcohol, Cerveza XX.")
add_to_menu("Campechana" , "Campechana con carne de trompo carne de bisteck y aguacate.")

# Mostrar el menú
show_menu()

# Tomar el pedido del cliente
order = take_order()

# Mostrar el pedido del cliente
show_order(order)