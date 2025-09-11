from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from borrower_list import BorrowerList
from kivy.graphics import Color, Rectangle

class UserScreen(Screen):
    def __init__(self, **kwargs):
        super(UserScreen, self).__init__(**kwargs)
        self.borrower_list = BorrowerList()  # Initialize BorrowerList instance
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
        
        back_button = Button(text="Back", size_hint=(0.1, 0.1), font_size='16sp')
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.app = BorrowerApp(self)  # Pass only the UserScreen instance to BorrowerApp
        self.app.build()
        layout.add_widget(self.app.root)

        self.add_widget(layout)

    def on_enter(self, *args):
        # Ensure ScreenManager is assigned
        self.app.screen_manager = self.manager

    def go_back(self, instance):
        self.manager.current = 'main_screen'
    
    def validate_login(self, username, password):
        borrower_data = self.borrower_list.validate_login(username, password)
        print(f"validate_login: {borrower_data}")  # Debugging print statement
        return borrower_data

    def add_fine(self, username, fine_data):
        success = self.borrower_list.add_fine(username, fine_data)
        if success:
            self.show_popup("Fine Added", "Fine has been added successfully.")
        else:
            self.show_popup("Error", "Failed to add fine.")

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        popup_label = Label(text=message, color=(0, 0, 0, 1), font_size='16sp')
        close_button = Button(text="Close", size_hint_y=None, height=40, font_size='16sp', on_press=lambda x: popup.dismiss())

        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(close_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(0.7, 0.3))
        popup.open()

