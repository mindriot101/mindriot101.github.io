layout: post
title: Tiling png images in linux
date: Thu Jun 26 16:25:31 BST 2014
comments: true
categories: linux
Category: Linux

For printing multiple images, it's usually handy to tile images so that more than one page fits on a piece of paper at once. This can be achieved with ImageMagick and the `montage` command.

### Building a tiled image

For a 2x2 image an example command is:

```
montage -tile 2x2 -geometry 1600x1200 1.png 2.png 3.png 4.png output.png
```

*Be careful with the output specification, as if you forget it it'll overwrite the last png in the list.*

This command produces a 1600x1200 sized image with 4 pngs arranged in a 2x2 grid. For more options see the man pages.
