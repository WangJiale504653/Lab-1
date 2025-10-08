WHITE="\x1b[38;5;255m"
RESET="\x1b[0m"


def jjjj(num):
    pattern_lines = [
        f"{WHITE}      ██      {RESET}",
        f"{WHITE}    ██  ██    {RESET}",
        f"{WHITE}  ██      ██  {RESET}",
        f"{WHITE}██          ██{RESET}",
        f"{WHITE}  ██      ██  {RESET}",
        f"{WHITE}    ██  ██    {RESET}",
        f"{WHITE}      ██      {RESET}",
    ]

    for i in pattern_lines:
        print(i*num)


jjjj(3)
