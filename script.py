
### **🐍 script.py**
```python
skills = int(input("How many core programming skills do you have? (0-10): "))
projects = int(input("How many completed projects do you have? (0-10): "))
internships = int(input("How many internships have you done? (0-5): "))

readiness_score = (skills * 3 + projects * 2 + internships * 5)

if readiness_score >= 40:
    level = "Expert 🔥"
elif readiness_score >= 25:
    level = "Intermediate ⚡"
else:
    level = "Beginner 🌱"

print(f"\n📌 Your Readiness Level: {level}")
