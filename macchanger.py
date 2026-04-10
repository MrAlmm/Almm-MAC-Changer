import subprocess
import optparse
import re

RED = "\033[91m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

print(f"{RED}") # ابدأ التلوين بالأحمر
print(r"           ")
print(r"   / \ _ / \   ")
print(r"  (  o ) ( o )  ")
print(r"   \  _ _ /  ")
print(r"    |  _  |  ")
print(r"    \_____/  ")
print(r"    /|   |\    ")
print(r"   / |   | \   ")
print(r"  /  |   |  \  ")
print(r"      ")

# تلوين قسم الاسم بالأبيض العريض
print(f"{RESET}{BOLD}{WHITE}-----------------------------{RESET}")
print(f"{RESET}{BOLD}{WHITE}      Almm - MAC CHANGER     {RESET}")
print(f"{RESET}{BOLD}{WHITE}-----------------------------{RESET}{RED}") # ارجع للأحمر

print(r"           ")
print(r" ( _ \( \/ ) ( \/ )( _ ) ")
print(r"  ) _ ( \  /  \  / )( ")
print(r" (____/ (__) (__) (__) ")
print(f"{RESET}") # إعادة اللون الطبيعي لبقية الكود

def get_arguments():
  parser = optparse.OptionParser()
  parser.add_option("-i", "--interface", dest="network_interfac", help="specify network interface")
  parser.add_option("-m", "--mac", dest="new_address", help="specify new address")
  options, arguments = parser.parse_args()


  if not options.network_interfac:
      parser.error("[-] Please specify network interfac , go tp -h")

  if not options.new_address:
      parser.error("[-] Please specify new address, go tp -h")

  return options
options = get_arguments()





def  mac_change (network_interface, new_address):
  subprocess.call("sudo ifconfig " + options.network_interfac + " down ", shell=True)
  subprocess.call("sudo ifconfig " + options.network_interfac + " hw ether " + options.new_address, shell=True)
  subprocess.call("sudo ifconfig " + options.network_interfac + " up", shell=True)
  print("[+] changing mac address to " + options.network_interfac + " to " + options.new_address)
  subprocess.call("ifconfig eth0", shell=True)


def get_mac(network_interface):
  ifconfig_result = subprocess.check_output("ifconfig " + options.network_interfac , shell=True).decode("utf-8")
  mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
  return mac_address


option = get_arguments()
mac_change(options.network_interfac, options.new_address)
mac_address = get_mac(options.network_interfac)

BLUE = "\033[94m"    # لون أزرق فاتح واحترافي

if mac_address[0] == options.new_address:
    # هنا غيرنا اللون إلى BLUE وزدنا BOLD عشان يطلع فخم
    print(f"{BLUE}{BOLD}[+] MAC address changed goooooood{RESET}")
else:
    print(f"{RED}{BOLD}[-] MAC address changed bad{RESET}")
