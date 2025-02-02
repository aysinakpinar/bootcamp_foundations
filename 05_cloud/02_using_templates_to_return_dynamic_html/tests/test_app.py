from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

def test_get_goodbye(page, test_web_address):
    page.goto(f"http://{test_web_address}/goodbye")
    strong_tag = page.locator("strong")
    expect(strong_tag).to_have_text("Bye!")

def test_get_greet(page, test_web_address):
    page.goto(f"http://{test_web_address}/greet?name=Aysin")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text(f"Hello Aysin")

def test_get_albums(page, test_web_address, db_connection,):
    db_connection.seed('seeds/music_web_html.sql')
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator('h2')
    p_tags = page.locator('p')
    expect(h2_tags).to_have_text([
        'Title: Doolittle',
        'Title: Dancing Queen',
        'Title: Waterloo',
        'Title: Super Trouper',
        'Title: Bossanova',
        'Title: Lover',
        'Title: Folklore',
        'Title: I Put a Spell on You',
        'Title: Baltimore',
        'Title: Here Comes the Sun',
        'Title: Fodder on My Wings',
        'Title: Ring Ring'
    ])
    expect(p_tags).to_have_text([
       'Released: 1989',
       'Released: 1976',
       'Released: 1974',
       'Released: 1980',
       'Released: 1990',
       'Released: 2019',
       'Released: 2020',
       'Released: 1965',
       'Released: 1978',
       'Released: 1971',
       'Released: 1982',
       'Released: 1973',
    ])

def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_html.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    div_tag = page.locator("div")
    expect(h1_tag).to_have_text('Doolittle')
    expect(div_tag).to_have_text(['Release year: 1989\nArtist: Pixies'])


    
# === End Example Code ===
