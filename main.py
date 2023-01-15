import pyautogui
import pyperclip
from time import sleep
import random

add_tweet_pos = (420, 671)
send_tweet_pos = (1220, 896)


# print(pyautogui.position())
# exit()


def send_tweet(tweet):
    # show tweet box
    pyautogui.moveTo(add_tweet_pos[0], add_tweet_pos[1], duration=0.2)
    pyautogui.click()
    sleep(1)
    # write tweet
    pyperclip.copy(f"{tweet} {random.randint(0, 9999)}")
    pyautogui.hotkey('ctrl', 'v')
    sleep(3)

    # send tweet
    pyautogui.moveTo(send_tweet_pos[0], send_tweet_pos[1], duration=0.2)
    pyautogui.click()


if __name__ == "__main__":
    sleep(3)
    while True:
        for i in range(20):
            send_tweet(open('/tmp/tweet.txt', 'r', encoding='utf-8').read())
            sleep(4 + random.randint(0, 4))
        sleep(60 * 5)
