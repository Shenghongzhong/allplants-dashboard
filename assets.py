import base64


def make_base(path):
    path_png = path
    base = base64.b64encode(open(path_png, 'rb').read()).decode('ascii')
    return base    



#logo images
logo_png = 'assets/logo.png'
logo_base64 = make_base(logo_png)

# fomular

formular_png = 'assets/weekly_average.png'
formular_base64 = make_base(formular_png)

# launch products

lan_products_png = 'assets/launch_products.png'
lan_products_base64 = make_base(lan_products_png)

# Breakfast 
breakfast_png = 'assets/breakfast.png'
breakfast_base64 = make_base(breakfast_png)

# treats
treats_png = 'assets/treats.png'
treats_base64 = make_base(treats_png)

# formular
formular_b_png ='assets/formular_2.png'
formular_b_base64 = make_base(formular_b_png)