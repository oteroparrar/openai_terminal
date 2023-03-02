import openai
import colorama

# Define OpenAI API key 


while True:
    openai.api_key = "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"
    question = input(colorama.Fore.RED + "\n ***You:***\n\n")
    
    if question == "exit":
        break
    else:
        # Set up the model and prompt
        model_engine = "text-davinci-003"
        prompt = question
        # Generate a response
        completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        )
    
        response = completion.choices[0].text
        print(colorama.Fore.YELLOW + "\n ***ChatGPT*** \n" + response +"\n")

    
