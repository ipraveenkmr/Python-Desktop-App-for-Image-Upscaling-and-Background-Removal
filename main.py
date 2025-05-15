import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from rembg import remove
import io

class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Remover")
        self.root.geometry("850x600")
        self.root.configure(bg="#1e1e1e")  # Set window background to black

        # Frame for buttons at the top
        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(pady=30)

        button_width = 20  # Width in characters

        self.upload_btn = tk.Button(btn_frame, text="Upload Image", command=self.upload_image,
                                    bg="#FFFFFF", fg="#222222", width=button_width)
        self.upload_btn.grid(row=0, column=0, padx=10)

        self.upscale_btn = tk.Button(btn_frame, text="Upscale Image", command=self.upscale_image,
                                     state=tk.DISABLED, bg="#444444", fg="#F5F5F5", width=button_width)
        self.upscale_btn.grid(row=0, column=1, padx=10)

        self.remove_btn = tk.Button(btn_frame, text="Remove Background", command=self.remove_bg,
                                    state=tk.DISABLED, bg="#373737", fg="#F5F5F5", width=button_width)
        self.remove_btn.grid(row=0, column=2, padx=10)

        self.save_btn = tk.Button(btn_frame, text="Save Result", command=self.save_image,
                                  state=tk.DISABLED, bg="#373737", fg="#F5F5F5", width=button_width)
        self.save_btn.grid(row=0, column=3, padx=10)

        # Frame for image display (centered below buttons)
        image_frame = tk.Frame(root, bg="#1e1e1e")
        image_frame.pack(pady=10)

        self.image_panel = tk.Label(image_frame, bg="#1e1e1e")
        self.image_panel.grid(row=0, column=0, padx=20)

        self.result_panel = tk.Label(image_frame, bg="#1e1e1e")
        self.result_panel.grid(row=0, column=1, padx=20)

        self.original_image = None
        self.result_image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if file_path:
            self.original_image = Image.open(file_path).convert("RGBA")
            img = self.original_image.resize((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            self.image_panel.configure(image=img_tk)
            self.image_panel.image = img_tk

            # Clear previous result image and disable save button
            self.result_panel.configure(image='')
            self.result_panel.image = None
            self.save_btn.config(state=tk.DISABLED)
            self.result_image = None

            self.remove_btn.config(state=tk.NORMAL)
            self.upscale_btn.config(state=tk.NORMAL)


    def upscale_image(self):
        if self.original_image:
            width, height = self.original_image.size
            new_size = (width * 2, height * 2)
            self.original_image = self.original_image.resize(new_size, Image.LANCZOS)
            img = self.original_image.resize((300, 300))  # Resize preview for display
            img_tk = ImageTk.PhotoImage(img)
            self.image_panel.configure(image=img_tk)
            self.image_panel.image = img_tk
            messagebox.showinfo("Upscaled", "Image upscaled successfully!")

    def remove_bg(self):
        if self.original_image:
            buffered = io.BytesIO()
            self.original_image.save(buffered, format="PNG")
            result = remove(buffered.getvalue())
            self.result_image = Image.open(io.BytesIO(result)).convert("RGBA")
            img = self.result_image.resize((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            self.result_panel.configure(image=img_tk)
            self.result_panel.image = img_tk
            self.save_btn.config(state=tk.NORMAL)

    def save_image(self):
        if self.result_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png")])
            if file_path:
                self.result_image.save(file_path)
                messagebox.showinfo("Saved", "Image saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()
