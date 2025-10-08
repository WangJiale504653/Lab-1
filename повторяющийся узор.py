WHITE="\x1b[38;5;15m"
RESET="\x1b[0m"
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
    print(i*5)
