#!/usr/bin/env python

from gaas import webapp
from gaas import dal
from gaas.blue import simple_page
from gaas.webapp import routes

dal.connect_to_db()
routes.create_routes()


app = webapp.app
app.register_blueprint(simple_page)

app.debug = True
app.run(debug=True)
