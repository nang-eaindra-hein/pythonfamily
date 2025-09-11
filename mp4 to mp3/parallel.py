import moviepy.editor as mp
import time
from concurrent.futures import ThreadPoolExecutor

def convert_mp4_to_mp3_parallel(args):
    input_file, output_file, codec = args
    start_time = time.time()

    video_clip = mp.VideoFileClip(input_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file, codec=codec)

    audio_clip.close()
    video_clip.close()

    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def convert_videos_parallel():
    while True:
        input_files = []
        output_files = []

        num_videos_input = input("How many videos to convert (type 'quit' to stop): ")

        if num_videos_input.lower() == 'quit':
            print("Exiting the program.")
            break

        try:
            num_videos = int(num_videos_input)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'quit'.")
            continue

        for i in range(1, num_videos + 1):
            input_file = input(f"Enter the path for video {i} (type 'quit' to stop): ")

            if input_file.lower() == 'quit':
                print("Exiting the program.")
                return

            output_file = f"output_parallel_{i}.mp3"
            input_files.append(input_file)
            output_files.append(output_file)

        # Load videos outside of the parallel function
        video_clips = [mp.VideoFileClip(input_file) for input_file in input_files]

        # Measure time for parallel conversion of each video
        parallel_times = []
        args_list = zip(input_files, output_files, ['mp3'] * num_videos)

        with ThreadPoolExecutor(max_workers=num_videos) as executor:
            futures = [executor.submit(convert_mp4_to_mp3_parallel, args) for args in args_list]

            for future in futures:
                parallel_time = future.result()
                parallel_times.append(parallel_time)

        # Print parallel conversion times
        for i in range(num_videos):
            print(f"Parallel conversion time (Video {i + 1}): {parallel_times[i]:.2f} seconds")

        # Calculate total parallel time
        total_parallel_time = sum(parallel_times)
        print(f"Total Parallel conversion time: {total_parallel_time:.2f} seconds")

        convert_more = input("Do you want to convert more videos? (yes/no): ")
        if convert_more.lower() != 'yes':
            print("Exiting the program.")
            break

# Call the function to convert multiple videos in parallel
convert_videos_parallel()


