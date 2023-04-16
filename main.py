from dotenv import load_dotenv
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import openai

load_dotenv()

# openai.api_key = os.getenv('API_KEY')
openai.api_key = "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"

welcomeText = "welcome, my name is monica, I am your personal assistant based on chatGPT, ask me anything"
line1 = welcomeText

if line1 != " ":
    speech1 = gTTS(text=line1, lang="en", slow=False, tld="com")
    speech1.save("welcome.mp3")
        
playsound("welcome.mp3")

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("say something...")

        audio = r.listen(source)

        try:
            print("you have said: \n" + r.recognize_google(audio))

        except Exception as e:
            print("error: " + str(e))

        with open("recorded_text.txt", "w") as f:
            f.write(r.recognize_google(audio))


if __name__ == "__main__":
    main()

audio_file = open("recorded_text.txt", "r")
prompt = [
     audio_file.read(),
     "what is your name?\n\nAnswer: Monica"
]
model = "text-davinci-002" # Replace with the name of the model you want to use
completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1000)
message = completions.choices[0].text.strip()

#extracting the name
name = message.split("Answer: ")[-1]
print(message)

line2 = message

if line2 != " ":
        speech2 = gTTS(text=line2, lang='en', slow=False, tld="com")
        speech2.save("gpt_ans.mp3")

playsound("gpt_ans.mp3")

textFile = open("gpt_ans.txt", "w")
textFile.write(message)