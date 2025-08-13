# BOSS CHALLENGE: The "Smart Assistant System"
# Build a multi-purpose smart assistant called smart_assistant() that:
# Takes the user name (first positional argument).
# Takes any number of commands (*args), like "weather", "reminder", or "music".
# Accepts preferences (**kwargs), like volume=5, language="en", etc.
# Returns a summary of:
# Commands given
# Preferences set
# A personalized function that can later be called to greet the user

print("Boss challenge: the 'smart assistant system'")


def smart_assistant(name, *commands, **preferences):
    command_str = ", ".join(commands)

    #preference string
    pref_lines= []
    for k, v in preferences.items():
        pref_lines.append(f"{k}: {v}")
    pref_str= "\n".join(pref_lines)

    #greeting
    def greet_user():
        joined_command = "and ".join(commands)
        return f"Greeting: Hello {name}! Ready to help you with your {joined_command}."
    
    # final summary
    summary = f"{name}'s Assistant summary:\nCommands: {command_str}\nPreferences:\n{pref_str}"

    #retrun dictionary
    return{
        "summary" : summary,
        "greet_user": greet_user
    }

assistant = smart_assistant("Dibash", "weather", "music", language="English", volume=5)
print(assistant["summary"])
print(assistant["greet_user"]())

