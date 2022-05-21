import requests
import os
import json
from dotenv import load_dotenv



fake_user_topic_sentence = (
    "I may not have been sure about what really did interest me, but I was absolutely sure about what didnt")

d_api_key = os.environ['DAPI']




def main(user_input):
    r = requests.post("https://api.deepai.org/api/text-generator",
                      data={
                          'text': user_input,
                      },
                      headers={'api-key': d_api_key}
                      )
   # print(r.json(['output']))
    f = open("output.txt", "w+", encoding="utf-8")
    f.write(json.dumps(r.text))
    return 200


print(main(fake_user_input))
if __name__ == '__main__':
    main(fake_user_input)
