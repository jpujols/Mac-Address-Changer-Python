'''
USAGE:
python main.py --interface <type-inter-here> --mac <type-mac-here>
'''
import subprocess
import optparse

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
  
options = get_arguments()
change_mac(options.interface, options.new_mac)




