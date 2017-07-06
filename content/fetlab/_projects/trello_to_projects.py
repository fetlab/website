#!/usr/bin/env python
import trello, codecs, urllib, os, re

api_key = '5c69ca414c89485442be9d4d0247c272'
token   = '30d09dd9e25873008c85a4dc7cb04784313b24f4f8fcf1c3cf57718d8ccb677f'

def trello_to_md(list_name, board_name, org_name):
	client = trello.TrelloClient(api_key, token=token)
	orgs = {org.name: org for org in client.list_organizations()}

	try:
		if org_name == 'me':
			boards = {board.name: board for board in client.list_boards()}
		else:
			boards = {board.name: board for board in orgs[org_name].all_boards()}
	except KeyError:
		print u"Can't find %s in %s" % (org_name, orgs.keys())
		raise

	try:
		lists = {tlist.name: tlist for tlist in boards[board_name].all_lists()}
	except KeyError:
		print u"Can't find %s in %s" % (board_name, boards.keys())
		raise

	try:
		cards = {card.name: card for card in lists[list_name].list_cards()}
	except KeyError:
		print u"Can't find %s in %s" % (list_name, lists.keys())

	for card in cards.values():
		with codecs.open(card.name + u'.md', 'w', encoding='utf-8') as f:
			f.write(u"Title: {}\n\n".format(card.name))
			#Munge images for convenience
			desc = re.sub(
					r'(!\[.*\])\((.*)\)',
					r'<img alt="\1" src="projects/\2" style="width:50%" class="center-block">',
					card.description,
					flags=re.M)
			f.write(desc)
		for a in card.get_attachments():
			urllib.urlretrieve(a.url, os.path.basename(a.url))

if __name__ == "__main__":
	import sys

	trello_to_md('Projects for export', 'Research planning', 'me')
