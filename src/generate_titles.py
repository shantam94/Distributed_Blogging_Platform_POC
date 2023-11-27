import random

def generate_random_title():
    adjectives = ["Amazing", "Mysterious", "Incredible", "Fantastic", "Magical"]
    nouns = ["Journey", "Adventure", "Story", "Life", "Secret"]
    themes = ["in the Mountains", "of the Ancient World", "Beyond the Stars", "Under the Sea", "in the Future"]

    # Randomly select one word from each list
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    theme = random.choice(themes)

    # Combine the words to form a title
    title = f"{adjective} {noun} {theme}"

    return title

# Generate a random title
random_title = generate_random_title()
# print(random_title)
