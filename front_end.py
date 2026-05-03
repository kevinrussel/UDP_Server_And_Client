import tkinter as tk

def main():
    root = tk.Tk()
    root.title("UDP")
    root.geometry("1500x1000")
    root.configure(background="grey32")

    # IP input
    ip_label = tk.Label(root, text="IP Address", bg="grey32", fg="white", font=("Helvetica", 45, "bold"))
    ip_label.pack(pady=(80, 10))

    ip_input = tk.Entry(root, font=("Helvetica", 24), width=40)
    ip_input.pack(ipady=10)

    # Port input
    port_label = tk.Label(root, text="Port", bg="grey32", fg="white", font=("Helvetica", 28, "bold"))
    port_label.pack(pady=(40, 10))

    port_input = tk.Entry(root, font=("Helvetica", 24), width=40)
    port_input.pack(ipady=10)

    # Send button
    def on_send():
        ip = ip_input.get().strip()
        port = port_input.get().strip()
        print(f"Sending to {ip}:{port}")

    send_button = tk.Button(
        root,
        text="Send",
        command=on_send,
        font=("Helvetica", 45, "bold"),
        bg="#4a90d9",
        fg="white",
        relief="flat",
        padx=60,
        pady=20,
        cursor="hand2"
    )
    send_button.pack(pady=(60, 0))

    root.mainloop()

if __name__ == '__main__':
    main()