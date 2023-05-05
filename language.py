languages = {
'pt-BR': 'Portuguese (Brazil)',
'en-US': 'English (United States)',
'es-ES': 'Spanish (Spain)',
'fr-FR': 'French (France)',
'pt-PT': 'Portuguese (Portugal)',
'en-GB': 'English (United Kingdom)',
'en-CA': 'English (Canada)',
'pt-AO': 'Portuguese (Angola)',
'pt-MZ': 'Portuguese (Mozambique)',
'pt-GW': 'Portuguese (Guinea-Bissau)',
'en-AU': 'English (Australia)',
'en-NZ': 'English (New Zealand)',
'en-ZA': 'English (South Africa)',
'de-DE': 'German (Germany)',
'ja-JP': 'Japanese (Japan)'
}

def code():
    print('Select the language:')
    for code, name in languages.items():
        print(f'{code} [{name}]')

    print('')
    select_code = input('Enter the language code: ')

    if select_code in languages:
        print(f'Selected language: {languages[select_code]}')
        print('')
        return select_code
    else:
        print('Invalid language code.')
