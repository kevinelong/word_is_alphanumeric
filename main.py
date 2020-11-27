phrase = """
This phrase has a non-alpha-numeric in it.
"""

for word in phrase.split():
    if not word.isalnum():
        print(word)

"""
OUTPUT:
non-alpha-numeric
it.
"""