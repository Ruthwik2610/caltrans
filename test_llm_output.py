import os
from dotenv import load_dotenv
load_dotenv()
from src.cucp_reevals import evaluations_model

test_text = "I am the owner of ABC Corp. My personal net worth is $1,000,000. I have experienced significant social and economic disadvantage."
try:
    res = evaluations_model(test_text)
    with open("llm_raw_test.md", "w") as f:
        f.write(res)
    print("Finished writing to llm_raw_test.md")
except Exception as e:
    print(f"Error: {e}")
