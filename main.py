
import torch
from fastapi import FastAPI, UploadFile, File, HTTPException
from diffusers import DiffusionPipeline, LCMScheduler
from fastapi.responses import FileResponse


app = FastAPI()

pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    variant="fp16",
    torch_dtype=torch.float16
).to("cuda")

# set scheduler
pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)

# load LCM-LoRA
pipe.load_lora_weights("latent-consistency/lcm-lora-sdxl")

@app.post("/generate_image/")
async def generate_image(prompt: str):
    try:
        generator = torch.manual_seed(42)
        image = pipe(
            prompt=prompt, num_inference_steps=4, generator=generator, guidance_scale=1.0
        ).images[0]

        # Save the image to a file
        output_file = "output_image.jpeg"

        image.save(output_file, format="JPEG")

        return FileResponse(output_file, media_type="image/jpeg")


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
