# Pixel Studio

**Pixel Studio** is a browser-based pixel-art editor for creating, editing, animating, converting, and sharing pixel art. It runs in your browser; your projects and gallery are stored locally on your device.

## Features

- Create a transparent pixel canvas up to 512 × 512 pixels.
- Import images and resize them to your canvas dimensions.
- Draw with pencil, eraser, fill, and color-picker tools.
- Undo and redo edits; crop or cut selected areas.
- Create animation frames and export animations as WebM where supported.
- Export PNG, JPEG, or WebP images, share/copy images, or save portable project files.
- Save projects to a browser-local gallery.
- Apply the shared arcade attention-font theme from `arcade-attention.css`.

## Use Pixel Studio

Open [Pixel Studio](https://handlevault-official.github.io/crisp-pixel-studio/).

The `index.html` file is the standalone Pixel Studio app. Other browser tools in this repository have their own pages, including Invoice Studio, Resume & CV Studio, Moonlit Beads, and the optional Seasonal Studio add-on.

## Privacy and limitations

- No account or cloud sync is required. Browser-local projects may not transfer between devices or browsers.
- WebM animation export depends on browser recording support.
- Please review exported files before sharing or using them.
- Support development on [Ko-fi](https://ko-fi.com/handlevaultofficial).

## Run locally

Open `index.html` in a modern browser, or serve the folder with a static file server:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000/`.

## License

This project is released under the [MIT License](LICENSE).
