from openai import OpenAI

def get_topic_representation(keywords):
    client = OpenAI(
        api_key='ollama',  
        # api_version = "2024-02-15-preview",
        base_url='http://localhost:11434/v1/',
    )
    # Create the prompt to generate a concise topic label
    prompt = f"Here is a list of keywords that represent a topic: {', '.join(keywords)}. Can you generate a concise and meaningful topic label for this? Please respond only with the topic label."

    # Generate the topic label using the GPT-4 model
    response = client.chat.completions.create(
            # model = "gpt4-nnfimpact",
            model = "llama3.2",
            temperature = 0.0,
            messages = [
                    {"role": "user", "content": prompt}
            ]
        )
    return response.choices[0].message.content