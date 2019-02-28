#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# File name: main.py

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
    pass

class DialerApp(App):
    def build(self):
        return MyGridLayout()

if __name__=="__main__":
    DialerApp().run()