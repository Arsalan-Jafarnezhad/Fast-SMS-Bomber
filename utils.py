"""
Utils for sms bomber
"""

from uuid import getnode
from platform import system, node, release, architecture
from machineid import id as unique_id
from time import sleep

# Registering colors

class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'
    
class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'

def output(text: str, newline: bool = True) -> None:
    """
    Flush prints text to terminal
    """
    prefix = f"{fg.MAGENTA}[{fg.GREEN}SMS {fg.BLUE}Bomber{fg.MAGENTA}] "
    for character in prefix + text + ("\n" if newline else ""):
        print(character, end="", flush=True)
        sleep(0.01)
    return None


def prompt(text: str) -> str:
    """
    Flush prints text to terminal
    """
    output(text, newline = False)
    return input()


def log(name: str) -> None:
    """
    Logs the named operator to terminal
    """
    output(f"{fg.YELLOW}[{fg.RED}{name}{fg.YELLOW}] {fg.GREEN}{style.BRIGHT}OK")
    return None


def generate_license_key() -> str:
    """
    Generates unique license per pc
    """
    raw_id = "".join(list(unique_id().split("-")))
    parts = []
    first_index = 0
    for last_index in range(0, len(raw_id) + 1, 4):
        parts.append(raw_id[first_index:last_index])
        first_index = last_index
    return "-".join(parts)[1:]


def is_iran_phone_number(phone_number: str) -> bool:
    """
    Verify's Iran phone number
    """
    if len(phone_number) == 13:
        if phone_number[1:].isalnum():
            if phone_number.startswith("+98"):
                return True
    return False


def system_information() -> None:
    """
    Returns available system data
    """
    data = {
        "Name": "Fast SMS Bomber",
        "Version": "1.0.0",
        "Developer": "Arsalan Jafarnezhad",
        "Channel": "t.me/AxiomLite",
        "System": f"{system()} {release()} {architecture()[0]}",
        "System Name": node(),
        "Special Message": "Welcome to Open-Source world",
    }
    for key, value in data.items():
        print(f"{fg.CYAN}{style.BRIGHT}{key}{fg.RED}{style.BRIGHT}: {fg.GREEN}{style.BRIGHT}{value}")
    return None


def get_mac_address():
    """
    Get system mac address
    """
    # Get the MAC address as a 48-bit integer
    mac_num = getnode()
    # Format it as a standard MAC address (e.g., 00:1A:2B:3C:4D:5E)
    mac = ":".join(
        ["{:02x}".format((mac_num >> ele) & 0xFF) for ele in range(40, -1, -8)]
    )
    return mac


if __name__ == "__main__":
    print(generate_license_key())
    system_information()
    print(get_mac_address())
