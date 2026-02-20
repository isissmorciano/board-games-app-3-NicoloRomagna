from app.db import get_db

def get_matches_for_game(game_id):
    db = get_db()
    return db.execute(
        "SELECT id, data, vincitore, punteggio_vincitore "
        "FROM partite WHERE gioco_id = ? ORDER BY data DESC",
        (game_id,),
    ).fetchall()

def create_match(game_id, data, vincitore, punteggio_vincitore):
    db = get_db()
    db.execute(
        "INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) "
        "VALUES (?, ?, ?, ?)",
        (game_id, data, vincitore, punteggio_vincitore),
    )
    db.commit()