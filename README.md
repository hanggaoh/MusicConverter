# Audio Converter

## Overview

This Python script utilizes the `pydub` library to convert audio files to various formats. It supports the conversion of common audio formats such as MP3, WAV, FLAC, APE, OGG, AAC, WMA, M4A, and more.

## Prerequisites

- Python 3.x
- Install required packages:

  ```bash
  pip install pydub
  ```

## Usage

1. Clone or download this repository.
2. Open a terminal and navigate to the script directory.

   ```bash
   cd path/to/audio-converter
   ```

3. Run the script with the following command:

   ```bash
   python script.py -s input_file -t output_file
   ```

   Replace `input_file` with the path to the input audio file and `output_file` with the desired output file path. The script will automatically detect the output format based on the file extension.

### Example Usage:

Convert WAV to MP3:

```bash
python script.py -s input.wav -t output.mp3
```

Convert FLAC to OGG:

```bash
python script.py -s input.flac -t output.ogg
```

## Supported Formats

The script supports the following output audio formats:

- MP3
- WAV
- FLAC
- APE
- OGG
- AAC
- WMA
- M4A
- (Add or remove formats from the `SUPPORTED_FORMATS` set in the script as needed)

## Notes

- Ensure that the required audio codecs are available on your system.
- Verify the input audio file is valid and not corrupted.

## License

This script is licensed under the [MIT License](LICENSE).
