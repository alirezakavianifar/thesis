import fitz, os, re
from PIL import Image

doc = fitz.open('thesis_full_toc_persian_v3.pdf')

# Build mapping of image resolutions to filenames
fig_dims = {}
figures_dir = 'figures'
for f in os.listdir(figures_dir):
    p = os.path.join(figures_dir, f)
    if os.path.isfile(p):
        try:
            with Image.open(p) as im:
                fig_dims[(im.size[0], im.size[1])] = f
        except Exception:
            pass

print(f"Known image files on disk: {len(fig_dims)}")

# Map of (file) -> list of pages where rendered
pdf_images = []
for p_idx in range(len(doc)):
    page = doc[p_idx]
    for img in page.get_images(full=True):
        xref = img[0]
        base_img = doc.extract_image(xref)
        w, h = base_img['width'], base_img['height']
        fname = fig_dims.get((w, h), f"unknown_{w}x{h}")
        rects = page.get_image_rects(xref)
        r = rects[0] if rects else None
        rw = r.width if r else 0
        rh = r.height if r else 0
        pdf_images.append({
            'page': p_idx + 1,
            'file': fname,
            'size': (w, h),
            'w_pt': rw,
            'h_pt': rh,
            'pct_textwidth': (rw / 425.2 * 100) if rw else 0
        })

print(f"\nTotal rendered images in PDF: {len(pdf_images)}")
for pf in pdf_images:
    print(f"Page {pf['page']:3d}: {pf['file']:35s} | size {pf['size'][0]:4d}x{pf['size'][1]:4d} | rendered: {pf['w_pt']:5.1f}pt ({pf['pct_textwidth']:4.1f}% textwidth), h={pf['h_pt']:5.1f}pt")
