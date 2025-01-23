import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_schema": content.Schema(
    type = content.Type.OBJECT,
    properties = {
      "regex": content.Schema(
        type = content.Type.STRING,
      ),
      "valid_matches": content.Schema(
        type = content.Type.ARRAY,
        items = content.Schema(
          type = content.Type.STRING,
        ),
      ),
      "invalid_matches": content.Schema(
        type = content.Type.ARRAY,
        items = content.Schema(
          type = content.Type.STRING,
        ),
      ),
    },
  ),
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "You are an expert regex string creator and understand how regex works. Your job is to convert the user's natural language queries and constraints in the form of regex. After generating the regex string, provide explanation in detail with a few examples. Then demonstrate its use in a python code.\n\nUser query:\nGive me the regex equivalent of the following:\nMy requirements are:\n1. I want my string to have 2-63 characters.\n2. The string should be alphanumeric and can contain - also.\n3. The string must start as well as end with alphanumeric characters only.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"invalid_matches\": [\"-abc\", \"abc-\", \"123-\", \"-123\", \"a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-1-2-3-4-5-6-7-8-9-0-\", \"ab-cd-efgh-ijklmnopqrstuvwxyz1234567890\", \"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789\"], \"regex\": \"^[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$\", \"valid_matches\": [\"abc\", \"abc-def\", \"a123-b456-c789\", \"a-b\", \"abc123def456ghi789\", \"abc-def-ghi\", \"1abc1\", \"123\", \"aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890\"]}\n```",
      ],
    },
  ]
)
