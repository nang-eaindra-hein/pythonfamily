import json
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# Admin Screen Class
class AdminScreen(Screen):
    def __init__(self, **kwargs):
        super(AdminScreen, self).__init__(**kwargs)
        self.build_ui()

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size
    def build_ui(self):
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)
        layout = BoxLayout(orientation='vertical', padding=[40, 20, 40, 20], spacing=20)
        
        # Back button
        back_button = Button(text="Back", size_hint=(0.1, 0.1))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.app = AdminApp(self)  # Pass the AdminScreen instance to AdminApp
        self.app.build()
        layout.add_widget(self.app.root)  # Add AdminApp's root widget to AdminScreen

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main_screen'
    
    def validate_login(self, username, password):
        admins = self.app.admin_list.get_admins()
        for admin in admins:
            if admin.username == username and admin.password == password:
                return True
        return False

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        popup_label = Label(text=message, color=(0, 0, 0, 1), font_size='16sp')
        close_button = Button(text="Close", size_hint_y=None, height=40, on_press=lambda x: popup.dismiss())

        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(close_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(0.7, 0.3))
        popup.open()

# Backend Classes
class Admin:
    def __init__(self, first_name, last_name, account_number, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "account_number": self.account_number,
            "username": self.username,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["first_name"],
            data["last_name"],
            data["account_number"],
            data["username"],
            data["password"]
        )

class AdminListNode:
    def __init__(self, admin):
        self.admin = admin
        self.next = None
        self.prev = None

class AdminList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.next_account_number = 1  # Start from 1

    def add_admin(self, admin):
        new_node = AdminListNode(admin)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def remove_admin(self, account_number):
        current = self.head
        while current:
            if current.admin.account_number == account_number:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                self.size -= 1
                return True
            current = current.next
        return False

    def update_admin(self, account_number, first_name=None, last_name=None, username=None, password=None):
        current_node = self.head
        while current_node:
            if current_node.admin.account_number == account_number:
                if first_name:
                    current_node.admin.first_name = first_name
                if last_name:
                    current_node.admin.last_name = last_name
                if username:
                    current_node.admin.username = username
                if password:
                    current_node.admin.password = password
                return True
            current_node = current_node.next
        return False

    def get_admins(self):
        admins_list = []
        current_node = self.head
        while current_node:
            admins_list.append(current_node.admin)
            current_node = current_node.next
        return admins_list

    def to_json(self, file_path):
        admins_list = self.get_admins()
        with open(file_path, 'w') as file:
            json.dump([admin.to_dict() for admin in admins_list], file, indent=4)

    def from_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                admins_data = json.load(file)
                for admin_data in admins_data:
                    admin = Admin.from_dict(admin_data)
                    self.add_admin(admin)
                    if admin.account_number is not None:
                        self.next_account_number = max(self.next_account_number, admin.account_number + 1)
        except FileNotFoundError:
            print("File not found. Starting with an empty admin list.")

    def get_next_account_number(self):
        account_number = self.next_account_number
        self.next_account_number += 1
        return account_number

