### Test of 120 images

First 30 images: 24 out of 30 correct (normal)

Second 30 images: 26 out of 30 correct (horizontally flip)

Third 30 images: 19 out of 30 correct (vertically flip)

Last 30 images: 20 out of 30 correct (rotate 90 degrees)

### Horizontally flip images

        magick mogrify -flop *.png
        gm mogrify -flop *.png

### Vertically flip images

        magick mogrify -flip *.png
        gm mogrify -flip *.png

### Clockwise rotate image

        magick mogrify -rotate 90 *.png
        gm mogrify -rotate 90 *.png
