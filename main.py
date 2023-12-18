import os
import cv2
import numpy as np
import pyautogui
import time
import matplotlib.pyplot as plt

strategy_chart = {5: {2: "H", 3: "H", 4: "H", 5: "H", 6: "H", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  7: {2: "H", 3: "H", 4: "H", 5: "H", 6: "H", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  8: {2: "H", 3: "H", 4: "H", 5: "H", 6: "H", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  9: {2: "H", 3: "D", 4: "D", 5: "D", 6: "D", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  10: {2: "D", 3: "D", 4: "D", 5: "D", 6: "D", 7: "D", 8: "D", 9: "D", 10: "H", 11: "H", },
                  11: {2: "D", 3: "D", 4: "D", 5: "D", 6: "D", 7: "D", 8: "D", 9: "D", 10: "H", 11: "H", },
                  12: {2: "H", 3: "H", 4: "S", 5: "S", 6: "S", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  13: {2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  14: {2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  15: {2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  16: {2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  17: {2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "S", 8: "S", 9: "S", 10: "S", 11: "S", },
                  18: {2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "S", 8: "S", 9: "S", 10: "S", 11: "S", },
                  19: {2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "S", 8: "S", 9: "S", 10: "S", 11: "S", },
                  20: {2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "S", 8: "S", 9: "S", 10: "S", 11: "S", },
                  ("A", 2): {2: "H", 3: "H", 4: "H", 5: "H", 6: "H", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  ("A", 3): {2: "H", 3: "H", 4: "H", 5: "H", 6: "H", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  ("A", 4): {2: "H", 3: "H", 4: "H", 5: "H", 6: "H", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  ("A", 5): {2: "H", 3: "H", 4: "H", 5: "H", 6: "H", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  ("A", 6): {2: "H", 3: "H", 4: "H", 5: "H", 6: "H", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  ("A", 7): {2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "S", 8: "S", 9: "H", 10: "H", 11: "H", },
                  ("A", 8): {2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "S", 8: "S", 9: "S", 10: "S", 11: "S", },
                  ("A", 9): {2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "S", 8: "S", 9: "S", 10: "S", 11: "S", },
                  (2, 2): {2: "P", 3: "P", 4: "P", 5: "P", 6: "P", 7: "P", 8: "H", 9: "H", 10: "H", 11: "H", },
                  (3, 3): {2: "P", 3: "P", 4: "P", 5: "P", 6: "P", 7: "P", 8: "H", 9: "H", 10: "H", 11: "H", },
                  (4, 4): {2: "H", 3: "H", 4: "H", 5: "P", 6: "P", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  (5, 5): {2: "D", 3: "D", 4: "D", 5: "D", 6: "D", 7: "D", 8: "D", 9: "D", 10: "H", 11: "H", },
                  (6, 6): {2: "P", 3: "P", 4: "P", 5: "P", 6: "P", 7: "H", 8: "H", 9: "H", 10: "H", 11: "H", },
                  (7, 7): {2: "P", 3: "P", 4: "P", 5: "P", 6: "P", 7: "P", 8: "H", 9: "H", 10: "H", 11: "H", },
                  (8, 8): {2: "P", 3: "P", 4: "P", 5: "P", 6: "P", 7: "P", 8: "P", 9: "P", 10: "H", 11: "H", },
                  (9, 9): {2: "P", 3: "P", 4: "P", 5: "P", 6: "P", 7: "S", 8: "P", 9: "P", 10: "S", 11: "S", },
                  (10, 10): {2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "S", 8: "S", 9: "S", 10: "S", 11: "S", },
                  ("A", "A"): {2: "P", 3: "P", 4: "P", 5: "P", 6: "P", 7: "P", 8: "P", 9: "P", 10: "P", 11: "H", },
                  }


def take_screenshot():
    time.sleep(2)
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_np = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)
    plt.title("w5s")
    plt.imshow(screenshot_np)
    plt.show()
    return screenshot_np

def find_all_elements(template_path, target_image, filename, roi=None, threshold=0.8, return_all=False):
    template = cv2.cvtColor(cv2.imread(template_path), cv2.COLOR_BGR2GRAY)
    target_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(target_image, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)
    print(template,target_image,result,locations)

    all_element_centers = []

    # Iterate through all possible locations above the threshold
    for loc in zip(*locations[::-1]):
        top_left = loc
        bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
        element_center_x = (top_left[0] + bottom_right[0]) // 2
        element_center_y = (top_left[1] + bottom_right[1]) // 2

        if roi is not None:
            roi_left, roi_top, roi_right, roi_bottom = roi
            if (
                int(element_center_x) in [*range(roi_left, roi_right)]
                and int(element_center_y) in [*range(roi_bottom, roi_top)]
                and (element_center_x, element_center_y) not in all_element_centers
            ):
                if not any(
                        abs(element_center_x - existing_x) < template.shape[1] // 2
                        and abs(element_center_y - existing_y) < template.shape[0] // 2
                        for existing_x, existing_y in all_element_centers
                ):
                    all_element_centers.append((element_center_x, element_center_y))
        else:
            # Check if the element is too close to any already found element
            if not any(
                abs(element_center_x - existing_x) < template.shape[1] // 2
                and abs(element_center_y - existing_y) < template.shape[0] // 2
                for existing_x, existing_y in all_element_centers
            ):
                all_element_centers.append((element_center_x, element_center_y))

    #if all_element_centers:
        #show_image_with_elements(target_image, all_element_centers, filename)
    if return_all:
        return all_element_centers
    else:
        if all_element_centers:
            return all_element_centers[0]
        else:
            return None, None


def show_image_with_elements(image, element_centers, filename):
    plt.title(filename)
    plt.imshow(image)

    for element_center in element_centers:
        plt.scatter(element_center[0], element_center[1], c='g', marker='x')

    plt.show()


def check_win():
    global loose_streak, target_image
    time.sleep(2)
    target_image = take_screenshot()

    won = './gewonnen.png'
    element_center_x, element_center_y = find_all_elements(won, target_image, "gewonnen", threshold=0.95)
    if element_center_x is not None:
        loose_streak = 0
        time.sleep(1)
        adjust_stack()
        return True
    else:
        return False

def check_lost():
    global loose_streak, target_image
    time.sleep(4)
    target_image = take_screenshot()

    won = './gewonnen.png'
    element_center_x, element_center_y = find_all_elements(won, target_image, "gewonnen", threshold=0.95)
    if element_center_x is not None:
        loose_streak = 0
        time.sleep(1)
        adjust_stack()
        return True
    else:
        hold = './halten.png'
        target_image = take_screenshot()
        element_center_x, element_center_y = find_all_elements(hold, target_image, "halten", threshold=0.95)
        if element_center_x is not None:
            return False
        else:
            loose_streak += 1
            time.sleep(1)
            adjust_stack()
            return False


def adjust_stack():
    global loose_streak, current_stake, stake_screenshot, target_image
    print(loose_streak)
    if 0 < loose_streak < 3:
        time.sleep(1.5)
        current_stake = (loose_streak + 1)*start_stake
        incremental = current_stake

        for i in stacks:
            print(incremental, i)
            while incremental >= i:
                incremental -= i
                incremental = int(incremental)

                pyautogui.click(plus_center_x, 100)
                time.sleep(5)
                print(i)

                stack = f'./stacks_img/{i}.png'
                print(2)

                element_center_x, element_center_y = find_all_elements(stack, stake_screenshot, "stack", threshold=0.92)
                print(element_center_x, element_center_y)

                pyautogui.click(plus_center_x, plus_center_y)
                print(4)
                time.sleep(1)

                pyautogui.click(element_center_x, element_center_y)
                time.sleep(0.2)

                pyautogui.click(place_stack_center_x, place_stack_center_y)
                break

    elif loose_streak == 3 or loose_streak == 0:
        time.sleep(1)
        incremental = start_stake
        current_stake = start_stake
        #remove_stack()
        while incremental > 0:
            print(incremental)
            for i in stacks:
                if incremental >= i:
                    incremental -= i
                    incremental = int(incremental)
                    pyautogui.click(plus_center_x, 100)
                    time.sleep(1)
                    pyautogui.click(plus_center_x, plus_center_y)
                    time.sleep(1)
                    stack = f'./stacks_img/{i}.png'
                    element_center_x, element_center_y = find_all_elements(stack, stake_screenshot, "stack2", threshold=0.95)
                    pyautogui.click(element_center_x, element_center_y)
                    time.sleep(0.2)
                    pyautogui.click(place_stack_center_x, place_stack_center_y)
                    break
        loose_streak = 0

def remove_stack():
    reset_stack = './reset_stack.png'
    target_image = take_screenshot()
    element_center_x, element_center_y = find_all_elements(reset_stack, target_image, "reset_stack", threshold=0.95)
    if element_center_x is not None:
        pyautogui.click(element_center_x, element_center_y)
        time.sleep(0.2)


def find_cards(roi=None, split=False):
    global player_cards, dealer_cards
    dir_num_name = "/Users/mac/Desktop/BlackJackBot/card_numbers"
    player_cards = []
    if not split:
        dealer_cards = []

    for filename in os.listdir(dir_num_name):
        center_elements = find_all_elements(os.path.join(dir_num_name, filename), target_image,
                                            filename, threshold=0.9, roi=roi, return_all=True)
        for element_center_x, element_center_y in center_elements:
            if element_center_x is not None and element_center_y is not None:

                if filename.split(".")[0] in ["Q", "J", "K"]:
                    player_cards.append(10)
                elif filename.split(".")[0] == "A":
                    player_cards.append("A")
                else:
                    player_cards.append(int(filename.split(".")[0]))
        if not split:
            element_center_x, element_center_y = find_all_elements(os.path.join(dir_num_name, filename), target_image,
                                                                   filename, threshold=0.9, roi=giver_cards_roi)
            if element_center_x is not None and element_center_y is not None:

                if filename.split(".")[0] in ["Q", "J", "K"]:
                    dealer_cards.append(10)
                elif filename.split(".")[0] == "A":
                    dealer_cards.append(11)
                else:
                    dealer_cards.append(int(filename.split(".")[0]))
    if not split:
        return player_cards, dealer_cards
    else:
        return player_cards


def which_action(player_cards, dealer_cards):
    try:
        if "A" in player_cards and len(player_cards) == 2:
            action = strategy_chart[("A", player_cards[0] if player_cards[0] != "A" else player_cards[1])][dealer_cards[0]]
        elif "A" in player_cards and len(player_cards) > 2:
            a_count = player_cards.count("A")
            for i, j in enumerate(player_cards):
                if j == "A":
                    player_cards[i] = 11
            print(12,player_cards)
            player_sum = sum(player_cards)
            print(11,player_sum)
            for i in range(a_count+1):
                if player_sum > 20:
                    player_sum -= 10
                    print(2,player_sum)
                else:
                    action = strategy_chart[player_sum][dealer_cards[0]]
        elif len(player_cards) == 2 and player_cards[0] == player_cards[1]:
            action = strategy_chart[(player_cards[0], player_cards[1])][dealer_cards[0]]
        else:
            action = strategy_chart[sum(player_cards)][sum(dealer_cards)]
    except:
        action = None
    return action


def do_the_action(action):
    global cards_given
    if action == "H":
        take = './ziehen.png'
        target_image = take_screenshot()
        element_center_x, element_center_y = find_all_elements(take, target_image, "ziehen", threshold=0.95)
        pyautogui.click(element_center_x, element_center_y)
        cards_given += 1
        check_lost()

    elif action == "S":
        hold = './halten.png'
        target_image = take_screenshot()
        element_center_x, element_center_y = find_all_elements(hold, target_image, "halten", threshold=0.95)
        pyautogui.click(element_center_x, element_center_y)
        check_lost()

    elif action == "D":
        double = './double.png'
        target_image = take_screenshot()
        element_center_x, element_center_y = find_all_elements(double, target_image, "double", threshold=0.95)
        if element_center_x is not None:
            pyautogui.click(element_center_x, element_center_y)
            cards_given += 1
        else:
            hold = './halten.png'
            element_center_x, element_center_y = find_all_elements(hold, target_image, "halten", threshold=0.95)
            pyautogui.click(element_center_x, element_center_y)
        check_lost()

    elif action == "P":
        split = './split.png'
        target_image = take_screenshot()
        element_center_x, element_center_y = find_all_elements(split, target_image, "split", threshold=0.95)
        if element_center_x is not None:
            pyautogui.click(element_center_x, element_center_y)
            right_roi = (player_element_center_x, player_element_center_y, player_element_center_x + 1000,
                         player_element_center_y - 200)
            left_roi = (player_element_center_x - 1000, player_element_center_y, player_element_center_x,
                        player_element_center_y - 200)
            while True:
                right_player_cards = find_cards(right_roi, True)
                print(right_player_cards)
                action = which_action(right_player_cards, dealer_cards)
                if action == "S" or action is None:
                    break
                do_the_action(action)

            while True:
                left_player_cards = find_cards(left_roi, True)
                print(left_player_cards)
                action = which_action(left_player_cards, dealer_cards)
                print(action)
                if action == "S" or action is None:
                    break
                do_the_action(action)

        else:
            hold = './halten.png'
            element_center_x, element_center_y = find_all_elements(hold, target_image, "halten", threshold=0.95)
            pyautogui.click(element_center_x, element_center_y)
        check_lost()


stacks = [20, 10, 4, 2, 1]
loose_streak = 2
start_stake = 10
current_stake = start_stake

cards_given = 0
time.sleep(1)
geber_karten = './geber_karten.png'
target_image = take_screenshot()
element_center_x, element_center_y = find_all_elements(geber_karten, target_image, "geber_karten", threshold=0.25)
print(element_center_x,element_center_y)
giver_cards_roi = (element_center_x - 1000, element_center_y + 200, element_center_x + 1000, element_center_y)
print(giver_cards_roi)
mitte = './mitte.png'
player_element_center_x, player_element_center_y = find_all_elements(mitte, target_image, "mitte", threshold=0.35)
player_cards_roi = (
player_element_center_x - 1000, player_element_center_y, player_element_center_x, player_element_center_y - 200)
print(player_element_center_x, player_element_center_y)
place_stack = './place_stack.png'
place_stack_center_x, place_stack_center_y = find_all_elements(place_stack, target_image, "place_stack", threshold=0.75)

plus = './plus.png'
target_image = take_screenshot()
plus_center_x, plus_center_y = find_all_elements(plus, target_image, "plus", threshold=0.95)
pyautogui.moveTo(plus_center_x, 100)
pyautogui.click(plus_center_x, plus_center_y)
time.sleep(0.5)
stake_screenshot = take_screenshot()
pyautogui.click(plus_center_x, 100)
time.sleep(1)
split = False

adjust_stack()
while True:
    try:
        # Example usage
        deal = './deal.png'
        target_image = take_screenshot()
        element_center_x, element_center_y = find_all_elements(deal, target_image, "deal", threshold=0.95)
        if element_center_x is not None:
            pyautogui.click(element_center_x, element_center_y)
            element_center_x, element_center_y = 0, 0
            cards_given = 2
    except:
        pass

    try:
        time.sleep(1)
        gewonnen = check_win()
        if not gewonnen:
            player_cards, dealer_cards = find_cards(player_cards_roi)
            action = which_action(player_cards, dealer_cards)
            do_the_action(action)

    except Exception as e:
        pass