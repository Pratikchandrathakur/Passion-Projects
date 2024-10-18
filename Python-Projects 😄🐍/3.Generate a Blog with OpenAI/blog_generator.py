import openai
import os

# Set up your OpenAI API key securely from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog(prompt, max_tokens=500):
    """
    Generate a blog based on the provided prompt using OpenAI API.
    
    :param prompt: The prompt for the blog generation
    :param max_tokens: Maximum number of tokens for the blog (default: 500)
    :return: Generated blog content
    """
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Or use GPT-4 if available: "gpt-4"
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.7,  # Adjust creativity level
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0.3
        )
        blog_content = response.choices[0].text.strip()
        return blog_content
    except Exception as e:
        return f"Error: {str(e)}"

# Example prompt for generating a blog
blog_prompt = "Write a blog post on the benefits of using AI in digital marketing."

# Generate the blog content
generated_blog = generate_blog(blog_prompt)

# Print the generated blog
print("Generated Blog Content:")
print(generated_blog)
