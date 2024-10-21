# ---------------------- JSON NATURES ----------------
nature_1 = {
    "id": 1,
    "nombre": "hardy",
    "aumenta_estadistica": "attack",
    "reduce_estadistica": "attack",
}

nature_2 = {
    "id": 2,
    "nombre": "bold",
    "aumenta_estadistica": "defense",
    "reduce_estadistica": "attack",
}
nature_3 = {
    "id": 3,
    "nombre": "modest",
    "aumenta_estadistica": "special-attack",
    "reduce_estadistica": "attack",
}
# ----------------- JSONS EQUIPOS --------------------------------
equipo_con_6_pokemons = {
    "id_equipo": 1,
    "nombre": "Equipo Elite",
    "pokemons_de_equipo": [
        {
            "id": 25,
            "nombre": "Pikachu",
            "naturaleza": {
                "id": 1,
                "nombre": "Activa",
                "aumenta_estadistica": "Velocidad",
                "reduce_estadistica": "Defensa",
            },
            "movimientos": [
                {
                    "id": 1,
                    "nombre": "Impactrueno",
                    "tipo": "Eléctrico",
                    "power": 40,
                    "accuracy": 100,
                    "pp": 30,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Parálisis",
                    "probabilidad_efecto": 10,
                },
                {
                    "id": 2,
                    "nombre": "Rayo",
                    "tipo": "Eléctrico",
                    "power": 90,
                    "accuracy": 100,
                    "pp": 15,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Parálisis",
                    "probabilidad_efecto": 10,
                },
            ],
        },
        {
            "id": 6,
            "nombre": "Charizard",
            "naturaleza": {
                "id": 2,
                "nombre": "Audaz",
                "aumenta_estadistica": "Ataque",
                "reduce_estadistica": "Defensa",
            },
            "movimientos": [
                {
                    "id": 3,
                    "nombre": "Llamarada",
                    "tipo": "Fuego",
                    "power": 110,
                    "accuracy": 85,
                    "pp": 5,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Quemadura",
                    "probabilidad_efecto": 30,
                }
            ],
        },
        {
            "id": 9,
            "nombre": "Blastoise",
            "naturaleza": {
                "id": 3,
                "nombre": "Modesta",
                "aumenta_estadistica": "Ataque Especial",
                "reduce_estadistica": "Ataque",
            },
            "movimientos": [
                {
                    "id": 4,
                    "nombre": "Hidrobomba",
                    "tipo": "Agua",
                    "power": 110,
                    "accuracy": 80,
                    "pp": 5,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 3,
            "nombre": "Venusaur",
            "naturaleza": {
                "id": 4,
                "nombre": "Serena",
                "aumenta_estadistica": "Defensa Especial",
                "reduce_estadistica": "Ataque",
            },
            "movimientos": [
                {
                    "id": 5,
                    "nombre": "Solar Rayo",
                    "tipo": "Planta",
                    "power": 120,
                    "accuracy": 100,
                    "pp": 10,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 94,
            "nombre": "Gengar",
            "naturaleza": {
                "id": 5,
                "nombre": "Miedosa",
                "aumenta_estadistica": "Velocidad",
                "reduce_estadistica": "Defensa",
            },
            "movimientos": [
                {
                    "id": 6,
                    "nombre": "Bola Sombra",
                    "tipo": "Fantasma",
                    "power": 80,
                    "accuracy": 100,
                    "pp": 15,
                    "generacion": "II",
                    "categoria": "Especial",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 149,
            "nombre": "Dragonite",
            "naturaleza": {
                "id": 6,
                "nombre": "Firme",
                "aumenta_estadistica": "Ataque",
                "reduce_estadistica": "Defensa Especial",
            },
            "movimientos": [
                {
                    "id": 7,
                    "nombre": "Puño Fuego",
                    "tipo": "Fuego",
                    "power": 100,
                    "accuracy": 100,
                    "pp": 15,
                    "generacion": "II",
                    "categoria": "Físico",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
    ],
}
equipo_siete_pokemons = {
    "id_equipo": 2,
    "nombre": "Equipo Sobrecargado",
    "pokemons_de_equipo": [
        {
            "id": 25,
            "nombre": "Pikachu",
            "naturaleza": {
                "id": 1,
                "nombre": "Activa",
                "aumenta_estadistica": "Velocidad",
                "reduce_estadistica": "Defensa",
            },
            "movimientos": [
                {
                    "id": 1,
                    "nombre": "Impactrueno",
                    "tipo": "Eléctrico",
                    "power": 40,
                    "accuracy": 100,
                    "pp": 30,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Parálisis",
                    "probabilidad_efecto": 10,
                }
            ],
        },
        {
            "id": 6,
            "nombre": "Charizard",
            "naturaleza": {
                "id": 2,
                "nombre": "Audaz",
                "aumenta_estadistica": "Ataque",
                "reduce_estadistica": "Defensa",
            },
            "movimientos": [
                {
                    "id": 3,
                    "nombre": "Llamarada",
                    "tipo": "Fuego",
                    "power": 110,
                    "accuracy": 85,
                    "pp": 5,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Quemadura",
                    "probabilidad_efecto": 30,
                }
            ],
        },
        {
            "id": 9,
            "nombre": "Blastoise",
            "naturaleza": {
                "id": 3,
                "nombre": "Modesta",
                "aumenta_estadistica": "Ataque Especial",
                "reduce_estadistica": "Ataque",
            },
            "movimientos": [
                {
                    "id": 4,
                    "nombre": "Hidrobomba",
                    "tipo": "Agua",
                    "power": 110,
                    "accuracy": 80,
                    "pp": 5,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 3,
            "nombre": "Venusaur",
            "naturaleza": {
                "id": 4,
                "nombre": "Serena",
                "aumenta_estadistica": "Defensa Especial",
                "reduce_estadistica": "Ataque",
            },
            "movimientos": [
                {
                    "id": 5,
                    "nombre": "Solar Rayo",
                    "tipo": "Planta",
                    "power": 120,
                    "accuracy": 100,
                    "pp": 10,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 94,
            "nombre": "Gengar",
            "naturaleza": {
                "id": 5,
                "nombre": "Miedosa",
                "aumenta_estadistica": "Velocidad",
                "reduce_estadistica": "Defensa",
            },
            "movimientos": [
                {
                    "id": 6,
                    "nombre": "Bola Sombra",
                    "tipo": "Fantasma",
                    "power": 80,
                    "accuracy": 100,
                    "pp": 15,
                    "generacion": "II",
                    "categoria": "Especial",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 149,
            "nombre": "Dragonite",
            "naturaleza": {
                "id": 6,
                "nombre": "Firme",
                "aumenta_estadistica": "Ataque",
                "reduce_estadistica": "Defensa Especial",
            },
            "movimientos": [
                {
                    "id": 7,
                    "nombre": "Puño Fuego",
                    "tipo": "Fuego",
                    "power": 100,
                    "accuracy": 100,
                    "pp": 15,
                    "generacion": "II",
                    "categoria": "Físico",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 4,
            "nombre": "Gyarados",
            "naturaleza": {
                "id": 7,
                "nombre": "Bashful",
                "aumenta_estadistica": "Defensa",
                "reduce_estadistica": "Ataque",
            },
            "movimientos": [
                {
                    "id": 8,
                    "nombre": "Tierra",
                    "tipo": "Tierra",
                    "power": 80,
                    "accuracy": 100,
                    "pp": 15,
                    "generacion": "IV",
                    "categoria": "Físico",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
    ],
}
equipo_mismo_id = {
    "id_equipo": 1,
    "nombre": "Equipo Filete",
    "pokemons_de_equipo": [
        {
            "id": 25,
            "nombre": "Pikachu",
            "naturaleza": {
                "id": 1,
                "nombre": "Activa",
                "aumenta_estadistica": "Velocidad",
                "reduce_estadistica": "Defensa",
            },
            "movimientos": [
                {
                    "id": 1,
                    "nombre": "Impactrueno",
                    "tipo": "Eléctrico",
                    "power": 40,
                    "accuracy": 100,
                    "pp": 30,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Parálisis",
                    "probabilidad_efecto": 10,
                },
                {
                    "id": 2,
                    "nombre": "Rayo",
                    "tipo": "Eléctrico",
                    "power": 90,
                    "accuracy": 100,
                    "pp": 15,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Parálisis",
                    "probabilidad_efecto": 10,
                },
            ],
        },
        {
            "id": 6,
            "nombre": "Charizard",
            "naturaleza": {
                "id": 2,
                "nombre": "Audaz",
                "aumenta_estadistica": "Ataque",
                "reduce_estadistica": "Defensa",
            },
            "movimientos": [
                {
                    "id": 3,
                    "nombre": "Llamarada",
                    "tipo": "Fuego",
                    "power": 110,
                    "accuracy": 85,
                    "pp": 5,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Quemadura",
                    "probabilidad_efecto": 30,
                }
            ],
        },
        {
            "id": 9,
            "nombre": "Blastoise",
            "naturaleza": {
                "id": 3,
                "nombre": "Modesta",
                "aumenta_estadistica": "Ataque Especial",
                "reduce_estadistica": "Ataque",
            },
            "movimientos": [
                {
                    "id": 4,
                    "nombre": "Hidrobomba",
                    "tipo": "Agua",
                    "power": 110,
                    "accuracy": 80,
                    "pp": 5,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 3,
            "nombre": "Venusaur",
            "naturaleza": {
                "id": 4,
                "nombre": "Serena",
                "aumenta_estadistica": "Defensa Especial",
                "reduce_estadistica": "Ataque",
            },
            "movimientos": [
                {
                    "id": 5,
                    "nombre": "Solar Rayo",
                    "tipo": "Planta",
                    "power": 120,
                    "accuracy": 100,
                    "pp": 10,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 94,
            "nombre": "Gengar",
            "naturaleza": {
                "id": 5,
                "nombre": "Miedosa",
                "aumenta_estadistica": "Velocidad",
                "reduce_estadistica": "Defensa",
            },
            "movimientos": [
                {
                    "id": 6,
                    "nombre": "Bola Sombra",
                    "tipo": "Fantasma",
                    "power": 80,
                    "accuracy": 100,
                    "pp": 15,
                    "generacion": "II",
                    "categoria": "Especial",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 149,
            "nombre": "Dragonite",
            "naturaleza": {
                "id": 6,
                "nombre": "Firme",
                "aumenta_estadistica": "Ataque",
                "reduce_estadistica": "Defensa Especial",
            },
            "movimientos": [
                {
                    "id": 7,
                    "nombre": "Puño Fuego",
                    "tipo": "Fuego",
                    "power": 100,
                    "accuracy": 100,
                    "pp": 15,
                    "generacion": "II",
                    "categoria": "Físico",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
    ],
}
equipo = {
    "id_equipo": 2,
    "nombre": "Equipo Elite",
    "pokemons_de_equipo": [
        {
            "id": 25,
            "nombre": "Pikachu",
            "naturaleza": {
                "id": 1,
                "nombre": "Activa",
                "aumenta_estadistica": "Velocidad",
                "reduce_estadistica": "Defensa",
            },
            "movimientos": [
                {
                    "id": 1,
                    "nombre": "Impactrueno",
                    "tipo": "Eléctrico",
                    "power": 40,
                    "accuracy": 100,
                    "pp": 30,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Parálisis",
                    "probabilidad_efecto": 10,
                },
                {
                    "id": 2,
                    "nombre": "Rayo",
                    "tipo": "Eléctrico",
                    "power": 90,
                    "accuracy": 100,
                    "pp": 15,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Parálisis",
                    "probabilidad_efecto": 10,
                },
            ],
        },
        {
            "id": 6,
            "nombre": "Charizard",
            "naturaleza": {
                "id": 2,
                "nombre": "Audaz",
                "aumenta_estadistica": "Ataque",
                "reduce_estadistica": "Defensa",
            },
            "movimientos": [
                {
                    "id": 3,
                    "nombre": "Llamarada",
                    "tipo": "Fuego",
                    "power": 110,
                    "accuracy": 85,
                    "pp": 5,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Quemadura",
                    "probabilidad_efecto": 30,
                }
            ],
        },
        {
            "id": 9,
            "nombre": "Blastoise",
            "naturaleza": {
                "id": 3,
                "nombre": "Modesta",
                "aumenta_estadistica": "Ataque Especial",
                "reduce_estadistica": "Ataque",
            },
            "movimientos": [
                {
                    "id": 4,
                    "nombre": "Hidrobomba",
                    "tipo": "Agua",
                    "power": 110,
                    "accuracy": 80,
                    "pp": 5,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 3,
            "nombre": "Venusaur",
            "naturaleza": {
                "id": 4,
                "nombre": "Serena",
                "aumenta_estadistica": "Defensa Especial",
                "reduce_estadistica": "Ataque",
            },
            "movimientos": [
                {
                    "id": 5,
                    "nombre": "Solar Rayo",
                    "tipo": "Planta",
                    "power": 120,
                    "accuracy": 100,
                    "pp": 10,
                    "generacion": "I",
                    "categoria": "Especial",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 94,
            "nombre": "Gengar",
            "naturaleza": {
                "id": 5,
                "nombre": "Miedosa",
                "aumenta_estadistica": "Velocidad",
                "reduce_estadistica": "Defensa",
            },
            "movimientos": [
                {
                    "id": 6,
                    "nombre": "Bola Sombra",
                    "tipo": "Fantasma",
                    "power": 80,
                    "accuracy": 100,
                    "pp": 15,
                    "generacion": "II",
                    "categoria": "Especial",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
        {
            "id": 149,
            "nombre": "Dragonite",
            "naturaleza": {
                "id": 6,
                "nombre": "Firme",
                "aumenta_estadistica": "Ataque",
                "reduce_estadistica": "Defensa Especial",
            },
            "movimientos": [
                {
                    "id": 7,
                    "nombre": "Puño Fuego",
                    "tipo": "Fuego",
                    "power": 100,
                    "accuracy": 100,
                    "pp": 15,
                    "generacion": "II",
                    "categoria": "Físico",
                    "efecto": "Ninguno",
                    "probabilidad_efecto": None,
                }
            ],
        },
    ],
}

# ------------------------ JSONS POKEMONS -----------------------------
infernape_mock = {
    "pokemon_id": 392,
    "nombre": "infernape",
    "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/392.png",
    "tipos": ["Lucha", "Fuego"],
    "habilidades": ["Mar Llamas", "Puño Férreo"],
    "altura": 12,
    "peso": 550,
    "estadisticas": {
        "hp": 76,
        "attack": 104,
        "defense": 71,
        "special-attack": 104,
        "special-defense": 71,
        "speed": 108,
        "accuracy": 0,
        "evasion": 0,
    },
    "cadena_evolutiva": [390, 391, 392],
}
