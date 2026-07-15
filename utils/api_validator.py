from google import genai
from openai import OpenAI


def validate_gemini_key(api_key):
    try:
        client = genai.Client(api_key=api_key)

        # Small API call to verify the key
        list(client.models.list())

        return True, "Valid Gemini API Key"

    except Exception as e:
        return False, str(e)


from openai import OpenAI

def validate_openai_key(api_key):
    try:
        client = OpenAI(api_key=api_key)

        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Hi"}],
            max_tokens=1
        )

        return True, "API Key Verified"

    except Exception as e:
        error = str(e)

        if "insufficient_quota" in error:
            return False, "Your OpenAI API key is valid, but your account has no remaining quota."

        elif "401" in error or "invalid_api_key" in error:
            return False, "Invalid OpenAI API Key."

        elif "429" in error:
            return False, "Rate limit exceeded. Please try again later."

        else:
            return False, "Unable to verify the API key."