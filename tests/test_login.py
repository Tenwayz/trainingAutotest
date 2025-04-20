from pages.login_page import LoginPage

def test_login_failue(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('invalid_user', 'invalid_password')
    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'