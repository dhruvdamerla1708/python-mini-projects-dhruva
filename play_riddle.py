# play_riddle.py

import random
from riddles import riddles

print("\n🧩 Welcome to Riddle Master! 🧩")
print("-------------------------------")

# Pick a random riddle
selected = random.choice(riddles)
print(f"🧠 Here's your riddle:\n➡️ {selected['question']}")

# Get user input
user_answer = input("\nYour answer: ").strip().lower()
correct_answer = selected['answer'].lower()

# Check answer
if user_answer == correct_answer:
    print("\n✅ Correct! You're a true Riddle Master!")
else:
    print("\n❌ Oops! That's not it.")
    print(f"💡 The correct answer was: {selected['answer']}")
