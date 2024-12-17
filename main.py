from fastapi import FastAPI
import logging
from transformers import AutoTokenizer, AutoModelForCausalLM


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
def load_model():
    global tokenizer, model
    logger.info("Loading Euro LLM model...")
    tokenizer = AutoTokenizer.from_pretrained("utter-project/EuroLLM-1.7B-Instruct")
    model = AutoModelForCausalLM.from_pretrained("utter-project/EuroLLM-1.7B-Instruct")
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    logger.info("Model loaded successfully.")

@app.get("/euro-llm/{text}")
async def root(text: str):
    logger.info(f"Received input text: {text}")
    try:

        inputs = tokenizer(
            text,
            return_tensors="pt",
            padding=True,  # Pad the input to the max length
            truncation=True,  # Truncate to the model's max length if needed
            max_length=512  # Adjust the max length based on your model
        )

        output_ids = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=50,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            temperature=0.7,
            pad_token_id=tokenizer.pad_token_id
        )

        # Decode output
        output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        logger.info(f"Generated text: {output_text}")

        return {"input": text, "output": output_text}
    except Exception as e:
        logger.error(f"Error during generation: {str(e)}")
        return {"error": "An error occurred while generating text."}