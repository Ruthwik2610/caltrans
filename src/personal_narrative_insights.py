import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def personal_narrative_insights(user_input):
    """
    Uses OpenAI Assistant API to generate personal narrative insights.
    
    Args:
        user_input: The user's input/question
        knowledge_base: Optional knowledge base file (currently not used but kept for compatibility)
    
    Returns:
        str: The assistant's response
    """
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Assistant ID
    assistant_id = os.getenv("CALTRANS_PERSONAL_NARRATIVE_INSIGHTS_ASSISTANT_ID")
    
    try:
        # Create a thread
        thread = client.beta.threads.create()
        
        # Add user message to the thread
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_input
        )
        
        # Run the assistant
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id
        )
        
        # Poll for completion
        while run.status in ["queued", "in_progress", "cancelling"]:
            time.sleep(0.5)
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
        
        # Check if run completed successfully
        if run.status == "completed":
            # Retrieve messages from the thread
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            
            # Get the assistant's response (first message in the list is the latest)
            for message in messages.data:
                if message.role == "assistant":
                    # Extract text content from the message
                    if message.content:
                        if isinstance(message.content, list):
                            # Handle list of content blocks
                            text_parts = []
                            for content_block in message.content:
                                if hasattr(content_block, 'text') and hasattr(content_block.text, 'value'):
                                    text_parts.append(content_block.text.value)
                            return "\n".join(text_parts) if text_parts else "No response generated."
                        elif hasattr(message.content, 'text') and hasattr(message.content.text, 'value'):
                            return message.content.text.value
                    return "No response content found."
            
            return "No assistant response found in thread."
        else:
            # Handle error states
            error_msg = f"Run failed with status: {run.status}"
            if hasattr(run, 'last_error') and run.last_error:
                error_msg += f" - {run.last_error.message}"
            return error_msg
            
    except Exception as e:
        return f"Error calling assistant: {str(e)}"