import json
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, Rectangle

class AdminLibraryScreen(Screen):
    def __init__(self, **kwargs):
        super(AdminLibraryScreen, self).__init__(**kwargs)
        self.library = Library()
        self.library.from_json_books()
        self.library.from_json_periodicals()
        self.library.from_json_audiobooks()
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

        # Header
        header = Label(text="View Library by Admin", font_size='24sp', color=[0.13, 0.55, 0.13, 1], size_hint=(1, 0.2), bold=True)
        header_box = BoxLayout(size_hint=(1, 0.2), padding=[0, 20, 0, 0])
        header_box.add_widget(header)
        layout.add_widget(header_box)

        # Buttons
        button_layout = GridLayout(cols=2, spacing=20, size_hint=(1, 0.6))

        add_book_button = Button(text="Add Book", size_hint=(1, 0.2), color=[0.13, 0.55, 0.13, 1], background_color=[0.6, 0.8, 1, 1])
        edit_book_button = Button(text="Edit Book", size_hint=(1, 0.2), color=[0.13, 0.55, 0.13, 1], background_color=[0.6, 0.8, 1, 1])
        add_periodical_button = Button(text="Add Periodical", size_hint=(1, 0.2), color=[0.13, 0.55, 0.13, 1], background_color=[0.6, 0.8, 1, 1])
        edit_periodical_button = Button(text="Edit Periodical", size_hint=(1, 0.2), color=[0.13, 0.55, 0.13, 1], background_color=[0.6, 0.8, 1, 1])
        add_audiobook_button = Button(text="Add Audiobook", size_hint=(1, 0.2), color=[0.13, 0.55, 0.13, 1], background_color=[0.6, 0.8, 1, 1])
        edit_audiobook_button = Button(text="Edit Audiobook", size_hint=(1, 0.2), color=[0.13, 0.55, 0.13, 1], background_color=[0.6, 0.8, 1, 1])

        add_book_button.bind(on_press=self.show_add_book_popup)
        edit_book_button.bind(on_press=lambda instance: self.show_edit_items_popup("Edit Books", self.library.books, self.edit_book, self.delete_book))
        add_periodical_button.bind(on_press=self.show_add_periodical_popup)
        edit_periodical_button.bind(on_press=lambda instance: self.show_edit_items_popup("Edit Periodicals", self.library.periodicals, self.edit_periodical, self.delete_periodical))
        add_audiobook_button.bind(on_press=self.show_add_audiobook_popup)
        edit_audiobook_button.bind(on_press=lambda instance: self.show_edit_items_popup("Edit Audiobooks", self.library.audiobooks, self.edit_audiobook, self.delete_audiobook))

        button_layout.add_widget(add_book_button)
        button_layout.add_widget(edit_book_button)
        button_layout.add_widget(add_periodical_button)
        button_layout.add_widget(edit_periodical_button)
        button_layout.add_widget(add_audiobook_button)
        button_layout.add_widget(edit_audiobook_button)

        layout.add_widget(button_layout)

        # Back button
        back_button = Button(text="Back", size_hint=(1, 0.2), background_color=[0.13, 0.55, 0.13, 1])
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'admin_pannel'

    def show_add_book_popup(self, instance):
        self.show_add_item_popup("Add Book", self.add_book, include_isbn=True)

    def show_add_periodical_popup(self, instance):
        self.show_add_item_popup("Add Periodical", self.add_periodical)

    def show_add_audiobook_popup(self, instance):
        self.show_add_item_popup("Add Audiobook", self.add_audiobook, include_isbn=True, include_audio_format=True)

    def show_add_item_popup(self, title, add_function, include_isbn=False, include_audio_format=False):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        header = Label(text=title, font_size='24sp', color=[0.13, 0.55, 0.13, 1], bold=True, size_hint_y=None, height=20)
        popup_layout.add_widget(header)

        input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=100)
        input_layout.bind(minimum_height=input_layout.setter('height'))

        self.title_input = TextInput(hint_text="Title", multiline=False, size_hint_y=None, height=40, font_size=18)
        self.category_input = Spinner(text="Select Category", values=("Fiction", "Non-Fiction", "Science", "History", "Biography", "Children", "Mystery", "Fantasy"), size_hint_y=None, height=40, font_size=18)
        self.language_input = Spinner(text="Select Language", values=("English", "Thai", "Burmese", "Spanish", "Chinese"), size_hint_y=None, height=40, font_size=18)
        self.authors_input = TextInput(hint_text="Authors", multiline=False, size_hint_y=None, height=40, font_size=18)
        self.year_published_input = TextInput(hint_text="Year Published", multiline=False, size_hint_y=None, height=40, font_size=18)

        input_layout.add_widget(Label(text="Title:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
        input_layout.add_widget(self.title_input)
        input_layout.add_widget(Label(text="Category:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
        input_layout.add_widget(self.category_input)
        input_layout.add_widget(Label(text="Language:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
        input_layout.add_widget(self.language_input)
        input_layout.add_widget(Label(text="Authors:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
        input_layout.add_widget(self.authors_input)
        input_layout.add_widget(Label(text="Year Published:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
        input_layout.add_widget(self.year_published_input)

        if include_isbn:
            self.isbn_input = TextInput(hint_text="ISBN", multiline=False, size_hint_y=None, height=40, font_size=18)
            input_layout.add_widget(Label(text="ISBN:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
            input_layout.add_widget(self.isbn_input)

        if include_audio_format:
            self.audio_format_input = Spinner(text="Select Audio Format", values=("Mp3", "Others"), size_hint_y=None, height=40, font_size=18)
            input_layout.add_widget(Label(text="Audio Format:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
            input_layout.add_widget(self.audio_format_input)

        popup_layout.add_widget(input_layout)

        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        add_button = Button(text="Add", size_hint_x=None, width=100, background_color=[0.13, 0.55, 0.13, 1])
        cancel_button = Button(text="Cancel", size_hint_x=None, width=100, background_color=[0.13, 0.55, 0.13, 1])

        add_button.bind(on_press=add_function)
        cancel_button.bind(on_press=lambda x: self.popup.dismiss())

        button_layout.add_widget(add_button)
        button_layout.add_widget(cancel_button)

        popup_layout.add_widget(button_layout)

        self.popup = Popup(title=title, content=popup_layout, size_hint=(0.9, 0.9))
        self.popup.open()

    def show_edit_items_popup(self, title, items, edit_function, delete_function):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        header = Label(text=title, font_size='24sp', color=[0.13, 0.55, 0.13, 1], bold=True, size_hint_y=None, height=30)
        popup_layout.add_widget(header)

        item_layout = GridLayout(cols=4, spacing=10, size_hint_y=None)
        item_layout.bind(minimum_height=item_layout.setter('height'))

        # Add the headers
        item_layout.add_widget(Label(text="Number", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=30, font_size=18))
        item_layout.add_widget(Label(text="Name of the item", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=30, font_size=18))
        item_layout.add_widget(Label(text="", size_hint_y=None, height=30))  # Empty for the buttons column
        item_layout.add_widget(Label(text="", size_hint_y=None, height=30))  # Empty for the buttons column

        scroll_view = ScrollView(size_hint=(1, 1))

        for index, item in enumerate(items, start=1):
            number_label = Label(text=str(index), color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=30, font_size=18)
            name_label = Label(text=item.title, color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=30, font_size=18)
            edit_button = Button(text="Edit", size_hint_y=None, height=30, size_hint_x=None, width=100, background_color=[0.13, 0.55, 0.13, 1])
            delete_button = Button(text="Delete", size_hint_y=None, height=30, size_hint_x=None, width=100, background_color=[0.13, 0.55, 0.13, 1])

            edit_button.bind(on_press=lambda x, item=item: edit_function(item))
            delete_button.bind(on_press=lambda x, item=item: delete_function(item))

            item_layout.add_widget(number_label)
            item_layout.add_widget(name_label)
            item_layout.add_widget(edit_button)
            item_layout.add_widget(delete_button)

        scroll_view.add_widget(item_layout)
        popup_layout.add_widget(scroll_view)

        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        close_button = Button(text="Close", size_hint_x=None, width=100, background_color=[0.13, 0.55, 0.13, 1])
        close_button.bind(on_press=lambda x: self.popup.dismiss())
        button_layout.add_widget(close_button)
        popup_layout.add_widget(button_layout)

        self.popup = Popup(title=title, content=popup_layout, size_hint=(0.9, 0.9))
        self.popup.open()

    def show_edit_item_popup(self, title, item, save_function):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        header = Label(text=title, font_size='24sp', color=[0.13, 0.55, 0.13, 1], bold=True, size_hint_y=None, height=30)
        popup_layout.add_widget(header)

        input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=100)
        input_layout.bind(minimum_height=input_layout.setter('height'))

        self.title_input = TextInput(text=item.title, multiline=False, size_hint_y=None, height=40, font_size=18)
        self.category_input = Spinner(text=item.category, values=("Fiction", "Non-Fiction", "Science", "History", "Biography", "Children", "Mystery", "Fantasy"), size_hint_y=None, height=40, font_size=18)
        self.language_input = Spinner(text=item.language, values=("English", "Thai", "Burmese", "Spanish", "Chinese"), size_hint_y=None, height=40, font_size=18)
        self.authors_input = TextInput(text=item.authors, multiline=False, size_hint_y=None, height=40, font_size=18)
        self.year_published_input = TextInput(text=item.year_published, multiline=False, size_hint_y=None, height=40, font_size=18)

        input_layout.add_widget(Label(text="Title:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
        input_layout.add_widget(self.title_input)
        input_layout.add_widget(Label(text="Category:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
        input_layout.add_widget(self.category_input)
        input_layout.add_widget(Label(text="Language:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
        input_layout.add_widget(self.language_input)
        input_layout.add_widget(Label(text="Authors:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
        input_layout.add_widget(self.authors_input)
        input_layout.add_widget(Label(text="Year Published:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
        input_layout.add_widget(self.year_published_input)

        if hasattr(item, 'isbn'):
            self.isbn_input = TextInput(text=item.isbn, multiline=False, size_hint_y=None, height=40, font_size=18)
            input_layout.add_widget(Label(text="ISBN:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
            input_layout.add_widget(self.isbn_input)

        if hasattr(item, 'audio_format'):
            self.audio_format_input = Spinner(text=item.audio_format, values=("Mp3", "Others"), size_hint_y=None, height=40, font_size=18)
            input_layout.add_widget(Label(text="Audio Format:", color=[0.13, 0.55, 0.13, 1], size_hint_y=None, height=40, font_size=18))
            input_layout.add_widget(self.audio_format_input)

        popup_layout.add_widget(input_layout)

        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        save_button = Button(text="Save", size_hint_x=None, width=100, background_color=[0.13, 0.55, 0.13, 1])
        cancel_button = Button(text="Cancel", size_hint_x=None, width=100, background_color=[0.13, 0.55, 0.13, 1])

        save_button.bind(on_press=lambda x: save_function(item))
        cancel_button.bind(on_press=lambda x: self.popup.dismiss())

        button_layout.add_widget(save_button)
        button_layout.add_widget(cancel_button)

        popup_layout.add_widget(button_layout)

        self.popup = Popup(title=title, content=popup_layout, size_hint=(0.9, 0.9))
        self.popup.open()

    def add_book(self, instance):
        title = self.title_input.text
        category = self.category_input.text
        language = self.language_input.text
        authors = self.authors_input.text
        year_published = self.year_published_input.text
        isbn = self.isbn_input.text if hasattr(self, 'isbn_input') else None

        book = Book(title, category, language, authors, year_published, isbn)
        self.library.add_book(book)
        self.library.to_json_books()
        self.popup.dismiss()
        self.show_confirmation_popup("Book added successfully.")

    def add_periodical(self, instance):
        title = self.title_input.text
        category = self.category_input.text
        language = self.language_input.text
        authors = self.authors_input.text
        year_published = self.year_published_input.text

        periodical = Periodical(title, category, language, authors, year_published)
        self.library.add_periodical(periodical)
        self.library.to_json_periodicals()
        self.popup.dismiss()
        self.show_confirmation_popup("Periodical added successfully.")

    def add_audiobook(self, instance):
        title = self.title_input.text
        category = self.category_input.text
        language = self.language_input.text
        authors = self.authors_input.text
        year_published = self.year_published_input.text
        isbn = self.isbn_input.text if hasattr(self, 'isbn_input') else None
        audio_format = self.audio_format_input.text if hasattr(self, 'audio_format_input') else None

        audiobook = AudioBook(title, category, language, authors, year_published, isbn, audio_format)
        self.library.add_audiobook(audiobook)
        self.library.to_json_audiobooks()
        self.popup.dismiss()
        self.show_confirmation_popup("Audiobook added successfully.")

    def edit_book(self, book):
        self.show_edit_item_popup("Edit Book", book, self.save_book)

    def save_book(self, book):
        book.title = self.title_input.text
        book.category = self.category_input.text
        book.language = self.language_input.text
        book.authors = self.authors_input.text
        book.year_published = self.year_published_input.text
        if hasattr(self, 'isbn_input'):
            book.isbn = self.isbn_input.text
        self.library.to_json_books()
        self.popup.dismiss()
        self.show_confirmation_popup("Book edited successfully.")

    def delete_book(self, book):
        self.library.books.remove(book)
        self.library.to_json_books()
        self.popup.dismiss()
        self.show_confirmation_popup("Book deleted successfully.")

    def edit_periodical(self, periodical):
        self.show_edit_item_popup("Edit Periodical", periodical, self.save_periodical)

    def save_periodical(self, periodical):
        periodical.title = self.title_input.text
        periodical.category = self.category_input.text
        periodical.language = self.language_input.text
        periodical.authors = self.authors_input.text
        periodical.year_published = self.year_published_input.text
        self.library.to_json_periodicals()
        self.popup.dismiss()
        self.show_confirmation_popup("Periodical edited successfully.")

    def delete_periodical(self, periodical):
        self.library.periodicals.remove(periodical)
        self.library.to_json_periodicals()
        self.popup.dismiss()
        self.show_confirmation_popup("Periodical deleted successfully.")

    def edit_audiobook(self, audiobook):
        self.show_edit_item_popup("Edit Audiobook", audiobook, self.save_audiobook)

    def save_audiobook(self, audiobook):
        audiobook.title = self.title_input.text
        audiobook.category = self.category_input.text
        audiobook.language = self.language_input.text
        audiobook.authors = self.authors_input.text
        audiobook.year_published = self.year_published_input.text
        if hasattr(self, 'isbn_input'):
            audiobook.isbn = self.isbn_input.text
        if hasattr(self, 'audio_format_input'):
            audiobook.audio_format = self.audio_format_input.text
        self.library.to_json_audiobooks()
        self.popup.dismiss()
        self.show_confirmation_popup("Audiobook edited successfully.")

    def delete_audiobook(self, audiobook):
        self.library.audiobooks.remove(audiobook)
        self.library.to_json_audiobooks()
        self.popup.dismiss()
        self.show_confirmation_popup("Audiobook deleted successfully.")

    def show_confirmation_popup(self, message):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        message_label = Label(text=message, font_size=18, color=(1, 1, 1, 1))
        close_button = Button(text="Close", size_hint_y=None, height=40, on_press=lambda x: self.popup.dismiss())

        popup_layout.add_widget(message_label)
        popup_layout.add_widget(close_button)

        self.popup = Popup(title="Confirmation", content=popup_layout, size_hint=(0.7, 0.3))
        self.popup.open()

class Book:
    def __init__(self, title, category, language, authors, year_published, isbn):
        self.title = title
        self.category = category
        self.language = language
        self.authors = authors
        self.year_published = year_published
        self.isbn = isbn

class Periodical:
    def __init__(self, title, category, language, authors, year_published):
        self.title = title
        self.category = category
        self.language = language
        self.authors = authors
        self.year_published = year_published

class AudioBook:
    def __init__(self, title, category, language, authors, year_published, isbn, audio_format):
        self.title = title
        self.category = category
        self.language = language
        self.authors = authors
        self.year_published = year_published
        self.isbn = isbn
        self.audio_format = audio_format

class Library:
    def __init__(self):
        self.books = []
        self.periodicals = []
        self.audiobooks = []

    def add_book(self, book):
        self.books.append(book)

    def add_periodical(self, periodical):
        self.periodicals.append(periodical)

    def add_audiobook(self, audiobook):
        self.audiobooks.append(audiobook)

    def to_json_books(self):
        with open('books.json', 'w') as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4)

    def from_json_books(self):
        try:
            with open('books.json', 'r') as f:
                self.books = [Book(**book) for book in json.load(f)]
        except FileNotFoundError:
            pass

    def to_json_periodicals(self):
        with open('periodicals.json', 'w') as f:
            json.dump([periodical.__dict__ for periodical in self.periodicals], f, indent=4)

    def from_json_periodicals(self):
        try:
            with open('periodicals.json', 'r') as f:
                self.periodicals = [Periodical(**periodical) for periodical in json.load(f)]
        except FileNotFoundError:
            pass

    def to_json_audiobooks(self):
        with open('audiobooks.json', 'w') as f:
            json.dump([audiobook.__dict__ for audiobook in self.audiobooks], f, indent=4)

    def from_json_audiobooks(self):
        try:
            with open('audiobooks.json', 'r') as f:
                self.audiobooks = [AudioBook(**audiobook) for audiobook in json.load(f)]
        except FileNotFoundError:
            pass
