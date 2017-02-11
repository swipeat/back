import sqlite3

# Is ingredient rated?
def is_rated(username, ingredient):

    # Connection and cursor
    conn = sqlite3.connect('swipeat.db')
    c = conn.cursor()

    # Search for the ingredient
    c.execute('''SELECT * FROM swipeat_profiles WHERE username like \'''' + username + '''\' AND ingredient like \'''' + ingredient + "\'")
    all_rows = c.fetchall()

    # Check if exists
    if len(all_rows) == 0:
        return False
    else:
        return True

# Add an ingredient to the user's profile
def rate_ingredient(username, ingredient, rating):

    # Connection and cursor
    conn = sqlite3.connect('swipeat.db')
    c = conn.cursor()

    # Already rated?
    if is_rated(username, ingredient):
        # Update the ingredient
        c.execute('''UPDATE swipeat_profiles SET note = :rating WHERE username LIKE :username AND ingredient LIKE :ingredient''', {'username' : username, 'ingredient' : ingredient, 'rating' : rating})
        conn.commit()
    else:
        # Add the ingredient
        c.execute('''INSERT INTO swipeat_profiles(username, ingredient, note) VALUES(:username,:ingredient,:rating)''', {'username' : username, 'ingredient' : ingredient, 'rating' : rating})
        conn.commit()

# Get the user's profile
def get_user_profile(username):

    # Connection and cursor
    conn = sqlite3.connect('swipeat.db')
    c = conn.cursor()

    # Search for the profile
    c.execute('''SELECT * FROM swipeat_profiles WHERE username LIKE \'''' + username + "\'")
    #c.execute('''SELECT * FROM swipeat_profiles''')
    return c.fetchall()