import openai
import os
from dotenv import load_dotenv


load_dotenv()

# Retrieve API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def analyze_review_tone_sentiment(text: str, stars: int):
    """
    Analyze the tone and sentiment of a review using OpenAI's GPT model.

    Args:
        text (str): The review text.
        stars (int): Star rating (out of 10).

    Returns:
        tuple: (tone, sentiment)
    """
    prompt = (
        f"Analyze the following review:\n\n"
        f"Review Text: \"{text}\"\n"
        f"Star Rating: {stars}/10\n\n"
        f"Provide:\n"
        f"- Tone (e.g., Positive, Neutral, Negative)\n"
        f"- Sentiment (e.g., Happy, Angry, Frustrated, Excited)\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )

        # Extract response content safely
        result = response.choices[0].message.content.strip().split("\n")

        tone = result[0].split(":")[-1].strip() if len(result) > 0 else "Unknown"
        sentiment = result[1].split(":")[-1].strip() if len(result) > 1 else "Unknown"

        return tone, sentiment

    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return "Error", "Error"
