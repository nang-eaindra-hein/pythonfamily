from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle



class UserPanel(Screen):
    def __init__(self, **kwargs):
        super(UserPanel, self).__init__(**kwargs)
        self.user_data = None  # Placeholder for user data
        self.build_ui()

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size
    def build_ui(self):
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)


    def on_pre_enter(self, *args):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        if self.user_data:
            welcome_label = Label(text=f"WELCOME, {self.user_data['username']}", color=(0.13, 0.55, 0.13, 1), font_size='24sp', size_hint_y=None, height=40)
            layout.add_widget(welcome_label)

            # View Profile button
            view_profile_button = Button(text="View Profile", size_hint=(1, 0.1), background_color=(0.6, 0.8, 1, 1),)  # Sky blue
            view_profile_button.bind(on_press=self.view_profile)
            layout.add_widget(view_profile_button)

            # View Library button
            view_library_button = Button(text="View Library", size_hint=(1, 0.1), background_color=(0.13, 0.55, 0.13, 1))  # Sky blue
            view_library_button.bind(on_press=self.view_library)
            layout.add_widget(view_library_button)

            # Logout button
            logout_button = Button(text="Logout", size_hint=(1, 0.1), background_color=(0.6, 0.8, 1, 1))  # Sky blue
            logout_button.bind(on_press=self.logout)
            layout.add_widget(logout_button)

        self.add_widget(layout)

    def view_profile(self, instance):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Display user profile information
        profile_info = f"Username: {self.user_data['username']}\nFirst Name: {self.user_data.get('first_name', '')}\nLast Name: {self.user_data.get('last_name', '')}\nAccount Number: {self.user_data.get('account_number', '')}"
        profile_label = Label(text=profile_info, font_size='18sp', size_hint_y=None, height=150, color=(0, 0, 0, 1))
        popup_layout.add_widget(profile_label)

        # Edit button
        edit_button = Button(text="Edit", size_hint=(1, 0.1), background_color=(0.6, 0.8, 1, 1))  # Sky blue
        edit_button.bind(on_press=self.edit_profile)
        popup_layout.add_widget(edit_button)

        # Back button
        back_button = Button(text="Back", size_hint=(1, 0.1), background_color=(0.6, 0.8, 1, 1))  # Sky blue
        back_button.bind(on_press=self.dismiss_popup)
        popup_layout.add_widget(back_button)

        self.profile_popup = Popup(title="Profile Information", content=popup_layout, size_hint=(0.7, 0.5))
        self.profile_popup.open()

    def edit_profile(self, instance):
        self.profile_popup.dismiss()

        edit_popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        edit_popup_layout.color = (1, 1, 1, 1)  # Set text color of the BoxLayout to white

        first_name_input = TextInput(hint_text="First Name", text=self.user_data.get('first_name', ''), background_color=(0.85, 0.85, 0.85, 1))  # Soft grey
        last_name_input = TextInput(hint_text="Last Name", text=self.user_data.get('last_name', ''), background_color=(0.85, 0.85, 0.85, 1))  # Soft grey
        username_input = TextInput(hint_text="Username", text=self.user_data['username'], background_color=(0.85, 0.85, 0.85, 1))  # Soft grey
        password_input = TextInput(hint_text="Password", password=True, background_color=(0.85, 0.85, 0.85, 1))  # Soft grey

        save_button = Button(text="Save", size_hint=(0.7, 0.6), background_color=(0.6, 0.8, 1, 1))  # Sky blue
        save_button.bind(on_press=lambda x: self.save_profile(first_name_input.text, last_name_input.text, username_input.text, password_input.text))
        edit_popup_layout.add_widget(first_name_input)
        edit_popup_layout.add_widget(last_name_input)
        edit_popup_layout.add_widget(username_input)
        edit_popup_layout.add_widget(password_input)
        edit_popup_layout.add_widget(save_button)

        # Back button
        back_button = Button(text="Back", size_hint=(0.7, 0.6), background_color=(0.6, 0.8, 1, 1))  # Sky blue
        back_button.bind(on_press=lambda x: self.view_profile(self))
        edit_popup_layout.add_widget(back_button)

        self.edit_popup = Popup(title="Edit Profile", content=edit_popup_layout, size_hint=(0.7, 0.6))
        self.edit_popup.open()

    def save_profile(self, new_first_name, new_last_name, new_username, new_password):
        self.user_data['first_name'] = new_first_name
        self.user_data['last_name'] = new_last_name
        self.user_data['username'] = new_username
        self.user_data['password'] = new_password  # Update password field if needed
        self.view_profile(self)

    def view_library(self, instance):
        self.manager.current = 'library_screen'

    def logout(self, instance):
        self.manager.current = 'main_screen'

    def dismiss_popup(self, instance=None):
        if hasattr(self, 'profile_popup') and self.profile_popup:
            self.profile_popup.dismiss()

        if hasattr(self, 'edit_popup') and self.edit_popup:
            self.edit_popup.dismiss()
