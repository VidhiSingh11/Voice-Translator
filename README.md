# Voice-Translator
The Voice Translator is designed to convert spoken language into  written text and then translate it into the user's desired language. The project  utilizes various Python libraries, such as SpeechRecognition, googletrans, gtts,  pygame, and os, to achieve this functionality. Functionality: 
1. Speech Recognition:
 - The project uses the SpeechRecognition library to capture audio input from 
the user's microphone. 
 - The function `take_command()` is responsible for recording the user's voice 
input and converting it into text using Google's speech recognition API. 
 - The recognized text is printed as the user's spoken command. 
2. Language Selection:
 - The project allows the user to select the language in which they want to 
translate their voice command. 
 - The function `destination_language()` prompts the user to enter their desired 
language. 
 - The input language is converted to lowercase and checked against the 
dictionary of available languages. 
 - If the language is not available, the user is prompted to enter another 
language. 
3. Translation and Text-to-Speech: 
 - The googletrans library is used for language translation. 
 - The user's voice command is translated into the desired language using the 
`translate()` function from the Translator class. 
 - The translated text is then converted into speech using the gTTS (Google 
Text-to-Speech) library. 
 - The generated speech is saved as an audio file named 
"captured_JTP_voice.mp3". 
4. Audio Playback: 
 - The pygame library is used for playing the generated audio file. 
 - The audio file is loaded and played using the pygame.mixer.music module. 
 - The program waits for the audio playback to finish before proceeding. 
5. Cleanup: 
 - Once the audio playback is complete, the pygame.mixer is stopped, and the 
audio file "captured_JTP_voice.mp3" is removed from the system. 
