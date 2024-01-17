import DDoSGuardCheckerAPI, CloudflareCheckerAPI
import sys, datetime, re, socket, json
from colorama import Fore, Back, Style

def printout(x):
    print(f"[Suzaku] {x}")

def checker(domain):
    try:
        printout(f"{Fore.GREEN}{Style.BRIGHT}Target Domain:{Fore.RESET} {domain}{Style.RESET_ALL}")
        printout(f"{Fore.GREEN}{Style.BRIGHT}Target IP{Fore.RESET}: {socket.gethostbyname(domain)}{Style.RESET_ALL}")
        
    except:
        printout(f"{Fore.RED}{Style.BRIGHT}Failed to Host name resolution.{Fore.RESET}")
        sys.exit(0)

    printout(f"{Fore.CYAN}Checking IP With Cloudflare Networks...{Fore.RESET}")
    cloudflare = CloudflareCheckerAPI.check(domain)
    if cloudflare:
        printout(f"{Fore.GREEN}{domain} was protected by Cloudflare!{Fore.RESET}")
        sys.exit(1)
    
    printout(f"{Fore.CYAN}Checking IP With DDoS-Guard Networks...{Fore.RESET}")
    ddosguard = DDoSGuardCheckerAPI.check(domain)
    if ddosguard:
        printout(f"{Fore.GREEN}{domain} was protected by DDos-Guard!{Fore.RESET}")
        sys.exit(1)

    printout(f"{Fore.LIGHTRED_EX}{domain} is Not Protected!{Fore.RESET}")


logo = """
░░      ░░  ░░░░  ░        ░░      ░░  ░░░░  ░  ░░░░  ░
▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒  ▒  ▒▒▒  ▒▒  ▒▒▒▒  ▒
▓▓      ▓▓  ▓▓▓▓  ▓▓▓▓  ▓▓▓▓  ▓▓▓▓  ▓     ▓▓▓▓  ▓▓▓▓  ▓
███████  █  ████  ██  ██████        █  ███  ██  ████  █
██      ███      ██        █  ████  █  ████  ██      ██
  v1.0                                    by GNUWood
"""
print(Fore.LIGHTRED_EX + Style.BRIGHT + logo + Style.RESET_ALL + Fore.RESET)
printout("Input target url of website.")
url = input("[Suzaku] >")
checker(url)
