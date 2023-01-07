import socket
import tkinter as tk
import threading 
from firebase_admin import db

ref = db.reference('server/saving-data/fireblog/posts')

print(ref.get())

def recieve():
    while True:
        data = sock.recv(16)
        if data:
            text.config(state="normal")
            text.insert(tk.END, data.decode()+"\n")
            text.config(state="disabled")
        else:
            print("Client disconnected?")
        

def sendMessage(event=None):
    message = nickname+": "+entry.get()
    sock.sendall(bytes(message, 'utf-8'))
    entry.delete(0,"end")

    
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nickname = input("Please enter your nickname\n> ")
opt = input("Would you like to connect through\n\n1.IP\n2.Server List\n\n> ")
# Connect to the server
if opt == "1":
    while True:
        try:
            shitez = input("Please enter the ip:\n> ")
            text,port = shitez.split(":")
            server_address = (text, int(port))
            sock.connect(server_address)
            break
        except:
            print("connection error")
else:
    print("ips")

# Send data


# Receive data


root = tk.Tk()
root.title("Client")


label = tk.Label(root, text="Chat")
label.pack()
text = tk.Text(root, height=5, width=30,state="disabled")
text.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Send", command=sendMessage)
button.pack()

root.bind("<Return>", sendMessage)

thread = threading.Thread(target=recieve, name="ReceiveThread")
thread.start()

root.mainloop()

sock.close()