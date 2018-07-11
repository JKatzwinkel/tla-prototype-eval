import webd.settings

import json

with open(webd.settings.CORPUS_OBJECT_MAPPING_FILE, 'r') as f:
    display_field_mappings = json.load(f)
    f.close()

