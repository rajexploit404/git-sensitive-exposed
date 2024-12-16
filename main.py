import requests
import threading
import warnings
from urllib3.exceptions import InsecureRequestWarning
from colorama import Fore, Style, init

warnings.simplefilter('ignore', InsecureRequestWarning)
init(autoreset=True)

def print_banner():
    banner = """
    ================================
    Made by Rajexploit404
    ================================
    """
    print(Fore.CYAN + banner)

def check_git_head(url, found_file):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    git_head_url = f"{url}/.git/HEAD"
    
    try:
        response = requests.get(git_head_url, timeout=10, verify=False)
        
        if response.status_code == 200:
            if 'ref: refs/' in response.text:
                print(f"{Fore.GREEN}{url} - 200 OK - ref: refs/ found")
                with open(found_file, 'a') as file:
                    file.write(f"{url}/.git\n")
            else:
                print(f"{Fore.RED}{url} - 404 Not Found - ref: refs/ not found")
        elif response.status_code == 404:
            print(f"{Fore.RED}{url} - 404 Not Found - File .git/HEAD not found")
        else:
            print(f"{Fore.RED}{url} - Bad Requests - Status Code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        if "NameResolutionError" in str(e):
            print(f"{Fore.RED}{url} - Bad Requests - DNS resolution failed")
        elif isinstance(e, requests.exceptions.ConnectionError):
            print(f"{Fore.RED}{url} - Bad Requests - Connection Error")
        else:
            print(f"{Fore.RED}{url} - Bad Requests - {e}")

def check_urls_from_file(filename, found_file):
    try:
        with open(filename, 'r') as file:
            urls = file.readlines()

            threads = []
            max_threads = 30
            for idx, url in enumerate(urls):
                url = url.strip()
                if url:
                    if len(threads) >= max_threads:
                        for t in threads:
                            t.join()
                        threads = []

                    thread = threading.Thread(target=check_git_head, args=(url, found_file))
                    threads.append(thread)
                    thread.start()

            for t in threads:
                t.join()
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"Error: {e}")

print_banner()
filename = input("Enter filename (e.g., 1.txt or 4.txt): ")
found_file = "found.txt"
check_urls_from_file(filename, found_file)

print(f"URLs found with 200 OK have been saved to {found_file}")
