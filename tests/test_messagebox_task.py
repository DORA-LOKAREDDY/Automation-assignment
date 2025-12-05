import pytest
from playwright.sync_api import Page

from pages.login_page import login_page
from pages.dashboard_page import dashboard_page
from pages.taskbot_page import taskbot_page
from utils.config import BASE_URL


@pytest.mark.ui
def test_messagebox_task_creation(page: Page):
    # --- PAGE OBJECT INITIALIZATION ---
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    taskbot = TaskBotPage(page)

    # --- STEP 1: GO TO LOGIN PAGE ---
    page.goto(BASE_URL)
    assert page.url.startswith(BASE_URL), "Failed to load login page"

    # --- STEP 2: PERFORM LOGIN ---
    login.login("lvdora92@gmail.com", "Dora7989@")   # replace before running
    dashboard.wait_for_dashboard()
    assert dashboard.is_loaded(), "Dashboard did not load correctly"

    # --- STEP 3: NAVIGATE TO TASK BOT CREATION ---
    dashboard.navigate_to_automation()
    dashboard.click_create_taskbot()

    # --- STEP 4: ENTER TASK BOT DETAILS ---
    taskbot.fill_task_details("Auto_Message_Task")
    assert taskbot.verify_task_form_filled(), "Task bot form did not fill correctly"

    # --- STEP 5: SELECT MESSAGE BOX ACTION ---
    taskbot.add_message_box_action()
    assert taskbot.verify_message_box_settings_opened(), "Message box panel did not open"

    # --- STEP 6: SAVE TASK ---
    taskbot.save_task()
    assert taskbot.verify_task_saved(), "Task was not saved successfully"

    # Final assertion
    print("✔ Test completed successfully")
