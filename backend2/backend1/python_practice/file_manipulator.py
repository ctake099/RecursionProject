# import sys
# import os

# command = sys.argv[1]
# input_list = sys.argv[2:]

# # バリデーション
# # コマンドは存在するか
# # 引数の数は正しいか
# # ファイルは存在するか
# # 入力された型は正しいか
# commands = ["reverse", "copy", "duplicate-contents", "replace-string"]

# if command not in commands:
#     print(f"エラー: 未知のコマンド '{command}' が指定されました。")
#     print("使用可能なコマンド:")
#     for cmd in commands:
#         print(f"- {cmd}")
#     exit(1)  # 非ゼロの終了コードを使用してエラーを示す

# def valid_file(file_path):
#     if not os.path.exists(file_path):
#         print(f"{file_path}は存在しません")
#         exit(1)

# def reverse(input_path, output_path):
#     with open(input_path, "r") as fi:
#         content = fi.read()
#     with open(output_path, "w") as fo:
#         fo.write(content[::-1])

# def copy(input_path, output_path):
#     with open(input_path, "r") as fi:
#         content = fi.read()
#     with open(output_path, "w") as fo:
#         fo.write(content)

# def duplicate_contents(input_path, n):
#     with open(input_path, "r") as fi:
#         content = fi.read()
#         content += "\n"
#     with open(input_path, "w") as fo:
#         fo.write(content * n)

# def replace_string(input_path, needle, new_string):
#     with open(input_path, "r") as fi:
#         content = fi.read()
#     with open(input_path, "w") as fo:
#         fo.write(content.replace(needle, new_string)) 

# if (command == "reverse"):
#     if (len(input_list) != 2):
#         print("引数の数が正しくありません")
#         exit(1)
#     input_path = input_list[0]
#     output_path = input_list[1]
#     valid_file(input_path)
#     reverse(input_path, output_path)

# if (command == "copy"):
#     if (len(input_list) != 2):
#         print("引数の数が正しくありません")
#         exit(1)
#     input_path = input_list[0]
#     output_path = input_list[1]
#     valid_file(input_path)
#     copy(input_path, output_path)

# if (command == "duplicate-contents"):
#     if (len(input_list) != 2):
#         print("引数の数が正しくありません")
#         exit(1)
#     input_path = input_list[0]
#     valid_file(input_path)
#     try:
#         n = int(input_list[1])
#     except ValueError:
#         print(f"数字ではなく{input_list[1]}が入力されました")
#         print("数字を入力してください")
#         exit(1)
#     duplicate_contents(input_path, n)

# if (command == "replace-string"):
#     if (len(input_list) != 3):
#         print("引数の数が正しくありません")
#         exit(1)
#     input_path = input_list[0]
#     valid_file(input_path)
#     needle = input_list[1]
#     new_string = input_list[2]
#     replace_string(input_path, needle, new_string)


import sys
import os

def valid_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path}は存在しません")

def reverse(input_path, output_path):
    valid_file(input_path)
    with open(input_path, "r") as fi, open(output_path, "w") as fo:
        fo.write(fi.read()[::-1])

def copy(input_path, output_path):
    valid_file(input_path)
    with open(input_path, "r") as fi, open(output_path, "w") as fo:
        fo.write(fi.read())

def duplicate_contents(input_path, n):
    valid_file(input_path)
    with open(input_path, "r+") as fi:
        content = fi.read()
        fi.seek(0)
        fi.write(content * n)

def replace_string(input_path, needle, new_string):
    valid_file(input_path)
    with open(input_path, "r+") as fi:
        content = fi.read()
        fi.seek(0)
        fi.write(content.replace(needle, new_string))
        fi.truncate()

def main():
    commands = {
        "reverse": reverse,
        "copy": copy,
        "duplicate-contents": duplicate_contents,
        "replace-string": replace_string
    }

    if len(sys.argv) < 3:
        print("コマンドと引数を指定してください。")
        sys.exit(1)

    command = sys.argv[1]
    if command not in commands:
        print(f"エラー: 未知のコマンド '{command}' が指定されました。")
        print("使用可能なコマンド:")
        for cmd in commands.keys():
            print(f"- {cmd}")
        sys.exit(1)

    try:
        if command in ["reverse", "copy"]:
            if len(sys.argv[2:]) != 2:
                raise ValueError("引数の数が正しくありません")
            commands[command](*sys.argv[2:])
        elif command == "duplicate-contents":
            if len(sys.argv[2:]) != 2:
                raise ValueError("引数の数が正しくありません")
            input_path, n = sys.argv[2], int(sys.argv[3])
            commands[command](input_path, n)
        elif command == "replace-string":
            if len(sys.argv[2:]) != 3:
                raise ValueError("引数の数が正しくありません")
            commands[command](*sys.argv[2:])
    except Exception as e:
        print(f"エラー: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
