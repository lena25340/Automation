from Lesson_7.Data_types.data import MainPage
from Lesson_7.Data_types.Datafildes import DataFild


def test_assertion(driver):
    main_page = MainPage(driver)
    main_page.find_fields()
    main_page.filling_in_the_field()
    main_page.click_submit_button()

    data_fild = DataFild(driver)
    assert "success" in data_fild.get_class_first_name()
    assert "success" in data_fild.get_class_last_name()
    assert "success" in data_fild.get_class_address()
    assert "success" in data_fild.get_class_email()
    assert "success" in data_fild.get_class_phone()
    assert "success" in data_fild.get_class_city()
    assert "success" in data_fild.get_class_country()
    assert "success" in data_fild.get_class_company()
    assert "success" in data_fild.get_class_jobposition()
    assert "danger" in data_fild.get_class_zipcode()
        