import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        'book_title',
        [
            'Гордость и предубеждение и зомби',
            'Преступление и наказание',
            'Мастер и Маргарита'
        ]
    )
    def test_add_new_book_new_book_has_empty_genre(self, collector, book_title):
        collector.add_new_book(book_title)

        assert collector.get_books_genre()[book_title] == ''

    def test_add_new_book_add_same_book_twice_book_is_present_only_once_in_collector(self, collector):
        book_title = 'Преступление и наказание'

        collector.add_new_book(book_title)
        collector.add_new_book(book_title)

        books = collector.get_books_genre()

        assert len(books) == 1 and books[book_title] == ''

    def test_add_new_book_book_title_is_empty_book_is_not_added_to_collector(self, collector):
        collector.add_new_book('')

        books = collector.get_books_genre()

        assert len(books) == 0

    @pytest.mark.parametrize(
        'book_title_length',
        [
            1,
            10,
            30,
            40
        ]
    )
    def test_add_new_book_book_title_is_between_0_and_41_characters_long_book_is_added_to_collection(self, collector, book_title_length):
        book_title = 'x' * book_title_length

        collector.add_new_book(book_title)

        books = collector.get_books_genre()

        assert len(books) == 1 and books[book_title] == ''

    @pytest.mark.parametrize(
        'book_title_length',
        [
            41,
            50,
            2002,
            11014
        ]
    )
    def test_add_new_book_book_title_is_more_than_41_characters_long_book_is_not_added_to_collection(self, collector, book_title_length):
        collector.add_new_book('x' * book_title_length)

        books = collector.get_books_genre()

        assert len(books) == 0
    
    @pytest.mark.parametrize(
        'genre',
        [
            'Фантастика',
            'Ужасы',
            'Детективы',
            'Мультфильмы',
            'Комедии'
        ]
    )
    def test_set_book_genre_book_and_genre_is_present_in_collector_genre_is_successfully_set(self, collector, genre):
        book_title = 'Братья Карамазовы'

        collector.add_new_book(book_title)

        collector.set_book_genre(book_title, genre)

        assert collector.get_book_genre(book_title) == genre

    @pytest.mark.parametrize(
        'genre',
        [
            'Фантастик',
            'Ужастик',
            'Детективчик',
            'Мультики среди книг',
            'Трагикомедия'
        ]
    )
    def test_set_book_genre_genre_is_not_present_in_collector_genre_is_not_set(self, collector, genre):
        book_title = 'Братья Карамазовы'

        collector.add_new_book(book_title)

        collector.set_book_genre(book_title, genre)

        assert collector.get_books_genre()[book_title] == ''
    
    def test_get_book_genre_book_is_added_to_collector_returns_book_genre(self, collector):
        book_title = 'Братья Карамазовы'

        collector.add_new_book(book_title)

        assert collector.get_book_genre(book_title) == ''

    @pytest.mark.parametrize(
        'book_title, book_genre',
        [
            ['Анна Каренина', 'Ужасы'],
            ['Война и мир', 'Фантастика'],
            ['Воскресение', 'Детективы']
        ]
    )
    def test_get_books_with_specific_genre_collector_has_books_with_specific_genre_returns_books_with_specific_genre(self, collector, book_title, book_genre):
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, book_genre)

        search_result = collector.get_books_with_specific_genre(book_genre)

        assert len(search_result) == 1 and book_title in search_result

    @pytest.mark.parametrize(
        'book_title, book_genre, searched_genre',
        [
            ['Анна Каренина', 'Ужасы', 'Мультфильмы'],
            ['Война и мир', 'Фантастика', 'Комедии'],
            ['Воскресение', 'Детективы', 'Фантастика']
        ]
    )
    def test_get_books_with_specific_genre_no_books_with_specific_genre_returns_empty_list(self, collector, book_title, book_genre, searched_genre):
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, book_genre)

        search_result = collector.get_books_with_specific_genre(searched_genre)

        assert len(search_result) == 0

    @pytest.mark.parametrize(
        'book_title, book_genre',
        [
            ['Марсианин', 'Фантастика'],
            ['Незнайка на луне', 'Мультфильмы'],
            ['Марс атакует!', 'Комедии']
        ]
    )
    def test_get_books_for_children_collector_has_books_of_child_genre_returns_appropriate_book_titles(self, collector, book_title, book_genre):
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, book_genre)

        child_books = collector.get_books_for_children()

        assert len(child_books) == 1 and book_title in child_books

    @pytest.mark.parametrize(
        'book_title, book_genre',
        [
            ['Нечто', 'Ужасы'],
            ['Твин Пикс', 'Детективы']
        ]
    )
    def test_get_books_for_children_collector_does_not_have_books_of_child_genre_returns_empty_list(self, collector, book_title, book_genre):
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, book_genre)

        child_books = collector.get_books_for_children()

        assert len(child_books) == 0

    def test_add_book_in_favorites_collector_has_book_book_is_added_to_favorites(self, collector):
        favorite_book_title = 'Сияние'
        collector.add_new_book(favorite_book_title)

        collector.add_book_in_favorites(favorite_book_title)

        assert favorite_book_title in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_collector_has_book_in_favorites_book_is_removed_from_favorites(self, collector):
        favorite_book_title = 'Властелин колец'
        collector.add_new_book(favorite_book_title)

        collector.add_book_in_favorites(favorite_book_title)
        collector.delete_book_from_favorites(favorite_book_title)

        assert len(collector.get_list_of_favorites_books()) == 0
