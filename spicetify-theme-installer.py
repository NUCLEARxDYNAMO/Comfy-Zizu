from os import getlogin, system

config_folder = f"/home/{getlogin()}/.config/spicetify"
cli_folder = f"/home/{getlogin()}/spicetify-cli"

def clear():
    system("clear")

def start():

    clear()
    print("Theme installation tool\n")
    print("'I' -Install theme")
    user = input("\nChoose an option:\n")
    if user.lower() == "i":
        print("This will install Comfy-Zizu")
        input("\nPress any key to continue...")
        system("git clone https://github.com/ShaunakPemmaraju/Comfy-Zizu")
        system(f"mv Comfy-Zizu {config_folder}/Themes")
        system(f"{cli_folder}/spicetify config current_theme Comfy-Zizu")
        system(f"{cli_folder}/spicetify config overwrite_assets 1")
        system(f"{cli_folder}/spicetify apply")
    else:
        start()
start()