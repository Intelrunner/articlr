import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()


# you can get your 
d_api_key=os.getenv("DAPI")



fake_user_input = (
    "I may not have been sure about what really did interest me, but I was absolutely sure about what didnt")





def main(user_input):
    r = requests.post("https://api.deepai.org/api/text-generator",
                      data={
                          'text': user_input,
                      },
                      headers={'api-key': d_api_key}
                      )
   # print(r.json(['output']))
    f = open("output.txt", "w+", encoding="utf-8")
    resp = (r.text)
    print(resp)
    f.write(resp)
    f.close()  
    return 200


if __name__ == '__main__':
    main(fake_user_input)
