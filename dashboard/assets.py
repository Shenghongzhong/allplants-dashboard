import base64

#testing images
test_png = '/Users/shenghongzhong/Documents/allplants-dashboard/assets/logo.png'
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')