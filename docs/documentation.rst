Documentation
=================

Audio
-----------------

.. autofunction:: mediaify.encode_audio
.. autofunction:: mediaify.batch_encode_audio
.. autoclass:: mediaify.AudioFile
    :members: data, mimetype, type, save
    :undoc-members:
    :noindex:

Image
-----------------

.. autofunction:: mediaify.encode_image
.. autofunction:: mediaify.batch_encode_image
.. autoclass:: mediaify.ImageFile
    :members: data, mimetype, ext, width, height, save
    :undoc-members:
    :noindex:

Animation
-----------------

.. autofunction:: mediaify.encode_animation
.. autofunction:: mediaify.batch_encode_animation
.. autoclass:: mediaify.AnimationFile
    :members: data, mimetype, ext, height, width, frame_count, duration, save
    :undoc-members:
    :noindex:

Video
-----------------

.. autofunction:: mediaify.encode_video
.. autofunction:: mediaify.batch_encode_video
.. autoclass:: mediaify.VideoFile
    :members: data, mimetype, ext, height, width, duration, framerate, hasAudio, save
    :undoc-members:
    :noindex:

Utils
-----------------

.. autofunction:: mediaify.guess_type

Configs
-----------------

Audio Configs
~~~~~~~~~~~~~~~~~

.. autoclass:: mediaify.MP3Format
    :members:
    :undoc-members:
.. autoclass:: mediaify.OpusFormat
    :members:
    :undoc-members:
.. autoclass:: mediaify.FLACFormat
    :members:
    :undoc-members:
.. autoclass:: mediaify.WAVFormat
    :members:
    :undoc-members:

Image Configs
~~~~~~~~~~~~~~~~~

.. autoclass:: mediaify.WEBPImageFormat
    :members:
    :undoc-members:
.. autoclass:: mediaify.JPEGFormat
    :members:
    :undoc-members:
.. autoclass:: mediaify.PNGFormat
    :members:
    :undoc-members:

Animation Configs
~~~~~~~~~~~~~~~~~

.. autoclass:: mediaify.GIFFormat
    :members:
    :undoc-members:
.. autoclass:: mediaify.WEBPAnimationFormat
    :members:
    :undoc-members:

Video Configs
~~~~~~~~~~~~~~~~~

.. autoclass:: mediaify.WEBMFormat
    :members:
    :undoc-members:
.. autoclass:: mediaify.MP4Format
    :members:
    :undoc-members:
.. autoclass:: mediaify.VideoPreviewAnimationEncoding
    :members:
    :undoc-members:

Codecs
~~~~~~~~~~~~~~~~~

.. autoclass:: mediaify.H264Codec
    :members:
    :undoc-members:
.. autoclass:: mediaify.VP9Codec
    :members:
    :undoc-members:
.. autoclass:: mediaify.AV1Codec
    :members:
    :undoc-members:
.. autoclass:: mediaify.OpusCodec
    :members:
    :undoc-members:

Shared Configs
~~~~~~~~~~~~~~~~~

.. autoclass:: mediaify.UnencodedEncoding
    :members:
    :undoc-members:
.. autoclass:: mediaify.ThumbnailEncoding
    :members:
    :undoc-members:

Resize Configs
~~~~~~~~~~~~~~~~~

.. autoclass:: mediaify.MaxResolutionResize
    :members:
    :undoc-members:
.. autoclass:: mediaify.TargetResolutionResize
    :members:
    :undoc-members:
