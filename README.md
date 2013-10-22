# RSS pager

Splits a long RSS feed into a RFC 5005 paged feed.

Works with Python 2.7, no external dependencies.

## Usage
	usage: rsspager.py [-h] [-o OUTPUT] [-b BASENAME] [-e EXTENSION] [-u BASEURL]
	                   feed

	positional arguments:
	  feed                  RSS/XML file which will be read.

	optional arguments:
	  -h, --help            show this help message and exit
	  -o OUTPUT, --output OUTPUT
	                        Output directory for paged feeds. If none specified,
	                        program writes to working directory.
	  -b BASENAME, --basename BASENAME
	                        Feed file basename. E.g. basename.1.xml. Default: feed
	  -e EXTENSION, --extension EXTENSION
	                        Feed file extension. Default: xml
	  -u BASEURL, --baseurl BASEURL
	                        Base url for link field. E.g.
	                        http://example.com/feeds/

## License

	The MIT License (MIT)

	Copyright (c) 2013, Thomas Skowron

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in
	all copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
	THE SOFTWARE.
