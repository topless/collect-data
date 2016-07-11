# coding: utf-8

import os
import json
import shutil


DEST_DIR = 'BenchData'
FNAME = 'meta.json'


def main():
  data = read_input()
  save_input(data)
  move_data()


def read_input():
  data = {
    'gender': raw_input("What's your gender (m/f)? ").lower(),
    'name': raw_input("What's your name? ").title(),
    'origin': raw_input("Where are you from? ").title(),
    'eye_color': raw_input("What's your eye color? ").lower(),
    'glasses': raw_input("Do you wear glasses (y/n)? ").lower(),
    'lenses': raw_input("Do you wear lenses (y/n)? ").lower()
  }
  return data


def save_input(data):
  with open(FNAME, 'w') as output:
    json.dump(data, output)
  print("{} saved in {}".format(data, FNAME))


def move_data():
  for entry in os.listdir('.'):
    if not os.path.isdir(entry) or entry == DEST_DIR:
      continue
    shutil.copy2(FNAME, entry)
    shutil.move(entry, DEST_DIR)


if __name__ == '__main__':
  main()
