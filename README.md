# Voting-App-Exercise-
This is my little project that I got in OOP (object-oriented programming) course in my 3rd semester.

The task is simple:
1) Create a simple app, which is voting app, that increase vote number for every candidate that available.
2) Use OOP's principal (I use inheritance) and other patternn (service layer pattern and observer pattern) that already been learned.

# Target Audience:
This project will useful for my junior in college. Other than that, maybe this project is useless for you.

# Here is the result:
1. Menu Scene
![menu_scene](https://github.com/cia2003/Voting-App-Exercise-/assets/137704190/a2de5c8e-c5e5-48c0-a0eb-d3596355fcca)

2. Voting Scene
![voting_scene](https://github.com/cia2003/Voting-App-Exercise-/assets/137704190/b370785b-c38c-4290-ae68-a2d6724b9d1d)

# How to run this file:
1) Download this repository (zip)
2) Extract the file in your computer (and don't forget to remember where you put your file)
3) Open your command prompt
4) go to the folder where you store the file, then type "python -m VotingApp"
5) Voila! you can run the app

# Other information (You can skip this)
1) I use pygame to create the app and sqlite to store candidate's data
2) About service layer pattern:
   1) I use this pattern to divide the jobs into 3:
      a) UI layer: displaying the app
      b) Service layer: voting logic -> what action will happen If I increase one vote (I use observer pattern).
      c) Persistence layer: handle the database
3) About observer pattern:
   1) I use this pattern to distinguish between the topic (subject) and the actions
      For example:
      - Topic: increase Candidate A's vote
      - Action:
        1) Send email the result of vote to all candidates
        2) Send email if a candidate got less vote than others
        3) Send email if a candidate got voted five times
