# Playing the sound
import threading
import pyaudio
import wave
# Plotting the data
import matplotlib
import matplotlib.pyplot as plt
from scipy.io import wavfile as wf
from math import floor
# Other features
import os
import signal


class SoundRecord:
    maxWaveformWidth = 65000
    __supportedExtensions = ['wav']

    def __init__(self, filename):
        extension = filename.split(".")[-1]
        if extension not in SoundRecord.__supportedExtensions:
            raise TypeError("Extension .'" + extension + "' is not supported")
        self.filename = filename
        self.extension = extension
        self.waveformFilename = None
        self.duration = None
        self.__streamThread = None
        self.__deletePictureOnExit = False

        def handleSignal(signum, frame):
            self.stop()

        for sig in set(signal.Signals) - {signal.SIGKILL, signal.SIGSTOP}:
            signal.signal(sig, handleSignal)

        if extension == 'wav':
            self.__init_wave()

    def __init_wave(self):
        self.wavfile = wave.open(self.filename, 'rb')
        self.sampWidth = self.wavfile.getsampwidth()
        self.channels = self.wavfile.getnchannels()
        self.frameRate = self.wavfile.getframerate()
        self.duration = self.wavfile.getnframes() / self.wavfile.getframerate()

    def __getWaveFormWidth(self):
        dotsPerSecond = 200
        width = floor(self.duration) * dotsPerSecond
        if width > SoundRecord.maxWaveformWidth:
            width = SoundRecord.maxWaveformWidth / floor
        return width

    def getWaveformPicture(self, width=None, height=148, dpi=2, deleteOnExit=True):
        self.__deletePictureOnExit = deleteOnExit
        green = "#5eff00"
        black = "#000000"
        _, scipyData = wf.read(self.filename)
        matplotlib.rcParams["figure.dpi"] = dpi
        color = green
        plt.plot(scipyData, color=color)
        plt.axis('off')
        plt.subplots_adjust(0, 0, 1, 1, 0, 0)
        plt.margins(0, 0)
        fig = plt.gcf()
        if not width:
            width = self.__getWaveFormWidth()
        width /= dpi
        height /= dpi
        fig.set_dpi(dpi)
        fig.set_size_inches(width, height)
        self.waveformFilename = self.filename.split(".")[0] + ".png"
        fig.savefig(fname=self.waveformFilename, dpi=dpi, facecolor=black)
        plt.clf()
        return self.waveformFilename

    class StreamThread(threading.Thread):
        def __init__(self, data, sampwidth, channels, rate):
            threading.Thread.__init__(self)
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(
                format=self.p.get_format_from_width(sampwidth),
                channels=channels,
                rate=rate,
                output=True)
            self.frameSize = sampwidth * channels
            self.data = data
            self.stopped = False
            self.stream.start_stream()
            print("StreamThread initialized...")

        def run(self):
            n = len(self.data)
            i = 0
            while i < n and not self.stopped:
                self.stream.write(self.data[i:i + self.frameSize])
                i += self.frameSize

            self.stopped = True
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()
            print("StreamThread terminated...")

        def stop(self):
            self.stopped = True

    def play(self, start=0, end=None):
        if start < 0 or start > self.duration:
            raise ValueError("Invalid start value was given")
        if self.__streamThread is not None and self.__streamThread.is_alive():
            self.stop()
        if not end or end > self.duration:
            end = self.duration
        length = end - start
        self.wavfile.setpos(int(start * self.frameRate))
        data = self.wavfile.readframes(int(length * self.frameRate))
        self.__streamThread = SoundRecord.StreamThread(data, self.sampWidth, self.channels, self.frameRate)
        self.__streamThread.start()

    def stop(self):
        if not self.__streamThread:
            return
        self.__streamThread.stop()
        self.__streamThread.join()

    def isPlaying(self) -> bool:
        if not self.__streamThread:
            return False
        return not self.__streamThread.stop

    def __del__(self):
        if self.__streamThread:
            self.__streamThread.stop()
        if self.__deletePictureOnExit:
            os.remove(self.waveformFilename)
        self.wavfile.close()


class SoundCombiner:
    def __init__(self):
        self.__output = None
        self.__params = None

    def create(self, filename):
        self.__output = wave.open(filename, 'wb')

    def __compareParams(self, params) -> bool:
        if self.__params is None:
            self.__output.setparams(params)
            self.__params = params
            self.channels, self.sampWidth, self.frameRate,\
            self.nframes, self.comptype, self.compname = params
            return True
        else:
            return self.__params == params

    def join(self, inputWavfile: wave.Wave_read, start, end):
        length = end - start
        if start < 0 or end < 0 or length < 0:
            raise ValueError("Invalid start value was given")
        params = inputWavfile.getparams()
        if not self.__compareParams(params):
            raise ValueError("File can not be joined due to inappropriate parameters")
        else:
            inputWavfile.setpos(int(start * self.frameRate))
            data = inputWavfile.readframes(int(length * self.frameRate))
            self.__output.writeframes(data)

    def detach(self):
        self.__output.close()
        self.__output = None
        self.__params = None

    def __del__(self):
        if self.__output:
            self.__output.close()


if __name__ == '__main__':
    fname = 'speech.wav'
    rec = SoundRecord(fname)
    rec.getWaveformPicture()
    rec.play(4, 10)
    comb = SoundCombiner()
    comb.create('combTest.wav')
    comb.join(rec.wavfile, 0.941, 1.082)
    comb.join(rec.wavfile, 0.722, 0.873)
    comb.join(rec.wavfile, 2.349, 2.431)
    comb.detach()

