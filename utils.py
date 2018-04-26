from datetime import datetime

simple_data_types = {
    "datetime": datetime(2018, 4, 26),
    "string": "TEST STRING",
    "int": 200,
    "point2d": [0.0, 0.0]
}

complex_data_types = {
    "array": {
        **{key: [value, value] for key, value in simple_data_types.items()}
    }
}