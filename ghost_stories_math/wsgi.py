import flask

from ghost_stories_math import Exorcism


def create_app():
    app = flask.Flask(__name__)

    @app.route("/")
    def index():
        return flask.render_template("index.html",
                                     result=None,
                                     dice=None,
                                     resistance=None,
                                     second_wind=False,
                                     nameless=False)

    @app.route("/probability")
    def probability():
        dice = int(flask.request.args.get("dice"))
        resistance = int(flask.request.args.get("resistance"))
        second_wind = flask.request.args.get("Second Wind") == "sw"
        nameless = flask.request.args.get("Nameless") == "nm"

        powers = []
        if second_wind:
            powers.append("Second Wind")
        if not nameless:
            powers.append("Wild White")
        result = Exorcism(dice, powers).probability(resistance)
        return flask.render_template("index.html",
                                     result=result,
                                     dice=dice,
                                     resistance=resistance,
                                     second_wind=second_wind,
                                     nameless=nameless)

    @app.route("/scenario")
    def scenario():
        dice = int(flask.request.args.get("dice"))
        resistance = int(flask.request.args.get("resistance"))
        second_wind = flask.request.args.get("Second Wind") == "sw"
        nameless = flask.request.args.get("Nameless") == "nm"

        powers = []
        if second_wind:
            powers.append("Second Wind")
        if not nameless:
            powers.append("Wild White")
        result = Exorcism(dice, powers).scenario(resistance)
        return flask.render_template("index.html",
                                     result=result,
                                     dice=dice,
                                     resistance=resistance,
                                     second_wind=second_wind,
                                     nameless=nameless)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
