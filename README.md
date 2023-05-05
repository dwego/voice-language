# Language Translation
This program allows the user to select a language and returns the name of the language in their chosen language.

# Installation
Clone the repository
bash
```
git clone https://github.com/dwego/voice-language.git
````
Install required packages
```
pip install pyaudio, wave, speech_recognition, googletrans, openai, os, pyttsx3
```
# Create an OpenAI API key here

Replace the OPENAI_API_KEY variable in the main.py file with your OpenAI API key.

# Usage
Run the language.py file
```python
python language.py
```
Select a language by entering its code when prompted. The available languages and their codes are displayed on screen.

The program will return the name of the selected language in the user's chosen language.

# Languages
The following languages are supported by this program:

- Portuguese (Brazil) - pt-BR
- English (United States) - en-US
- Spanish (Spain) - es-ES
- French (France) - fr-FR
- Portuguese (Portugal) - pt-PT
- English (United Kingdom) - en-GB
- English (Canada) - en-CA
- Portuguese (Angola) - pt-AO
- Portuguese (Mozambique) - pt-MZ
- Portuguese (Guinea-Bissau) - pt-GW
- English (Australia) - en-AU
- English (New Zealand) - en-NZ
- English (South Africa) - en-ZA
- German (Germany) - de-DE
- Japanese (Japan) - ja-JP
# API Key
To use this program, you must have an OpenAI API key. You can create an API key by signing up for the OpenAI beta <a href="https://platform.openai.com/account/api-keys">here</a>. Once you have your API key, replace the OPENAI_API_KEY variable in the language.py file with your key.

# License
This program is licensed under the MIT License.
