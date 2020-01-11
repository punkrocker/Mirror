from aip import AipSpeech
import os

''' 你的APPID AK SK  参数在申请的百度云语音服务的控制台查看'''
APP_ID = '16301424'
API_KEY = '4BW72IamBjvfo62VSAE893Dq'
SECRET_KEY = 'pskYTCuTZxKpYGgN6WqroDP40wwvN0kU'

# 新建一个AipSpeech
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):  # filePath  待读取文件名
    with open(filePath, 'rb') as fp:
        return fp.read()


def stt(filename):  # 语音识别
    # 识别本地文件
    result = client.asr(get_file_content(filename),
                        'wav',
                        16000,
                        {'dev_pid': 1536, }  # dev_pid参数表示识别的语言类型 1536表示普通话
                        )
    # 解析返回值，打印语音识别的结果
    if result['err_msg'] == 'success.':
        word = result['result'][0]
        print(word)
    else:
        print("错误")


# main函数 识别本地录音文件yahboom.wav
if __name__ == '__main__':
    stt('output.wav')
