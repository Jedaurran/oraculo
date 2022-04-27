def pulsador_a():
    basic.show_string("Mi nombre es Cathyvipi")
def pulsador_b():
    basic.show_string("Menti soy el Xocas")
    
input.on_button_pressed(Button.A, pulsador_a)
input.on_button_pressed(Button.B, pulsador_b)
