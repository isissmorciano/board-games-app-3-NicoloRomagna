from app.db import get_db

def get_all_games():
    db = get_db()
    return db.execute(
        "SELECT id, nome, numero_giocatori_massimo, durata_media, categoria FROM giochi ORDER BY nome"
    ).fetchall()

def get_game_by_id(game_id):
    db = get_db()
    return db.execute(
        "SELECT id, nome, numero_giocatori_massimo, durata_media, categoria FROM giochi WHERE id = ?",
        (game_id,),
    ).fetchone()

def create_game(nome, numero_giocatori_massimo, durata_media, categoria):
    db = get_db()
    db.execute(
        "INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria) VALUES (?, ?, ?, ?)",
        (nome, numero_giocatori_massimo, durata_media, categoria),
    )
    db.commit()