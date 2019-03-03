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
from kivymd.tabs import MDTab
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivy.clock import Clock
from openpyxl import load_workbook, Workbook
import openpyxl
import sqlite3
#Clock.max_iteration = 20
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
            self.root.ids.ToolbarMain.right_action_items =  [['brightness-2', lambda x: MD_InventoryEXI_SMV_GUI.MDButton_DarkMode(self)]]
            self.theme_cls.theme_style = 'Light'
            # Make it time based, if possible
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

    def ExcelLoadInit_Prototype(self):
        #Should be selectable
        CounterList = 0
        IDTabs_Accessible = ['MD_WorkSheet_One','MD_WorkSheet_Two','MD_WorkSheet_Three','MD_WorkSheet_Four','MD_WorkSheet_Five']
        ExcelID_UniqueListIndex = 0
        ExcelID_MDTabbedPanel = 0
        ExcelFile = openpyxl.load_workbook('E:\A Development That No One Knows\Github\InventoryEditor-Data_List_Simplier_AEMB\TrialError_ExperimentalPrototype\sample.xlsx')
        ExcelWorksheet = ExcelFile.worksheets[0]
        self.MDUserNotif_SnackbarHandler('Excel Data has been reloaded from the editor!') 
        #Load per Column each with SheetNames on MDTabbedPanel - Seperatable or not or remove based on file
        for SheetData in ExcelFile.sheetnames:
            ExcelID_MDTabbedPanel += 1
            #self.root.ids.FirstTimer_DataFirstName.text = SheetData
            pass
        for row in ExcelWorksheet['B6:P25']:#.format(ExcelWorksheet.min_row,ExcelWorksheet.max_row)]:
            CounterCheck = 1
            # This could be changed, or prolly make the set of ids into list, not dictionary
            for cell in row:
                if CounterCheck == 1 and CounterCheck <= 11:
                    self.root.ids.Resource_ItemNumVal.text = str(cell.value)
                    CounterCheck += 1
                    CounterList += 1
                elif CounterCheck == 2 and CounterCheck <= 11:
                    self.root.ids.Resource_ParticularProperty.text = str(cell.value)
                    CounterCheck += 1
                    CounterList += 1
                elif CounterCheck == 3 and CounterCheck <= 11:
                    self.root.ids.Resource_OnHandVal.text = str(cell.value)
                    CounterCheck += 1
                    CounterList += 1
                elif CounterCheck == 4 and CounterCheck <= 11:
                    self.root.ids.Resource_ProposedVal.text = str(cell.value)
                    CounterCheck += 1
                    CounterList += 1
                elif CounterCheck == 5 and CounterCheck <= 11:
                    self.root.ids.Resource_UnitTypeProperty.text = str(cell.value)
                    CounterCheck += 1
                    CounterList += 1
                elif CounterCheck == 6 and CounterCheck <= 11:
                    self.root.ids.Resource_UnitVal.text = str(cell.value)
                    CounterCheck += 1
                    CounterList += 1
                elif CounterCheck == 7 and CounterCheck <= 11:
                    self.root.ids.Quartile_TextFieldVal_One.text = str(cell.value)
                    CounterCheck += 1
                    CounterList += 1
                elif CounterCheck == 8 and CounterCheck <= 11:
                    self.root.ids.Quartile_TextFieldVal_Two.text = str(cell.value)
                    CounterCheck += 1
                    CounterList += 1
                elif CounterCheck == 9 and CounterCheck <= 11:
                    self.root.ids.Quartile_TextFieldVal_Three.text = str(cell.value)
                    CounterCheck += 1
                    CounterList += 1
                elif CounterCheck == 10 and CounterCheck <= 11:
                    self.root.ids.Quartile_TextFieldVal_Four.text = str(cell.value)
                    CounterCheck += 1
                    CounterList += 1
                elif CounterCheck == 11 and CounterCheck <= 11:
                    # This value which instantly changed when its applied or when editing is done... (I guess)
                    # The value of this show not be saved in the way it is modified here. Get the formmula by getting the function reference from undo function
                    # Create a function to dice the formula and compute it with possible iterations from any n number
                    self.root.ids.Total_ComputedVal.text = str(cell.value)
                    CounterCheck += 1
                    CounterList += 1
                else:
                    break;
                print (cell, cell.value, CounterCheck)
        print(ExcelWorksheet.min_row)
        print(ExcelWorksheet.max_row)
        print(ExcelWorksheet.min_column)
        print(ExcelWorksheet.max_column)
        #self.root.ids.MDList_UserInsertion_Selection.add_widget(TwoLineListItem(id=('IterationItem_%d' % CounterList), name=cell.value))

    def MDWorksheetWorker_DataEditor_Apply(self):
        # Create an Undo Method here?
        self.MDUserNotif_SnackbarHandler('Selected Data Edit has been applied!')

    def MDWorksheetWorker_DataEditor_CleanInput(self):
        self.root.ids.Resource_ItemNumVal.text = ''
        self.root.ids.Resource_ParticularProperty.text = ''
        self.root.ids.Resource_OnHandVal.text = ''
        self.root.ids.Resource_ProposedVal.text = ''
        self.root.ids.Resource_UnitTypeProperty.text = ''
        self.root.ids.Resource_UnitVal.text = ''
        self.root.ids.Total_ComputedVal.text = ''
        self.root.ids.Quartile_TextFieldVal_One.text = ''
        self.root.ids.Quartile_TextFieldVal_Two.text = ''
        self.root.ids.Quartile_TextFieldVal_Three.text = ''
        self.root.ids.Quartile_TextFieldVal_Four.text = ''
        self.MDUserNotif_SnackbarHandler('Selected Data Edit has been cleared!')

    #Reference this function on the funciton who handles when selected this one it should show up on the data editor
    def MDWorksheetWorker_DataEditor_Undo_DataHandler(self):
        pass

    def MDWorksheetWorker_DataEditor_Undo(self):
        self.MDUserNotif_SnackbarHandler('Selected Data has been reverted back to last save state!')

    def MDWorksheet_QuickActions(self, params_actionPerformed):
        #Get Active ID of Selected Data and transfer something or Notif this shit...
        if params_actionPerformed == 'IncVOnHandal':
            pass
        elif params_actionPerformed == 'DecOnHandVal':
            pass
        elif params_actionPerformed == 'IncProposedVal':
            pass
        elif params_actionPerformed == 'DecProposedVal':
            pass
        elif params_actionPerformed == 'IncPerUnitVal':
            pass
        elif params_actionPerformed == 'DecPerUnitVal':
            pass
        else:
            raise ValueError('Parameter Variable -> params_actionPerformed: Received an invalid string from function caller!')
            LoggerDebug.error('Parameter Variable -> params_actionPerformed: Received an invalid string from function caller!')
            app.stop()
        self.MDUserNotif_SnackbarHandler('Selected Data has been reverted back to last save state!')

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