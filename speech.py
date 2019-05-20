from aip import AipSpeech
import appkey

client = AipSpeech(appkey.APP_ID, appkey.API_KEY, appkey.SECRET_KEY)

if __name__ == '__main__':
    for i in range(4):
        if (i == 0):
            content = '你瞅啥？'
        if (i == 1):
            content = '瞅你咋地。'
        if (i == 2):
            content = '再瞅一个试试！'
        if (i == 3):
            content = '试试就试试。'
        if (i == 0 or i == 2):
            result = client.synthesis(content, 'zh', 1, {'spd': 0, 'vol': 5, 'per': 3})
        if (i == 1 or i == 3):
            result = client.synthesis(content, 'zh', 1, {'spd': 0, 'vol': 5, 'per': 4})
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        filename = str(i)
        if not isinstance(result, dict):
            with open('文件的保存路径' + filename + '.mp3', 'wb') as f:
                f.write(result)
