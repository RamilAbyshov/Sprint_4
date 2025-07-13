import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Машина времени')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name, expected", [
        ("451 градус по Фаренгейту", True),
        ("", False),
        ("A" * 41, False),
    ])
    def test_add_new_book_various_names(self, collector, book_name, expected):
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected

    def test_new_book_has_empty_genre(self, collector):
        collector.add_new_book("Мечтают ли андроиды об электроовцах")
        assert collector.get_book_genre("Мечтают ли андроиды об электроовцах") == ""

    def test_set_book_genre_for_existing_book(self, collector):
        collector.add_new_book("Сияние")
        collector.set_book_genre("Сияние", "Ужасы")
        assert collector.get_book_genre("Сияние") == "Ужасы"

    def test_set_book_genre_for_nonexistent_book(self, collector):
        collector.set_book_genre("Неизвестная книга", "Ужасы")
        assert collector.get_book_genre("Неизвестная книга") is None

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Исторический")
        assert collector.get_book_genre("Дюна") == ""

    def test_get_books_with_specific_genre_returns_correct_list(self, collector):
        collector.add_new_book("Дюна")
        collector.add_new_book("Сияние")
        collector.add_new_book("Убийство в Восточном экспрессе")
        collector.set_book_genre("Дюна", "Фантастика")
        collector.set_book_genre("Сияние", "Ужасы")
        collector.set_book_genre("Убийство в Восточном экспрессе", "Детективы")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Дюна"]

    def test_get_books_with_specific_genre_empty_for_unknown_genre(self, collector):
        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")
        assert collector.get_books_with_specific_genre("Исторический") == []

    def test_get_books_genre_returns_correct_dict(self, collector):
        collector.add_new_book("Заводной апельсин")
        collector.set_book_genre("Заводной апельсин", "Фантастика")
        assert collector.get_books_genre() == {"Заводной апельсин": "Фантастика"}

    def test_get_books_for_children_includes_only_allowed_genres(self, collector):
        collector.add_new_book("451 градус по Фаренгейту")
        collector.add_new_book("Сияние")
        collector.add_new_book("Убийство в Восточном экспрессе")
        collector.add_new_book("Трое в лодке, не считая собаки")
        collector.set_book_genre("451 градус по Фаренгейту", "Фантастика")
        collector.set_book_genre("Сияние", "Ужасы")
        collector.set_book_genre("Убийство в Восточном экспрессе", "Детективы")
        collector.set_book_genre("Трое в лодке, не считая собаки", "Комедии")
        children_books = collector.get_books_for_children()
        assert "451 градус по Фаренгейту" in children_books

    def test_get_books_for_children_excludes_horror_and_detective(self, collector):
        collector.add_new_book("Сияние")
        collector.add_new_book("Убийство в Восточном экспрессе")
        collector.set_book_genre("Сияние", "Ужасы")
        collector.set_book_genre("Убийство в Восточном экспрессе", "Детективы")
        children_books = collector.get_books_for_children()
        assert "Сияние" not in children_books
        assert "Убийство в Восточном экспрессе" not in children_books

    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Дюна")
        assert "Дюна" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_nonexistent_book(self, collector):
        collector.add_book_in_favorites("Неизвестная книга")
        assert "Неизвестная книга" not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_no_duplicates(self, collector):
        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Дюна")
        collector.add_book_in_favorites("Дюна")
        assert collector.get_list_of_favorites_books().count("Дюна") == 1

    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book("Сияние")
        collector.add_book_in_favorites("Сияние")
        collector.delete_book_from_favorites("Сияние")
        assert "Сияние" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_nonexistent_book(self, collector):
        collector.delete_book_from_favorites("Неизвестная книга")
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.add_new_book("Дюна")
        collector.add_new_book("Сияние")
        collector.add_book_in_favorites("Дюна")
        collector.add_book_in_favorites("Сияние")
        assert collector.get_list_of_favorites_books() == ["Дюна", "Сияние"]
