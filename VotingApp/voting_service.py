from VotingApp.voting_persistence import VotingDb
from VotingApp.voting_emailsender import EmailSender
from VotingApp.voting_dto import CandidateDto
from abc import ABC, abstractmethod

class VotingService():
    def __init__(self):
        self.voting_db = VotingDb()
    
    def show_all_voters(self):
        return self.voting_db.get_number_of_voters()
    
    def add_one_voting(self, _name_candidate):
        # subject = IncOneVoteSubject()
        # subject.notify(self.show_all_voters())
        return self.voting_db.add_vote_to_candidate(_name_candidate)
    
    def delete_all_vote(self):
        return self.voting_db.reset_vote()

######################################################################
# Observer Pattern
# interface
class VoteListener(ABC):
    @abstractmethod
    def notified(self, candidates):
        pass

# subject 1: increase one vote
class IncOneVoteSubject():
    def __init__(self):
        self.subscribers = [SendVoteToAllCandidate(), GotLessVoting(), FiveTimesVoted()]

    def notify(self, candidates: list[CandidateDto]):
        for subscriber in self.subscribers:
            subscriber.notified(candidates)

# observer 1.1
class SendVoteToAllCandidate(VoteListener):
    def __init__(self) -> None:
        self.email_sender = EmailSender()
    
    def notified(self, candidates: list[CandidateDto]):
        subject = "Voting Result"

        for current_candidate in candidates:
            body = f"Dear {current_candidate.name},\nhere is your voting result {current_candidate.vote}"

            if current_candidate.vote != 0 and current_candidate.vote % 20 >= 0:
                    return True, self.email_sender.send_email(current_candidate.get_email(), subject, body)
            return False, ""
    
# observer 1.2
class GotLessVoting(VoteListener):
    def __init__(self) -> None:
        self.email_sender = EmailSender()
    
    def notified(self, candidates: list[CandidateDto]):
        subject = "Voting Result"

        candidate_with_lesser_vote = None
        same_vote = False
        for index, current_candidate in enumerate(candidates):
            if candidate_with_lesser_vote == None or current_candidate.vote < candidate_with_lesser_vote.vote:
                candidate_with_lesser_vote = current_candidate
                same_vote = False

            elif candidate_with_lesser_vote.vote == current_candidate.vote:
                same_vote = True

            if index == len(candidates)-1 and candidate_with_lesser_vote != None and same_vote == False:
                print(candidate_with_lesser_vote.name)
                body = f"Dear {candidate_with_lesser_vote.name},\nyour voting is lesser than others"
                return True, self.email_sender.send_email(current_candidate.get_email(), subject, body)
        return False, ""

# observer 1.3
class FiveTimesVoted(VoteListener):
    def __init__(self) -> None:
        self.email_sender = EmailSender()
    
    def notified(self, candidates: list[CandidateDto]):
        subject = "Voted 5 times"

        for current_candidate in candidates:
            body = f"Dear {current_candidate.name},\nyou are voted 5 times"

            if current_candidate.vote != 0 and current_candidate.vote % 5 == 0:
                    return True, self.email_sender.send_email(current_candidate.get_email(), subject, body)
            return False, ""