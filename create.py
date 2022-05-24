import os
from dotenv import load_dotenv
import requests

fake_user_topic_sentence = (
    "Donald Trump kicked in the door and leveled a steely gaze at the terrorist leader. 'Not today buddy' he intoned, opening fire with his well-worn Desert Eagle hand-cannon"
    )

deep_api_key = os.getenv('DAPI')


class Gentext:
    def __init__(self, input_text):
          self.input_text = input_text
          print(input_text)
          
    def get_text(self):
        r = requests.post("https://api.deepai.org/api/text-generator",
                          data={
                              'text': self.input_text,
                          },
                          headers={'api-key': deep_api_key}
                          )
        # print(r.json(['output']))
        f = open("output.txt", "w+", encoding="utf-8")
        resp = (r.text)
        print(resp)
        f.write(resp)
        f.close()  
        return 200
          

