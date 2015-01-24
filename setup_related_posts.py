#!/usr/bin/env python

import re
import sys

from glob import glob


SEP = "\n<!-- DO NOT EDIT BELOW THIS LINE -->\n* * *"


def load(filename):
   """Load a file containing groups of posts to be cross-linked.

   The format is: a post per line, group separated by an empty line.

   """
   groups = open(filename).read().split("\n\n")
   groups = [set(group.strip().split("\n")) for group in groups]
   return groups


def check(groups, posts):
   """Check that each referenced post exist."""
   for group in groups:
      for post in group:
         if post not in posts:
            print >> sys.stderr, "Post %s not found" % post
            return False
   return True


def find_contents_and_titles(posts):
   """Extract the non-auto-generated content and the title of each post."""
   contents = {}
   titles = {}
   for post in posts:
      contents[post] = open("./_posts/%s.md" % post).read().split(SEP)[0]
      title_match = re.search(r'title: (.*)', contents[post])
      if title_match is None:
         print >> sys.stderr, "Cannot find title for post %s" % post
         titles[post] = ""
      else:
         titles[post] = title_match.group(1).strip("'")
   return contents, titles

def build_links(series, related, titles):
   """Build and return the cross-link part of the post."""
   if series == set() and related == set():
      return ""

   # Keep only related posts that are not part of the series.
   related.difference_update(series)

   links = [SEP]
   if series != set():
      links.append("\n\n### Part of this series\n\n")
      for i, post in enumerate(sorted(series)):
         links.append("1. [%s][%d]\n" % (titles[post], i + 1000))
      links.append("\n")
      for i, post in enumerate(sorted(series)):
         links.append(" [%d]: {%% post_url %s %%}\n" % (i + 1000, post))

   if related != set():
      links.append("\n\n### See also\n\n")
      for i, post in enumerate(sorted(related)):
         links.append("1. [%s][%d]\n" % (titles[post], i + 2000))
      links.append("\n")
      for i, post in enumerate(sorted(related)):
         links.append(" [%d]: {%% post_url %s %%}\n" % (i + 2000, post))

   return "".join(links)


def run():
   """Main function.

   Load all cross-linked content from series.txt and related.txt, and
   rewrites all posts to update the cross-link part.

   """
   posts = [path.replace("./_posts/", "").replace(".md", "")
            for path in glob("./_posts/*.md")]

   series = load("./series.txt")
   if not check(series, posts):
      return 1

   related = load("./related.txt")
   if not check(related, posts):
      return 1

   contents, titles = find_contents_and_titles(posts)

   for post in posts:
      this_series = set()
      this_related = set()

      # Find posts to link
      for group in series:
         if post in group:
            this_series = set(group)
      for group in related:
         if post in group:
            this_related = set(group)

      this_related.discard(post)

      links = build_links(this_series, this_related, titles)

      with open("./_posts/%s.md" % post, "w") as f:
         f.write(contents[post] + links)

   return 0


if __name__ == "__main__":
   sys.exit(run());
