from abc import ABC, abstractmethod
import sqlite3
import os
from VotingApp.voting_dto import CandidateDto
from sqlite3 import Error

class VotingDb():
    def __init__(self):
        self.db_init = False
        self.db_filename = "voting.db"
        self.db_path = os.path.join(os.path.split(__file__)[0], self.db_filename)

        # inisialization connection
        self.conn = None
        self.cursor = None
        
        self.setup_database()
    
    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
        except Error as e:
            print(e)
        
        return conn
    
    def setup_database(self):
        if self.db_init == True:
            self.create_database()
        
        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()

        if self.db_init == True:
            self.setup_table()
    
    def create_database(self):
        if os.path.exists(self.db_path):
            self.drop_database()
        
        with open(self.db_filename, "w"):
            pass

    def setup_table(self):
        sql_setup_table = """CREATE TABLE vote_result (
                            candidate text,
                            email text,
                            vote int
        );"""

        self.cursor.execute(sql_setup_table)
        self.conn.commit()

        self.insert_candidate("Diana", "diana@gmail.com", 0)
        self.insert_candidate("Hans", "hans@gmail.com", 0)
        self.insert_candidate("Niko", "niko@gmail.com", 0)
    
    def insert_candidate(self, _name, _email, _vote):
        sql_insert_candidate = f'''
                INSERT INTO vote_result VALUES (?,?,?)'''
        all_records = self.cursor.execute(sql_insert_candidate, (_name, _email, _vote,))
        self.conn.commit()

        results = []
        for row in all_records:
            results.append(CandidateDto(row[0], row[1], row[2]))
        
        return results

    def get_number_of_voters(self):
        sql_get_number = "SELECT * FROM vote_result"

        all_records = self.cursor.execute(sql_get_number)
        
        results = []
        for row in all_records.fetchall():
            results.append(CandidateDto(row[0], row[1], row[2]))

        self.conn.commit()
        return results

    def add_vote_to_candidate(self, _name_candidate):
        sql_add_vote = f'''
                UPDATE vote_result 
                SET vote = vote + 1
                WHERE candidate = ?'''
        
        all_records = self.cursor.execute(sql_add_vote, (_name_candidate, ))
        self.conn.commit() 

        results = []
        for row in all_records:
            results.append(CandidateDto(row[0], row[1], row[2]))
        
        return results
    
    def reset_vote(self):
        sql_reset_vote = f'''
                UPDATE vote_result
                SET vote = 0'''
        
        all_records = self.cursor.execute(sql_reset_vote)
    
        results = []
        for row in all_records.fetchall():
            results.append(CandidateDto(row[0], row[1], row[2]))

        self.conn.commit() 
        return results
    
    def drop_table(self):
        sql_drop_table = '''DROP TABLE vote_result'''

        self.cursor.execute(sql_drop_table)
        self.conn.commit()
    
    def drop_database(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()
        os.remove(self.db_path)