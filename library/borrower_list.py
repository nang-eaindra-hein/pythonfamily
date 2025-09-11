from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import json

class BorrowerList:
    def __init__(self):
        self.borrowers = []
        self.load_from_json("borrowers.json")
        

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                self.borrowers = json.load(file)
        except FileNotFoundError:
            self.borrowers = []

    def to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.borrowers, file, indent=4)

    def get_next_account_number(self):
        if not self.borrowers:
            return 1
        else:
            return max(borrower['account_number'] for borrower in self.borrowers) + 1

    def create_borrower(self, first_name, last_name, account_number, username, password):
        return {
            "account_number": account_number,
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "password": password,
            "fine": []
        }

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)

    def get_borrowers(self):
        return self.borrowers

    def find_borrower_by_username(self, username):
        for borrower in self.borrowers:
            if borrower['username'] == username:
                return borrower
        return None

    def get_borrower_by_account_number(self, account_number):
        for borrower in self.borrowers:
            if borrower['account_number'] == account_number:
                return borrower
        return None

    def validate_login(self, username, password):
        for borrower in self.borrowers:
            if borrower['username'] == username and borrower['password'] == password:
                return borrower
        return None

    def search_borrower(self, search_key):
        # Assuming search_key can be either account_number (ID) or username
        try:
            search_key = int(search_key)  # Try to convert to int for account_number search
            result = self.binary_search_by_account_number(search_key)
        except ValueError:
            result = self.binary_search_by_username(search_key)

        return result

    def binary_search_by_account_number(self, account_number):
        borrowers_sorted_by_id = sorted(self.borrowers, key=lambda x: x['account_number'])
        low, high = 0, len(borrowers_sorted_by_id) - 1

        while low <= high:
            mid = (low + high) // 2
            if borrowers_sorted_by_id[mid]['account_number'] == account_number:
                return borrowers_sorted_by_id[mid]
            elif borrowers_sorted_by_id[mid]['account_number'] < account_number:
                low = mid + 1
            else:
                high = mid - 1

        return None

    def binary_search_by_username(self, username):
        borrowers_sorted_by_username = sorted(self.borrowers, key=lambda x: x['username'])
        low, high = 0, len(borrowers_sorted_by_username) - 1

        while low <= high:
            mid = (low + high) // 2
            if borrowers_sorted_by_username[mid]['username'] == username:
                return borrowers_sorted_by_username[mid]
            elif borrowers_sorted_by_username[mid]['username'] < username:
                low = mid + 1
            else:
                high = mid - 1

        return None

    def show_search_result_popup(self):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        search_input = TextInput(hint_text='Enter username or account number...', multiline=False, size_hint_y=None, height=40)
        search_input.bind(text=self.on_search_text)
        popup_layout.add_widget(search_input)

        self.results_layout = BoxLayout(orientation='vertical', spacing=10)
        popup_layout.add_widget(self.results_layout)

        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        close_button = Button(text="Close", size_hint_x=None, width=100, background_color=[0.13, 0.55, 0.13, 1])
        close_button.bind(on_press=lambda x: self.popup.dismiss())
        button_layout.add_widget(close_button)
        popup_layout.add_widget(button_layout)

        self.popup = Popup(title="Search Borrowers", content=popup_layout, size_hint=(0.9, 0.9))
        self.popup.open()

    def on_search_text(self, instance, value):
        # Clear previous results
        self.results_layout.clear_widgets()

        # Perform search based on value
        if value.strip():
            result = self.search_borrower(value.strip())
            if result:
                self.display_search_results(result)
            else:
                self.display_search_results("No matching borrower found.")
        else:
            self.display_search_results("Enter a search query.")

    def display_search_results(self, result):
        if isinstance(result, dict):
            header = Label(text="Search Result", font_size='24sp', color=[0.13, 0.55, 0.13, 1], bold=True, size_hint_y=None, height=30)
            self.results_layout.add_widget(header)

            borrower_info = Label(text=f"Account Number: {result['account_number']}\n"
                                      f"Username: {result['username']}\n"
                                      f"Name: {result['first_name']} {result['last_name']}",
                                 font_size=18, color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=100)
            self.results_layout.add_widget(borrower_info)
        else:
            error_message = Label(text=result, font_size='18sp', color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=50)
            self.results_layout.add_widget(error_message)








