import os
import subprocess
import sys
import time


def clear_console():
    # コンソールをクリア
    cmd = "cls"
    return_line = subprocess.Popen(
        cmd, stdout=subprocess.PIPE,
        shell=True).stdout.readlines()

    if len(return_line) == 0:
        os.system('clear')
    else:
        os.system('cls')


def is_install_package(package_name):
    cmd = f"pip show {package_name}"
    return_line = subprocess.Popen(
        cmd, stdout=subprocess.PIPE,
        shell=True).stdout.readlines()

    if len(return_line) == 0:
        return False
    else:
        return True


def ask_y_n(input_text):
    # Yes か NO かを聞く
    # "y" か "n"でないときは、再帰でもう一度選択
    ans = input(input_text)
    if ans == "y":
        return True
    elif ans == "n":
        return False
    else:
        print('Error (Please enter "y" or "n")')
        return ask_y_n(input_text)


def install_rich():
    if is_install_package("rich"):
        pass
    else:
        if ask_y_n("「rich」がインストールされていません。\nインストールしますか?(y/n)..."):
            try:
                os.system('pip install rich')
                import rich
                from rich import print
            except Exception as e:
                print("Error installing")
                print(e)
                print("Exit.")
                sys.exit()

            print("Successfully installed")
            return True
        else:
            print("プログラムを実行することができません")
            print("終了します")
            sys.exit()


def one_letter_at_a_time(input_text, **args):
    # 一文字ずつ表示する関数
    input_text_list = list(input_text)

    text_color = args.get("color")
    delay_time = args.get("delay_time", 0.2)
    end = args.get("end", "\n")

    for character in input_text_list:
        if text_color == None:
            print(character, end="")
        else:
            print(f"[{text_color}]{character}[/]", end="")
        time.sleep(delay_time)

    print("", end=end)

    if not end == "":
        time.sleep(0.5)


def exit():
    one_letter_at_a_time("ゲームを終了します", color="red")
    sys.exit()


def ask_continue():
    ans = console.input("[blink]___[/]")
    if ans == "b":
        exit()


# richモジュールのインストール確認と、インポート
install_rich()
try:
    import rich
    from rich import print
    from rich.console import Console
    print("[green]import rich OK![/]")
    time.sleep(1)
    clear_console()
except Exception as e:
    print("Error import rich")
    print(e)
    print("Exit.")
    sys.exit(1)


console = Console()
# ここからメイン処理
one_letter_at_a_time("GAME START!!", color="yellow")
one_letter_at_a_time(
    "==========================================", delay_time=0.01)
one_letter_at_a_time("操作説明:")
one_letter_at_a_time("  続ける:「___」エンターキーを押す", delay_time=0.1)
one_letter_at_a_time("  選択するとき:「>>ここに数字を入力」", delay_time=0.1)
one_letter_at_a_time("  途中で終了するとき:「b」を入力", delay_time=0.1)
one_letter_at_a_time(
    "==========================================", delay_time=0.01)
time.sleep(2)
one_letter_at_a_time("ゲームを始めますか？", end="")
ask_continue()
one_letter_at_a_time(
    "==========================================", delay_time=0.01)
time.sleep(2)
one_letter_at_a_time("これは、ある少年の話...")
