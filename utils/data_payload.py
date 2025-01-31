# import json
# import os
#
"""NOT USE ANYMORE AS WE ARE PUTTING A PAYLOAD IN A VARIABLE"""
# class DataPayload:
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.data = self.load_data()
#
#     def load_data(self):
#         """Load data from the JSON file."""
#         if not os.path.exists(self.file_path):
#             raise FileNotFoundError(f"{self.file_path} not found")
#
#         with open(self.file_path, 'r') as f:
#             return json.load(f)
#
#     def get_payload(self):
#         """Return the payload data."""
#         return self.data
