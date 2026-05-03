import tkinter as tk



def create_window(root):
    root.title("UDP")
    root.geometry("1500x1000")
    return root



def main():
    root = tk.Tk()
    create_window(root)

    root.configure(background="grey")
    root.mainloop()

if __name__ == '__main__':
    print("hitting")
    main()