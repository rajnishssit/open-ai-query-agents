import os
import json

def lookup_domain_info(domain: str) ->str:
    """
    Fetches the company information based on domain supplied to the functions. Enrichs the company data
    for helping agent make quick and concise descision.
    """

    print(f'\n-----look up domain info tool ACTIVATED for domain={domain}-----')

    # load Data from company source could be RDBMS, Excel etc
    mock_data=mock_data = {
    "northstar.example": {
        "industry": "Healthcare Technology",
        "size": "251-500 employees",
        "revenue": "$25M - $50M",
    },
    "brightpath.example": {
        "industry": "Education",
        "size": "51-100 employees",
        "revenue": "$5M - $10M",
    },
    "evergreen.example": {
        "industry": "Renewable Energy",
        "size": "1001-5000 employees",
        "revenue": "$250M - $500M",
    },
    "silverline.example": {
        "industry": "Logistics",
        "size": "501-1000 employees",
        "revenue": "$100M - $250M",
    },
    "bluepeak.example": {
        "industry": "Retail",
        "size": "100-250 employees",
        "revenue": "$10M - $25M",
    },
    "copperfield.example": {
        "industry": "Construction",
        "size": "251-500 employees",
        "revenue": "$50M - $100M",
    },
    "orbitworks.example": {
        "industry": "Aerospace",
        "size": "1001-5000 employees",
        "revenue": "$500M - $1B",
    },
    "harborstone.example": {
        "industry": "Hospitality",
        "size": "51-100 employees",
        "revenue": "$5M - $10M",
    },
    }

    return json.dumps(mock_data.get(domain, {'error': 'No information found for provided domain'}))

def check_crm_history(email: str) ->str:
    
    """
    fetches the crm history based on email address supplied to the function. Helps agent get details of 
    specific customer and enrich data for making quick descision.
    """  

    print(f'\n----- Check CRM history tool ACTIVATED for email={email}-----')

    mock_data = {
    "maria@northstar.example": {
        "last_contact": "2026-09-12",
        "status": "Qualified Lead",
        "notes": "Requested a product demo for her operations team.",
    },
    "sam@brightpath.example": {
        "last_contact": "2026-09-18",
        "status": "Follow-up Scheduled",
        "notes": "Interested in an annual plan; check back next week.",
    },
    "lee@evergreen.example": {
        "last_contact": "2026-08-29",
        "status": "Active Opportunity",
        "notes": "Reviewing the proposal with the finance team.",
    },
    "priya@silverline.example": {
        "last_contact": "2026-09-05",
        "status": "Cold Lead",
        "notes": "Met at an industry event; has not replied to the follow-up.",
    },
    "alex@bluepeak.example": {
        "last_contact": "2026-09-20",
        "status": "Active Opportunity",
        "notes": "Discussed integration requirements and implementation timing.",
    },
    "jordan@copperfield.example": {
        "last_contact": "2026-07-14",
        "status": "No Response",
        "notes": "Sent two emails after the initial discovery call.",
    },
    "taylor@orbitworks.example": {
        "last_contact": "2026-09-22",
        "status": "Closed Won",
        "notes": "Signed a one-year agreement; onboarding is scheduled.",
    },
    "default": {
        "last_contact": "N/A",
        "status": "No Record",
        "notes": "New lead, first contact opportunity.",
    }
    }
    crm_history=mock_data.get(email,mock_data['default']) 
    return json.dumps(crm_history)

def generate_crm_lead_score(data_summary: str) -> str:
    """

    Analyzes the supplied data and retuns a Lead Score based on CRM history on params like revenue, status etc

    """
    print(f'\n------ generate CRM lead score tool ACTIVATED---------')
    data = json.loads(data_summary)
    score = "Low" # Default score

    # Simple scoring logic for demonstration
    if data["domain_info"].get("revenue", "").startswith("$1B+"):
        score = "High"
    elif data["crm_history"].get("status") == "Active Opportunity":
        score = "High"
    elif data["domain_info"].get("revenue", "").startswith("$50M"):
        score = "Medium"

    return json.dumps({"lead_score": score})

def available_funcs()->dict:
    """
    This returns list of avilable functions available to the agents for use.
    """
    return {"lookup_domain_info": lookup_domain_info,
    "check_crm_history": check_crm_history,
    "generate_crm_lead_score": generate_crm_lead_score
    }

    