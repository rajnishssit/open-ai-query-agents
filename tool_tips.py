import os
import json



def tool_schema()-> list:
    """
    This function defaines and returns the internal tools available for agents to use. This outlines details
    of different function, their description, input params etc. This must strictly follow tool schema requested
    by Open AI systems.
    """   

    t_schma=[
        {
            "type": "function",
            "function":
            {
                "name": "lookup_domain_info",
                "description": "This would help identfy details of company like Type of company, size of company, type of company, revenue of company.",
                "parameters":
                {
                    "type": "object",
                    "properties":
                    {
                        "domain":
                        {
                            "type": "string",
                            "description": "This is domain name of company like acmecorp.com"
                        }
                    },
                    "required": ["domain"]
                }
            }
        },
        {
            "type": "function",
            "function":
            {
                "name": "check_crm_history",
                "description": "This would help identfy details like Last contacted, additional notes, status of leads",
                "parameters":
                {
                    "type": "object",
                    "properties":
                    {
                        "email":
                        {
                            "type": "string",
                            "description": "This is email address of the person for which we want to check the crm history"
                        }
                    },
                    "required": ["email"]
                }
            }
        },
        {
            "type": "function",
            "function":
            {
                "name": "generate_crm_lead_score",
                "description": "This would help generate the final LEAD score based on status and revenue params",
                "parameters":
                {
                    "type": "object",
                    "properties":
                    {
                        "data_summary":
                        {
                            "type": "string",
                            "description": """
                            A JSON string representing an object with two keys: 
                            'domain_info' and 'crm_history'. Each value must be a JSON object.
                            """
                        }
                    },
                    "required": ["data_summary"]
                }
            }
        }
    ]
    return t_schma