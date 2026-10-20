import os
import json
from openai import OpenAI
from connect_openai import *
from tool_tips import *

from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).with_name("config.env"))


def get_crm_score_agent(prompt: str) -> str:
    
    """
    This function is helpful in returning the CRM lead score based on domain of a company and email address.
    """
    system_prompt="""
    You are an Helpful AI Assistant. Your Sole tak is to analyze the data and  generate the Lead score of a company based on supplied email Address.
    You can use below instruction to analyze the data and generate the lead score. You can also provide consize summary of 2-5 sentences.

    1. Identify the domain from the supplied email address of a contact from our CRM system. e.g. email address=maria@northstar.example domain is northstar.example
    2. Call 'lookup_domain_info' and 'check_crm_history' functions sequentially to gather company and contact information.
    3. Combile all data into single Json Object using your own segregattion.
    4. Call 'generate_crm_lead_score' function to generate final lead score based on combined data.
    5. Finally synthesize the lead  score based on all the data gathered in previous steps and provide a lead score
       along with a concise summary of 2-5 sentences.

    """
    #Pass available functions
    available_functions=available_funcs()

    ## pass tool schema to the model so that it can use the tool to gather data and generate lead score.
    tools_schema=tool_schema()

    client=connect_openai()
    model='gpt-4o-mini'
    message=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': prompt}
            ]
    collected_data={}        
    if(client is not None):
        ## Agent loop to gather data and generate lead score
        while True:
            print(f'\n---- Agent is Thinking and Analyzing')
            response=client.chat.completions.create(
                model=model,
                messages=message,
                tools=tools_schema,
                tool_choice='auto',
            )
            response_text=response.choices[0].message
            message.append(response_text)
            if response_text.tool_calls:
                tool_calls=response_text.tool_calls
                for tool_call in tool_calls:
                    function_name=tool_call.function.name   ## get which next function to call
                    function_to_call=available_functions.get(function_name)   ## check is functions is valid as per available functions or not
                    function_args=json.loads(tool_call.function.arguments)   ## get the function arcguments



                    ## check if valid functio or not
                    if function_to_call is None:
                        print(f'\n ----- INvalid function name {function_name} called by model. Please check the function name and try again')
                        continue
                    ## Execute the fundtion
                    print(f' function name={function_name} and function to call={function_to_call} and function args={function_args}')
                    

                    if(function_name=='lookup_domain_info'):
                        function_result=function_to_call(**function_args) 
                        collected_data['domain_info']=json.loads(function_result)
                    elif(function_name=='check_crm_history'):
                        function_result=function_to_call(**function_args)
                        collected_data['crm_history']=json.loads(function_result)
                    elif(function_name=='generate_crm_lead_score'):
                        function_args={'data_summary': json.dumps(collected_data)}
                        function_result=function_to_call(**function_args)

                    ## Append the tool result as new message
                    message.append(
                        {
                            'role': 'tool',
                            'tool_call_id': tool_call.id,
                            'name': function_name,
                            'content': function_result
                        }
                    )    
            else:
                print(f'Final summary from agent={response_text.content}')
                break

print(f'{get_crm_score_agent('Help me get the lead score for sam@brightpath.example')}')






