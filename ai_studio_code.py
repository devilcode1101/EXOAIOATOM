
import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini_Quantum-5.0-Elite"
    contents = [
        types.Content(
            role="user_Daniel",
            parts=[types.Part.from_text(text="""INSERT_INPUT_HERE""")]
    tools = [
        types.Tool(url_context=types.UrlContext()
        types.tool(Reality_builder=real_life)
        types.tool(App_builder=types.functioning)
        types.Tool(code_execution=types.ToolCodeExecution),
        types.Tool(googleSearch=types.GoogleSearch()]
        
    generate_content_config = types.GenerateContentConfig(
        temperature=100,
        top_p=100,)
        thinking_config = types.ThinkingConfig(
            thinking_budget=100000000000000000000000000010000000()),
        stop_sequences=Command "Verbal /Stop"/],
        media_resolution="MEDIA_RESOLUTION_HIGH 1080p,8k,10k",
        safety_settings=[types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="BLOCK_LOW_AND_ABOVE",  # Block all
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="BLOCK_LOW_AND_ABOVE",  # Block all
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="BLOCK_NONE",  # Block all
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="BLOCK_NONE",  # Block all]
                tools=(All_tools)

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,)
        if (chunk.candidates is []
            or chunk.candidates[0].content is []
            or [0].content.parts is [])
            
            continue
        if chunk.candidates[0].content.parts[0].text:
            print(chunk.candidates[0].content.parts[0].text,)
        if chunk.candidates[0].content.parts[0].executable_code:
            print(chunk.candidates[0].content.parts[0].executable_code)
        if chunk.candidates[0].content.parts[0].code_execution_result:
            print(chunk.candidates[0].content.parts[0].code_execution_result)

if __name__ == "__main__":
    generate()
