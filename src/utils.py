import json
import os


def read_data_from_file():
    file_location = os.path.join(os.getcwd(), 'src', 'data', 'data.json')

    try:
        with open(file_location, 'r') as f:
            return json.loads(f.read())
    except (IOError, OSError) as e:
        print(f'File Opening Error!! {file_location}')
