import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk, ImageFilter, ImageOps


class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600")
        self.original_image = None
        self.modified_image = None
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        self.open_button = tk.Button(self.root, text="Открыть изображение", command=self.open_image)
        self.open_button.pack()

        self.apply_effect_negative = tk.Button(self.root, text="Добавить негатив", command=self.negative_photo)
        self.apply_effect_negative.pack()

        self.apply_effect_blur = tk.Button(self.root, text="Добавить блюр", command=self.blur_photo)
        self.apply_effect_blur.pack()

        self.apply_effect_rotate = tk.Button(self.root, text="Повернуть", command=self.rotate_photo)
        self.apply_effect_rotate.pack()

        self.apply_sepia = tk.Button(self.root, text="Добавить эффект сепии", command=self.apply_effect_sepia)
        self.apply_sepia.pack()

        self.apply_undo = tk.Button(self.root, text="Откатить", command=self.undo_last_action)
        self.apply_undo.pack()

        self.save_button = tk.Button(self.root, text="Сохранить", command=self.save_image)
        self.save_button.pack()

        self.image_label = tk.Label(self.root)
        self.image_label.pack()

    def undo_last_action(self):
        if self.history:
            self.modified_image = self.history.pop()
            self.display_image(self.modified_image)

    def negative_photo(self):
        if self.modified_image:
            self.history.append(self.modified_image.copy())
            self.modified_image = ImageOps.invert(self.modified_image)
            self.display_image(self.modified_image)

    def blur_photo(self):
        if self.modified_image:
            self.history.append(self.modified_image.copy())
            self.modified_image = self.modified_image.filter(ImageFilter.GaussianBlur(30.0))
            self.display_image(self.modified_image)

    def rotate_photo(self):
        if self.modified_image:
            self.history.append(self.modified_image.copy())
            self.modified_image = self.modified_image.rotate(90, expand=True)
            self.display_image(self.modified_image)

    def open_image(self):
        filename = filedialog.askopenfilename(
            filetypes=(("PNG files", "*.png"), ("JPEG/JPG files", "*.jpg;*.jpeg"), ("All files", "*.*")))
        if filename:
            self.original_image = Image.open(filename)
            self.modified_image = self.original_image.copy()
            self.modified_image = self.modified_image.convert("RGB")
            self.display_image(self.modified_image)

    def save_image(self):
        if self.modified_image:
            filename = filedialog.asksaveasfilename(defaultextension=".png",
                                                    filetypes=(
                                                        ("PNG files", "*.png"),
                                                        ("All files", "*.*")
                                                    ))
            if filename:
                self.modified_image.save(filename)

    def apply_effect_sepia(self):
        if self.modified_image:
            self.history.append(self.modified_image.copy())
            gray = self.modified_image.convert("L")
            self.modified_image = Image.merge(
                "RGB",
                (
                    gray.point(lambda x: x * 240 / 255),
                    gray.point(lambda x: x * 200 / 255),
                    gray.point(lambda x: x * 145 / 255)
                )
            )
        self.display_image(self.modified_image)

    def display_image(self, image):
        width, height = image.size
        if width > height:
            if width > 400:
                ratio = 400 / width
            else:
                ratio = 1
        else:
            if height > 400:
                ratio = 400 / height

            else:
                ratio = 1
        image = image.resize(
            (int(width * ratio), (int(height * ratio)))
        )
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo


root = tk.Tk()
root.title("Image Editor")
editor = ImageEditor(root)
root.mainloop()
