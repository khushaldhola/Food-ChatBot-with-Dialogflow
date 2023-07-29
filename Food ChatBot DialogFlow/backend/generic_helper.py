import re

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result
def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""

# if __name__ == "__main__":
#     print(extract_session_id("projects/mira-chatbot-vabo/agent/sessions/f62c380f-9148-a984-913e-96513e639f87/contexts/ongoing-order"))