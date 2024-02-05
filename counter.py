import os
import time

def count_images_live(folder_path):
    try:
        while True:
            # Initialize a counter for the number of images
            image_count = 0

            # Loop through all files in the input folder
            for filename in os.listdir(folder_path):
                filepath = os.path.join(folder_path, filename)

                # Check if the file is an image
                if os.path.isfile(filepath) and any(filename.lower().endswith(ext) for ext in (".png", ".jpg", ".jpeg", ".gif")):
                    image_count += 1

            # Clear the console
            os.system('cls' if os.name == 'nt' else 'clear')

            # Print the live count
            print(f"Live image count: {image_count}")

            # Wait for a short duration before updating again
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nCounting stopped.")

if __name__ == "__main__":
    # Specify the input folder (Catgirls)
    input_folder = "Catgirls"

    # Call the count_images_live function
    count_images_live(input_folder)
