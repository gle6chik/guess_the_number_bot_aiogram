DIFFICULTIES = {
    'easy': {
        'description': 'лёгкий',
        'attempts': 10,
        'range': 100
    },
    'medium': {
        'description': 'средний',
        'attempts': 7,
        'range': 100
    },
    'hard': {
        'description': 'сложный',
        'attempts': 10,
        'range': 1000
    }
}

def get_description(difficulty: str) -> str:
    return DIFFICULTIES[f"{difficulty}"]['description']

def get_attempts(difficulty: str) -> int:
    return DIFFICULTIES[f"{difficulty}"]['attempts']

def get_range(difficulty: str) -> int:
    return DIFFICULTIES[f"{difficulty}"]['range']
