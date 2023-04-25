Mediaify
=================

.. toctree::
   :maxdepth: 4

   documentation
   guide

Media encoding made simple!

Encode media without the hassle of wrangling ffmpeg and pillow, instead declare your output declaratively!
::

    import mediaify
    with open('ricardo.gif', 'rb') as f:
        data = f.read()
    mediaify.batch_encode_animation(data)
    >>> [
        ImageFile(51x64, image/webp, 402.0B),
        ImageFile(102x128, image/webp, 808.0B),
        ImageFile(205x256, image/webp, 2.6KB),
        ImageFile(241x300, image/webp, 3.3KB),
        AnimationFile(241x300, 6.4s 128 frames, 20.00fps, image/gif, 400.3KB)
    ]
