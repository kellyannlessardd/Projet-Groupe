from machine import ADC, Pin

# Potentiomètres
pot_x = ADC(26)
pot_y = ADC(27)

# Interrupteur (stylo)
switch = Pin(16, Pin.IN, Pin.PULL_UP)

# --- Etat mémoire du stylo (False = haut, True = bas) ---
pen_state = False
last_switch_value = 1

def read_potentiometers():
    """
    Lit les deux potentiomètres et retourne X et Y.
    Retourne : (x, y) entre 0 et 65535.
    """
    x = pot_x.read_u16()
    y = pot_y.read_u16()
    return x, y

def read_switch():
    """
    Modifie l'état du stylo à chaque pression sur l'interrupteur.
    Retourne l'état actuel du stylo : True = bas, False = haut.
    """
    global pen_state, last_switch_value

    current_value = switch.value()

    if last_switch_value == 1 and current_value == 0:
        pen_state = not pen_state  # Toggle de l'état

    # Mise à jour du précédent état
    last_switch_value = current_value

    return pen_state
