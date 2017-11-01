def verify_that_browse_screen_is_opened(app):
    app.browse_screen.wait_page_to_load()
    assert app.browse_screen.get_title_text == "Browse Phrends"