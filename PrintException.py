import datetime
import os


def fcolor(r,g,b,text):
    return f'\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m'
def bcolor(r,g,b,text):
    return f'\033[48;2;{r};{g};{b}m{text} \033[48;2;0;0;0m'

os.system('color')

LOGDIR=fr'.\Log'
DATE=datetime.date.today().strftime("%Y%m%d")

def print_ex(ex:Exception):
    exc_tb=ex.__traceback__
    print(f"{fcolor(255,0,0,'Traceback Error: ')}{ex}")
    with open(fr'{LOGDIR}\{DATE}-ErrorLog.txt','a') as file:
        time=datetime.datetime.now()
        file.write(f"{time.hour:02}:{time.minute:02}:{time.second:02}>>{fcolor(255,0,0,'Traceback Error: ')}{ex}"+'\n')
    while exc_tb is not None:
        exc_dir=exc_tb.tb_frame.f_code.co_filename
        exc_line=exc_tb.tb_lineno
        exc_func=exc_tb.tb_frame.f_code.co_name
        exc_str='\t'.join(list(map(str,(f"{fcolor(50,250,255,'File: ')}{exc_dir}",f"| {fcolor(255,100,200,'Line: ')}{exc_line}",f"| {fcolor(250,250,0,'Function: ')}{exc_func}"))))
        print(exc_str)
        with open(fr'{LOGDIR}\{DATE}-ErrorLog.txt','a') as file:
            file.write(f'{exc_str}'+'\n')
        exc_tb=exc_tb.tb_next
    print(fcolor(255,50,30,'Error End.'))

def print_log(text:str):
    print(text)
    with open(fr'{LOGDIR}\{DATE}-CommonLog.txt','a') as file:
        time=datetime.datetime.now()
        file.write(f"{time.hour:02}:{time.minute:02}:{time.second:02}>>{text}"+'\n')