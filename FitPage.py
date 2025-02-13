import os
import shutil

def main():
    # Step 1: Request the folder path and desired pages.
    folder_path = input("Enter the folder path: ").strip()
    try:
        desired_pages = int(input("Enter the number of desired pages: "))
    except ValueError:
        print("Invalid number of pages. Exiting.")
        return

    target_count = desired_pages * 9

    # List and sort JPEG files.
    images = [f for f in os.listdir(folder_path)
              if f.lower().endswith(('.jpg', '.jpeg'))]
    images.sort()
    total_images = len(images)
    
    if total_images < target_count:
        print("Not enough images to fill the desired number of pages.")
        return

    # Step 3: Compute indices for exactly target_count images,
    # evenly spread over the available images.
    selected_indices = [int(i * total_images / target_count) for i in range(target_count)]
    # Just in case, ensure indices don't exceed the list boundaries.
    selected_indices = [min(idx, total_images - 1) for idx in selected_indices]

    # Step 5: Create a new folder to copy the selected images.
    output_folder = os.path.join(folder_path, f"selected_{desired_pages}_pages")
    os.makedirs(output_folder, exist_ok=True)

    for count, idx in enumerate(selected_indices, start=1):
        src = os.path.join(folder_path, images[idx])
        dst = os.path.join(output_folder, f"image_{count:03d}.jpeg")
        shutil.copy(src, dst)

    print(f"Copied {len(selected_indices)} images to {output_folder}")

if __name__ == "__main__":
    main()
