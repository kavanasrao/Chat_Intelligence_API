def prompt_engine(raw_text):
    return '''
    you are an extraction engine.
    your task is to extrac the required details from the user text and return the details in dict 

    Extract the following field:
    - client_name 
    - discussion_topic
    - meeting_date
    - action_item

    Rules :

    - Return only valid Json,
    - Don't include explaition,
    - Don't include markdown,
    - if field is missing return null,
    - dont invent data,
    - use exact field provided
    - give strictly json file


    Expected Output :

    {{
    client_name,
    discussion_topic,
    meeting_date,
    action_item
    }}

    user_text

    \"\"\" {raw_text}\"\"\"
    
'''