from seleniumbase import Driver, SB
with SB(uc=True,
        xvfb=True,
        browser="Chrome") as sb:
    print('getting base_url')
    sb.open(BASE_URL)

    time.sleep(2)

    sb.uc_gui_click_captcha()

    time.sleep(2)

    print('past')
    print('another test')
    print('yet another test')
    if 'Pinned Pastes' in sb.driver.page_source:
        print('test passed')
    sb.driver.save_screenshot('doxbin.png')

    


print('done')
