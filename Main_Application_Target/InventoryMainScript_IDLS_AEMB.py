from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker
#class HackedDemoNavDrawer(MDNavigationDrawer):
#    # DO NOT USE
#    def add_widget(self, widget, index=0):
#        if issubclass(widget.__class__, BaseListItem):
#            self._list.add_widget(widget, index)
#            if len(self._list.children) == 1:
#                widget._active = True
#                self.active_item = widget
#            # widget.bind(on_release=lambda x: self.panel.toggle_state())
#            widget.bind(on_release=lambda x: x._set_active(True, list=self))
#        elif issubclass(widget.__class__, NavigationDrawerHeaderBase):
#            self._header_container.add_widget(widget)
#        else:
#            super(MDNavigationDrawer, self).add_widget(widget, index)


class KitchenSink(App):
    theme_cls = ThemeManager()
    previous_date = ObjectProperty()
    title = "Inventory System | DLS-AEMB"

    menu_items = [
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
    ]

    def build(self):
        main_widget = Builder.load_file("MD_DesignClass_File.kv")
        self.theme_cls.primary_palette = 'Orange'
        #self.theme_cls.theme_style = 'Light'
       # main_widget.ids.text_field_error.bind(
       #     on_text_validate=self.set_error_message,
       #     on_focus=self.set_error_message)
        # self.bottom_navigation_remove_mobile(main_widget)
        return main_widget

#    def bottom_navigation_remove_mobile(self, widget):
#        # Removes some items from bottom-navigation demo when on mobile
#        if DEVICE_TYPE == 'mobile':
#            widget.ids.bottom_navigation_demo.remove_widget(
#                widget.ids.bottom_navigation_desktop_2)
#        if DEVICE_TYPE == 'mobile' or DEVICE_TYPE == 'tablet':
#            widget.ids.bottom_navigation_demo.remove_widget(
#                widget.ids.bottom_navigation_desktop_1)
#
#    def show_example_snackbar(self, snack_type):
#
#        if snack_type == 'simple':
#            Snackbar(text="This is a snackbar!").show()
#        elif snack_type == 'button':
#            Snackbar(text="This is a snackbar", button_text="with a button!",
#                     button_callback=lambda *args: 2).show()
#        elif snack_type == 'verylong':
#            Snackbar(
#                text="This is a very very very very very very very long snackbar!").show()
#
#    def show_example_dialog(self):
#        content = MDLabel(font_style='Body1',
#                          theme_text_color='Secondary',
#                          text="This is a dialog with a title and some text. "
#                               "That's pretty awesome right!",
#                          size_hint_y=None,
#                          valign='top')
#        content.bind(texture_size=content.setter('size'))
#        self.dialog = MDDialog(title="This is a test dialog",
#                               content=content,
#                               size_hint=(.8, None),
#                               height=dp(200),
#                               auto_dismiss=False)
#
#        self.dialog.add_action_button("Dismiss",
#                                      action=lambda *x: self.dialog.dismiss())
#        self.dialog.open()
#
#    def show_example_long_dialog(self):
#        content = MDLabel(font_style='Body1',
#                          theme_text_color='Secondary',
#                          text="Lorem ipsum dolor sit amet, consectetur "
#                               "adipiscing elit, sed do eiusmod tempor "
#                               "incididunt ut labore et dolore magna aliqua. "
#                               "Ut enim ad minim veniam, quis nostrud "
#                               "exercitation ullamco laboris nisi ut aliquip "
#                               "ex ea commodo consequat. Duis aute irure "
#                               "dolor in reprehenderit in voluptate velit "
#                               "esse cillum dolore eu fugiat nulla pariatur. "
#                               "Excepteur sint occaecat cupidatat non "
#                               "proident, sunt in culpa qui officia deserunt "
#                               "mollit anim id est laborum.",
#                          size_hint_y=None,
#                          valign='top')
#        content.bind(texture_size=content.setter('size'))
#        self.dialog = MDDialog(title="This is a long test dialog",
#                               content=content,
#                               size_hint=(.8, None),
#                               height=dp(200),
#                               auto_dismiss=False)
#
#        self.dialog.add_action_button("Dismiss",
#                                      action=lambda *x: self.dialog.dismiss())
#        self.dialog.open()
#
#    def get_time_picker_data(self, instance, time):
#        self.root.ids.time_picker_label.text = str(time)
#        self.previous_time = time
#
#    def show_example_time_picker(self):
#        self.time_dialog = MDTimePicker()
#        self.time_dialog.bind(time=self.get_time_picker_data)
#        if self.root.ids.time_picker_use_previous_time.active:
#            try:
#                self.time_dialog.set_time(self.previous_time)
#            except AttributeError:
#                pass
#        self.time_dialog.open()
#
#    def set_previous_date(self, date_obj):
#        self.previous_date = date_obj
#        self.root.ids.date_picker_label.text = str(date_obj)
#
#    def show_example_date_picker(self):
#        if self.root.ids.date_picker_use_previous_date.active:
#            pd = self.previous_date
#            try:
#                MDDatePicker(self.set_previous_date,
#                             pd.year, pd.month, pd.day).open()
#            except AttributeError:
#                MDDatePicker(self.set_previous_date).open()
#        else:
#            MDDatePicker(self.set_previous_date).open()
#
#    def show_example_bottom_sheet(self):
#        bs = MDListBottomSheet()
#        bs.add_item("Here's an item with text only", lambda x: x)
#        bs.add_item("Here's an item with an icon", lambda x: x,
#                    icon='clipboard-account')
#        bs.add_item("Here's another!", lambda x: x, icon='nfc')
#        bs.open()
#
#    def show_example_grid_bottom_sheet(self):
#        bs = MDGridBottomSheet()
#        bs.add_item("Facebook", lambda x: x,
#                    icon_src='./assets/facebook-box.png')
#        bs.add_item("YouTube", lambda x: x,
#                    icon_src='./assets/youtube-play.png')
#        bs.add_item("Twitter", lambda x: x,
#                    icon_src='./assets/twitter.png')
#        bs.add_item("Da Cloud", lambda x: x,
#                    icon_src='./assets/cloud-upload.png')
#        bs.add_item("Camera", lambda x: x,
#                    icon_src='./assets/camera.png')
#        bs.open()
#
#    def set_error_message(self, *args):
#        if len(self.root.ids.text_field_error.text) == 2:
#            self.root.ids.text_field_error.error = True
#        else:
#            self.root.ids.text_field_error.error = False
#
#    def on_pause(self):
#        return True
#
#    def on_stop(self):
#        pass
#
#
#class AvatarSampleWidget(ILeftBody, Image):
#    pass
#
#
#class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
#    pass
#
#
#class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
#    pass


if __name__ == '__main__':
    KitchenSink().run()
