from adafruit_pybadger import PyBadger

pybadger = PyBadger()

pybadger.show_badge(name_string="Blinka", hello_scale=2, my_name_is_scale=2, name_scale=3)

while True:
    pybadger.auto_dim_display(delay=10)
    if pybadger.button.a:
        pybadger.show_business_card(image_name="Blinka.bmp", name_string="Blinka", name_scale=2,
                                    email_string_one="blinka@", email_string_two="adafruit.com")
    elif pybadger.button.b:
        pybadger.show_qr_code(data="https://circuitpython.org")
    elif pybadger.button.start:
        pybadger.show_badge(name_string="Blinka", hello_scale=2, my_name_is_scale=2, name_scale=3)