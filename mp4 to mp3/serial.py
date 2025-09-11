import moviepy.editor as mp
import time

def convert_mp4_to_mp3_serial(input_file, output_file, codec='mp3'):
    start_time = time.time()

    video_clip = mp.VideoFileClip(input_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file, codec=codec)

    audio_clip.close()
    video_clip.close()

    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def convert_videos_serial():
    while True:
       
        input_files = []
        output_files = []

        num_videos_input = input("Number of videos to convert or (type 'quit' to stop): ")

        if num_videos_input.lower() == 'quit':
            print("Program end.Thankyou.")
            break

        try:
            num_videos = int(num_videos_input)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'quit'.")
            continue

        for i in range(1, num_videos + 1):
            input_file = input(f"Enter the path for video {i}: ")

            output_file = f"output_serial_{i}.mp3"
            input_files.append(input_file)
            output_files.append(output_file)

       
        serial_times = []
        for i in range(num_videos):
            serial_time = convert_mp4_to_mp3_serial(input_files[i], output_files[i])
            serial_times.append(serial_time)
            print(f"___________Serial conversion time (Video {i + 1}): {serial_time:.2f} seconds______________")

    
        total_serial_time = sum(serial_times)
        print(f"____________Total Serial conversion time: {total_serial_time:.2f} seconds______________")

        convert_more = input("Do you want to convert more videos? (yes/no): ")
        if convert_more.lower() != 'yes':
            print("Program end.Thankyou.")
            break

# Call the function to convert multiple videos in ayeserial
convert_videos_serial()
