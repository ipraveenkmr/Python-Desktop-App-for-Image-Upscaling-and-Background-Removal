# Background Remover App

A Python GUI application to remove backgrounds from images, with an optional image upscaling feature. Built with Tkinter, `rembg`, and `Pillow`.

---

## Features

- Upload images (PNG, JPG, JPEG)
- Upscale images before background removal
- Remove image backgrounds using AI (`rembg`)
- Save the processed image
- Simple and clean GUI interface

---

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python -m venv venv



* On Windows:

  ```bash
  venv\Scripts\activate
  ```
* On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### 2. Install dependencies

```bash
pip install rembg pillow pyinstaller
```

### 3. Freeze dependencies to a file

```bash
pip freeze > requirements.txt
```

---

## Running the App

Start the app by running:

```bash
python main.py
```

---

## Building an Executable

To create a standalone executable (without console window):

```bash
pyinstaller --noconsole --onefile main.py
```

The executable will be available in the `dist` folder.

---

## Usage

1. Click **Upload Image** to select an image file.
2. (Optional) Click **Upscale Image** to increase image resolution.
3. Click **Remove Background** to process the image.
4. Click **Save Result** to save the background-removed image.

---

## Notes

* Tested with Python 3.7+.
* Virtual environment recommended for dependency management.
* The app GUI has a dark theme for better viewing experience.



