from gtts import gTTS 
import random


words = ['hello', 'hi', 'how are you?', 'thanks', 'salam', 'necesen Joseph?']


randomWord = random.choice(words)
tts = gTTS(text=randomWord, lang='tr')

tts.save('001.mp3')