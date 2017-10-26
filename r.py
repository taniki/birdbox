import requests
import random
import shutil
from pydub import AudioSegment
from pydub.playback import play

endpoint = "http://www.xeno-canto.org/api/2/recordings"
query = 'cnt:France'

r = requests.get(endpoint, params={'query': query })
data = r.json()["recordings"]


def play_bird(bird):
    print "{} {} {}".format(bird["gen"], bird["sp"], bird["ssp"])
    
    response = requests.get(bird["file"], stream=True)
    with open('tmp.mp3', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    
    del response

    song = AudioSegment.from_mp3("./tmp.mp3")
    play(song)

while True:
    bird = random.choice(data)

    play_bird(bird)

