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

def get_attempts(mode: str):
    return DIFFICULTIES[mode]['attempts']

def get_range(mode: str):
    return DIFFICULTIES[mode]['range']