# Clara, [6/22/2024 4:54 PM]
# # Create a layout for the search bar
#         search_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10, padding=[10, 10, 10, 10])
#         self.search_bar = TextInput(hint_text='Search by First Name, Last Name, Username, or Account Number', multiline=False, size_hint_y=None, height=40, font_size=18)
#         search_layout.add_widget(self.search_bar)

#         # Add a search button
#         search_button = RoundedButton(text='Search', size_hint=(None, None), size=(150, 40))
#         search_button.bind(on_press=self.on_search)
#         search_layout.add_widget(search_button)

#         root.add_widget(search_layout)

#         # Create a layout for the titles
#         titles_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10, padding=[10, 10, 10, 10])
#         titles_layout.add_widget(Label(text='First Name', font_size=18, bold=True, color=(0, 0, 0, 1), size_hint=(0.25, 1)))
#         titles_layout.add_widget(Label(text='Last Name', font_size=18, bold=True, color=(0, 0, 0, 1), size_hint=(0.25, 1)))
#         titles_layout.add_widget(Label(text='Username', font_size=18, bold=True, color=(0, 0, 0, 1), size_hint=(0.25, 1)))
#         titles_layout.add_widget(Label(text='Account Number', font_size=18, bold=True, color=(0, 0, 0, 1), size_hint=(0.25, 1)))
#         titles_layout.add_widget(Label(text='', size_hint=(0.25, 1)))  # Placeholder for the delete button

#         root.add_widget(titles_layout)

#         # Layout for borrower details
#         self.scroll_view = ScrollView(size_hint=(1, 1))
#         self.borrower_details_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
#         self.borrower_details_layout.bind(minimum_height=self.borrower_details_layout.setter('height'))
#         self.scroll_view.add_widget(self.borrower_details_layout)
#         root.add_widget(self.scroll_view)

#         # Add the Back button
#         back_button = RoundedButton(text='Back', font_size=18, bold=True, size_hint=(None, None), size=(200, 60))
#         back_button.bind(on_press=self.go_back_to_admin_options)
#         root.add_widget(back_button)

#         self.add_widget(root)
#         self.load_borrowers()

#     def _update_rect(self, instance, value):
#         self.rect.pos = instance.pos
#         self.rect.size = instance.size

#     def load_borrowers(self, borrowers=None):
#         self.borrower_details_layout.clear_widgets()
#         if borrowers is None:
#             borrowers = self.borrower_list.get_borrowers()
#         for borrower in borrowers:
#             borrower_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10, padding=[10, 10, 10, 10])
#             borrower_layout.add_widget(Label(text=borrower.first_name, font_size=16, color=(0, 0, 0, 1), size_hint=(0.25, 1)))
#             borrower_layout.add_widget(Label(text=borrower.last_name, font_size=16, color=(0, 0, 0, 1), size_hint=(0.25, 1)))
#             borrower_layout.add_widget(Label(text=borrower.username, font_size=16, color=(0, 0, 0, 1), size_hint=(0.25, 1)))
#             borrower_layout.add_widget(Label(text=borrower.account_number, font_size=16, color=(0, 0, 0, 1), size_hint=(0.25, 1)))
#             delete_button = RoundedButton(text='Delete', size_hint=(0.25, 1), font_size=16, bold=True)
#             delete_button.bind(on_press=lambda instance, acc_number=borrower.account_number: self.delete_borrower(acc_number))
#             borrower_layout.add_widget(delete_button)
#             self.borrower_details_layout.add_widget(borrower_layout)

#     def delete_borrower(self, account_number):
#         self.borrower_list.remove_borrower(account_number)
#         self.borrower_list.to_json('borrowers.json')
#         self.load_borrowers()
#         self.show_popup('Success', f'Borrower with account number {account_number} has been deleted.')

#     def on_search(self, instance):
#         query = self.search_bar.text.lower()
#         if query:
#             filtered_borrowers = [borrower for borrower in self.borrower_list.get_borrowers() if query in borrower.first_name.lower() or query in borrower.last_name.

# Clara, [6/22/2024 4:54 PM]
# lower() or query in borrower.username.lower() or query in borrower.account_number.lower()]
#             self.load_borrowers(filtered_borrowers)
#         else:
#             self.load_borrowers()

#     def show_popup(self, title, message):
#         popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
#         popup_label = Label(text=message, font_size=18, color=(0.2, 0.2, 0.2, 1))
#         popup_button = RoundedButton(text='Close', font_size=16, bold=True, size_hint=(None, None), size=(100, 40))

#         popup_layout.add_widget(popup_label)
#         popup_layout.add_widget(popup_button)