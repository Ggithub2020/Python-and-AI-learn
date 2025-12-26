#below is the best chatbot exapmle for list data type practice
# Example 1: Simple FAQ Chatbot
# Chatbot knowledge stored in a LIST
# faqs = [
#     ["hours", "We are open 9 AM to 6 PM"],
#     ["location", "We are located downtown"],
#     ["delivery", "Yes, we deliver in the city"]
# ]

# # List to store conversation history
# history = []

# print("Chatbot Ready! Type 'exit' to stop.")

# while True:
#     user = input("You: ").lower()
#     if user == "exit":
#         break

#     history.append(user)   # store conversation

#     found = False
#     for item in faqs:
#         if item[0] in user:     # keyword found
#             print("Bot:", item[1])
#             found = True
#             break

#     if not found:
#         print("Bot: Sorry, I don't know that yet.")
# Example Shopping Cart Chatbot (List + Input, Real Life)
# cart = []

# print("Welcome to Smart Shopping Assistant")
# print("1 = Add Item  |  2 = View Cart  |  3 = Update Item  |  4 = Remove Item  |  5 = Exit")

# while True:
#     choice = input("Choose option: ")

#     if choice == "1":
#         item = input("Enter item to add: ")
#         cart.append(item)
#         print("Item added!")
#         print("Current Cart:", cart)

#     elif choice == "2":
#         print("Your Shopping Cart:")
#         for c in cart:
#             print("-", c)

#     elif choice == "3":
#         print("Cart:", cart)
#         index = int(input("Which item number to update? (0,1,2...): "))
#         new_item = input("Enter new item name: ")
#         cart[index] = new_item
#         print("Item Updated!")
#         print("Current Cart:", cart)

#     elif choice == "4":
#         print("Cart:", cart)
#         item = input("Enter exact item to remove: ")
#         if item in cart:
#             cart.remove(item)
#             print("Item removed!")
#         else:
#             print("Item not found.")
#         print("Current Cart:", cart)

#     elif choice == "5":
#         print("Thank you for shopping! Goodbye!")
#         break

#     else:
#         print("Invalid choice, try again.")
# 🤖 Simple Agentic Chatbot (Beginner Friendly)
# memory = []   # chatbot memory list
# tasks = []    # task list

# print("Agentic Chatbot Started!")
# print("Type: ask, remember, task, show, exit")

# while True:
#     user = input("\nYou: ").lower()

#     # EXIT
#     if user == "exit":
#         print("Agent: Goodbye!")
#         break

#     # CHAT ANSWER MODE
#     elif user == "ask":
#         question = input("Ask something: ").lower()
#         memory.append(question)

#         if "name" in question:
#             print("Agent: I am your Agentic Chatbot.")

#         elif "time" in question:
#             print("Agent: I cannot tell real time, but I know it's now 😊")

#         else:
#             print("Agent: I do not know yet, but I remembered it.")

#     # REMEMBER SOMETHING (Agent stores info)
#     elif user == "remember":
#         info = input("What should I remember? ")
#         memory.append(info)
#         print("Agent: I stored that in my memory!")

#     # HANDLE TASKS
#     elif user == "task":
#         t = input("Enter a task: ")
#         tasks.append(t)
#         print("Agent: Task added!")

#     # SHOW MEMORY + TASKS
#     elif user == "show":
#         print("\n--- Agent Memory ---")
#         print(memory)

#         print("\n--- Tasks ---")
#         print(tasks)

#     else:
#         print("Agent: I don't understand, choose ask / remember / task / show / exit")
