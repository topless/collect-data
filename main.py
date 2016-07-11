#!/usr/bin/env python
# coding: utf-8

import os
import sys
import json
import shutil


DEST_DIR = 'BenchData'
FNAME = 'meta.json'


def main():
  data = read_input()
  save_input(data)
  move_data(os.path.join(DEST_DIR, data['name']))


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
  print("Info saved in {}".format(FNAME))


def move_data(dest):
  count = 1
  for entry in sorted(os.listdir(os.getcwd())):
    if not entry.startswith('2016'):
      continue
    shutil.copy2(FNAME, entry)
    final_dest = os.path.join(dest, str(count), entry)
    print("Moving to {}".format(final_dest))
    shutil.move(entry, final_dest)
    count += 1


if __name__ == '__main__':
  main()
  sys.exit()
