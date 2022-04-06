'''
USAGE:
python main.py --interface <type-inter-here> --mac <type-mac-here>
'''
import subprocess
import optparse
import re

def get_arguments():
  #Adding options to the scripts --i show info. about interface --m show info about mac.
  parser = optparser.OptionParser()
  parser.add_option("-i", "--interface", dest="interface", help="Interface to change tis Mac address")
  parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
  (options, arguments) = parser.parse_args()
  if  not options.interface:
    parser.error("[-] Please specify an interface, use --help for more info")
  elif not options.new_mac:
    parser.error("[-] Please specify new mac, use --help for more info")
  return options
  

def change_mac(interface, new_mac):
  print("[+] Changing Mac address for " + interface + " to " + new_mac)
  subprocess.call(["ifconfg", interface, "down", shell=True])
  subprocess.call(["ifconfg", interface, "hw", "ether", + new_mac, shell=True])
  subprocess.call(["ifconfg", interface, "up", shell=True])

#Verify if the Mac address was changed as requested
options = get_arguments()
change_mac(options.interface, options.new_mac)

def get_current_mac(interface):
  #capture output of ifconfig command and stores it in a variable
  check_inter = subprocess.check_output(["ifconfig", options.interface])

  #Extract field of ether address by using regular expressions
  #Hint use www.pythex.org 
  filter_mac-address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", check_inter)

  #Verify if the mac-address was changed as requested
  if filter_mac-address:
    return print(filter_mac-address.group(0))
  else:
    print("[-] Could not read MAC address.")


#Check user input and check if the value of the variable is the same as user entered

options = get_arguments
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
  print("[+] MAC address was successfully chaned to " + current_mac)
else:
  print(["[-] MAC address did not changed.")


                             
