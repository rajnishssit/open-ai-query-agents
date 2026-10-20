import os
from connect_openai import *


def main():
    """
    This function helps you connect with open ai and other models and return response
    """

    input_text=input("which AI provider would you like to use? 1=OpenAI, 2=OpenRouter")
    if(input_text=="1"):
        client=connect_openai()
        if(client is not None):
            prompt=input("Please let me know!! How may i help you today?   ")
            print(f'Response from Open AI= {query_openai(prompt,client)}')
    elif(input_text=='2'):
        client=connect_openrouter()
        if(client is not None):
            prompt=input("Please let me know!! How may i help you today?  ")
            print(f'Open router response={query_openrouter(prompt,client)}')
    else:
        print(f'Invalid selection. Please select either 1 or 2')  
        return None      
def query_openai(prompt,client):
    
    try:
        response=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an Helpful AI Assistant"},
                {"role": "user", "content": prompt}],
            temperature=0.7
        )
        reponse_text=response.choices[0].message.content
        return reponse_text
    except Exception as e:
        print(f'Exception cocured while querying open ai: {e}')
        return None
def query_openrouter(prompt,client):
    try:
        response=client.chat.completions.create(
            model='gpt-40-mini',
            messages=[
                {'role','system','content': 'You are very helpful AI Assistant'},
                {'role': 'user', 'content': prompt}

            }],
            temperature=0.7
        )
        response_text=response.choices[0].message.content
        return response_text
    except Exception as e:
        print(f'Exception while connecting with open router: {e}')
        return None    
if __name__ == "__main__":
    main()