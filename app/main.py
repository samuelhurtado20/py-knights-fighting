from app.models.knight import Knight

knights_config = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}

def battle(knights_config: dict) -> dict:
    # Instanciar a todos los caballeros usando un diccionario por comprensión
    knights = {
        key: Knight(config)
        for key, config in knights_config.items()
    }

    # Definir los combatientes para mayor claridad y menor complejidad
    pairs = [
        (knights["lancelot"], knights["mordred"]),
        (knights["arthur"], knights["red_knight"])
    ]

    # Ejecutar los ataques
    for knight_a, knight_b in pairs:
        # Ataque simultáneo
        hp_a_pre = knight_a.power
        hp_b_pre = knight_b.power
        
        knight_a.receive_damage(hp_b_pre)
        knight_b.receive_damage(hp_a_pre)

    # Devolver el formato exacto que espera el test
    return {
        k.name: k.hp for k in knights.values()
    }


print(battle(KNIGHTS))
