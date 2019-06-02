import shutil
import sys
import os

def main():
	try:
		if shutil.which("netsh"):
			print("<AnachakHacker DNS Changer>")
			print("1. Google")
			print("2. Cloudflare")
			print("3. OpenDNS")
			print("4. Custom")
			print("5. Reset to default")

			while True:
				choice = input("Select a provider [1-5]: ")
				if choice not in list(map(str, list(range(1, 5 + 1)))):
					continue
				choice = int(choice)
				break

			if choice == 1:
				provider = "Google"
				primaryAddress = "8.8.8.8"
				secondaryAddress = "8.8.4.4"
			elif choice == 2:
				provider = "Cloudflare"
				primaryAddress = "1.1.1.1"
				secondaryAddress = "1.0.0.1"
			elif choice == 3:
				provider = "OpenDNS"
				primaryAddress = "208.67.222.222"
				secondaryAddress = "208.67.220.220"
			elif choice == 4:
				primaryAddress = input("Enter address: ")
			elif choice == 5:
				pass

			if choice <= 4:
				execute("netsh interface ip set dns \"Local Area Connection\" static {0}".format(repr(primaryAddress)))
				if choice <= 3:
					execute("netsh interface ip add dns \"Local Area Connection\" addr={0} index=2".format(repr(secondaryAddress)))
				print("The DNS {0} has been changed to {1}".format("provider" if choice <= 3 else "address", provider if choice <= 3 else primaryAddress))
			else:
				execute("netsh netsh interface ip set dns \"Local Area Connection\" dhcp")
				print("The DNS provider has been reset to default")
		else:
			print("Command 'netsh' not found")
			os._exit(1)

	except (EOFError, KeyboardInterrupt):
		print()
		os._exit(0)

def execute(command):
	os.system(command)

if __name__ == "__main__":
	if sys.version_info.major == 3:
		main()
	else:
		print("Please run this script with python3")
