import os, sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

SRC_DIR = r'C:\Users\anurag\Desktop\Building Agentic AI Applications with a Problem-First Approach'
KB_ROOT = r'c:\Users\anurag\Desktop\notes\COURSE_KNOWLEDGE_BASE'

with open('scratch/raw_data_summary.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# Define the 106 logical lesson records
# Each record contains:
# id (1..106)
# title
# category (Core, Build, Grow, Office Hours, AMA, Guest, Capstone, Other)
# type (Lecture, Demo, Workshop, Assignment, Solution, Office Hours, AMA, Guest Lecture, Reference, Code Archive)
# primary_file
# alternate_files
# description
# week (1..4, Capstone, or Orientation)
# module_id (1..10)

print("Building logical mapping for all 152 files...")
