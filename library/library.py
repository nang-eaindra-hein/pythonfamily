import json
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from datetime import date, datetime, timedelta

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0, 0.6, 0.8, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(pos=self.update_rect, size=self.update_rect)
        
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class LibraryTreeNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class LibraryTree:
    def __init__(self):
        self.root = None

    def insert(self, item):
        if not self.root:
            self.root = LibraryTreeNode(item)
        else:
            self._insert_recursive(self.root, item)

    def _insert_recursive(self, node, item):
        if item['title'].lower() < node.item['title'].lower():
            if node.left:
                self._insert_recursive(node.left, item)
            else:
                node.left = LibraryTreeNode(item)
        else:
            if node.right:
                self._insert_recursive(node.right, item)
            else:
                node.right = LibraryTreeNode(item)

    def search(self, title):
        return self._search_recursive(self.root, title.lower())

    def _search_recursive(self, node, title):
        if not node:
            return []
        results = []
        if title in node.item['title'].lower():
            results.append(node.item)
        results += self._search_recursive(node.left, title)
        results += self._search_recursive(node.right, title)
        return results

class BorrowedItemsDatabase:
    def __init__(self, db_file='borrowed_items.json'):
        self.db_file = db_file
        self.borrowed_items = []
        self.load_from_json()

    def add_borrowed_item(self, item, first_name, last_name, username, account_number):
        borrowed_item = {
            'item': item,
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'account_number': account_number,
            'date_borrowed': str(date.today()),
            'date_returned': None  # Set to None when initially borrowed
        }
        self.borrowed_items.append(borrowed_item)
        self.save_to_json()

    def remove_borrowed_item(self, item):
        self.borrowed_items = [borrowed_item for borrowed_item in self.borrowed_items if borrowed_item['item'] != item]
        self.save_to_json()

    def load_from_json(self):
        try:
            with open(self.db_file, 'r') as file:
                self.borrowed_items = json.load(file)
        except FileNotFoundError:
            self.borrowed_items = []

    def save_to_json(self):
        with open(self.db_file, 'w') as file:
            json.dump(self.borrowed_items, file, indent=4)

    def get_active_borrowed_items_count(self):
        return sum(1 for item in self.borrowed_items if item['date_returned'] is None)

    def calculate_fines(self):
        fines = []
        for borrowed_item in self.borrowed_items:
            if borrowed_item['date_returned'] is None:
                date_borrowed = datetime.strptime(borrowed_item['date_borrowed'], '%Y-%m-%d').date()
                days_borrowed = (date.today() - date_borrowed).days
                if days_borrowed > 25:
                    days_delayed = days_borrowed - 25
                    fine_amount = days_delayed * 10  # $10 per day
                    fines.append({
                        'first_name': borrowed_item.get('first_name', 'Unknown'),
                        'last_name': borrowed_item.get('last_name', 'Unknown'),
                        'username': borrowed_item.get('username', 'Unknown'),
                        'account_number': borrowed_item.get('account_number', 'Unknown'),
                        'title': borrowed_item['item']['title'],
                        'days_delayed': days_delayed,
                        'fine_amount': fine_amount
                    })
        return fines

    def calculate_due_date(self, date_borrowed):
        return date_borrowed + timedelta(days=25)

