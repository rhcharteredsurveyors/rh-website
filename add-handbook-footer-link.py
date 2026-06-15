#!/usr/bin/env python3
"""
Adds the "Tenant's Handbook" link to the Practice column of the footer
on every .html page in a folder.

HOW TO USE
  1. Put this file in your RHCS-Website folder (the one with all the .html pages).
  2. Open a terminal in that folder and run:
        python3 add-handbook-footer-link.py
     (or point it at the folder:  python3 add-handbook-footer-link.py path\\to\\RHCS-Website )
  3. It only changes pages that have the standard footer and don't already
     have the link, so it is safe to run more than once, and safe to run after
     you've saved the pages Rob already edited (those get skipped).
  4. Check a couple of pages, then push the changed files to GitHub.
"""
import sys, glob, os

OLD = """        <div class="footer-col-title">Practice</div>
        <ul>
          <li><a href="about.html">About Rob</a></li>
          <li><a href="insights.html">Insights</a></li>
          <li><a href="properties.html">Properties</a></li>
          <li><a href="compliance.html">Compliance</a></li>
          <li><a href="privacy.html">Privacy</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>"""

NEW = """        <div class="footer-col-title">Practice</div>
        <ul>
          <li><a href="about.html">About Rob</a></li>
          <li><a href="insights.html">Insights</a></li>
          <li><a href="commercial-tenants-handbook.html">Tenant's Handbook</a></li>
          <li><a href="properties.html">Properties</a></li>
          <li><a href="compliance.html">Compliance</a></li>
          <li><a href="privacy.html">Privacy</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>"""

folder = sys.argv[1] if len(sys.argv) > 1 else "."
files = sorted(glob.glob(os.path.join(folder, "*.html")))

updated, skipped, warned = [], [], []
for path in files:
    s = open(path, encoding="utf-8").read()
    name = os.path.basename(path)
    if 'commercial-tenants-handbook.html">Tenant\'s Handbook' in s:
        skipped.append(name)          # already has the link
    elif OLD in s:
        open(path, "w", encoding="utf-8").write(s.replace(OLD, NEW, 1))
        updated.append(name)
    else:
        warned.append(name)           # footer not in the standard shape

print(f"\nScanned {len(files)} pages in: {os.path.abspath(folder)}\n")
print(f"Updated ({len(updated)}): " + (", ".join(updated) if updated else "none"))
print(f"Already linked, skipped ({len(skipped)}): " + (", ".join(skipped) if skipped else "none"))
if warned:
    print(f"\nNo standard footer found, check by hand ({len(warned)}):")
    print("  " + ", ".join(warned))
print("\nDone. Push the updated files to GitHub.")
