import base64

#testing images
test_png = '/Users/shenghongzhong/Documents/pinich/assets/Pinich-Logos5.png'
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')