class LibraryScreen(Screen):
    def __init__(self, **kwargs):
        super(LibraryScreen, self).__init__(**kwargs)
        self.page = 0
        self.items_per_page = 5
        self.library_tree = LibraryTree()
        self.borrowed_items_db = BorrowedItemsDatabase()
        self.load_items()
        self.build_ui()

    def load_items(self):
        self.books = self.load_items_from_file('books.json')
        self.audiobooks = self.load_items_from_file('audiobooks.json')
        self.periodicals = self.load_items_from_file('periodicals.json')
        for item in self.books + self.audiobooks + self.periodicals:
            self.library_tree.insert(item)

    def load_items_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                items = json.load(file)
                return items
        except FileNotFoundError:
            print(f"{file_path} not found. Starting with an empty list.")
            return []

    def build_ui(self):
        self.root = FloatLayout()

        # Set background color to white
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Add a vertical BoxLayout for top elements (search bar, title)
        top_layout = BoxLayout(orientation='vertical', size_hint=(1, None), height=150, spacing=10)
        top_layout.pos_hint = {'top': 1}

        # Add a horizontal BoxLayout for search bar and button
        search_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50, spacing=10)
        search_layout.pos_hint = {'top': 1}

        # Add the search bar
        self.search_bar = TextInput(hint_text='Search for a book...', size_hint=(0.7, None), height=40)
        search_layout.add_widget(self.search_bar)

        # Add the search button
        search_button = RoundedButton(text='Search', size_hint=(0.3, None), background_color=(0.6, 0.8, 1, 1), height=40)
        search_button.bind(on_press=self.on_search)
        search_layout.add_widget(search_button)

        # Add the search layout to the top layout
        top_layout.add_widget(search_layout)

        # Add a label for the title
        self.title = Label(text='Library', font_size=32, bold=True, color=(0, 0, 0, 1))
        self.title.size_hint = (None, None)
        self.title.size = (self.width, 50)
        self.title.pos_hint = {'center_x': 0.5}
        top_layout.add_widget(self.title)

        # Add the top layout to the root layout
        self.root.add_widget(top_layout)

        # Add the ScrollView to hold the library items
        self.scroll_view = ScrollView(size_hint=(1, 0.6))
        self.scroll_view.pos_hint = {'center_x': 0.5, 'top': 0.65}
        self.library_list_content = BoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=20)
        self.library_list_content.bind(minimum_height=self.library_list_content.setter('height'))
        self.scroll_view.add_widget(self.library_list_content)
        self.root.add_widget(self.scroll_view)

        # Add a horizontal BoxLayout for bottom buttons
        bottom_layout = BoxLayout(orientation='vertical', size_hint=(1, None), height=150, spacing=20)
        bottom_layout.pos_hint = {'center_x': 0.5, 'y': 0.05}

        # Add a fine button
        fine_button = RoundedButton(text='Fine', font_size=18, bold=True, size_hint=(None, None), background_color=(0.6, 0.8, 1, 1), size=(150, 50))
        fine_button.bind(on_press=self.show_fine)
        bottom_layout.add_widget(fine_button)

        # Add a back button
        back_button = RoundedButton(text='Back', font_size=18, bold=True, size_hint=(None, None), background_color=(0.6, 0.8, 1, 1), size=(100, 50))
        back_button.bind(on_press=self.go_back)
        bottom_layout.add_widget(back_button)

        # Add a borrow item button
        borrow_item_button = RoundedButton(text='Borrow Item', font_size=18, bold=True, size_hint=(None, None), background_color=(0.6, 0.8, 1, 1), size=(150, 50))
        borrow_item_button.bind(on_press=self.show_borrowed_items)
        bottom_layout.add_widget(borrow_item_button)

        self.root.add_widget(bottom_layout)

        # Add pagination buttons layout to the bottom layout
        self.pagination_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50, spacing=20)
        self.root.add_widget(self.pagination_layout)

        self.add_widget(self.root)
        self.update_book_list()
        self.update_pagination_buttons()

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_search(self, instance):
        search_query = self.search_bar.text
        search_results = self.library_tree.search(search_query)
        if search_results:
            self.show_search_results_popup(search_results)
        else:
            self.show_popup('Search Results', 'No book found with the given title.')

    def show_search_results_popup(self, items):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        scroll_view = ScrollView(size_hint=(1, 1))
        items_list = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        items_list.bind(minimum_height=items_list.setter('height'))

        for item in items:
            item_layout = BoxLayout(orientation='horizontal', padding=10, spacing=20, size_hint_y=None)
            item_label = Label(text=f"Title: {item['title']}\nAuthor: {item['authors']}\nYear Published: {item['year_published']}", font_size=18, color=(1, 1, 1, 1))
            borrow_button = RoundedButton(text='Borrow', size_hint=(None, None), size=(100, 40))
            borrow_button.bind(on_press=lambda instance, item=item: self.borrow_item_and_update_popup(item, items_list, item_layout))
            item_layout.add_widget(item_label)
            item_layout.add_widget(borrow_button)
            items_list.add_widget(item_layout)

        scroll_view.add_widget(items_list)
        popup_layout.add_widget(scroll_view)

        close_button = RoundedButton(text='Close', font_size=16, bold=True, size_hint=(None, None), size=(100, 40))
        close_button.bind(on_press=lambda instance: popup.dismiss())
        popup_layout.add_widget(close_button)

        popup = Popup(title='Search Results', content=popup_layout, background_color=(0.53, 0.81, 0.92, 1), size_hint=(0.75, 0.75))
        popup.open()

    def borrow_item_and_update_popup(self, item, items_list, item_layout):
        self.borrow_item(item)
        items_list.remove_widget(item_layout)

    def show_borrowed_items(self, instance):
        borrowed_items = self.borrowed_items_db.borrowed_items

        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        scroll_view = ScrollView(size_hint=(1, 1))
        items_list = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        items_list.bind(minimum_height=items_list.setter('height'))

        for borrowed_item in borrowed_items:
            item = borrowed_item['item']
            if not borrowed_item['date_returned']:
                item_layout = BoxLayout(orientation='horizontal', padding=10, spacing=20, size_hint_y=None)
                date_borrowed = datetime.strptime(borrowed_item['date_borrowed'], '%Y-%m-%d').date()
                due_date = self.borrowed_items_db.calculate_due_date(date_borrowed)
                item_label = Label(text=f"Title: {item['title']}\nBorrowed Date: {borrowed_item['date_borrowed']}\nDue Date: {due_date}", font_size=18, color=(1, 1, 1, 1))
                remove_button = RoundedButton(text='Remove', size_hint=(None, None), size=(100, 40))
                remove_button.bind(on_press=lambda instance, item=item: self.remove_borrowed_item(item, items_list, item_layout))
                item_layout.add_widget(item_label)
                item_layout.add_widget(remove_button)
                items_list.add_widget(item_layout)

        scroll_view.add_widget(items_list)
        popup_layout.add_widget(scroll_view)

        close_button = RoundedButton(text='Close', font_size=16, bold=True, size_hint=(None, None), background_color=(0.6, 0.8, 1, 1), size=(100, 40))
        close_button.bind(on_press=lambda instance: popup.dismiss())
        popup_layout.add_widget(close_button)

        popup = Popup(title='Borrowed Items', content=popup_layout, background_color=(0.6, 0.8, 1, 1), size_hint=(0.75, 0.75))
        popup.open()

    def remove_borrowed_item(self, item, items_list, item_layout):
        self.borrowed_items_db.remove_borrowed_item(item)
        items_list.remove_widget(item_layout)

    def go_back(self, instance):
        self.manager.current = 'user_panel'

    def update_book_list(self):
        self.library_list_content.clear_widgets()
        start_index = self.page * self.items_per_page
        end_index = start_index + self.items_per_page
        all_items = self.books + self.audiobooks + self.periodicals
        for item in all_items[start_index:end_index]:
            item_info = self.create_item_info(item)
            self.library_list_content.add_widget(item_info)

    def create_item_info(self, item):
        item_info = BoxLayout(orientation='horizontal', padding=10, spacing=20, size_hint_y=None)
        
        # Information Box
        info_box = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_x=0.8)
        title_label = Label(text=f"Title: {item['title']}", font_size=20, color=(1, 1, 1, 1), bold=True)
        author_label = Label(text=f"Author: {item['authors']}", font_size=18, color=(1, 1, 1, 1))
        year_label = Label(text=f"Year Published: {item['year_published']}", font_size=18, color=(1, 1, 1, 1))
        info_box.add_widget(title_label)
        info_box.add_widget(author_label)
        info_box.add_widget(year_label)

        # Borrow Button
        borrow_button = RoundedButton(text='Borrow', size_hint=(None, None), background_color=(0.6, 0.8, 1, 1), size=(150, 50))
        borrow_button.bind(on_press=lambda instance, item=item: self.borrow_item(item))

        item_info.add_widget(info_box)
        item_info.add_widget(borrow_button)

        return item_info

    def update_pagination_buttons(self):
        self.pagination_layout.clear_widgets()
        all_items = self.books + self.audiobooks + self.periodicals
        num_pages = len(all_items) // self.items_per_page + (1 if len(all_items) % self.items_per_page != 0 else 0)
        for i in range(num_pages):
            btn = RoundedButton(text=str(i + 1), size_hint=(None, None), size=(50, 50))
            btn.bind(on_press=lambda instance, page=i: self.goto_page(page))
            self.pagination_layout.add_widget(btn)

    def goto_page(self, page):
        self.page = page
        self.update_book_list()
        self.update_pagination_buttons()

    def borrow_item(self, item):
        try:
            # Check the number of active borrowed items
            active_borrowed_count = self.borrowed_items_db.get_active_borrowed_items_count()
            print(f"Active borrowed items count: {active_borrowed_count}")

            if active_borrowed_count >= 8:
                self.show_popup('Limit Reached!', 'You cannot borrow more than 8 items at a time.')
                return

            # Add the item to the borrowed items database
            # Using placeholder names for demonstration
            self.borrowed_items_db.add_borrowed_item(item, "First", "Last", "username", "account_number")
            self.show_popup('Success', f'You have successfully borrowed "{item["title"]}".')
        except Exception as e:
            print(f"Error borrowing item: {e}")
            self.show_popup('Error', f'An error occurred: {str(e)}')

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        popup_label = Label(text=message, font_size=18, color=(1, 1, 1, 1))
        popup_button = RoundedButton(text='Close', font_size=16, bold=True, size_hint=(None, None), size=(100, 40))
        
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(0.75, 0.5))
        popup_button.bind(on_press=popup.dismiss)

        popup.open()

    def show_fine(self, instance):
        fines = self.borrowed_items_db.calculate_fines()

        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        scroll_view = ScrollView(size_hint=(1, 1))
        fines_list = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        fines_list.bind(minimum_height=fines_list.setter('height'))

        if fines:
            for fine in fines:
                fine_layout = BoxLayout(orientation='vertical', padding=10, spacing=20, size_hint_y=None)
                fine_label = Label(text=f"Borrower Name: {fine['first_name']} {fine['last_name']}\n"
                                        f"Username: {fine['username']}\n"
                                        f"Account Number: {fine['account_number']}\n"
                                        f"Borrowed Item: {fine['title']}\n"
                                        f"Days Delayed: {fine['days_delayed']}\n"
                                        f"Total Fine: ${fine['fine_amount']}", font_size=18, color=(1, 1, 1, 1))
                print_receipt_button = RoundedButton(text='Print the Receipt', size_hint=(None, None), size=(150, 40))
                print_receipt_button.bind(on_press=lambda instance, fine=fine: self.print_receipt(fine))
                fine_layout.add_widget(fine_label)
                fine_layout.add_widget(print_receipt_button)
                fines_list.add_widget(fine_layout)
        else:
            no_fines_label = Label(text="No fines to display.", font_size=18, color=(1, 1, 1, 1))
            fines_list.add_widget(no_fines_label)

        scroll_view.add_widget(fines_list)
        popup_layout.add_widget(scroll_view)

        close_button = RoundedButton(text='Close', font_size=16, bold=True, size_hint=(None, None), size=(100, 40))
        close_button.bind(on_press=lambda instance: popup.dismiss())
        popup_layout.add_widget(close_button)

        popup = Popup(title='Fines:an additional fine of $10 per item per day will be applied for delayed return of items. Borrowers are encouraged to return items on or before the specified due date to avoid accruing extra charges.There will need to be charge 10$ ',
                       content=popup_layout, background_color=(0.6, 0.8, 1, 1), size_hint=(0.75, 0.75))
        popup.open()

    def print_receipt(self, fine):
        receipt_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        receipt_label = Label(text=f"Fine Receipt\n\n"
                                   f"Borrower Name: {fine['first_name']} {fine['last_name']}\n"
                                   f"Username: {fine['username']}\n"
                                   f"Account Number: {fine['account_number']}\n"
                                   f"Borrowed Item: {fine['title']}\n"
                                   f"Days Delayed: {fine['days_delayed']}\n"
                                   f"Total Fine: ${fine['fine_amount']}", font_size=18, color=(1, 1, 1, 1))
        
        close_button = RoundedButton(text='Close', font_size=16, bold=True, size_hint=(None, None), size=(100, 40))
        close_button.bind(on_press=lambda instance: receipt_popup.dismiss())

        receipt_layout.add_widget(receipt_label)
        receipt_layout.add_widget(close_button)

        receipt_popup = Popup(title='Receipt', content=receipt_layout, background_color=(0.6, 0.8, 1, 1), size_hint=(0.75, 0.5))
        receipt_popup.open()