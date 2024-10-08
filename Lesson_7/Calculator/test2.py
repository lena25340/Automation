from Lesson_7.Calculator.Calculator import CalcMain

def test_calculator_assert(driver):
    calcmain = CalcMain(driver)
    calcmain.insert_time()
    calcmain.clicking_buttons()
    assert "15" in calcmain.wait_button_gettext()