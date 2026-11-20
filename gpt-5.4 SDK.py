from openai import OpenAI
    
endpoint ="https://project292912345-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5.4-mini"
api_key = "3M3CF4vlGYJGlFs7p84RT3Ii8JdQNyaMNWMkZWYVUeWv4d16KyOdJQQJ99CKACF24PCXJ3w3AAAAACOGg2rf"
    
client = OpenAI(
     base_url=endpoint,
     api_key=api_key
 )
    
response = client.responses.create(
     model=deployment_name,
     input=[{
         "role": "user",
         "content": [
             {"type": "input_text", "text": "what's in this image?"},
             {"type": "input_image", "image_url": ""},
         ],
     }],
 )
    
print(f"answer: {response.output_text}")