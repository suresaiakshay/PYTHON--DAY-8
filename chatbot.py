print("Hello! I'm SimpleBot. How can I help you today?")
print("You can ask me about the weather, time, or just say hello. Type 'bye' to end the chat.")

while True:
    # Get user input and convert to lowercase for easier matching
    user_input = input("You: ").lower()
    
    if user_input == 'bye' or user_input == 'goodbye':
        print("SimpleBot: Goodbye! Have a great day!")
        break
        
    elif 'hello' in user_input or 'hi' in user_input:
        print("SimpleBot: Hello there! How are you?")
        
    elif 'how are you' in user_input:
        print("SimpleBot: I'm just a simple bot, but I'm functioning well! Thanks for asking.")
        
    elif 'weather' in user_input:
        print("SimpleBot: I'm not connected to weather services, but I hope it's nice where you are!")
        
    elif 'time' in user_input:
        # For a more advanced version, you could import datetime module
        print("SimpleBot: I don't have access to the current time, but you can check your device's clock!")
        
    elif 'name' in user_input:
        print("SimpleBot: My name is SimpleBot. Nice to meet you!")
        
    elif 'help' in user_input:
        print("SimpleBot: I can respond to greetings, questions about weather, time, or my name. Try saying hello!")
        
    else:
        print("SimpleBot: I'm not sure I understand. Could you try asking something else?")