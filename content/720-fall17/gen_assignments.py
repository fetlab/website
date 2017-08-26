"""Generate _assignments from assignments: open each file in
assignments, split on --- (which generates <hr> in Markdown), and
write the first half to the same filename in _assignments with a link
to the original file in assignments."""
import sys, os, re

for fn in os.listdir('assignments'):
	fp = os.path.join('assignments', fn)
	basename, ext = os.path.splitext(fn)
	if not os.path.isfile(fp) or ext != '.md':
		continue
	with open(fp) as f:
		l = f.read()
		l = re.sub('^Template:.*$', '', l, flags=re.M)
		h = re.split('^---\s*$', l, maxsplit=1, flags=re.M)
		if len(h > 1):
			with open(os.path.join('_assignments', fn), 'w') as f2:
				f2.write(h[0])
				f2.write('\n\n')
				f2.write('[Full details](assignments/{}.html)'.format(basename))
