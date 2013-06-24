# -*- coding: utf-8 -*-
from lxml import etree
from math import ceil
from copy import deepcopy

import argparse
import sys
import os

__version__ = (0, 0, 1)
__author__ = "Thomas Skowron (thomersch)"

elements_per_page = 10

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("feed", help="RSS/XML file which will be read.")
	parser.add_argument("-o", "--output", help="Output directory for paged feeds. If none specified, program writes to working directory.", default="./")
	parser.add_argument("-b", "--basename", help="Feed file basename. E.g. basename.1.xml. Default: feed", default="feed")
	parser.add_argument("-e", "--extension", help="Feed file extension. Default: xml", default="xml")
	parser.add_argument("-u", "--baseurl", help="Base url for link field. E.g. http://example.com/feeds/", default="/")
	args = parser.parse_args()

	if not args.baseurl.endswith("/"):
		args.baseurl += "/"

	with open(args.feed, "r") as f:
		parseAndConvert(f, args)

def parseAndConvert(stream, args):
	xmltree = etree.parse(stream)
	items = xmltree.findall("//item")
	for item in items:
		item.getparent().remove(item)

	number_of_pages = int(ceil(len(items)/float(elements_per_page)))

	for p in range(number_of_pages):
		pageitems = items[elements_per_page*p:elements_per_page*(p+1)]
		currentpagexml = deepcopy(xmltree)
		h = currentpagexml.find("//channel")
		first = "{}{}.{}".format(args.baseurl, args.basename, args.extension)
		last = "{}{}.{}.{}".format(args.baseurl, args.basename, number_of_pages, args.extension)
		next = "{}{}.{}.{}".format(args.baseurl, args.basename, str(p+1), args.extension)
		if p == 1:
			h.append(etree.Element("link", rel="previous", href=first))
		elif p > 1:
			previous = "{}{}.{}.{}".format(args.baseurl, args.basename, str(p-1), args.extension)
			h.append(etree.Element("link", rel="previous", href=previous))

		h.append(etree.Element("link", rel="next", href=next))
		h.append(etree.Element("link", rel="last", href=last))
		h.append(etree.Element("link", rel="first", href=first))

		for pageitem in pageitems:
			h.append(pageitem)
		
		if p == 0:
			filename = "{}.{}".format(args.basename, args.extension)
		else:
			filename = "{}.{}.{}".format(args.basename, str(p), args.extension)

		with open(os.path.join(args.output, filename), "w+") as p:
			p.write(etree.tostring(currentpagexml, pretty_print=True))

if __name__ == "__main__":
	main()