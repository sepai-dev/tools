from pydub import AudioSegment
import numpy as np
from scipy.signal import resample

def resample_audio(audio, new_sample_rate):
    # Get raw audio data and convert it to a numpy array
    raw_audio_data = np.array(audio.get_array_of_samples())

    # Calculate new length of the sample
    new_length = int(len(raw_audio_data) * new_sample_rate / audio.frame_rate)

    # Resample the audio to a new sample rate
    resampled_audio_data = resample(raw_audio_data, new_length)

    # Ensure the data type is consistent with the original audio
    if audio.sample_width == 1:  # 8-bit
        resampled_audio_data = np.int8(np.clip(resampled_audio_data, -128, 127))
    elif audio.sample_width == 2:  # 16-bit
        resampled_audio_data = np.int16(np.clip(resampled_audio_data, -32768, 32767))
    elif audio.sample_width == 3:  # 24-bit
        resampled_audio_data = np.int32(np.clip(resampled_audio_data, -8388608, 8388607))
    else:  # 32-bit
        resampled_audio_data = np.int32(resampled_audio_data)

    # Convert the resampled numpy array back into an AudioSegment
    resampled_audio = AudioSegment(
        resampled_audio_data.tobytes(),
        frame_rate=new_sample_rate,
        sample_width=audio.sample_width,
        channels=audio.channels
    )

    return resampled_audio
