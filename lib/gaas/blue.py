from flask import (
    Blueprint,
    render_template,
    abort,
    session,
    url_for,
    redirect)

from jinja2 import TemplateNotFound

from . import game
from . import dal


simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        if 'uuid' in session:
            uuid = session.get('uuid')
            return render_template('pages/{}.html'.format(page), game_id=uuid)
        else:
            g = game.CardGame()
            dal.save_game(g)
            session['uuid'] = g.uuid
            return render_template('pages/{}.html'.format(page), game_id=g.uuid)
    except TemplateNotFound:
        abort(404)


@simple_page.route('/logout')
def logout():
    print "logging out"
    session.pop('uuid', None)
    print session.get("uuid")
    return redirect(url_for('simple_page.show'))