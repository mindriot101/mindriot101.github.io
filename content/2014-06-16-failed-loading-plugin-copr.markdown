---
layout: post
title: "Failed loading plugin: copr"
date: Mon 16 Jun 16:09:35 BST 2014
comments: true
categories: linux fedora
---

If you're:

* running Fedora
* using dnf as a package manager
* get the following error: `Failed loading plugin: copr`

then listen up, your solution is at hand: install `python-requests` using yum:

```
sudo yum install -y python-requests
```

I have not tested if this will work installing with pip yet.
The linked bug report suggests that this will be registered as a dependency as of 2014-06-05 so this problem should go away.

Source: [this bug report](https://bugzilla.redhat.com/show_bug.cgi?id=1104088)


  
