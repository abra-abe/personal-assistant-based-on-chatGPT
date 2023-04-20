# personal-assistant-based-on-chatGPT
This project helps to communicate with chatGPT through the use of voice commands
it uses google's speech recognition to convert speech (your voice commands) to text
and passes the text as prompts to chatGPT API then the response by chatGPT is then 
converted into sound using google's text to speech (gtts) and played using playsound
to simulate realtime voice communication between the user and chatGPT

# Using the project
in order to use the project you will have to modify a few lines of code in the main.py
but first things first make sure that you have an openai account then generate an API key
you can follow this link to generate the API key https://platform.openai.com/account/api-keys
after generating the key and copying it, go to main.py and comment out the following lines of code

      from dotenv import load_dotenv
      /
      /
      /
      load_dotenv()
  
  then in line number 10 delete 'os.getenv('API-KEY')' and replace it with the API key you have generated
  therefore it will appear as follows:
    
      openai.api_key = " your api key "
     
  after modifying the file main.py save it and then install the required libraries such as speech recognition
  gtts, openai and playsound you can install these atomatically by running the file requirements.py.
  After running the file requirements.py the neccessary libraries will be installed now you can run main.py
  feel free to modify the code to fit your needs as you please....
