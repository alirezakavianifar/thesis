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
                fig_dims[(im.size[0], im.size[1])] = (f, im.size[0], im.size[1])
        except Exception:
            pass

# Map rendered images in PDF
pdf_renders = []
for p_idx in range(len(doc)):
    page = doc[p_idx]
    for img in page.get_images(full=True):
        xref = img[0]
        base_img = doc.extract_image(xref)
        w, h = base_img['width'], base_img['height']
        match = fig_dims.get((w, h))
        fname = match[0] if match else f"unknown_{w}x{h}"
        rects = page.get_image_rects(xref)
        r = rects[0] if rects else None
        rw = r.width if r else 0
        rh = r.height if r else 0
        pdf_renders.append({
            'page': p_idx + 1,
            'file': fname,
            'w_pt': rw,
            'h_pt': rh,
            'pct_tw': (rw / 425.2 * 100) if rw else 0
        })

# Parse tex files
chapters = [
    'chapters/chapter1.tex',
    'chapters/chapter2.tex',
    'chapters/chapter3.tex',
    'chapters/chapter4.tex',
    'chapters/chapter5.tex',
    'chapters/chapter6.tex',
    'chapters/appendices.tex'
]

fig_pattern = re.compile(r'\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}', re.DOTALL)
label_pattern = re.compile(r'\\label\{([^}]+)\}')
inc_pattern = re.compile(r'\\includegraphics\[(.*?)\]\{([^}]+)\}')
caption_pattern = re.compile(r'\\caption(?:\[(.*?)\])?\{([^}]+)\}')

print("================================================================================")
print("COMPREHENSIVE AUDIT OF ALL FIGURES IN THESIS")
print("================================================================================")

all_figs = []
for chap in chapters:
    if not os.path.exists(chap): continue
    with open(chap, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Also find all refs in this file
    for fig_m in fig_pattern.finditer(content):
        ftext = fig_m.group(1)
        lbl_m = label_pattern.search(ftext)
        lbl = lbl_m.group(1) if lbl_m else 'NO_LABEL'
        inc_m = inc_pattern.search(ftext)
        opts = inc_m.group(1) if inc_m else ''
        fpath = inc_m.group(2) if inc_m else ''
        cap_m = caption_pattern.search(ftext)
        cap = cap_m.group(2)[:60] if cap_m else ''
        
        # line number
        start_line = content[:fig_m.start()].count('\n') + 1
        
        # count references across all chapters
        all_refs = []
        for other_chap in chapters:
            if not os.path.exists(other_chap): continue
            with open(other_chap, 'r', encoding='utf-8') as of:
                ocontent = of.read()
            for rm in re.finditer(r'\\ref\{' + re.escape(lbl) + r'\}', ocontent):
                rline = ocontent[:rm.start()].count('\n') + 1
                all_refs.append((other_chap, rline))
                
        # find matching render in PDF
        base_name = os.path.basename(fpath)
        matching_renders = [pr for pr in pdf_renders if pr['file'] == base_name]
        
        all_figs.append({
            'chap': chap,
            'label': lbl,
            'opts': opts,
            'file': base_name,
            'line': start_line,
            'caption': cap,
            'refs': all_refs,
            'renders': matching_renders
        })

for fig in all_figs:
    ref_str = f"{len(fig['refs'])} refs"
    if fig['refs']:
        ref_details = ", ".join([f"{os.path.basename(c)}:L{l}" for c, l in fig['refs'][:2]])
        ref_str += f" ({ref_details})"
    else:
        ref_str = "!!! UNREFERENCED (0 refs) !!!"
        
    render_str = ""
    if fig['renders']:
        render_str = ", ".join([f"Page {r['page']} ({r['pct_tw']:.1f}% textwidth, {r['w_pt']:.0f}x{r['h_pt']:.0f}pt)" for r in fig['renders']])
    else:
        render_str = "NOT FOUND IN PDF"
        
    print(f"\n[{fig['label']}] in {os.path.basename(fig['chap'])}:L{fig['line']}")
    print(f"  File: {fig['file']} | LaTeX opts: [{fig['opts']}]")
    print(f"  Refs: {ref_str}")
    print(f"  PDF Render: {render_str}")
