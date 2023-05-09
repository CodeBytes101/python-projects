#Download the openai library with command 'pip install openai'
import openai
import sys
from time import sleep

#Get your api key from your openai account on 'platform/openai.com'
#Create the file and storing your api key in it

#Read your api key from the file and store it in the 'openai.api_key'
openai.api_key = open(r'C:\Users\rosha\Downloads\api.txt','r').read()

#For experience of chat embed the code in infinte loop
while 1:
    response = openai.ChatCompletion.create(
        # we need to specify the model we want to use in this case we our using 'gpt-3.5-turbo'
        model='gpt-3.5-turbo',
        # messages will take list of Dictonary
        messages = [{
            'role':'user',
            'content':str(input('>> '))
        }]

    )
    # To fetch the exact answer from response
    reply = str((dict(((response['choices'])[0])['message']))['content'])
    
    # For Type Writer Effect itterate the reply in loop
    for char in reply:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    print( )
