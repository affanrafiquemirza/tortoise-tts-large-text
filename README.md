# Tortoise TTS Large Text Processor

This is a Python script that uses [Tortoise TTS](https://github.com/neonbjb/tortoise-tts) to convert large input text files into high-quality audio.

## 🔧 Features
- Reads long text files
- Converts them into speech using Tortoise TTS
- Supports voice customization (if applicable)
- Ideal for long-form content or narration

## 📦 Requirements
- Python 3.8+
- Tortoise TTS
- PyTorch
- Other dependencies (optional - list your actual ones if needed)
- Not prefered to run on CPU (Will take very to complete)

## 🚀 Usage

1. Install dependencies for Tortoise TTS (inside a virtual environment is recommended):

```bash
pip install -r requirements.txt
```

2. Place your text file the Tortoise TTS directory named input.txt. If file name is different, don't forget to change the file name in the script.

3. Place **generate.py** file in the same directory

4. Run the script

```bash
python generate.py
```

5. The time for the processing to end will depend on the amount of text you have in the input file. Will take way longer if run on CPU alone.

6. Audio generated can be found in **results** folder 
