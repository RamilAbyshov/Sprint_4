# qa_python

# Тесты для приложения BooksCollector

| №  | Название теста                                             | Описание                                                                                   |
|-----|------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| 1   | `test_add_new_book_add_two_books`                          | Проверяет добавление двух разных книг и их наличие в коллекции.                            |
| 2   | `test_add_new_book_various_names`                          | Проверяет добавление книги с разными названиями: корректными, пустыми и слишком длинными.  |
| 3   | `test_new_book_has_empty_genre`                            | Проверяет, что у только что добавленной книги жанр не установлен (пустая строка).          |
| 4   | `test_set_book_genre_for_existing_book`                    | Проверяет успешную установку жанра для существующей книги.                                |
| 5   | `test_set_book_genre_for_nonexistent_book`                 | Проверяет, что жанр не устанавливается для книги, если она отсутствует в коллекции.              |
| 6   | `test_set_book_genre_invalid_genre`                        | Проверяет, что нельзя установить жанр, отсутствующий в списке жанров.         |
| 7   | `test_get_books_with_specific_genre_returns_correct_list`  | Проверяет, что метод возвращает список книг с заданным жанром.                             |
| 8   | `test_get_books_with_specific_genre_empty_for_unknown_genre` | Проверяет, что для неизвестного жанра возвращается пустой список.                          |
| 9   | `test_get_books_genre_returns_correct_dict`                | Проверяет, что возвращается полный словарь книг с жанрами.                               |
| 10  | `test_get_books_for_children_includes_only_allowed_genres` | Проверяет, что в список детских книг попадают только книги без возрастных ограничений.    |
| 11  | `test_get_books_for_children_excludes_horror_and_detective` | Проверяет, что книги с возрастным рейтингом (ужасы, детективы) исключены из детских книг. |
| 12  | `test_add_book_in_favorites_success`                       | Проверяет успешное добавление книги из коллекции в избранное.                             |
| 13  | `test_add_book_in_favorites_nonexistent_book`              | Проверяет, что нельзя добавить в избранное книгу, отсутствующую в коллекции.              |
| 14  | `test_add_book_in_favorites_no_duplicates`                 | Проверяет, что одна и та же книга не добавляется в избранное дважды.                      |
| 15  | `test_delete_book_from_favorites_success`                  | Проверяет успешное удаление книги из избранного.                                          |
| 16  | `test_delete_book_from_favorites_nonexistent_book`         | Проверяет, что удаление несуществующей книги из избранного не вызывает ошибок.            |
| 17  | `test_get_list_of_favorites_books_returns_correct_list`    | Проверяет, что возвращается корректный список избранных книг.                             |


В файле conftest.py определена фикстура collector, которая возвращает новый экземпляр класса BooksCollector.