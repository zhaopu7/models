"""Contains the speech segment class."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from data_utils.audio import AudioSegment


class SpeechSegment(AudioSegment):
    """Speech segment abstraction, a subclass of AudioSegment,
    with an additional transcript.

    :param samples: Audio samples [num_samples x num_channels].
    :type samples: ndarray.float32
    :param sample_rate: Audio sample rate.
    :type sample_rate: int
    :param transcript: Transcript text for the speech.
    :type transript: basestring
    :raises TypeError: If the sample data type is not float or int.
    """

    def __init__(self, samples, sample_rate, transcript):
        AudioSegment.__init__(self, samples, sample_rate)
        self._transcript = transcript

    def __eq__(self, other):
        """Return whether two objects are equal.
        """
        if not AudioSegment.__eq__(self, other):
            return False
        if self._transcript != other._transcript:
            return False
        return True

    def __ne__(self, other):
        """Return whether two objects are unequal."""
        return not self.__eq__(other)

    @classmethod
    def from_file(cls, filepath, transcript):
        """Create speech segment from audio file and corresponding transcript.
        
        :param filepath: Filepath or file object to audio file.
        :type filepath: basestring|file
        :param transcript: Transcript text for the speech.
        :type transript: basestring
        :return: Audio segment instance.
        :rtype: AudioSegment
        """
        audio = AudioSegment.from_file(filepath)
        return cls(audio.samples, audio.sample_rate, transcript)

    @classmethod
    def from_bytes(cls, bytes, transcript):
        """Create speech segment from a byte string and corresponding
        transcript.
        
        :param bytes: Byte string containing audio samples.
        :type bytes: str
        :param transcript: Transcript text for the speech.
        :type transript: basestring
        :return: Audio segment instance.
        :rtype: AudioSegment
        """
        audio = AudioSegment.from_bytes(bytes)
        return cls(audio.samples, audio.sample_rate, transcript)

    @property
    def transcript(self):
        """Return the transcript text.

        :return: Transcript text for the speech.
        :rtype: basestring
        """
        return self._transcript
