'''
Project Name: InventoryEXT_SMV_GUI - Inventory To Simplified Model View, Code Material Design
Proper Name: Excel Inventory To Simplified View
Version: unknown.beta
Authors: Janrey Tuazon Licas - App Design (Semi)
        Sam Matienzo (Database Worker)
GUI Library Used: Kivy
    Base Theme: KivyMD (Material Design Preset Designs)

Date Initialization: 02/21/2019

'''
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
from kivy.logger import Logger as LoggerDebug
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase, NavigationDrawerIconButton
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker
from kivymd.toolbar import Toolbar
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
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


class MD_InventoryEXI_SMV_GUI(App):
    theme_cls = ThemeManager()
    previous_date = ObjectProperty()
    title = "Welcome to Excel Inventory To Simplified Model View | EXI_SMV" #Excel to Simplified Model VIew in GUI
    Icon_Status = 'brightness-1'
    def KivyConfig_Init(self): # Get Values from DB and Change App Behavior Accordingly
        pass

    def KivyConfig_Setup_FirstTime(self): #This Config can be changed from DB
        #Config.set('graphics', 'fullscreen', 'fake')
        Config.set('graphics','width','1024')
        Config.set('graphics','height','768')
        Config.set('graphics','show_cursor','1')
        Config.set('graphics','minimum_width','1024')
        Config.set('graphics','minimum_height','768')
        Config.write()
    def SQLite_Generate_FirstTime(self):
        pass

    def SQLite_Init(self): #Init Files and Creates when it doesnt exist but show snackbar that is doesnt exist
        pass

    def SQLite_ChangeModify(self): # Not Sure
        pass

    def CriticalComponent_Check(self):
        return 1
        if self.KivyConfig_Init() == 'Passed':
            LoggerDebug.info()
        elif self.KivyConfig_Init() == 'FileDoesNotExist': #Not Consistent, Maybe Clarify this one soon
            LoggerDebug.info('FILE EXISTENT: App knows this is not the first. File does not exist. Relocate the application...') # Add save file
            raise Exception('FILE EXISTENT: App knows this is not the first. File does not exist. Relocate the application...')
            self.get_running_app().stop() 
        else: #Add Path does not exist
            if self.KivyConfig_Setup_FirstTime() == 'Passed':
                LoggerDebug.info('Kivy Config: First Time Settings is loaded and saved.') # Add save file
                if self.SQLite_Init() == 'Passed':
                    LoggerDebug.info('Kivy Config: First Time Settings is loaded and saved.') # Add save file
                else:
                    if self.SQLite_Generate_FirstTime() == 'Passed':
                        LoggerDebug.info('Kivy Config: First Time Files is Initialized and Ready To Go!') # Add save file
                        return 1
                    else:
                        return 0
            else:
                return 0

    def build(self):
        self.MainClassBuildFile = Builder.load_file("MD_DesignClass_File.kv")
        self.theme_cls.primary_palette = 'DeepOrange'
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = 'Light'
        return self.MainClassBuildFile
        
    def MD_DataManage_ShowCellToList(self):
        pass

    def MD_DataManage_Modify(self):
        pass

    def MD_FirstTime_DataSubmission(self):
        pass

    def MDCard_GenerateReport(self):
        pass

    #For Add and Delete
    def MDAuthor_DeleteData(self):
        pass

    def MDAuthor_AddData(self):
        pass

    def MDAuthor_EditData(self):
        pass

    def MDStartup_FirstTime_AdminAccess(self, BooleanPrompt):
        pass
    
    #For Checking Previledge on Accessing Admin Features
    def MDAuthor_CheckAdminPrev_OnAction(self):
        pass

    # For Logon Screen
    def MDAuthor_DialogBooleanPrompt(self):
        pass

    #For Logon and Admin for Modifying User and Assign
    def MDAuthor_PasswordAccessPrompt(self):
        pass
        
    def MDToolbar_DynamicContent_Change(self, params_title, params_pallete, params_left_action_items, params_right_action_items):
        self.root.ids.ToolbarMain.title = params_title
        self.root.ids.ToolbarMain.md_bg_color = get_color_from_hex(colors[params_pallete][self.theme_cls.primary_hue])
        self.root.ids.ToolbarMain.background_palette = params_pallete
        self.root.ids.ToolbarMain.left_action_items = params_left_action_items
        self.root.ids.ToolbarMain.right_action_items = params_right_action_items

    #For First TIme

    def MDNavigationDrawer_DynamicContent_Change(self, Params_Mode):
        if Params_Mode == 'User.Logon_Passed':
            #self.root.ids.
            pass
        elif Params_Mode == 'User.LogonPrompt':
            pass
        elif Params_Mode == 'User.PromptedAdmin_Passed':
            pass
        else:
            LoggerDebug.error('RUNTIME ERROR: Unknown String Passed with No Valid Statement To Run!')
            raise ValueError('RUNTIME ERROR:  Unknown String Passed with No Valid Statement To Run!')
    
    def MDButton_DarkMode(self):
        if self.root.ids.ToolbarMain.darkBooleanParameter == True and self.theme_cls.theme_style == 'Dark':
            self.root.ids.ToolbarMain.darkBooleanParameter = False
            self.root.ids.ToolbarMain.right_action_items =  [['brightness-1', lambda x: MD_InventoryEXI_SMV_GUI.MDButton_DarkMode(self)]]
            self.theme_cls.theme_style = 'Light'
            # Make it time based
            self.MDUserNotif_SnackbarHandler('Dark Mode Activated!')
        elif self.root.ids.ToolbarMain.darkBooleanParameter == False and self.theme_cls.theme_style == 'Light':
            self.root.ids.ToolbarMain.darkBooleanParameter = True
            self.root.ids.ToolbarMain.right_action_items =  [['brightness-7', lambda x: MD_InventoryEXI_SMV_GUI.MDButton_DarkMode(self)]]
            self.theme_cls.theme_style = 'Dark'
            self.MDUserNotif_SnackbarHandler('Light Mode Activated!')
        else:
            LoggerDebug.error('MDButton_DarkMode received invalid parameters, reset SQL Database or modify the property of App_ReadibilityMode to Light or Dark in String Form')
            raise ValueError('MDButton_DarkMode received invalid parameters, reset SQL Database or modify the property of App_ReadibilityMode to Light or Dark in String Form')
    
    def MDButton_Trigger_GoBack(self, param_ScreenFrame_LastKW): #Last Known Window
        pass

    def MDButton_Trigger_ExitConfirm(self):
         BooleanPrompt = MDDialog(title='Exit Confirmation', text='Are you sure you want to quit the application?', text_button_ok='Yes', text_button_cancel='No').open() 
    
    def MDUserNotif_SnackbarHandler(self, params_message):
        Snackbar(text=params_message).show()
    # Unsure Method Call
    def MDSnackbar_CallbackHandler(self):
        pass

class AvatarSampleWidget(ILeftBody, Image):
    pass

class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass

class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass

if __name__ == '__main__':
    if MD_InventoryEXI_SMV_GUI().CriticalComponent_Check():
        LoggerDebug.info('Resource: File Checks Completed... ')
        MD_InventoryEXI_SMV_GUI().KivyConfig_Setup_FirstTime()
        MD_InventoryEXI_SMV_GUI().run()
    else:
        LoggerDebug.error('CHECK FAILURE: Application was succesfully failed to comply on one of the files to create or check those files. Set the application run with admin previledges...')
        raise Exception('CHECK FAILURE: Application was succesfully failed to comply on one of the files to create or check those files. Set the application run with admin previledges...')
        get_running_app().stop()