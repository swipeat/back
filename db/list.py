#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Nils Schaetti <n.schaetti@gmail.com>
# @date: Fri 11 Feb

import sqlite3

# Get the complete list of the ingredient
def get_list(username):
    """ Get the complete list of the ingredient """

    # Connection and cursor
    conn = sqlite3.connect('swipeat.db')
    c = conn.cursor()

    # Search for the ingredient
    c.execute('''SELECT * FROM swipeat_lists WHERE username like \'''' + username + "\'")
    return c.fetchall()

# Remove ingredient from the list
def remove_ingredient(username, ingredient):
    """ Remove ingredient from the list """

    # Connection and cursor
    conn = sqlite3.connect('swipeat.db')
    c = conn.cursor()

    # Remove
    c.execute('''DELETE FROM swipeat_lists WHERE username like \'''' + username + '''\' AND ingredient like \'''' + ingredient + "\'")
    conn.commit()

# Remove all ingredients from the list
def purge_list(username):
    """ Remove all ingredients from the list """

    # Connection and cursor
    conn = sqlite3.connect('swipeat.db')
    c = conn.cursor()

    # Remove all
    c.execute('''DELETE FROM swipeat_lists WHERE username LIKE \'''' + username + "\'")
    conn.commit()

# Is an ingredient in the list
def is_in_list(username, ingredient):
    """
    Is an ingredient in the user's list?
    :param username: User's name
    :param ingredient: Ingredient to test
    :return: Yes or no
    """

    # Connection and cursor
    conn = sqlite3.connect('swipeat.db')
    c = conn.cursor()

    # Search for the ingredient
    c.execute('''SELECT * FROM swipeat_lists WHERE username like \'''' + username + '''\' AND ingredient LIKE \'''' + ingredient + "\'")
    rows = c.fetchall()

    # Check results
    if len(rows) > 0:
        return True
    else:
        return False


# Add an ingredient to the list
def add_ingredient(username, ingredient):
    """
    An an ingredient to the user's list
    :param username: User's name
    :param ingredient: Ingredient to add
    :return: Nothing
    """

    # If not existing
    if not is_in_list(username, ingredient):
        # Connection and cursor
        conn = sqlite3.connect('swipeat.db')
        c = conn.cursor()

        # Add the ingredient
        c.execute('''INSERT INTO swipeat_lists(username, ingredient) VALUES(:username,:ingredient)''', {'username': username, 'ingredient': ingredient})
        conn.commit()