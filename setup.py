#!/usr/bin/env python
  
import os
import argparse
import subprocess

from os import listdir
from os.path import join


def get_directory_list(dirname):
   file_list = [join(dirname,f) for f in listdir(dirname) if f != ".." and f != "."]
   return file_list

def copy_dir(src,dst):
   sub_args = ['cp','-a']
   dir_list = get_directory_list(src)
   sub_args.extend(dir_list)
   sub_args.append(dst)
   process = subprocess.Popen(sub_args)
   process.communicate()

def main(args):
   kaniko_dir = None
   var_dir = None
   volumes = None
   volume_list = []

   if os.environ.get('KANIKO_DIR') != None: kaniko_dir = os.environ.get('KANIKO_DIR')
   if os.environ.get('VAR_DIR') != None: var_dir = os.environ.get('VAR_DIR')
   if os.environ.get('VOLUMES') != None: volumes = os.environ.get('VOLUMES')
   if args.kaniko_dir != None: kaniko_dir = args.kaniko_dir
   if args.var_dir != None: var_dir = args.var_dir
   if args.volumes != None: volumes = args.volumes
   if volumes != None: volume_list = volumes.split(':')
   if len(volume_list) > 0:
      sub_args = ['chmod','777']
      sub_args.extend(volume_list)
      process = subprocess.Popen(sub_args)
      process.communicate()
   if kaniko_dir != None: copy_dir('/kaniko-src',kaniko_dir)
   if var_dir != None: copy_dir('/var-src',var_dir)

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument("--volumes",help="colon separated list of volumes")
   parser.add_argument("--kaniko_dir",help="destination kaniko dir")
   parser.add_argument("--var_dir",help="destination var dir")

   args = parser.parse_args()
   main(args)


