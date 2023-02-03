import ctypes
import datetime
import locale
import configparser

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
img_qua = config['img_culto']['img_qua']
img_sex = config['img_culto']['img_sex']
img_sab = config['img_culto']['img_sab']
img_dom = config['img_culto']['img_dom']
img_ebd = config['img_culto']['img_ebd']
img_outros = config['img_culto']['img_padrao']

hoje = datetime.datetime.now()
hoje_string = hoje.strftime("%a")
hoje_dia = int(hoje.strftime("%d"))
hoje_hora = int(hoje.strftime("%H"))


def alterar_wallpaper():
    if hoje_string == 'qua':
        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, img_qua, 0)

    elif hoje_string == 'sex':
        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, img_sex, 0)

    elif hoje_string == 'sáb':
        if (hoje_dia >= 8) and (hoje_dia <= 14):
            ctypes.windll.user32.SystemParametersInfoW(
                20, 0, img_sab, 0)
        else:
            ctypes.windll.user32.SystemParametersInfoW(
                20, 0, img_outros, 0)
    elif hoje_string == 'dom':
        if hoje_hora <= 15:
            ctypes.windll.user32.SystemParametersInfoW(
                20, 0, img_ebd, 0)
        elif hoje_hora >= 16:
            ctypes.windll.user32.SystemParametersInfoW(
                20, 0, img_dom, 0)
    else:
        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, img_outros, 0)


alterar_wallpaper()
