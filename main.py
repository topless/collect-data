# coding: utf-8

import os
import json
import shutil


DEST_DIR = 'BenchData'
FNAME = 'meta.json'


def main():
  data = read_input()
  save_input(data)
  move_data(data['name'])


def read_input():
  data = {
    'name': raw_input("What's your name? ").title(),
    'gender': raw_input("What's your gender (m/f)? ").lower(),
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


def move_data(user_name):
  for entry in os.listdir(os.getcwd()):
    if not entry.startswith('2016'):
      continue
    shutil.move(entry, user_name)
  shutil.move(user_name, DEST_DIR)


if __name__ == '__main__':
  main()
