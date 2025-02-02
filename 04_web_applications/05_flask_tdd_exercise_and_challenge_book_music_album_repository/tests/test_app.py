# Tests for your routes go here

# === Example Code Below ===

"""
POST /albums
posts an album with:
title=Voyage
release_year=2022
artist_id=2

"""
def test_post_album(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.post("/albums", data = {
        "title": "Voyage", 
        "release_year": 2022, 
        "artist_id": 2})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album successfully added."

    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, Bossanova, 1990, 1)\n" \
        "Album(6, Lover, 2019, 3)\n" \
        "Album(7, Folklore, 2020, 3)\n" \
        "Album(8, I Put a Spell on You, 1965, 4)\n" \
        "Album(9, Baltimore, 1978, 4)\n" \
        "Album(10, Here Comes the Sun, 1971, 4)\n" \
        "Album(11, Fodder on My Wings, 1982, 4)\n" \
        "Album(12, Ring Ring, 1973, 2)\n" \
        "Album(13, Voyage, 2022, 2)"
    
def test_get_artist_names(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'

def test_post_artist(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.post('/artists', data = {
        'name': 'Wild nothing',
        'genre': 'Indie'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Artist was successfully added"

    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'
# === End Example Code ===
