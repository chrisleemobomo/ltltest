from proj.terrain import *
from proj.preconditions import PreconditionSteps
import time


def clear_screenshots():
    dir_name = "videos"
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".png") and not item.startswith("screenshot"):
            os.remove(os.path.join(dir_name, item))


@steps
class DesignSteps(PreconditionSteps):

    @step(u'I scroll down to the bottom of "([^"]*)"')
    def scroll_to_bottom(step, url):
        clear_screenshots()
        time.sleep(1)
        step = 10
        images = []
        height = world.driver.execute_script(
            "return document.body.scrollHeight") / 2
        for i in range(0, height, step):
            world.driver.execute_script("window.scrollTo(0,{})".format(i))
            padded_i = str(i).zfill(len(str(height)))
            world.driver.save_screenshot(
                "videos/{}{}.png".format(url, padded_i))
        else:
            world.driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight)")
            padded_i = str(i+step).zfill(len(str(height)))
            world.driver.save_screenshot(
                "videos/{}{}.png".format(url, padded_i))

        # create video from screenshots
        os.system('ffmpeg -r 10 -pattern_type glob -i "videos/*.png" -vcodec libx264 -y -an videos/{}-{}x{}.mp4 -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2"^C'.format(
            url, world.browser_width, world.browser_height))
        clear_screenshots()

    @step(u'I take a screenshot')
    def take_screenshot(step):
        url = world.driver.current_url.split("/")[-1]
        world.driver.save_screenshot("screenshots/{}-{}x{}.png".format(
            url, world.browser_width, world.browser_height))

    @step(u'I go to the top of the page')
    def take_screenshot(step):
        world.driver.execute_script("window.scrollTo(0,0)")

    @step(u'I go to the bottom of the page')
    def take_screenshot(step):
        height = world.driver.execute_script(
            "return document.body.scrollHeight")
        world.driver.execute_script("window.scrollTo(0,{})".format(height))
