from rich.console import Console

console = Console(highlight=False)
STEP_COL = 32

def banner():
    console.print(   

        '           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n' +
        '                ⠀⠀⠀⠀⠀⡀⡀⠀⡀⠀⠂⡀⢀⢰⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀\n' +
        '               ⠀⠀⠀ ⢀⣀⣐⣬⣄⣷⡀⢸⡃⡘⡸⡄⢸⠀⠀⡇⠀⢠⠀⠀⠀\n' +
        '          ⠀⠀⠀ ⠀⣠⡴⠚⢉⢍⢂⣼⣴⣿⣿⣿⣷⣷⣷⣣⣏⣆⣼⠀⠀⠄⠀⠀⠀\n' +
        '        ⠀⠀⠀  ⢠⡞⠋⠀⡑⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣼⣆⣌⡠⢁⡤\n' +
        '  mmmmm  ⠀⠀ ⣰⠋⠀⣀⣺⣾⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟                "                 \n' +
        '  #   "#  ⠀⡼⠁⢀⣿⣿⣿⡿⣿⡛⣿⣿⣿⡷⢸⣿⠀⠀⠀⠀⣹⣿⣿⣿⣟⠣    mmm    mmm   mmm    m   m   mmm  ⠀\n' +
        '  #mmm#"  ⡰⠁⢀⣼⣿⠟⢿⡇⠹⣿⣿⣿⠟⠀⢠⡿⠀⠀⣠⣾⡿⣿⡥⠊⠁    #   "  #   "    #    "m m"  #"  # ⠀\n' +
        '  #     ⠁ ⢠⣾⠟⠁⠀⠈⠳⢿⣦⣠⣤⣦⣼⠟⠁⣠⣾⣿⣿⣟⠍⠒⠀⠠      """m   """m    #     #m#   #"""" ⠀\n' +
        '  #      ⢠⡟⠁⢀⣀⣀⣀⣀⡀⠈⣉⣉⣡⣤⣶⣿⡿⡿⡿⡻⠥⠑⡀       "mmm"  "mmm"  mm#mm    #    "#mm" ⠀\n' +
        '         ⠏⡠⠚⠉⠋⢍⠋⢫⠋⠛⢹⢻⡟⠻⣟⢏⠌⢊⡌⠌⠄⠀⠀⠀⠀⠀⠀⠀⠀  \n' +
        '      ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠘⠂⠘⠂⠿⠈⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀  \n' +
        '\n')
    console.print(
        '[bold cyan]0xPassive[/bold cyan] — Passive Recon Framework\n' +
        '[dim]Author: 0xW41th[/dim]\n'
    )

def info(msg):
    console.print(f"[bold cyan][INF][/bold cyan] {msg}")

def step(tag, msg):
    padded = f"{msg:<{STEP_COL}}"
    console.print(f"[bold green][{tag}][/bold green] {padded}", end="")

def done(msg="done"):
    console.print(f" [bold green]{msg}[/bold green]")
