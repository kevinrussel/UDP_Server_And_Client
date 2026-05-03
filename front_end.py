import tkinter as tk



def create_window(root):
    root.title("UDP")
    root.geometry("1600x1000")
    return root

def create_box(root):
    frame = tk.Frame(
        root,
        bg="white",
        width=1200,
        height=300,
        relief="solid",   # gives it a border
        borderwidth=1
    )
    frame.place(x = 200, y = 50)
    return frame

def main():
    root = tk.Tk()
    create_window(root)

    root.configure(background="grey")
    box = create_box(root)
    root.mainloop()

if __name__ == '__main__':
    print("hitting")
    main()