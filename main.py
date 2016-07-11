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
    'name': raw_input("What's your name? ").title(),
    'gender': raw_input("What's your gender? ").lower(),
    'color': raw_input("What's your eye color? ").lower(),
    'origin': raw_input("Where are you from? ").title()
  }
  return data


def save_input(info):
  with open(FNAME, 'w') as output:
    json.dump(info, output)
  print("{} saved in {}".format(info, FNAME))


def move_data():
  for entry in os.listdir('.'):
    if not os.path.isdir(entry) or entry == DEST_DIR:
      continue
    shutil.copy2(FNAME, entry)
    shutil.move(entry, DEST_DIR)


if __name__ == '__main__':
  main()
