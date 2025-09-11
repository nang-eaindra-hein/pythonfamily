import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from user_screen import UserScreen
from admin_screen import AdminScreen 
from mainscreen import MainScreen  
from adminpannel import AdminPannel  
from library import LibraryScreen  
from borrower_list import BorrowerList
from adminlibrary import AdminLibraryScreen
from userpanel import UserPanel 
from borrower_list_admin import BorrowerListAdmin
class LibraryApp(App):
    def build(self):
        sm = ScreenManager()

        # Add screens to ScreenManager
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(UserScreen(name='user_screen'))
        sm.add_widget(AdminScreen(name='admin_screen'))
        sm.add_widget(AdminPannel(name='admin_pannel'))
        sm.add_widget(LibraryScreen(name='library_screen'))
        sm.add_widget(AdminLibraryScreen(name='admin_library_screen'))
        sm.add_widget(UserPanel(name='user_panel'))
        
        sm.add_widget(BorrowerListAdmin(name='borrower_list_admin'))
        sm.current = 'main_screen'  # Set the initial screen

        return sm

if __name__ == "__main__":
    LibraryApp().run()
