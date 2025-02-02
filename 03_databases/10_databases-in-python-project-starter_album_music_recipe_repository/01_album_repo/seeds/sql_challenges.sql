music_library=# SELECT title
music_library-# FROM albums
music_library-# WHERE  artist_id = 1;
    title    
-------------
 Doolittle
 Surfer Rosa
 Bossanova
(3 rows)

music_library=# DELETE FROM albums
music_library-# WHERE id = 12;
DELETE 1
music_library=# SELECT id, title, release_year, artist_id
FROM albums;
 id |        title         | release_year | artist_id 
----+----------------------+--------------+-----------
  1 | Doolittle            |         1989 |         1
  2 | Surfer Rosa          |         1988 |         1
  3 | Waterloo             |         1974 |         2
  4 | Super Trouper        |         1980 |         2
  5 | Bossanova            |         1990 |         1
  8 | I Put a Spell on You |         1965 |         4
  9 | Baltimore            |         1978 |         4
 10 | Here Comes the Sun   |         1971 |         4
 11 | Fodder on My Wings   |         1982 |         4
  6 | Lover                |         1972 |         3
  7 | Folklore             |         1972 |         3
 13 | Mezzanine            |         1998 |          
(12 rows)

music_library=# INSERT INTO artists
music_library-# (name, genre)
music_library-# VALUES('Queen', 'Rock');
INSERT 0 1
music_library=# SELECT id, name, genre FROM artists;
 id |      name      |    genre    
----+----------------+-------------
  1 | Pixies         | Rock
  2 | ABBA           | Pop
  3 | Taylor Swift   | Pop
  4 | Nina Simone    | Jazz
  5 | Massive Attack | Alternative
  6 | Queen          | Rock
(6 rows)

music_library=# INSERT INTO albums
music_library-# (title, release_year, artist_id)
music_library-# VALUES('A Night at the Opera', 1975, 6);
INSERT 0 1
music_library=# SELECT id, title, release_year, artist_id FROM albums;
 id |        title         | release_year | artist_id 
----+----------------------+--------------+-----------
  1 | Doolittle            |         1989 |         1
  2 | Surfer Rosa          |         1988 |         1
  3 | Waterloo             |         1974 |         2
  4 | Super Trouper        |         1980 |         2
  5 | Bossanova            |         1990 |         1
  8 | I Put a Spell on You |         1965 |         4
  9 | Baltimore            |         1978 |         4
 10 | Here Comes the Sun   |         1971 |         4
 11 | Fodder on My Wings   |         1982 |         4
  6 | Lover                |         1972 |         3
  7 | Folklore             |         1972 |         3
 13 | Mezzanine            |         1998 |          
 14 | A Night at the Opera |         1975 |         6
(13 rows)

music_library=# 