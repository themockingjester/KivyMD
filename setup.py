# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='kivymd',
      version='0.1.2',
      description='Set of widgets for Kivy inspired by Google\'s Material '
                  'Design',
      author='Andrés Rodríguez',
      author_email='andres.rodriguez@lithersoft.com',
      url='https://github.com/mixedCase/kivymd',
      packages=['kivymd'],
      package_data={
          'kivymd': ['images/*.png', 'images/*.jpg', 'images/*.atlas',
                     'vendor/*.py',
                     'fonts/*.ttf', 'vendor/circleLayout/*.py',
                     'vendor/circularTimePicker/*.py']},
      requires=['kivy']
      )
