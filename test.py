import pyaudio
import wave


def list_microphones():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    num_devices = info.get('deviceCount')

    microphones = []

    for i in range(num_devices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        if device_info.get('maxInputChannels') > 0:
            microphones.append((i, device_info.get('name')))

    p.terminate()

    return microphones


def record_audio(device_index, duration=5, filename="output.wav"):
    p = pyaudio.PyAudio()

    # Налаштування параметрів запису
    format = pyaudio.paInt16
    channels = 1
    rate = 44100
    frames_per_buffer = 1024

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    input_device_index=device_index,
                    frames_per_buffer=frames_per_buffer)

    print(f"Recording from device {device_index} for {duration} seconds...")

    frames = []

    for _ in range(0, int(rate / frames_per_buffer * duration)):
        data = stream.read(frames_per_buffer)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == "__main__":
    mics = list_microphones()
    if mics:
        print("Доступні мікрофони:")
        for mic in mics:
            print(f"ID: {mic[0]}, Назва: {mic[1]}")

        # Запис аудіо з кожного мікрофона
        for mic in mics:
            mic_id, mic_name = mic
            filename = f"mic_{mic_id}.wav"
            record_audio(mic_id, duration=5, filename=filename)
            print(f"Audio recorded from {mic_name} saved as {filename}")
    else:
        print("Не знайдено доступних мікрофонів.")
