from aip import AipSpeech
from voice import appkey
from pydub import AudioSegment
from pydub.playback import play
import io


class Speech:
    def __init__(self):
        self.client = AipSpeech(appkey.APP_ID, appkey.API_KEY, appkey.SECRET_KEY)

    def makeMp3(self, content):
        result = self.client.synthesis(content, 'zh', 1, {'spd': 0, 'vol': 5, 'per': 3})
        song = AudioSegment.from_file(io.BytesIO(result), format="mp3")
        play(song)


if __name__ == '__main__':
    speech = Speech()
    speech.makeMp3("Hello,I'm Angle")
