DIFFICULTIES = {
    'easy': {
        'attempts': 10,
        'range': 100
    },
    'medium': {
        'attempts': 7,
        'range': 100
    },
    'difficult': {
        'attempts': 12,
        'range': 1000
    }
}

def get_attempts(difficulty: str) -> int:
    return DIFFICULTIES[f"{difficulty}"]['attempts']

def get_range(difficulty: str) -> int:
    return DIFFICULTIES[f"{difficulty}"]['range']
