# Handlevault · Crisp Suite Studio

**Crisp Suite Studio** is a collection of browser-based creative and productivity products by **Handlevault**. Each product has its own name and purpose; **Pixel Studio is one app in the suite, not the name of the whole collection**. The products are in public beta. They run in your browser; drafts are stored in that browser, and uploaded images are processed locally.

## Products

- **[Pixel Studio](https://handlevault-official.github.io/crisp-pixel-studio/)** — create, edit, animate, convert, and export pixel art in your browser.
- **[Invoice Studio](https://handlevault-official.github.io/crisp-pixel-studio/invoice.html)** — create invoices with editable business and client details, line items, currency, tax, and discount calculations; print or save as PDF.
- **[Resume & CV Studio](https://handlevault-official.github.io/crisp-pixel-studio/resume.html)** — build a resume or CV with editable sections, design themes, a live preview, local draft controls, and print/PDF output.
- **[Moonlit Beads](https://handlevault-official.github.io/crisp-pixel-studio/moonlit-beads.html)** — turn an image into a bead-pattern chart with palette and grid settings, color quantities, and export/print options.

## Seasonal add-on

**[Seasonal Studio](https://handlevault-official.github.io/crisp-pixel-studio/seasonal-studio.html)** is an optional seasonal-theme add-on for browsing and using the suite's apps. It is separate from the four products above, not a separate name for Pixel Studio or Moonlit Beads.

## Notes

- These are browser-based tools; there is no account or cloud sync. Browser-local drafts may not transfer between devices or browsers.
- Invoice Studio creates documents but does not send invoices, accept payments, or provide tax or legal advice. Check local invoice requirements before use.
- PDF output uses your browser’s print dialog. Choose **Save as PDF** there.
- The products are in beta. Please review generated output before using or sharing it, and report bugs through [GitHub Issues](https://github.com/handlevault-official/crisp-pixel-studio/issues).
- Support development on [Ko-fi](https://ko-fi.com/handlevaultofficial).

## Run locally

Clone the repository and open `index.html` in a modern browser. Each product is a standalone HTML file in the repository root; no build step or Python backend is required.

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