# Kivy App Class for Admin Management
class AdminApp(App):
    def __init__(self, admin_screen, **kwargs):
        super(AdminApp, self).__init__(**kwargs)
        self.admin_screen = admin_screen

    def build(self):
        self.admin_list = AdminList()
        self.admin_list.from_json("admins.json")

        Window.clearcolor = (0.95, 0.95, 0.95, 1)  # Set the background color to light grey

        main_layout = BoxLayout(orientation='vertical', padding=[40, 20, 40, 20], spacing=20)

        # Title
        title_label = Label(
            text="Admin Management System",
            font_size='28sp',
            size_hint=(1, 0.2),
            color=(1,1,1, 1),
            bold=True
        )
        main_layout.add_widget(title_label)

        # Input Fields
        input_layout = GridLayout(cols=2, spacing=20, size_hint=(1, 0.4))

        self.username_input = TextInput(hint_text="Username", multiline=False, padding=(10, 10), size_hint_y=None, background_color=(1,1,1, 1), height=40)
        self.password_input = TextInput(hint_text="Password", multiline=False, password=True, padding=(10, 10), size_hint_y=None,background_color=(1,1,1, 1), height=40)

        input_layout.add_widget(Label(text="Username:", color=(1,1,1, 1), font_size='18sp', size_hint_y=None, height=40, halign='right', valign='middle'))
        input_layout.add_widget(self.username_input)
        input_layout.add_widget(Label(text="Password:", color=(1,1,1, 1), font_size='18sp', size_hint_y=None, height=40, halign='right', valign='middle'))
        input_layout.add_widget(self.password_input)

        main_layout.add_widget(input_layout)

        # Buttons
        button_layout = BoxLayout(size_hint=(1, 0.2), spacing=20)

        login_button = Button(text="Login", on_press=self.login, background_color=(0, 0.6, 0, 1), font_size='16sp', size_hint_y=None, height=40)
        signup_button = Button(text="Sign Up", on_press=self.signup, background_color=(0, 0.4, 0.6, 1), font_size='16sp', size_hint_y=None, height=40)

        button_layout.add_widget(login_button)
        button_layout.add_widget(signup_button)

        main_layout.add_widget(button_layout)

        self.root = main_layout

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        if self.admin_screen.validate_login(username, password):
            self.admin_screen.manager.current = 'admin_pannel'
        else:
            self.admin_screen.show_popup("Login Failed", "Invalid username or password")

    def signup(self, instance):
        self.show_signup_popup()

    def show_signup_popup(self):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        input_layout = GridLayout(cols=2, spacing=10)
        first_name_input = TextInput(hint_text="First Name", multiline=False, padding=(10, 10), size_hint_y=None, height=60)
        last_name_input = TextInput(hint_text="Last Name", multiline=False, padding=(10, 10), size_hint_y=None, height=60)
        username_input = TextInput(hint_text="Username", multiline=False, padding=(10, 10), size_hint_y=None, height=60)
        password_input = TextInput(hint_text="Password", multiline=False, password=True, padding=(10, 10), size_hint_y=None, height=60)

        input_layout.add_widget(Label(text="First Name:", color=(0.1, 0.5, 0.7, 1), size_hint_y=None, height=60, halign='right', valign='middle'))
        input_layout.add_widget(first_name_input)
        input_layout.add_widget(Label(text="Last Name:", color=(0.1, 0.5, 0.7, 1), size_hint_y=None, height=60, halign='right', valign='middle'))
        input_layout.add_widget(last_name_input)
        input_layout.add_widget(Label(text="Username:", color=(0.1, 0.5, 0.7, 1), size_hint_y=None, height=60, halign='right', valign='middle'))
        input_layout.add_widget(username_input)
        input_layout.add_widget(Label(text="Password:", color=(0.1, 0.5, 0.7, 1), size_hint_y=None, height=60, halign='right', valign='middle'))
        input_layout.add_widget(password_input)
        
        popup_layout.add_widget(input_layout)

        add_button_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=60)
        add_button = Button(text="Sign Up", background_color=(0, 0.6, 0, 1), font_size='16sp')
        add_button.bind(on_press=lambda instance: self.add_admin_popup(first_name_input, last_name_input, username_input, password_input))
        close_button = Button(text="Cancel", background_color=(0.6, 0, 0, 1), font_size='16sp')
        close_button.bind(on_press=lambda instance: popup.dismiss())

        add_button_layout.add_widget(add_button)
        add_button_layout.add_widget(close_button)

        popup_layout.add_widget(add_button_layout)

        popup = Popup(title="Sign Up", content=popup_layout, size_hint=(0.8, 0.6))
        popup.open()

    def add_admin_popup(self, first_name_input, last_name_input, username_input, password_input):
        first_name = first_name_input.text
        last_name = last_name_input.text
        username = username_input.text
        password = password_input.text

        if all([first_name, last_name, username, password]):
            account_number = self.admin_list.get_next_account_number()
            admin = Admin(first_name, last_name, account_number, username, password)
            self.admin_list.add_admin(admin)
            self.admin_list.to_json("admins.json")  # Save to JSON file
            self.admin_screen.show_popup("Success", "Admin added successfully")
        else:
            self.admin_screen.show_popup("Error", "Please fill in all fields")
