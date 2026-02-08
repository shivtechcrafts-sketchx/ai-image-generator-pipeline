from zimage.model import ZImageModel

prompts = [
    "A majestic tiger walking in neon forest",
    "Portrait painting of a wizard with glowing staff"
]

model = ZImageModel()
for i, p in enumerate(prompts):
    out = model.generate(p)
    out.save(f"batch_{i}.png")
    print(f"[+] Saved batch_{i}.png")
