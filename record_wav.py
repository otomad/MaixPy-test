import image, lcd, time
import audio
from Maix import GPIO, I2S
from fpioa_manager import fm

# user setting
sample_rate   = 16000
record_time   = 5  #s
# default seting
sample_points = 2048
wav_ch        = 2

fm.register(34,fm.fpioa.I2S0_IN_D0, force=True)
fm.register(33,fm.fpioa.I2S0_WS, force=True)    # 19 on Go Board and Bit(new version)
fm.register(35,fm.fpioa.I2S0_SCLK, force=True)  # 18 on Go Board and Bit(new version)

mic = I2S(I2S.DEVICE_0)
mic.channel_config(mic.CHANNEL_0, mic.RECEIVER, resolution = I2S.RESOLUTION_16_BIT, cycles = I2S.SCLK_CYCLES_32, align_mode = I2S.STANDARD_MODE)
mic.set_sample_rate(sample_rate)
print(mic)

fm.register(30,fm.fpioa.I2S2_WS, force=True)
fm.register(31,fm.fpioa.I2S2_OUT_D1, force=True)
fm.register(32,fm.fpioa.I2S2_SCLK, force=True)

spk = I2S(I2S.DEVICE_2)
spk.channel_config(spk.CHANNEL_1, I2S.TRANSMITTER, resolution = I2S.RESOLUTION_16_BIT, cycles = I2S.SCLK_CYCLES_32, align_mode = I2S.RIGHT_JUSTIFYING_MODE)
spk.set_sample_rate(sample_rate)
print(spk)

# import time
# init audio
sdcard_mode = False
wave = "/%s/record.wav" % ("sdcard" if sdcard_mode else "flash")
recorder = audio.Audio(path=wave, is_create=True, samplerate=sample_rate)
print(dir(recorder))

queue = []

frame_cnt = record_time * sample_rate // sample_points

for i in range(frame_cnt):
    tmp = mic.record(sample_points*wav_ch)
    if len(queue) > 0:
        ret = recorder.record(queue[0])
        queue.pop(0)
    mic.wait_record()
    queue.append(tmp)
    print(str(i) + ":" + str(time.ticks()))

recorder.finish()

# init audio
player = audio.Audio(path=wave)
player.volume(40)

# loop to play audio
while True:
    ret = player.play()
    if ret == None:
        print("format error")
        break
    elif ret == 0:
        print("end")
        break
player.finish()