class BorrowerApp:
    def __init__(self, user_screen):
        self.user_screen = user_screen
        self.screen_manager = None  # ScreenManager will be assigned later

    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=[40, 20, 40, 20], spacing=20)

        title_label = Label(
            text="Borrower Management System",
            font_size='28sp',
            size_hint=(1, 0.2),
            color=(1,1,1, 1),
            bold=True
        )
        main_layout.add_widget(title_label)

        input_layout = GridLayout(cols=2, spacing=20, size_hint=(1, 0.4))

        self.username_input = TextInput(hint_text="Username", multiline=False, padding=(10, 10), size_hint_y=None, height=40, background_color=(1,1,1,1))
        self.password_input = TextInput(hint_text="Password", multiline=False, password=True, padding=(10, 10), size_hint_y=None, height=40, background_color=(1,1,1,1))

        input_layout.add_widget(Label(text="Username:", color=(1,1,1,1), font_size='18sp', size_hint_y=None, height=40, halign='right', valign='middle'))
        input_layout.add_widget(self.username_input)
        input_layout.add_widget(Label(text="Password:", color=(1,1,1,1), font_size='18sp', size_hint_y=None, height=40, halign='right', valign='middle'))
        input_layout.add_widget(self.password_input)

        main_layout.add_widget(input_layout)

        button_layout = BoxLayout(size_hint=(1, 0.2),spacing=20)

        login_button = Button(text="Login", on_press=self.login, background_color=(0.13, 0.55, 0.13, 1), font_size='16sp', size_hint_y=None, height=60)
        signup_button = Button(text="Sign Up", on_press=self.signup, background_color=(0, 0.6, 0.8, 1), font_size='16sp', size_hint_y=None, height=60)

        button_layout.add_widget(login_button)
        button_layout.add_widget(signup_button)

        main_layout.add_widget(button_layout)

        self.root = main_layout

    def login(self, instance):
    
        username = self.username_input.text
        password = self.password_input.text
        print(f"Login attempt: username={username}, password={password}")  # Debugging print statement
        borrower_data = self.user_screen.validate_login(username, password)
        print(f"Login result: {borrower_data}")  # Debugging print statement
        if borrower_data:
            self.screen_manager.get_screen('user_panel').user_data = borrower_data
            self.screen_manager.current = 'user_panel'
        else:
            self.user_screen.show_popup("Login Failed", "Invalid username or password")

    def signup(self, instance):
        self.show_signup_popup()

    def show_signup_popup(self):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        input_layout = GridLayout(cols=2, spacing=10)
        first_name_input = TextInput(hint_text="First Name", multiline=False, padding=(10, 10), size_hint_y=None, height=60, background_color=(0.85, 0.85, 0.85, 1))
        last_name_input = TextInput(hint_text="Last Name", multiline=False, padding=(10, 10), size_hint_y=None, height=60, background_color=(0.85, 0.85, 0.85, 1))
        username_input = TextInput(hint_text="Username", multiline=False, padding=(10, 10), size_hint_y=None, height=60, background_color=(0.85, 0.85, 0.85, 1))
        password_input = TextInput(hint_text="Password", multiline=False, password=True, padding=(10, 10), size_hint_y=None, height=60, background_color=(0.85, 0.85, 0.85, 1))

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

        add_button = Button(text="Sign Up", font_size='16sp')
        add_button.bind(on_press=lambda instance: self.add_borrower_popup(first_name_input, last_name_input, username_input, password_input))
        close_button = Button(text="Cancel",  font_size='16sp')
        close_button.bind(on_press=lambda instance: popup.dismiss())

        add_button_layout.add_widget(add_button)
        add_button_layout.add_widget(close_button)

        popup_layout.add_widget(add_button_layout)

        popup = Popup(title="Sign Up", content=popup_layout, size_hint=(0.8, 0.6))
        popup.open()

    def add_borrower_popup(self, first_name_input, last_name_input, username_input, password_input):
        first_name = first_name_input.text
        last_name = last_name_input.text
        username = username_input.text
        password = password_input.text

        if all([first_name, last_name, username, password]):
            account_number = self.user_screen.borrower_list.get_next_account_number()
            borrower = self.user_screen.borrower_list.create_borrower(first_name, last_name, account_number, username, password)
            self.user_screen.borrower_list.add_borrower(borrower)
            self.user_screen.borrower_list.to_json("borrowers.json")  # Save to JSON file
            self.user_screen.show_popup("Success", "Borrower added successfully")
        else:
            self.user_screen.show_popup("Error", "Please fill in all fields")

    def add_fine_popup(self, username):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        fine_title_input = TextInput(hint_text="Fine Title", multiline=False, padding=(10, 10), size_hint_y=None, height=40, background_color=(0.85, 0.85, 0.85, 1))
        days_delayed_input = TextInput(hint_text="Days Delayed", multiline=False, input_type='number', padding=(10, 10), size_hint_y=None, height=40, background_color=(0.85, 0.85, 0.85, 1))
        fine_amount_input = TextInput(hint_text="Fine Amount", multiline=False, input_type='number', padding=(10, 10), size_hint_y=None, height=40, background_color=(0.85, 0.85, 0.85, 1))

        popup_layout.add_widget(Label(text="Fine Title:", color=(0.1, 0.5, 0.7, 1), size_hint_y=None, height=40, halign='right', valign='middle'))
        popup_layout.add_widget(fine_title_input)
        popup_layout.add_widget(Label(text="Days Delayed:", color=(0.1, 0.5, 0.7, 1), size_hint_y=None, height=40, halign='right', valign='middle'))
        popup_layout.add_widget(days_delayed_input)
        popup_layout.add_widget(Label(text="Fine Amount:", color=(0.1, 0.5, 0.7, 1), size_hint_y=None, height=40, halign='right', valign='middle'))
        popup_layout.add_widget(fine_amount_input)

        add_button_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=40)
        add_button = Button(text="Add Fine", background_color=(0, 0.6, 0.8, 1), font_size='16sp')
        add_button.bind(on_press=lambda instance: self.user_screen.add_fine(username, {
            "title": fine_title_input.text,
            "days_delayed": int(days_delayed_input.text),
            "fine_amount": float(fine_amount_input.text)
        }))
        close_button = Button(text="Cancel",  font_size='16sp')
        close_button.bind(on_press=lambda instance: popup.dismiss())

        add_button_layout.add_widget(add_button)
        add_button_layout.add_widget(close_button)

        popup_layout.add_widget(add_button_layout)

        popup = Popup(title="Add Fine", content=popup_layout, size_hint=(0.8, 0.5))
        popup.open()
