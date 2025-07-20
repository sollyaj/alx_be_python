adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
adjective4 = input("Enter a final adjective: ")
animal = input("Enter an animal: ")
activity = input("Enter something you do (verb): ")

story = (
    f"On a beautiful {adjective1} day, I went to the zoo. "
    f"I saw a funny {adjective2} monkey swinging from the trees. "
    f"Then, I spotted a majestic {adjective3} {animal} lounging in the sun. "
    f"What a wild and {adjective4} experience! "
)
if activity.lower() == "dance":
    story += "Then suddenly, everyone at the zoo started dancing! 🕺"
elif activity.lower() == "run":
    story += "Then suddenly, all the animals started running in circles! 🐾"
else:
    story += f"Then suddenly, a zookeeper asked me to {activity} with them! 🧑‍🌾"
print("\nHere’s your Mad Libs story:")
print(story)
