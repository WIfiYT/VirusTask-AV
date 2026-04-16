import json

class SignatureDatabase:
    def __init__(self, db_file='signatures.json'):
        self.db_file = db_file
        self.signatures = self.load_signatures()

    def load_signatures(self):
        try:
            with open(self.db_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_signatures(self):
        with open(self.db_file, 'w') as file:
            json.dump(self.signatures, file, indent=4)

    def add_signature(self, signature_id, signature_data):
        self.signatures[signature_id] = signature_data
        self.save_signatures()

    def get_signature(self, signature_id):
        return self.signatures.get(signature_id, None)

    def update_signature(self, signature_id, signature_data):
        if signature_id in self.signatures:
            self.signatures[signature_id] = signature_data
            self.save_signatures()
        else:
            raise ValueError('Signature ID does not exist.')

    def initialize_database(self):
        self.signatures = {}
        self.save_signatures()  

# Example usage:
# db = SignatureDatabase()
# db.add_signature('malware1', {'name': 'Malware Example 1', 'type': 'virus'})
# print(db.get_signature('malware1'))