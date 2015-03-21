#!/usr/bin/env python

import os
import re
import sys

from glob import glob


def run():
   """Main function.

   Will remove all images starting with 'thumbnail_', and create new
   thumbnails for the width specified in the posts.

   """
   # Finding the widths of the thumbnails.
   widths = {}
   for post in glob("./_posts/*.md"):
      content = open(post).read()
      figures = re.findall(r'{% include figure\.html .* %}', content) \
                + re.findall(r'{% include gallery\.html .* %}', content)
      for figure in figures:
         url = re.search(r"url=\'([^\']*)\'", figure).groups()[0]
         try:
            width = re.search(r"width=([^ ]*)", figure).groups()[0]
            if url not in widths:
               widths[url] = set()
            widths[url].add(width)
         except:
            continue

   # Removing existing thumbnails.
   thumbnails = glob("./images/thumbnail_*")
   for thumbnail in thumbnails:
      print "Deleting", thumbnail
      os.unlink(thumbnail)

   # Creating the new thumbnails.
   for image in widths:
      for width in widths[image]:
         name = "./images/" + image
         newname = ("./images/thumbnail_%s_" % width) + image
         print "Converting", image
         os.system("convert %s -resize %s %s" % (name, width, newname))

   return 0


if __name__ == "__main__":
   sys.exit(run());
