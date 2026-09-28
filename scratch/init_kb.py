import os, sys, re, json, shutil

sys.stdout.reconfigure(encoding='utf-8')

KB_ROOT = r'c:\Users\anurag\Desktop\notes\COURSE_KNOWLEDGE_BASE'
ALT_ROOT = r'c:\Users\anurag\Desktop\notes\Building_Agentic_AI_Applications_with_a_Problem_First_Approach\COURSE_KNOWLEDGE_BASE'

os.makedirs(KB_ROOT, exist_ok=True)
os.makedirs(os.path.join(KB_ROOT, 'Lessons'), exist_ok=True)
os.makedirs(os.path.join(KB_ROOT, 'Lesson_Groups'), exist_ok=True)
os.makedirs(os.path.join(KB_ROOT, 'Assignments'), exist_ok=True)
os.makedirs(os.path.join(KB_ROOT, 'Projects'), exist_ok=True)

print("Base directories created successfully.")
