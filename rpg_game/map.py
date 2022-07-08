"""Alta 3 RPG Final Project
   Patrick Haggerty"""

ship = {

    'Bridge': {
        'description': 'Where the ship is operated from, also known as the pilothouse. It is eerily empty and quiet.',
        'items': '',
        'enemies': 'Big Alien',
        'aft': 'Main Passageway'
    },

    'Main Passageway': {
        'description': 'A long passageway with doors on all sides. The bulkheads have lots of pipes, wires, and damage control equipment.',
        'items': '',
        'enemies': '',
        'forward': 'Bridge',
        'aft': 'Aft Passageway',
        'port': 'Port Passageway',
        'starboard': 'Starboard Passageway'
    },

    'Aft Passageway': {
        'description': 'A short passageway with doors on all sides.',
        'items': '',
        'enemies': 'Small Alien',
        'forward': 'Main Passageway',
        'aft': 'Engine Room',
        'port': 'Armory',
        'starboard': 'Storage Room'
    },

    'Engine Room': {
        'description': 'A large engine room filled with machinery, and loud mechanical noises of whirring and humming.',
        'items': '',
        'enemies': 'Small Alien',
        'forward': 'Aft Passageway'
    },

    'Armory': {
        'description': 'The armory of the ship, filled with all kinds of useful weapons and tools.',
        'items': '',
        'enemies': '',
        'starboard': 'Aft Passageway'
    },

    'Storage Room': {
        'description': 'A large room with shelves filled with parts and supplies.',
        'items': '',
        'enemies': '',
        'port': 'Aft Passageway'
    },

    'Starboard Passageway': {
        'description': 'A short passageway with doors on three sides.',
        'items': '',
        'enemies': '',
        'forward': 'Crew Quarters #1',
        'port': 'Main Passageway',
        'starboard': 'Crew Quarters #2'
    },

    'Crew Quarters #1': {
        'description': 'A large sleeping quarters crammed with lockers and beds for the enlisted crew.',
        'items': '',
        'enemies': 'Small Alien',
        'aft': 'Starboard Passageway'
    },

    'Crew Quarters #2': {
        'description': 'A small sleeping quarters with just a few lockers and beds for the officers of the ship.',
        'items': '',
        'enemies': '',
        'port': 'Starboard Passageway',
    },

    'Port Passageway': {
        'description': 'A short passageway with doors on three sides.',
        'items': '',
        'enemies': '',
        'forward': 'Galley',
        'port': 'Mess Decks',
        'starboard': 'Main Passageway'
    },

    'Galley': {
        'description': 'A large kitchen with appliances for cooking food everywhere.',
        'items': '',
        'enemies': 'Big Alien',
        'aft': 'Port Passageway',
    },

    'Mess Decks': {
        'description': 'A large room filled with tables and chairs where the crew eats and socializes.',
        'items': '',
        'enemies': '',
        'starboard': 'Port Passageway'
    },
}
