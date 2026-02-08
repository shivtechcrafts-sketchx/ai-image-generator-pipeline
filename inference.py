from zimage.model import ZImageModel
from zimage.utils import create_output_dir, generate_filename
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, required=True)
    args = parser.parse_args()

    model = ZImageModel()
    img = model.generate(args.prompt)

    out_dir = create_output_dir()
    filename = generate_filename("zimage")
    path = f"{out_dir}/{filename}"

    img.save(path)
    print(f"[+] Image saved at: {path}")

if __name__ == "__main__":
    main()
