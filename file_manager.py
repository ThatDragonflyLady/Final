import json
import os

def save_data(filename, data):
    # Handles both dictionary saving and object-list saving structures safely
    with open(filename, 'w') as f:
        if isinstance(data, dict):
            # If data is a dictionary, check if the values are objects with to_dict
            serialized = {k: (v.to_dict() if hasattr(v, 'to_dict') else v) for k, v in data.items()}
        else:
            # Fallback for standard lists
            serialized = [obj.to_dict() if hasattr(obj, 'to_dict') else obj for obj in data]
        json.dump(serialized, f, indent=4)

def load_data(filename, model_class=None):
    # Check if the file is missing or completely empty (0 bytes)
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        return {}

    try:
        with open(filename, 'r') as f:  
            raw_data = json.load(f) 
            
            if model_class is None:
                return raw_data
            
            # Rebuild dictionaries or lists safely based on the JSON structure
            if isinstance(raw_data, dict):
                return {k: model_class(**v) if isinstance(v, dict) else v for k, v in raw_data.items()}
            else:
                return [model_class(**item) for item in raw_data] 
                
    except (json.JSONDecodeError, ValueError):
        # Catch bad formatting/corrupted lines and return an empty dictionary safely
        print(f"Warning: '{filename}' was corrupted. Resetting data structure.")
        return {}
