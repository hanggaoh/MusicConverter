import argparse
import os
from pydub import AudioSegment

SUPPORTED_FORMATS = {'.mp3', '.wav', '.flac', '.ape', '.ogg', '.aac', '.wma', '.m4a'}

def convert_audio_to_format(input_file, output_file):
    # Detect output file extension
    _, output_extension = os.path.splitext(output_file)

    # Detect input file extension
    _, input_extension = os.path.splitext(input_file)

    if output_extension.lower() in SUPPORTED_FORMATS:
        convert_to_format(input_file, input_extension[1:], output_file, output_extension[1:])
    else:
        print(f"Unsupported output file format: {output_extension}")

def convert_to_format(input_file, input_format, output_file, output_format):
    audio = AudioSegment.from_file(input_file, format=input_format)
    audio.export(output_file, format=output_format)

def main():
    parser = argparse.ArgumentParser(description='Convert audio to specified format')
    parser.add_argument('-s', '--source', help='Input audio file', required=True)
    parser.add_argument('-t', '--target', help='Output file', required=True)
    args = parser.parse_args()

    convert_audio_to_format(args.source, args.target)

if __name__ == "__main__":
    main()
