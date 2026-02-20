from flask import Blueprint, render_template, request, redirect, url_for, abort
from .repositories import game_repository, match_repository

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    giochi = game_repository.get_all_games()
    return render_template("index.html", giochi=giochi)

@bp.route("/giochi/nuovo", methods=["GET", "POST"])
def crea_gioco():
    if request.method == "POST":
        nome = request.form["nome"]
        numero = request.form["numero_giocatori_massimo"]
        durata = request.form["durata_media"]
        categoria = request.form["categoria"]

        if not nome or not numero or not durata or not categoria:
            error = "Tutti i campi sono obbligatori."
            return render_template("creagioco.html", error=error)

        game_repository.create_game(
            nome,
            int(numero),
            int(durata),
            categoria,
        )
        return redirect(url_for("main.index"))

    return render_template("creagioco.html")

@bp.route("/giochi/<int:gioco_id>/partite")
def partite_gioco(gioco_id):
    gioco = game_repository.get_game_by_id(gioco_id)
    if gioco is None:
        abort(404)
    partite = match_repository.get_matches_for_game(gioco_id)
    return render_template("partite_gioco.html", gioco=gioco, partite=partite)

@bp.route("/giochi/<int:gioco_id>/partite/nuova", methods=["GET", "POST"])
def crea_partita(gioco_id):
    gioco = game_repository.get_game_by_id(gioco_id)
    if gioco is None:
        abort(404)

    if request.method == "POST":
        data = request.form["data"]
        vincitore = request.form["vincitore"]
        punteggio = request.form["punteggio_vincitore"]

        if not data or not vincitore or not punteggio:
            error = "Tutti i campi sono obbligatori."
            return render_template(
                "creapartita.html", gioco=gioco, error=error
            )

        match_repository.create_match(
            gioco_id,
            data,
            vincitore,
            int(punteggio),
        )
        return redirect(url_for("main.partite_gioco", gioco_id=gioco_id))

    return render_template("creapartita.html", gioco=gioco)

@bp.route("/about")
def about():
    return render_template("about.html")