#!/usr/bin/env python
from PIL import Image
from PIL.ImageOps import fit
import os, sys

if __name__ == "__main__":
	size = (1200, 500)
	for infile in sys.argv[1:]:
		print infile
		i = Image.open(infile)
		ic = fit(i, size, Image.ANTIALIAS, centering=(.5, .5))
		fn, ext = os.path.splitext(infile)
		os.rename(infile, "%s-bak.%s" % (fn, ext))
		ic.save(infile)
