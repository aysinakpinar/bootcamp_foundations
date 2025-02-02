import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

@app.route('/goodbye', methods = ['GET'])
def get_goodbye():
    return render_template('/goodbye.html', goodbye = 'Bye!')

@app.route('/greet')
def greet():
    name = request.args.get('name')
    return render_template('greet.html', name = name)

@app.route('/albums', methods = ['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums=albums)

@app.route('/albums/<int:id>', methods = ['GET'])
def get_album_contents(id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    album = album_repository.find(id)
    artist = artist_repository.find(album.artist_id)
    artist_name = artist.name
    return render_template("albums/get_album.html",  artist_name=artist_name, album=album)

# @app.route('/albums', methods = ['GET'])
# def get_album()


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
