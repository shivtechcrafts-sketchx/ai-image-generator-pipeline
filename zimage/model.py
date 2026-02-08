import torch
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import StableDiffusionPipeline

class ZImageModel:
    def __init__(self, model_name="runwayml/stable-diffusion-v1-5"):
        print("[*] Loading Stable Diffusion model...")

        self.pipe = StableDiffusionPipeline.from_pretrained(
    model_name
)

        # Smart device selection
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[*] Using device: {self.device}")

        self.pipe.to(self.device)

    def generate(self, prompt, height=512, width=512, steps=30, guidance_scale=7.5):
        print(f"[*] Generating image for: {prompt}")

        output = self.pipe(
            prompt=prompt,
            height=height,
            width=width,
            num_inference_steps=steps,
            guidance_scale=guidance_scale
        )

        return output.images[0]

        print("[*] Model loaded successfully.")