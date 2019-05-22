from aip import AipSpeech
import appkey

client = AipSpeech(appkey.APP_ID, appkey.API_KEY, appkey.SECRET_KEY)


def makeMp3(content):
    result = client.synthesis(content, 'zh', 1, {'spd': 0, 'vol': 5, 'per': 3})
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    filename = 'test'
    if not isinstance(result, dict):
        with open('文件的保存路径' + filename + '.mp3', 'wb') as f:
            f.write(result)


if __name__ == '__main__':
    makeMp3("你好")
