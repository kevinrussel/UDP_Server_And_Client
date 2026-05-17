import tkinter as tk
from tkinter import font as tkfont

# Placeholder imports - swap in your real client when ready
from client import UDP_Client

def main():
    root = tk.Tk()
    root.title("UDP Tool")
    root.geometry("1100x750")
    root.configure(background="#1a1a2e")
    root.resizable(False, False)
    client_udp = UDP_Client()
    # ── Colour palette ──────────────────────────────────────────────
    BG          = "#1a1a2e"
    CARD        = "#16213e"
    ACCENT      = "#0f3460"
    BTN_IDLE    = "#0f3460"
    BTN_HOVER   = "#1a4a80"
    BTN_ACTIVE  = "#e94560"
    FG          = "#eaeaea"
    FG_DIM      = "#8892a4"
    ENTRY_BG    = "#0d1b2a"
    BORDER      = "#2a3a5c"

    # ── Helpers ─────────────────────────────────────────────────────
    def make_label(parent, text, size=13, bold=False, color=FG):
        weight = "bold" if bold else "normal"
        return tk.Label(parent, text=text,
                        bg=parent["bg"] if hasattr(parent, "__getitem__") else BG,
                        fg=color,
                        font=("Courier New", size, weight))

    def make_entry(parent, width=22):
        e = tk.Entry(parent,
                     font=("Courier New", 14),
                     bg=ENTRY_BG, fg=FG,
                     insertbackground=FG,
                     relief="flat",
                     bd=0,
                     width=width,
                     highlightthickness=1,
                     highlightbackground=BORDER,
                     highlightcolor=BTN_ACTIVE)
        return e

    def make_button(parent, text, command=None, accent=False, width=18):
        color = BTN_ACTIVE if accent else BTN_IDLE
        btn = tk.Button(parent,
                        text=text,
                        command=command,
                        font=("Courier New", 12, "bold"),
                        bg=color,
                        fg=FG,
                        activebackground=BTN_HOVER,
                        activeforeground=FG,
                        relief="flat",
                        bd=0,
                        cursor="hand2",
                        width=width,
                        pady=10)
        # hover effect
        def on_enter(e): btn.config(bg=BTN_ACTIVE)
        def on_leave(e): btn.config(bg=color)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    def section_frame(parent, padx=30, pady=15):
        f = tk.Frame(parent, bg=CARD,
                     highlightthickness=1,
                     highlightbackground=BORDER)
        f.pack(fill="x", padx=padx, pady=pady)
        return f

    # ── Title bar ────────────────────────────────────────────────────
    title_bar = tk.Frame(root, bg=ACCENT, height=50)
    title_bar.pack(fill="x")
    title_bar.pack_propagate(False)
    tk.Label(title_bar, text="[ UDP TOOL ]",
             bg=ACCENT, fg=BTN_ACTIVE,
             font=("Courier New", 16, "bold")).pack(side="left", padx=20, pady=10)
    tk.Label(title_bar, text="network diagnostics v0.1",
             bg=ACCENT, fg=FG_DIM,
             font=("Courier New", 10)).pack(side="right", padx=20, pady=14)

    # ── Connection section ───────────────────────────────────────────
    conn_frame = section_frame(root, pady=(20, 8))
    conn_inner = tk.Frame(conn_frame, bg=CARD)
    conn_inner.pack(fill="x", padx=20, pady=15)

    # IP + Port side by side
    fields_row = tk.Frame(conn_inner, bg=CARD)
    fields_row.pack(fill="x")

    ip_col = tk.Frame(fields_row, bg=CARD)
    ip_col.pack(side="left", expand=True, fill="x", padx=(0, 20))
    tk.Label(ip_col, text="IP", bg=CARD, fg=FG_DIM,
             font=("Courier New", 11, "bold")).pack(anchor="w")
    ip_input = make_entry(ip_col, width=28)
    ip_input.pack(fill="x", ipady=6, pady=(4, 0))

    port_col = tk.Frame(fields_row, bg=CARD)
    port_col.pack(side="left", expand=True, fill="x")
    tk.Label(port_col, text="Port", bg=CARD, fg=FG_DIM,
             font=("Courier New", 11, "bold")).pack(anchor="w")
    port_input = make_entry(port_col, width=28)
    port_input.pack(fill="x", ipady=6, pady=(4, 0))

    # Connection buttons row
    conn_btns = tk.Frame(conn_inner, bg=CARD)
    conn_btns.pack(fill="x", pady=(14, 0))

    def use_device():
        ip,port = client_udp.set_known_json_value(0)
        ip_input.delete(0, tk.END)
        port_input.delete(0, tk.END)
        ip_input.insert(0, ip)
        port_input.insert(0, port)

    def use_last():
        pass  # wire to your JSON loader

    def add_connection():
        pass  # wire to your JSON saver

    make_button(conn_btns, "Use Device",        command=use_device).pack(side="left", padx=(0,10))
    make_button(conn_btns, "Use Last Connection",command=use_last).pack(side="left", padx=(0,10))
    make_button(conn_btns, "Add New Connection", command=add_connection).pack(side="left")

    # ── Packet loss section ──────────────────────────────────────────
    pkt_frame = section_frame(root, pady=8)
    pkt_inner = tk.Frame(pkt_frame, bg=CARD)
    pkt_inner.pack(fill="x", padx=20, pady=15)

    pkt_row = tk.Frame(pkt_inner, bg=CARD)
    pkt_row.pack(fill="x", pady=(4, 0))

    pkt_loss_col = tk.Frame(pkt_row, bg=CARD)
    pkt_loss_col.pack(side="left", padx=(0, 20), anchor="s")
    tk.Label(pkt_loss_col, text="% Of Packet Loss", bg=CARD, fg=FG_DIM,
             font=("Courier New", 11, "bold")).pack(anchor="w")
    pkt_input = make_entry(pkt_loss_col, width=18)
    pkt_input.pack(ipady=6)

    num_pkt_col = tk.Frame(pkt_row, bg=CARD)
    num_pkt_col.pack(side="left", padx=(0, 20), anchor="s")
    tk.Label(num_pkt_col, text="# Of Packets", bg=CARD, fg=FG_DIM,
             font=("Courier New", 11, "bold")).pack(anchor="w")
    num_packets_input = make_entry(num_pkt_col, width=18)
    num_packets_input.pack(ipady=6)

    def drop_packets():
        val = pkt_input.get().strip()
        print(f"Dropping {val}% of packets")
        num_pack = num_packets_input.get().strip()
        print(f"Total Number of Packets {num_pack}")
        
    btn_col = tk.Frame(pkt_row, bg=CARD)
    btn_col.pack(side="left", anchor="s")
    make_button(btn_col, "Drop Packets", command=drop_packets, accent=True, width=16).pack(ipady=3)

    # ── Send section ─────────────────────────────────────────────────
    send_frame = section_frame(root, pady=8)
    send_inner = tk.Frame(send_frame, bg=CARD)
    send_inner.pack(fill="x", padx=20, pady=15)

    tk.Label(send_inner, text="Actions", bg=CARD, fg=FG_DIM,
             font=("Courier New", 11, "bold")).pack(anchor="w", pady=(0, 10))

    send_btns = tk.Frame(send_inner, bg=CARD)
    send_btns.pack(fill="x")

    def send_hello():
        ip   = ip_input.get().strip()
        port = port_input.get().strip()
        print(f"Sending hello to {ip}:{port}")
        # client_udp.send(ip, int(port))

    def send_packets():
        ip   = ip_input.get().strip()
        port = port_input.get().strip()
        print(f"Sending packets to {ip}:{port}")
        # client_udp.test(ip, int(port))

    def send_file():
        print("Send file")

    make_button(send_btns, "Send Hello",   command=send_hello,   width=16).pack(side="left", padx=(0,10))
    make_button(send_btns, "Send Packets", command=send_packets, width=16).pack(side="left", padx=(0,10))
    make_button(send_btns, "Send File",    command=send_file,    width=16).pack(side="left")

    # ── Status bar ───────────────────────────────────────────────────
    status_bar = tk.Frame(root, bg=ACCENT, height=30)
    status_bar.pack(fill="x", side="bottom")
    status_bar.pack_propagate(False)
    tk.Label(status_bar, text="● idle",
             bg=ACCENT, fg=FG_DIM,
             font=("Courier New", 9)).pack(side="left", padx=15, pady=6)

    root.mainloop()

if __name__ == '__main__':
    main()