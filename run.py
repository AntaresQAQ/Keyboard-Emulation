from pykeyboard import PyKeyboard
import time
import config


class Keyboard:
    def gen_keymap(self):
        self.special_key_map = {
            '\n': self.keyboard.enter_key,
            '\t': self.keyboard.tab_key,
            '<': self.keyboard.lookup_character_keycode('<')  # It's a bug in PyUserInput
        }

    def run(self):
        self.keyboard = PyKeyboard()
        self.gen_keymap()
        print(f"Keyboard Emulation will run after {config.EXECUTION_DELAY}s")
        time.sleep(config.EXECUTION_DELAY)
        print("Running...")
        with open("input.txt", "r") as file:
            data = file.read()
        for item in data:
            key = self.special_key_map[item] if item in self.special_key_map else item
            try:
                self.keyboard.press_key(key)
                time.sleep(config.PRESS_DURATION / 1000)
                self.keyboard.release_key(key)
            except Exception as ex:
                print(ex)
                print(f"Ignore invalid symbol {item.encode()}")
            time.sleep(config.KEYS_INTERVAL / 1000)
        print("End!")


if __name__ == "__main__":
    program = Keyboard()
    program.run()
