#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from pykeyboard import PyKeyboard
import time
import sys
import platform

try:
    import config
except ModuleNotFoundError:
    import config_default as config


class Keyboard:
    def gen_keymap(self):
        self.special_key_map = {
            '\n': self.keyboard.enter_key,
            '\t': self.keyboard.tab_key
        }

        # It's a bug in PyUserInput
        if platform.system() == "Linux":
            self.special_key_map['<'] = self.keyboard.lookup_character_keycode('<')

    def init(self):
        self.keyboard = PyKeyboard()
        self.gen_keymap()

    @staticmethod
    def read_file() -> str:
        try:
            with open("input.txt", "r") as file:
                data = file.read()
        except FileNotFoundError:
            with open("input-example.txt", "r") as file:
                data = file.read()
        return data

    def run(self):
        self.init()
        data = self.read_file()
        print(f"Keyboard Emulation will run after {config.EXECUTION_DELAY}s")
        time.sleep(config.EXECUTION_DELAY)
        print("Running...")
        for item in data:
            key = self.special_key_map[item] if item in self.special_key_map else item
            try:
                self.keyboard.press_key(key)
                time.sleep(config.PRESS_DURATION / 1000)
                self.keyboard.release_key(key)
                if config.DEBUG:
                    print(f"Succeed input {item.encode()}")
            except Exception as ex:
                if config.DEBUG:
                    print(ex, file=sys.stderr)
                print(f"Ignore invalid symbol {item.encode()}")
            time.sleep(config.KEYS_INTERVAL / 1000)
        print("End!")


if __name__ == "__main__":
    Keyboard().run()
