import os
import socket
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
    # コマンドラインからpipでライブラリをインストール
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


def print_stats():
    print(socket.gethostname())
    os.system('python --version')
    os.system('pip -V')
    print(os.getcwd())


def install_rich():
    # rich モジュールが入っているか
    # ない場合の選択と、インストールをする
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


def one_letter_print(input_text, **args):
    """一文字ずつ表示する関数

    Args:
        input_text (str):出力する文字列

        color (str):出力する文字列の色
            default:色なし
        delay_time (int):一文字の待機する時間   
            default:0.2
        end (str):最後の文字
            default:"\n"
    """

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
    # 本当に終了するか確認し、停止
    one_letter_print("本当にゲームを終了しますか？", color="red", delay_time=0.05)
    user_ans = choose_option(["終了", "続ける"])
    if user_ans == 0:
        print("[red]終了します[/]")
        sys.exit()


def ask_continue():
    # エンターで続ける
    ans = console.input("[blink]___[/]")
    if ans == "b":
        exit()


def choose_option(options):
    # 選択肢を表示し、選ぶプロンプトを出す
    # 選択肢になかったら、再帰
    def choose(option_len):
        user_ans = input(">>")

        if user_ans == "b":
            exit()

        try:
            user_ans = int(user_ans)
        except ValueError:
            print("[red]上の選択肢から選んでください[/]")
            return choose(option_len)

        if user_ans in range(option_len):
            return user_ans
        else:
            print("[red]上の選択肢から選んでください[/]")
            return choose(option_len)

    for i, option in enumerate(options):
        print(f"[green]{i}[/]:{option}")

    return choose(len(options))


# richモジュールのインストール確認と、インポート
print_stats()
install_rich()
try:
    import rich
    from rich import print
    from rich.console import Console
    console = Console()
    print("[green]import rich OK![/]")
    time.sleep(1)
    clear_console()
except Exception as e:
    print("Error import rich")
    print(e)
    print("Exit.")
    sys.exit()


""""
説明

関数:「one_letter_print()」
    一文字ずつ文字を表示する

    第一引数:表示する文字列(必須)
    
    ここから順番なし(なくても良い)
    color="" : 文字色("red" 、"yellow" 、"blue" など)
    delay_time="" : 一文字で待機する時間(0.1、0.01 など)(デフォルト:0.2)
    end="" : 最後の文字 (デフォルト="\n" (改行))
    
関数:「choose_option()」
    選択肢から選ぶ
    
    第一引数(list) : 選択肢のリスト(必ず、リストにする)
    
    戻り値(int) : 選んだ選択肢の番号(数値)

関数: 「ask_continue()」
    エンターキーを押すのを待つ
    
    引数、戻り値なし
    
関数: 「exit()」
    本当に終了させるか聞いて、プログラムを終了させる
    
    引数、戻り値なし
"""


# ここからメイン処理
one_letter_print("GAME START!!", color="yellow")
one_letter_print(
    "==========================================", delay_time=0.01
)
one_letter_print("操作説明:", delay_time=0.01)
one_letter_print("  続ける:「___」エンターキーを押す", delay_time=0.01)
one_letter_print("  選択するとき:「>>ここに数字を入力」", delay_time=0.01)
one_letter_print("  途中で終了するとき:「b」を入力", delay_time=0.01)
one_letter_print(
    "==========================================", delay_time=0.01
)
time.sleep(2)
one_letter_print("ゲームを始めますか？")
if choose_option(["始める", "やめる"]) == 1:
    exit()
one_letter_print(
    "==========================================", delay_time=0.01
)
time.sleep(2)
one_letter_print("これは、ある少年の話...")
