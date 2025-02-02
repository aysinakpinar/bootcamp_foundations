import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/albums', methods = ['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    albums_strings = [f"{album}" for album in albums]
    return "\n".join(albums_strings)

@app.route('/albums', methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    album = Album(None, title, release_year, artist_id)
    repository.create(album)

    return "Album successfully added."

@app.route('/artists', methods = ['GET'])
def get_artist_names():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    artist_names = [artist.name for artist in artists]
    return ", ". join(artist_names)

@app.route('/artists', methods = ['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form["name"]
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    repository.create(artist)
    return "Artist was successfully added"




# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

