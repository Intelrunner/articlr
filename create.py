import os


fake_user_topic_sentence = (
    "Donald Trump kicked in the door and leveled a steely gaze at the terrorist leader. 'Not today buddy' he intoned, opening fire with his well-worn Desert Eagle hand-cannon"
    )

deep_api_key = os.environ['DAPI']


class Gentext:
    def __init__(self, input_text):
          self.input_text = input_text
          print(input_text)
          
        
        

g1 = Gentext(input_text = fake_user_topic_sentence)