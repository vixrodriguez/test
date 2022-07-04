from app import app
from app import products, users, audit


# @app.route("/products/notify")
# def notify():
#     ctx = {
#         'action': 'changed',
#         'username': 'admin1234',
#         'field': 'price',
#         'product': 'PC GAMING',
#         'previous_value': '10',
#         'new_value': '15'
#     }
#     email = Email(recipient='info@mitco.cloud',
#                   subject='Change in product - {}'.format('PC GAMING'),
#                   message_html=render_template('email_template_updated.html', **ctx)
#                   )
#     email.send()
#     return 'OK'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
