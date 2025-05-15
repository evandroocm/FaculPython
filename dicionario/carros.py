carros = {
    'Polo': {
        'km': 35000,
        'ano': 2018,
        'cor': 'azul',
        'modelo': 'Hatch',
        'potencia': '128 cv',
        'combustivel': 'Flex',
        'cambio': 'Automático'
    },
    'Civic': {
        'km': 45000,
        'ano': 2020,
        'cor': 'preto',
        'modelo': 'Sedan',
        'potencia': '155 cv',
        'combustivel': 'Gasolina',
        'cambio': 'Automático'
    },
    'Corolla': {
        'km': 38000,
        'ano': 2019,
        'cor': 'branco',
        'modelo': 'Sedan',
        'potencia': '177 cv',
        'combustivel': 'Híbrido',
        'cambio': 'CVT'
    },
    'Compass': {
        'km': 29000,
        'ano': 2021,
        'cor': 'cinza',
        'modelo': 'SUV',
        'potencia': '170 cv',
        'combustivel': 'Diesel',
        'cambio': 'Automático'
    },
    'Onix': {
        'km': 15000,
        'ano': 2022,
        'cor': 'vermelho',
        'modelo': 'Hatch',
        'potencia': '116 cv',
        'combustivel': 'Flex',
        'cambio': 'Manual'
    },
    'HR-V': {
        'km': 22000,
        'ano': 2021,
        'cor': 'prata',
        'modelo': 'SUV',
        'potencia': '140 cv',
        'combustivel': 'Gasolina',
        'cambio': 'Automático'
    }
}

print(carros.get('Civic', 'veiculo nao encontrado'))