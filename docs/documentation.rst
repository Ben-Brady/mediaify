Documentation
=================

Image
-----------------

.. autofunction:: mediaify.encode_image
.. autofunction:: mediaify.batch_encode_image
.. autofunction:: mediaify.load_image
.. autoclass:: mediaify.ImageFile
    :members: data, mimetype, ext, width, height
    :undoc-members:
    :noindex:

Animation
-----------------

.. autofunction:: mediaify.load_animation
.. autofunction:: mediaify.encode_animation
.. autofunction:: mediaify.batch_encode_animation
.. autoclass:: mediaify.AnimationFile
    :members: data, mimetype, ext, height, width, frame_count, duration
    :undoc-members:
    :noindex:

Video
-----------------

.. autofunction:: mediaify.load_video
.. autofunction:: mediaify.encode_video
.. autofunction:: mediaify.batch_encode_video
.. autoclass:: mediaify.VideoFile
    :members: data, mimetype, ext, height, width, duration, framerate, hasAudio
    :undoc-members:

Utils
-----------------

.. autofunction:: mediaify.guess_type

Configs
-----------------

Image Configs
~~~~~~~~~~~~~~~~~

.. autoclass:: mediaify.configs.WEBPImageEncodeConfig
    :members:
    :undoc-members:
.. autoclass:: mediaify.configs.PNGEncodeConfig
    :members:
    :undoc-members:
.. autoclass:: mediaify.configs.JPEGEncodeConfig
    :members:
    :undoc-members:

Animation Configs
~~~~~~~~~~~~~~~~~

.. autoclass:: mediaify.configs.GIFEncodeConfig
    :members:
    :undoc-members:
.. autoclass:: mediaify.configs.WEBPAnimationEncodeConfig
    :members:
    :undoc-members:

Video Configs
~~~~~~~~~~~~~~~~~

.. autoclass:: mediaify.configs.WEBMEncodeConfig
    :members:
    :undoc-members:
.. autoclass:: mediaify.configs.MP4EncodeConfig
    :members:
    :undoc-members:
.. autoclass:: mediaify.configs.VideoPreviewAnimationConfig
    :members:
    :undoc-members:

Codecs
~~~~~~~~~~~~~~~~~

.. autoclass:: mediaify.configs.H264EncodeConfig
    :members:
    :undoc-members:
.. autoclass:: mediaify.configs.VP9EncodeConfig
    :members:
    :undoc-members:
.. autoclass:: mediaify.configs.OpusEncodeConfig
    :members:
    :undoc-members:

Special Configs
~~~~~~~~~~~~~~~~~

.. autoclass:: mediaify.configs.UnencodedConfig
    :members:
    :undoc-members:
.. autoclass:: mediaify.configs.ThumbnailConfig
    :members:
    :undoc-members:
