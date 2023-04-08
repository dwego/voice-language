linguagens = {
    'pt-BR': 'Português (Brasil)',
    'en-US': 'Inglês (Estados Unidos)',
    'es-ES': 'Espanhol (Espanha)',
    'fr-FR': 'Francês (França)',
    'pt-PT': 'Português (Portugal)',
    'en-GB': 'Inglês (Reino Unido)',
    'en-CA': 'Inglês (Canadá)',
    'pt-AO': 'Português (Angola)',
    'pt-MZ': 'Português (Moçambique)',
    'pt-GW': 'Português (Guiné-Bissau)',
    'en-AU': 'Inglês (Austrália)',
    'en-NZ': 'Inglês (Nova Zelândia)',
    'en-ZA': 'Inglês (África do Sul)',
    'de-DE': 'Alemão (Alemanha)',
    'ja-JP': 'Japonês (Japão)'
}

print('Selecione o idioma:')
for codigo, nome in linguagens.items():
    print(f'{codigo} [{nome}]')

print('')
codigo_selecionado = input('Digite o código do idioma desejado: ')

if codigo_selecionado in linguagens:
    print(f'Idioma selecionado: {linguagens[codigo_selecionado]}')
    print('')
else:
    print('Código de idioma inválido.')