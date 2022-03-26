from Maix import GPIO, I2S
import image, lcd, math
import audio
from fpioa_manager import fm

# maixduino:
maixduino = False  # 默认True就没法正常运行了
if maixduino:
    fm.fpioa.set_function(2, fm.fpioa.GPIO0)
    pa=GPIO(GPIO.GPIO0, GPIO.OUT)
    pa.value(1)

sample_rate = 22050
sample_points = 1024

fm.register(33,fm.fpioa.I2S0_WS, force=True)
fm.register(34,fm.fpioa.I2S0_IN_D0, force=True)
fm.register(35,fm.fpioa.I2S0_SCLK, force=True)

mic = I2S(I2S.DEVICE_0)
mic.channel_config(mic.CHANNEL_0, mic.RECEIVER, resolution = I2S.RESOLUTION_16_BIT, cycles = I2S.SCLK_CYCLES_32, align_mode = I2S.STANDARD_MODE)
mic.set_sample_rate(sample_rate)

fm.register(30,fm.fpioa.I2S2_WS, force=True)
fm.register(31,fm.fpioa.I2S2_OUT_D1, force=True)
fm.register(32,fm.fpioa.I2S2_SCLK, force=True)

spk = I2S(I2S.DEVICE_2)
spk.channel_config(spk.CHANNEL_1, I2S.TRANSMITTER, resolution = I2S.RESOLUTION_16_BIT, cycles = I2S.SCLK_CYCLES_32, align_mode = I2S.RIGHT_JUSTIFYING_MODE)
spk.set_sample_rate(sample_rate)

while True:
    spk.play(mic.record(sample_points))
