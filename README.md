# Pixel Studio

**Pixel Studio** is a collection of four small, browser-based creative tools for indie creators. The project is in public beta. Apps run client-side; drafts are stored in the browser you use, and uploaded images are processed locally.

## Try the four apps

- **[Pixel Art Crisp Scaler](https://handlevault-official.github.io/crisp-pixel-studio/)** — upscale pixel art with nearest-neighbor rendering and download a PNG. The current scaler uses a fixed 4× scale.
- **[Invoice Studio](https://handlevault-official.github.io/crisp-pixel-studio/invoice.html)** — create an invoice with editable business and client details, line items, currency, tax and discount calculations; print or save as PDF.
- **[Resume & CV Studio](https://handlevault-official.github.io/crisp-pixel-studio/resume.html)** — build a resume or CV with editable sections, design themes, a live preview, local draft controls, and print/PDF output.
- **[Moonlit Beads](https://handlevault-official.github.io/crisp-pixel-studio/moonlit-beads.html)** — turn an image into a bead-pattern chart with palette and grid settings, color quantities, and export/print options.

## Seasonal browsing

[Seasonal Studio](https://handlevault-official.github.io/crisp-pixel-studio/seasonal-studio.html) is a seasonal-themed way to browse the apps; it is separate from the four tools listed above.

## Notes

- These are browser-based tools; there is no account or cloud sync. Browser-local drafts may not transfer between devices or browsers.
- Invoice Studio creates documents but does not send invoices, accept payments, or provide tax or legal advice. Check local invoice requirements before use.
- PDF output uses your browser’s print dialog. Choose **Save as PDF** there.
- The tools are in beta. Please review generated output before using or sharing it, and report bugs through [GitHub Issues](https://github.com/handlevault-official/crisp-pixel-studio/issues).
- Support development on [Ko-fi](https://ko-fi.com/handlevaultofficial).

## Run locally

Clone the repository and open `index.html` in a modern browser. Each tool is a standalone HTML file in the repository root; no build step or Python backend is required.

```bash
git clone https://github.com/handlevault-official/crisp-pixel-studio.git
cd crisp-pixel-studio
```

You can also serve the folder with any static file server. For example:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000/`.

## License

This project is released under the [MIT License](LICENSE).
