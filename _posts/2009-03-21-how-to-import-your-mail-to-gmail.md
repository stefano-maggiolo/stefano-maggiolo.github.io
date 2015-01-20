---
title: How to import your mail to GMail
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2009/03/how-to-import-your-mail-to-gmail/
categories:
  - Software
---
There are many blog posts with the same title, but since there seems to be also many GMail's different behaviors, I'm adding mine to the list.  

<!--more-->

The usual steps one could try to import its mails to GMail (from an offline client) is the following:

  * add GMail's IMAP to its client's accounts;
  * copy local messages to the right GMail folder.

This obvious attempt fails because for some strange reason, in my configuration (Claws mail as offline client, but with Evolution nothing change) the mails' order is completely screwed in the messages' list. This is so since the date displayed in the messages' list is the date GMail, not you, received the mail. Strange enough, looking at the single message, the date displayed is the correct one. I tried using [GMail Loader][1], but the problem was still there.

 [1]: http://marklyon.org/gmail/

Instead, what works is letting GMail retrieve the mails from a POP3 server. If you, like me, are migrating from a complete mail stack (Fetchmail, Postfix, Courier, &hellip;), it is quite simple: just install Courier's POP3 package and it will offers by default all mails contained in the INBOX folder. Then do the following:

  * move the mails you have in the INBOX folder in some subfolder;
  * add a POP3 account "your\_username@your\_public_IP" to the account GMail watches;
  * for every folder you want to import, move the mails in it to the INBOX folder, go to GMail and tell it to download the mails (in the settings' page); then attach to all these mail the right label and store them.

Of course if you are behind a firewall you have to forward port 110 (POP3's port) to your local IP address.

In this way, the dates are correct everywhere, plus sent messages goes to GMail's sent messages (if you configured GMail to send mails with your old address); moreover, conversation partially already in GMail are unified.
