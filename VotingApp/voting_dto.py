class CandidateDto():
    def __init__(self, _name, _email, _vote):
        self.name = _name
        self.email = _email
        self.vote = _vote
    
    def get_vote(self):
        return self.vote
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email