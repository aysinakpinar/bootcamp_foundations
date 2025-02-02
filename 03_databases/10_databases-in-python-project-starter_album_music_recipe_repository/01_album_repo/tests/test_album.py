from lib.album import Album

def test_album_attributes():
    album1 = Album(1, 'Doolittle', 1989, 1)
    assert album1.id == 1
    assert album1.title == 'Doolittle'
    assert album1.release_year == 1989
    assert album1.title_id == 1

def test_albums_equal():
    album1 = Album(1, 'Doolittle', 1989, 1)
    album2 = Album(1, 'Doolittle', 1989, 1)
    assert album1 == album2

def test_album_format():
    album1 = Album(1, 'Doolittle', 1989, 1)
    assert str(album1) == "Album(1, Doolittle, 1989, 1)"
    