from els import els
import shutil
import minecraft

def yes_no_input(input_text):
    while True:
        choice = input(input_text).lower()
        if choice in ['1']:
            server_exec()
        elif choice in ['2']:
            return
        else:
            print("存在しません")
            return False

def server_exec():
    print("※メモリの設定がありますがよくわからない人はググってください（空白だと1GBになります。）")
    xmx_mem = input("Xmx(最大メモリ量)を入力してください　※数字のみ、GB不要：")
    xms_mem = input("Xms(最小メモリ量)を入力してください　※数字のみ、GB不要：")
    yes_no_text = "この構成で起動します{\nXmx:"+str(xmx_mem)+"GB\nXms:"+str(xms_mem)+"GB  }\nこの構成でよろしいでしょうか？　yes か no [Y/n]："
    minecraft.yes_no_input(yes_no_text)
    minecraft.minecraft_exec(str(xmx_mem), str(xms_mem))
    main()

def server_delete():
    minecraft.yes_no_input("サーバーを削除します。よろしいでしょうか？ yes か no [y/n]：")
    minecraft.yes_no_input("※最終警告※ サーバーを削除します。よろしいでしょうか？ yes か no [y/n]：")
    print("削除します。")
    shutil.rmtree("minecraft")
def main():
    #path = ['minecraft/cache/', 'minecraft/config/', 'minecraft/libraries/', 'minecraft/logs/', 'minecraft/plugins/', 'minecraft/versions/', 'minecraft/banned-ips.json', 'minecraft/banned-players.json', 'minecraft/bukkit.yml', 'minecraft/commands.yml', 'minecraft/eula.txt', 'minecraft/help.yml', 'minecraft/ops.json', 'minecraft/paper-1.19.2.jar', 'minecraft/permissions.yml', 'minecraft/server.properties', 'minecraft/usercache.json', 'minecraft/version_history.json', 'minecraft/whitelist.json', 'minecraft/spigot.yml']
    #for pathcount in path:
        #els.check_file_dir(pathcount, "True", "True")
    print("サーバー起動:1\n戻る:2")
    yes_no_input("どれを行うか選択してください。[1,2]：")

if __name__ == "__main__":
    main()