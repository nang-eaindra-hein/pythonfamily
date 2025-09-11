from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
import json

class BorrowerListAdmin(Screen):
    def __init__(self, **kwargs):
        super(BorrowerListAdmin, self).__init__(**kwargs)
        self.build_ui()

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def build_ui(self):
        self.clear_widgets()
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)
        self.layout = BoxLayout(orientation='vertical', padding=[40, 20, 40, 20], spacing=20)

        # Add search bar
        search_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10, padding=[10, 10, 10, 10])
        self.search_bar = TextInput(hint_text='Search by First Name, Last Name, Username, or Account Number', multiline=False, size_hint_y=None, height=40, font_size=18)
        search_layout.add_widget(self.search_bar)

        search_button = Button(text='Search', size_hint=(None, None), size=(150, 40), background_color=(0.6, 0.8, 1, 1))
        search_button.bind(on_press=self.on_search)
        search_layout.add_widget(search_button)

        self.layout.add_widget(search_layout)

        # Add titles layout
        titles_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10, padding=[10, 10, 10, 10])
        titles_layout.add_widget(Label(text='First Name', font_size=18, bold=True, color=(1, 1, 1, 1), size_hint=(0.25, 1)))
        titles_layout.add_widget(Label(text='Last Name', font_size=18, bold=True, color=(1, 1, 1, 1), size_hint=(0.25, 1)))
        titles_layout.add_widget(Label(text='Username', font_size=18, bold=True, color=(1, 1, 1, 1), size_hint=(0.25, 1)))
        titles_layout.add_widget(Label(text='Account Number', font_size=18, bold=True, color=(1, 1, 1, 1), size_hint=(0.25, 1)))
        titles_layout.add_widget(Label(text='', size_hint=(0.25, 1)))  # Placeholder for the delete button
        self.layout.add_widget(titles_layout)

        # Add scroll view for borrower details
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.borrower_details_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        self.borrower_details_layout.bind(minimum_height=self.borrower_details_layout.setter('height'))
        self.scroll_view.add_widget(self.borrower_details_layout)
        self.layout.add_widget(self.scroll_view)

        # Add back button
        back_button = Button(text='Back', font_size=18, bold=True, size_hint=(None, None), size=(200, 60), background_color=(0.6, 0.8, 1, 1))
        back_button.bind(on_press=self.go_back)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)
        self.load_borrowers()

    def go_back(self, instance):
        self.manager.current = 'admin_pannel'

    def load_borrowers(self, borrowers=None):
        self.borrower_details_layout.clear_widgets()
        if borrowers is None:
            borrowers = self.get_borrowers()
        for borrower in borrowers:
            borrower_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10, padding=[10, 10, 10, 10])
            borrower_layout.add_widget(Label(text=borrower['first_name'], font_size=16, color=(1, 1, 1, 1), size_hint=(0.25, 1)))
            borrower_layout.add_widget(Label(text=borrower['last_name'], font_size=16, color=(1, 1, 1, 1), size_hint=(0.25, 1)))
            borrower_layout.add_widget(Label(text=borrower['username'], font_size=16, color=(1, 1, 1, 1), size_hint=(0.25, 1)))
            borrower_layout.add_widget(Label(text=str(borrower['account_number']), font_size=16, color=(1, 1, 1, 1), size_hint=(0.25, 1)))
            delete_button = Button(text='Delete', size_hint=(0.25, 1), font_size=16, bold=True, background_color=(0.6, 0.8, 1, 1))
            delete_button.bind(on_press=lambda instance, acc_number=borrower['account_number']: self.delete_borrower(acc_number))
            borrower_layout.add_widget(delete_button)
            self.borrower_details_layout.add_widget(borrower_layout)

    def delete_borrower(self, account_number):
        self.remove_borrower(account_number)
        self.save_borrowers()
        self.load_borrowers()
        self.show_popup('Success', f'Borrower with account number {account_number} has been deleted.')

    def on_search(self, instance):
        query = self.search_bar.text.lower()
        if query:
            filtered_borrowers = [borrower for borrower in self.get_borrowers() if query in borrower['first_name'].lower() or query in borrower['last_name'].lower() or query in borrower['username'].lower() or query in str(borrower['account_number']).lower()]
            self.load_borrowers(filtered_borrowers)
        else:
            self.load_borrowers()

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        popup_label = Label(text=message, font_size=18, color=(1, 1, 1, 1))
        popup_button = Button(text='Close', font_size=16, bold=True, size_hint=(None, None), size=(100, 40), background_color=(0.6, 0.8, 1, 1))
        popup_button.bind(on_press=lambda x: popup.dismiss())
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_button)
        popup = Popup(title=title, content=popup_layout, size_hint=(0.75, 0.5))
        popup.open()

    def get_borrowers(self):
        try:
            with open("borrowers.json", 'r') as file:
                borrowers_data = json.load(file)
                return borrowers_data
        except FileNotFoundError:
            return []

    def remove_borrower(self, account_number):
        borrowers = self.get_borrowers()
        borrowers = [borrower for borrower in borrowers if borrower['account_number'] != account_number]
        with open("borrowers.json", 'w') as file:
            json.dump(borrowers, file, indent=4)

    def save_borrowers(self):
        with open("borrowers.json", 'w') as file:
            json.dump(self.get_borrowers(), file, indent=4)
